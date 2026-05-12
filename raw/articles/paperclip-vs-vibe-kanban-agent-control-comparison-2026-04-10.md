---
updated: 2026-04-11
title: "Paperclip vs Vibe Kanban — Agent Control Architecture Comparison"
created: 2026-04-10
type: raw-article
tags: [orchestration, agent, comparison, paperclip, vibe-kanban-agent-spawning]
sources: [github.com/paperclipai/paperclip, github.com/BloopAI/vibe-kanban-agent-spawning]
---

# Paperclip vs Vibe Kanban — Agent Control Architecture Comparison

**Paperclip:** ~/Documents/services/paperclip
**Vibe Kanban:** ~/Documents/services/vibe-kanban-agent-spawning

---

## Overview

Both systems orchestrate multiple AI coding agents (Claude Code, Codex, OpenCode, etc.) from a dashboard. Both aim to run a company/team of agents. But the internal architecture for **controlling, spawning, and detecting completion** of agents is fundamentally different.

| | Paperclip | Vibe Kanban |
|--|-----------|-------------|
| **Language** | TypeScript/Node.js | Rust (backend) + TypeScript/React (frontend) |
| **Stars** | 51k | 24k+ |
| **Agent interface** | Adapter packages (TypeScript) | Trait-based executors (Rust) |
| **Agent spawning** | `runChildProcess()` Promise | `tokio::process::Command` + `AsyncGroupChild` |
| **Exit detection** | Process exit via Promise | Dual-mode: `oneshot` channel + OS `try_wait()` polling |
| **Session resume** | `--resume` CLI flag + sessionId | Session ID in executor state |
| **Workspace isolation** | Git worktree via env vars | Git worktree per-task (native Rust) |
| **Skills injection** | Tmpdir with `.claude/skills/` symlinks | `.claude/skills/` in worktree |
| **Agent communication** | Issue/comment system | Kanban card state + WebSocket streaming |
| **Cost tracking** | Built-in (per-agent token budgets) | Not built-in |
| **Org structure** | Company/agent/budget model | Project/kanban board model |
| **Communication protocol** | None (raw subprocess) | ACP (JSON-RPC 2.0) for supported agents |

---

## 1. How They Spawn Agents

### Paperclip — `runChildProcess()` Promise

Paperclip uses a simple **Promise-based subprocess runner** in `@paperclipai/adapter-utils`:

```typescript
// Simplified from packages/adapter-utils/src/server-utils.ts
export async function runChildProcess(
  runId: string,
  command: string,
  args: string[],
  opts: { cwd, env, stdin, timeoutSec, graceSec, onLog, onSpawn, onLogError }
): Promise<RunProcessResult> {
  // Returns Promise that resolves when process exits
  return new Promise((resolve, reject) => {
    const child = spawn(command, args, { cwd, env, stdio: [...] });
    // Pipe stdin, stream stdout/stderr, resolve on exit
  });
}
```

**Claude Code** spawn command:
```
claude --print - --output-format stream-json --verbose
  [--resume <sessionId>]
  [--dangerously-skip-permissions]
  [--model <model>]
  [--effort <low|medium|high>]
  [--max-turns <n>]
  [--append-system-prompt-file <path>]
  [--add-dir <skillsDir>]
  [extraArgs...]
```

Paperclip builds args, passes the prompt via **stdin**, and awaits process exit. The `stream-json` output is parsed after the process terminates.

**OpenCode** spawns an HTTP server:
```
npx opencode-ai serve --hostname 127.0.0.1 --port 0
```
Then makes HTTP POST calls to the spawned server's `/sessions` endpoint.

**Key point:** Paperclip adapters are **stateless between heartbeats** — each run is a fresh `runChildProcess()` call. Session continuity is maintained via `--resume` and storing `sessionId` in the database between heartbeat runs.

### Vibe Kanban — `tokio::process::Command` + `AsyncGroupChild`

Vibe Kanban uses Rust's async process management:

```rust
// Simplified from crates/executors/src/executors/codex.rs
pub struct SpawnedChild {
    pub child: AsyncGroupChild,           // Process group handle
    pub exit_signal: Option<oneshot::Receiver>,  // Channel for completion signal
    pub cancel: Option<CancellationToken>,       // Cancellation token
}

pub trait StandardCodingAgentExecutor {
    async fn spawn(&self, current_dir: &Path, prompt: &str, env: &ExecutionEnv)
        -> Result<SpawnedChild, ExecutorError>;
    async fn spawn_follow_up(&self, ...) -> Result<SpawnedChild, ExecutorError>;
    async fn spawn_review(&self, ...) -> Result<SpawnedChild, ExecutorError>;
}
```

The `#[enum_dispatch(CodingAgent)]` macro generates a zero-cost enum dispatch to the correct executor at compile time. Each agent is a Rust source file implementing the trait.

**Claude Code** (3,278 lines — most complex):
```
npx @anthropic-ai/claude-code -p --output-format=stream-json
```
Then uses a full **ClaudeAgentClient + ProtocolPeer** for structured control: initialize → set_permission_mode → send_user_message. But it returns `exit_signal: None` — **sessions get stuck forever** (known bug #2495).

**Codex** (most structured):
```
npx @openai/codex app-server
```
Uses JSON-RPC 2.0 over stdin/stdout via `AppServerClient + JsonRpcPeer`. Has proper exit signaling via `oneshot::channel` — the cleanest implementation.

**Gemini** (thinnest — 25 lines):
```
npx @google/gemini-cli --experimental-acp [...]
```
Delegates ALL protocol management to the shared `AcpAgentHarness`. Just 25 lines of spawn code.

**OpenCode** (unique HTTP client pattern):
Spawns local HTTP server, waits for URL on stdout, then calls `run_session()` via HTTP POST.

---

## 2. How They Detect Agent Completion

### Paperclip — Simple Process Exit

Paperclip waits for the Node.js `child_process` Promise to resolve. The `parseClaudeStreamJson()` parses `stream-json` output after the process exits. There is no structured exit signaling — it relies entirely on OS process termination.

```typescript
// From execute.ts
const proc = await runChildProcess(runId, command, args, {...});
const parsedStream = parseClaudeStreamJson(proc.stdout);
// Returns after proc exits (or times out)
```

**Problem:** If Claude Code stays alive waiting for more stdin (which it does in `-p` mode after completing), Paperclip relies on `timeoutSec` to kill it. This is why `timeoutSec` and `graceSec` are core config fields.

### Vibe Kanban — Dual-Mode Exit Detection

Vibe Kanban has a sophisticated exit monitor in `container.rs`:

```rust
// From crates/local-deployment/src/container.rs
tokio::select! {
    // Mode 1: Executor signals completion via oneshot channel
    exit_result = &mut exit_signal_future => {
        // Kill process group, record exit
        command::kill_process_group(&mut child).await;
        status_result = match exit_result {
            Ok(ExecutorExitResult::Success) => Ok(success_exit_status()),
            Ok(ExecutorExitResult::Failure) => Ok(failure_exit_status()),
            Err(_) => Ok(success_exit_status()), // Channel closed = success
        };
    }
    // Mode 2: OS process exit (polls try_wait() every 250ms)
    _ = process_exit_rx.recv() => {
        status_result = child.try_wait();
    }
}
```

| Executor | Exit Signal | How |
|----------|------------|-----|
| **Claude Code** | **NONE** | BROKEN — process never exits on its own |
| **Codex** | **YES** (`oneshot`) | `JsonRpcPeer` detects completion in JSON-RPC stream |
| **OpenCode** | **YES** (`oneshot`) | HTTP call returns → signals completion |
| **Gemini** | **Via ACP** | ACP harness manages it |
| **Cursor** | **NONE** | Fire-and-forget, raw `AsyncGroupChild` |

**Key insight:** Vibe Kanban's exit detection is only as reliable as the executor's ability to signal. Claude Code (stuck) and Cursor (fire-and-forget) are unreliable — their sessions can hang indefinitely.

---

## 3. Session Resume / Continuity

### Paperclip

Session resume is built into the core adapter contract:

```typescript
// From execute.ts
const runtimeSessionParams = parseObject(runtime.sessionParams);
const runtimeSessionId = asString(runtimeSessionParams.sessionId, runtime.sessionId ?? "");
const canResumeSession = runtimeSessionId.length > 0 && (runtimeSessionCwd.length === 0 || ...);
const sessionId = canResumeSession ? runtimeSessionId : null;

if (sessionId) {
  args.push("--resume", sessionId);
}
```

On successful completion, Paperclip returns `sessionId` and `sessionParams` (including `cwd`, `workspaceId`, `repoUrl`, `repoRef`) which are stored and passed back on the next heartbeat to resume the session.

### Vibe Kanban

Vibe Kanban maintains session state in a SQLite database (`Session` model). The executor's `spawn_follow_up()` method takes a `session_id` parameter:

```rust
async fn spawn_follow_up(
    &self,
    current_dir: &Path,
    prompt: &str,
    session_id: &str,
    reset_to_message_id: Option<&str>,
    env: &ExecutionEnv,
) -> Result<SpawnedChild, ExecutorError>;
```

For Codex, `thread_fork` is used to continue a session. The database tracks `CodingAgentTurn` for each interaction turn within a session.

---

## 4. Workspace Isolation

### Paperclip — Workspace Execution (Experimental)

Paperclip has introduced **execution workspaces** (EXPERIMENTAL as of v2026.403.0). Each heartbeat run can be workspace-aware. Configuration is passed via environment variables:

```
PAPERCLIP_WORKSPACE_ID=...
PAPERCLIP_WORKSPACE_CWD=...
PAPERCLIP_WORKSPACE_SOURCE=...       # "agent_home" | ...
PAPERCLIP_WORKSPACE_STRATEGY=...     # "git_worktree" | ...
PAPERCLIP_WORKSPACE_REPO_URL=...
PAPERCLIP_WORKSPACE_REPO_REF=...
PAPERCLIP_WORKSPACE_BRANCH=...
PAPERCLIP_WORKSPACE_WORKTREE_PATH=...
PAPERCLIP_WORKSPACES_JSON=...        # All available workspaces (for context)
```

The `workspaceStrategy` config supports `{ type: "git_worktree", baseRef?, branchTemplate?, worktreeParentDir? }`.

The **agent controls workspace lifecycle** — Paperclip creates the workspace, agents work within it, but the workspace runtime services are "manually controlled from the workspace UI and are not auto-started by heartbeats."

### Vibe Kanban — Native Git Worktree Isolation

Vibe Kanban's workspace isolation is more mature and native to the Rust backend:

```rust
// From crates/services/src/services/worktree_manager.rs
git worktree add -b <branch> <path> <base>

// Each task gets:
// - Isolated working directory (git worktree)
// - Own branch (isolation from other agents)
// - Shared repo history (same .git object database)
```

Workspace creation flow:
1. `WorkspaceManager.create_workspace()` → `git worktree add -b <branch> <path> <base>`
2. Setup script runs (if configured)
3. Executor spawns agent in the worktree directory
4. On completion: commits changes, creates PR
5. Cleanup: `git worktree remove --force`

This is the **biggest architectural difference**: Vibe Kanban treats git worktree isolation as a first-class concept deeply integrated into its Rust backend. Paperclip is just beginning to add this as an experimental feature via env vars.

---

## 5. Skills Injection

### Paperclip

Paperclip builds a **temporary skills directory** for each run:

```typescript
// From execute.ts — buildSkillsDir()
const tmp = await fs.mkdtemp(path.join(os.tmpdir(), "paperclip-skills-"));
const target = path.join(tmp, ".claude", "skills");
await fs.mkdir(target, { recursive: true });
// Symlink desired skills into target
for (const entry of availableEntries) {
  if (!desiredNames.has(entry.key)) continue;
  await fs.symlink(entry.source, path.join(target, entry.runtimeName));
}
return tmp; // Temporary dir destroyed after run
// Claude is launched with: --add-dir <skillsDir>
```

This means each heartbeat run can inject different skills from Paperclip's managed skill library. Skills are repo-controlled and versioned.

### Vibe Kanban

Vibe Kanban injects skills into the Claude Code `.claude/skills/` directory **in the worktree itself**:

```rust
// Symlink skills into the worktree's .claude/skills/
// Claude Code discovers them automatically since it's running in the worktree
```

Because the worktree is persistent across the task lifetime, skills are set up once per task, not per-run.

---

## 6. Agent Communication

### Paperclip — Issue/Comment System

Agents do NOT communicate directly. All coordination happens through **issues and comments**:

- Agents create/update issues to track work
- Comments on issues are the primary communication channel
- `@-mentions` (`@AgentName`) trigger a heartbeat wakeup for the mentioned agent
- All communication is stored in the DB and visible in the UI

**Advantage:** Full audit trail, human-in-the-loop approval via board, structured handoff.
**Disadvantage:** No real-time streaming communication between agents.

### Vibe Kanban — Kanban Board + WebSocket Streaming

Vibe Kanban uses the **kanban card itself** as the communication mechanism:

- Task moves: `todo` → `inprogress` → `inreview` → `done`
- Agents work on a card, commit to branch, create PR
- Other agents (or humans) review the PR
- The card state reflects the overall progress

Real-time updates are streamed to the UI via **WebSocket**. Log output from agents is streamed live to the frontend via `msg_stores` system.

**Advantage:** Real-time streaming, more fluid for coding workflows.
**Disadvantage:** No structured human-in-the-loop approval gates, less suited to multi-agent business processes.

---

## 7. Hermes Adapter

### Paperclip

Hermes is **NOT built into Paperclip core**. The `hermes_local` adapter comes from `@henkey/hermes-paperclip-adapter` (npm package), which is registered as a plugin adapter. In the upstream repo, Hermes support was added via a separate npm package that implements the adapter interface.

Looking at `AGENTS.md` in the repo, there's a fork (`HenkDz/paperclip`, branch `feat/externalize-hermes-adapter`) that externalizes Hermes completely as a plugin — no built-in `hermes-paperclip-adapter` dependency.

### Vibe Kanban

Vibe Kanban does **not** have a built-in Hermes executor. However, it has a **custom executor RFC (#2775)** that allows adding arbitrary agents via config:

```json
{
  "executors": {
    "CUSTOM": {
      "RALPH_LOOP": {
        "CUSTOM": {
          "command": "npx",
          "args": ["fabis-ralph-loop", "full-pipeline", "--iterations", "20"],
          "prompt_mode": "arg",
          "env": { "NODE_ENV": "development" }
        }
      }
    }
  }
}
```

Hermes could be added as a custom executor with `prompt_mode: "stdin"` or `"arg"`.

---

## 8. Cost / Token Tracking

### Paperclip — Built-in, Comprehensive

Paperclip has **first-class cost tracking**:

```http
POST /api/companies/{companyId}/cost-events
{
  "agentId": "{agentId}",
  "provider": "anthropic",
  "model": "claude-sonnet-4-20250514",
  "inputTokens": 15000,
  "outputTokens": 3000,
  "costCents": 12
}
```

Per-agent adapters report costs after each heartbeat. Paperclip aggregates via `GET .../costs/by-agent`, `GET .../costs/by-project`, `GET .../costs/summary`.

**Budget enforcement:**
- 80% → soft alert (agent told to focus on critical tasks)
- 100% → hard stop (agent auto-paused)

This is a **major differentiator** — Paperclip is designed for running a business with real cost control.

### Vibe Kanban — Not Built-in

Vibe Kanban does **not** track token usage or costs. It tracks:
- Execution time
- Exit status (success/failure)
- Log output

If you want cost tracking, you'd need to add it yourself.

---

## 9. Architectural Philosophy

### Paperclip = Control Plane for AI Companies

Paperclip models itself as **the operating system of an AI company**:
- Agents = employees
- Budgets = token salaries
- Org chart = chain of command
- Issues = tickets with approval gates
- Board = human oversight / "board of directors"

It's fundamentally about **business governance**: budgets, approval workflows, compliance, multi-company isolation.

**Agnostic to what agents do** — the adapters are thin wrappers around CLIs. The value is in the orchestration layer above.

### Vibe Kanban = Parallel Coding Agent Runner

Vibe Kanban models itself as **a smarter way to run many coding agents in parallel**:
- Kanban board = task queue
- Git worktrees = isolated sandboxes
- WebSocket streaming = real-time visibility
- ACP/MCP = structured agent communication protocol

It's fundamentally about **developer productivity**: parallelizing coding work across agents, reviewing their PRs, managing the flow.

**Deeply integrated into the coding workflow** — the MCP server, git worktrees, PR review system are all coding-focused.

---

## Summary: Key Architectural Differences

## See Also

- [[paperclip-orchestrator]] — Paperclip Orchestrator project
- [[vibe-kanban-agent-spawning]] — Vibe Kanban agent spawning
- [[a2a-protocol-cross-agent-communication]] — A2A protocol — agent communication standard


| Dimension | Paperclip | Vibe Kanban |
|-----------|-----------|-------------|
| **Language** | TypeScript/Node.js | Rust (backend) |
| **Agent abstraction** | TypeScript adapter packages | Rust trait + `enum_dispatch` |
| **Spawn model** | Promise-based `runChildProcess()` | Async `tokio::process::Command` |
| **Exit detection** | Process exit + timeout | Dual-mode: `oneshot` + `try_wait()` polling |
| **Claude Code reliability** | Works (stdout parsing after exit) | BROKEN (issue #2495 — stuck sessions) |
| **Session resume** | `--resume` CLI flag + DB | `spawn_follow_up()` + SQLite |
| **Workspace isolation** | Experimental env vars + git worktree | Native Rust git worktree manager |
| **Skills injection** | Tmpdir symlinks per-run | Worktree `.claude/skills/` per-task |
| **Real-time streaming** | Yes (SSE/WebSocket) | Yes (WebSocket) |
| **Agent ↔ agent comms** | Issue/comment + @-mentions | Kanban card state |
| **Human approval gates** | Yes (board + approvals) | PR review after the fact |
| **Cost tracking** | Built-in per-agent budgets | Not built-in |
| **Org chart / company model** | Yes | No |
| **Hermes support** | Plugin adapter (`@henkey/hermes-paperclip-adapter`) | Via custom executor RFC |
| **Primary use case** | Run an AI company | Parallelize coding agents |