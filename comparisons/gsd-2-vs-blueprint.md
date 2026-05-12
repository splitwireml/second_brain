---
title: GSD-2 vs Blueprint — Comparative Analysis
created: 2026-04-06
updated: 2026-04-06
type: comparison
tags: [comparison, agent, framework, orchestration]
sources: [raw/articles/x-bookmarks-2026.md]
---

# GSD-2 vs Blueprint — Comparative Research


---

## Overview

This note compares GSD-2 (a standalone AI vibe coding framework built on the Pi SDK) against Blueprint's `phase-runner` and `planning-coach` skills (Hermes-native multi-agent orchestrators). The two systems occupy overlapping problem space — autonomous coding agents, milestone planning, parallel execution, git-based isolation — but differ fundamentally in architecture, philosophy, and extensibility.

**GSD-2** is a standalone CLI application (~4,400 GitHub stars, 80 contributors). **Blueprint** is a workflow layer running inside Hermes Agent, orchestrating existing CLI coding agents (Claude Code, Codex, OpenCode) via PTY terminals and process management.

---

## Architecture: Fundamental Difference

### GSD-2 — Standalone Application

GSD-2 is a **self-contained TypeScript application** that wraps the Pi SDK. It owns the entire agent runtime — it *is* the coding agent.

```
User → gsd CLI → Pi SDK (agent loop) → LLM Provider API
                ↓
         23 bundled extensions
         (browser-tools, mcp-client, subagent, etc.)
```

- Owns the agent loop, session management, and tool execution
- Ships its own extensions (TypeScript plugins via the Pi extension API)
- State lives in `.gsd/` on disk
- Ships a VS Code extension and web UI
- Runs as: CLI, headless (RPC), MCP server mode

### Blueprint (phase-runner) — Hermes-native Orchestrator

Blueprint does **not run agents itself**. It *spawns and coordinates* existing CLI coding agents as background PTY processes managed by Hermes's terminal tool.

```
User → Hermes → phase-runner skill
                ↓
         terminal(background=True, pty=True)
                ↓
         claude / codex / opencode / gemini (as background processes)
                ↓
         Each agent: own CLI session, own tool execution, own session state
```

- phase-runner is a Hermes *skill*, not a standalone app
- Each coding agent is a separate OS process with its own terminal session
- No shared agent runtime — Claude Code runs `claude`, Codex runs `codex exec`
- State lives in project docs (`docs/project-progress.md`, kanban MCP)
- Works with any coding agent that exposes a TUI/CLI

---

## Multi-Agent Model

### GSD-2

GSD-2 has **one active agent** at a time — the Pi/agent session. Parallelism is achieved by:

- **Parallel Milestone Orchestration**: Multiple `gsd` worker processes (separate OS processes), each running a full GSD/Pi instance, isolated via git worktrees
- **Subagent extension**: One-shot delegated tasks (`subagent` extension) with isolated context windows — but these are fire-and-forget, not persistent coordinated agents
- **Bundled agents**: Scout (fast codebase recon), Researcher (web research), Worker (isolated execution) — but these are Pi agent types, not separate processes

**Limitation**: You cannot run two different agent engines simultaneously (e.g., Claude Code + Codex on different milestones). All workers run the GSD/Pi stack.

### Blueprint (phase-runner)

Blueprint is explicitly **multi-agent from the ground up**. It runs multiple agents *simultaneously*:

- **Gate agent** — one agent executes the gate (foundation/shared work)
- **Multiple Stream agents** — each Stream gets its own dedicated agent, all running in parallel
- **Reviewer agents** — separate高端模型 agents for code review
- **Supported agents**: Claude Code (`claude`), Codex (`codex exec`), OpenCode (`opencode`), Gemini CLI (`gemini`)

**Key advantage**: Each Stream can use a **different agent engine**. You can run Claude Code on Stream A and Codex on Stream B simultaneously. The orchestrator (phase-runner) doesn't care — it just manages their PTY terminals.

```
phase-runner coordinator
  ├── Gate TTY:    claude --model opus    (Claude Code)
  ├── Stream A TTY: codex exec --full-auto (Codex)
  ├── Stream B TTY: opencode --model sonnet (OpenCode)
  └── Stream C TTY: claude --model sonnet  (Claude Code)
```

---

## Parallel Execution

### GSD-2

**Parallel Milestone Orchestration** — milestone-level parallelism:

```yaml
parallel:
  enabled: true
  max_workers: 2    # 1-4 workers
  budget_ceiling: 50.00
```

- Coordinator (main GSD session) spawns N worker `gsd` processes
- Workers run in isolated git worktrees with `GSD_MILESTONE_LOCK`
- File-based IPC via `.gsd/parallel/<MID>.signal.json` and `.status.json`
- Eligibility check: dependency graph + file overlap analysis before spawning
- Merge: sequential by ID order or by-completion
- **Limitation**: All workers run the GSD/Pi engine. No heterogeneity.

### Blueprint (phase-runner)

**Parallel Stream Execution** — Stream-level parallelism within a phase:

```
STREAMS_EXECUTING:
  Stream A ──┐
  Stream B ──┤  (all parallel, isolated worktrees)
  Stream C ──┘

  Gate (must complete first, serial)
```

- Streams are defined in the Blueprint phase document with a Parallelization Map
- phase-runner reads dependencies and spawns independent Streams in parallel
- Each Stream gets its own PTY terminal with a dedicated agent
- Sequential dependency enforcement: Stream C waits for A and B if dependent
- Review can also run in parallel across Streams
- **Advantage over GSD-2**: True agent heterogeneity — each Stream can use a different agent CLI

---

## Bring Your Own Agent

### GSD-2

| Component | Supported? | How |
|-----------|-----------|-----|
| Claude Code CLI | Yes (as model provider) | `claude-code` extension — delegates inference to local Claude Code CLI via `@anthropic-ai/claude-agent-sdk` |
| Claude Code MCPs | Partial | Discoverable via `universal-config` extension; not auto-imported |
| Claude Code skills | Partial | Skills follow agentskills.io — compatible format; auto-migrated to `~/.agents/skills/` |
| Codex | Partial | Context files discoverable; TOML MCP not parsed |
| OpenCode | Partial | Context files discoverable; not a registered model provider |
| Generic MCP servers | Yes | Via `.mcp.json` / `.gsd/mcp.json` native MCP client (stdio/HTTP) |
| Custom agents (subagent) | Fire-and-forget | `subagent` extension — one-shot, isolated, no persistent session |

**Bottom line**: GSD-2 detects your existing Claude Code/Cursor/Windsurf/Codex configs passively but doesn't run them. It can use Claude Code's CLI for inference, but can't use Codex or OpenCode as execution engines.

### Blueprint (phase-runner)

| Component | Supported? | How |
|-----------|-----------|-----|
| Claude Code | Yes (full) | Spawned as PTY terminal: `claude` or `claude --model opus` |
| Codex | Yes (full) | Spawned as PTY terminal: `codex exec --full-auto` |
| OpenCode | Yes (full) | Spawned as PTY terminal: `opencode` |
| Gemini CLI | Yes (full) | Spawned as PTY terminal: `gemini` |
| MCPs | Agent-native | Each agent handles its own MCP setup from its own config files |
| Skills | Agent-native | Each agent loads its own skills from its own config dirs |

**Bottom line**: Blueprint fully embraces your existing agents — it literally runs them as subprocesses. Each agent brings its own MCP config, skills, and session state. No translation or import layer needed.

---

## Planning & Workflow Model

### GSD-2

GSD-2 uses **spec-driven development** — you write a `.gsd/` directory with:

- `STATE.md` — current project state
- `roadmap.md` — milestones and slices
- `plans/` — task-level plans
- `.gsd` file format (replaces v1's `.planning`)

The agent is guided by **disk state files** that it reads and writes autonomously. Planning is implicit in the state machine — there's no human-in-the-loop phase planning step.

```
Auto mode dispatch loop:
  read state → classify complexity → route model →
  build prompt → fresh session → execute → verify →
  persist state → repeat
```

GSD-2 can run **fully autonomously** (`/gsd auto`) with no human involvement. It also has quality gates, verification commands, and a supervisor that enforces timeouts.

**Planning coach equivalent**: None — GSD-2 doesn't have a structured PRD/SRS/milestone interview workflow. Planning is done by writing `.gsd/` files directly.

### Blueprint (planning-coach + phase-runner)

Blueprint separates **Mode 1 (planning)** from **Mode 2 (execution)**:

**planning-coach** guides the user through:
1. PRD Stage 1 — Understanding goals and scope (chunked Q&A)
2. SRS — Technical decomposition
3. PRD Stage 2 — Refining PRD with SRS knowledge
4. Milestone Planning — Grouping into milestones and phases

Each stage requires **explicit user confirmation** before advancing. The agent asks 2-3 questions at a time, never assumes, and escalates on ambiguity.

**phase-runner** then executes an approved plan:
- Gate → Streams → Review → Merge workflow
- Gate must complete and merge before Streams start
- Streams can run in parallel based on dependency analysis
- Full TDD cycle per task (write test → fail → implement → pass → lint → review)

**Key difference**: Blueprint keeps humans in the loop during planning. GSD-2 is more autonomous once started.

---

## Git Strategy

### GSD-2

GSD-2 manages git via **git worktrees**:

```yaml
git:
  isolation: worktree  # default — separate directory per milestone
  merge_strategy: squash  # or "merge"
  auto_push: false
  snapshots: true        # WIP commits during long tasks
```

- Each milestone gets its own worktree: `.gsd/worktrees/M001/`, `M002/`, etc.
- Each worktree has its own `.gsd/` state directory
- Milestone branches: `milestone/<MID>`
- `GSD_MILESTONE_LOCK` env var isolates state derivation per worktree
- Pre-merge checks, snapshot commits, auto-PR creation

### Blueprint (phase-runner)

Blueprint also uses **git worktrees**, but the naming and lifecycle are different:

```bash
# Gate worktree
git worktree add worktrees/M{ N }-P{ N }-0 -b M{ N }-P{ N }-0

# Stream worktrees (created from main after Gate merges)
git worktree add worktrees/M{ N }-P{ N }-A -b M{ N }-P{ N }-A
git worktree add worktrees/M{ N }-P{ N }-B -b M{ N }-P{ N }-B
```

- Gate worktree is **discarded after merge** (or kept for hotfixes)
- Stream worktrees persist until all Streams in the phase are merged
- phase-runner executes the **merge** via `git merge --ff-only` or full merge
- Regression handling: creates `[BUG]` kanban tasks if tests fail post-merge

---

## State Management

### GSD-2

**Disk-based, single source of truth** — `.gsd/` directory:

```
.gsd/
├── STATE.md           # Current project state (derived from disk)
├── roadmap.md         # Milestones, slices, tasks
├── plans/             # Per-task plans
├── metrics.json       # Token and cost tracking
├── auto.lock          # Crash recovery lock
├── parallel/          # Coordinator ↔ worker IPC
│   ├── M002.status.json
│   └── M002.signal.json
└── worktrees/         # Git worktrees per milestone
```

- No in-memory state survives sessions
- `deriveState()` reads `.gsd/` and computes current state
- Crash recovery: lock files + disk state persistence
- Multi-terminal: multiple GSD sessions can read/write the same `.gsd/`

### Blueprint (phase-runner)

**Document-based state** — project docs managed by humans and the kanban MCP:

```
docs/
├── project-progress.md    # Phase graph, milestone status, kanban board reference
├── milestones/
│   └── milestone-{n}-{name}/
│       ├── phase-{n}-{name}.md  # Phase doc with Gate + Streams + Test Plan
├── conventions.md         # Tech stack, patterns, testing framework
├── core/
│   ├── execution.md      # TDD workflow
│   ├── git-execution-workflow.md
│   └── review.md         # Review criteria and note format
```

- State is **human-authored and human-maintained** for planning
- phase-runner reads phase docs to know what to execute
- Kanban MCP tracks task status (IN-PROGRESS, IN-REVIEW, DONE)
- Agent commits are made within worktrees, not a central state dir

---

## Extension & Plugin Ecosystem

### GSD-2

**23 bundled extensions** + open extension API:

| Extension | Notes |
|-----------|-------|
| MCP Client | Native `@modelcontextprotocol/sdk` integration |
| Claude Code CLI | Claude Code as model provider |
| Universal Config | Discovers Claude Code, Cursor, Windsurf, Codex, Gemini configs |
| Browser Tools | Full Playwright integration |
| Context7 | Live library/framework docs |
| GitHub Sync | Issues + PRs via `gh` CLI |
| Ollama | Local model support |
| Remote Questions | Route decisions to Discord/Slack/Telegram |

**Extension installation:**
```bash
gsd install npm:pi-dashscope   # Community extension
```

Custom extensions live at:
- `~/.gsd/agent/extensions/*.ts` (global)
- `.gsd/extensions/*.ts` (project-local)
- Or via `settings.json` `"packages": ["npm:@foo/bar@1.0.0"]`

### Blueprint (phase-runner)

Blueprint has **no extension system** — it's a skill that orchestrates external CLI tools. The "ecosystem" is whatever each coding agent supports:

- Claude Code extensions/plugins → stay in Claude Code, Blueprint doesn't touch them
- Codex config → stays in Codex
- OpenCode MCPs → stay in OpenCode

**Integration point**: Kanban MCP (project management), which Blueprint reads/writes via tool calls.

---

## Observability & Debugging

### GSD-2

- **Real-time TUI dashboard** — `gsd --mode tui` or within session
- **`/gsd parallel watch`** — native TUI overlay for worker monitoring
- **`/gsd doctor`** — detects stale sessions, worktree orphans, lock issues
- **Metrics ledger** — token and cost tracking per session and milestone
- **Auto-mode verbose output** — real-time streaming, colorized headless output
- ** Stuck detection** — `auto-stuck-detection.ts` with retry escalation
- **`/gsd skill-health`** — skill performance dashboard

### Blueprint (phase-runner)

- **PTY terminals are observable** — `process(action="log")` shows each agent's full output in real-time
- **process(action="poll")** — check if agent is still running
- **process(action="list")** — see all active agent sessions
- **Kanban MCP** — task-level status visibility
- **No built-in cost tracking** — each agent handles its own
- **No stuck detection** — phase-runner polls for unresponsiveness, but relies on the agent's own mechanisms

---

## Headless / CI/CD

### GSD-2

GSD-2 explicitly supports headless operation:

```bash
gsd headless              # CI/cron orchestration via RPC child process
gsd --mode mcp            # MCP server mode over stdin/stdout
```

- Docker sandbox: `docker/docker-compose.yaml` for isolated auto-mode
- `GSD_STATE_DIR` and `GSD_PROJECT_ID` env vars for CI state management
- Web interface: `gsd --web` for browser-based project management
- Designed to run and complete milestones with no human present

### Blueprint (phase-runner)

Blueprint is designed for **interactive use** — a human approves each phase, reviews MAJOR notes, and triggers execution. It is not designed for fully autonomous headless runs.

- No headless mode per se — the PTY terminals can run in background
- No native CI/CD pipeline integration
- Kanban MCP dependency means it needs the MCP server reachable

---

## Summary Comparison Table

| Dimension | GSD-2 | Blueprint (phase-runner) |
|-----------|-------|--------------------------|
| **Runtime model** | Standalone CLI app (Pi SDK) | Hermes-native orchestrator (skill) |
| **Agent engine** | Pi SDK (single engine) | Spawns Claude Code, Codex, OpenCode, Gemini as PTY processes |
| **Multi-agent** | One at a time (parallel milestones) | Many simultaneous (Gate + N Streams) |
| **Agent heterogeneity** | No — all workers run Pi/GSD | Yes — each Stream can use different agent |
| **Bring your own Claude Code** | As model provider (inference only) | Full Claude Code CLI as execution agent |
| **Bring your own Codex/OpenCode** | Discoverable only | Full execution agent |
| **MCP support** | Native MCP client (stdio/HTTP) | Via each agent's own config |
| **Skills/extensions** | Agent Skills standard + 23 bundled extensions | Agent-native (Blueprint doesn't manage skills) |
| **Planning** | Implicit in disk state files | Explicit PRD→SRS→Milestone interview workflow |
| **Human in loop** | Optional (auto mode is fully autonomous) | Required (approves before each phase) |
| **Parallel execution** | Milestone-level, 1-4 workers | Stream-level, unlimited (resource-bound) |
| **Git isolation** | Worktrees + milestone branches | Worktrees per Gate/Stream |
| **State management** | `.gsd/` on disk | `docs/` + Kanban MCP |
| **Observability** | TUI dashboard, skill-health, doctor | PTY log polling, kanban board |
| **Cost tracking** | Built-in per session/milestone | Per-agent (external) |
| **Headless/CI** | Yes (headless mode, Docker, MCP server) | Not designed for fully autonomous |
| **VS Code extension** | Yes (sidebar, chat participant) | No |
| **Web UI** | Yes (`gsd --web`) | No |
| **Setup complexity** | Medium (npm install, provider config) | Low (just install agents, configure kanban MCP) |

---

## When to Use Which

### Use GSD-2 when:

- You want a **self-contained coding agent** that manages its own state, git, and milestones
- You need **managed RTK compression**, cost tracking, and budget enforcement at the framework level
- You're a **solo developer or small team** and want a "set it and walk away" autonomous experience
- You need the **VS Code sidebar** or **web UI** for visual progress tracking
- You're using **Claude Code subscription** for subsidized inference via the `claude-code` provider
- You want **spec-driven development** with automatic context injection, snapshot commits, and worktree isolation
- You need **browser automation** built-in (Playwright-based)
- You want **20+ model providers** with dynamic cost-aware routing out of the box

### Use Blueprint (phase-runner) when:

- You already have **Claude Code, Codex, and OpenCode** configured and want to keep using them
- You want **heterogeneous agents** — e.g., Claude Code on the frontend, Codex on the backend, simultaneously
- You need **structured human-in-the-loop planning** — PRD interviews, explicit scope decisions, escalation on ambiguity
- You already live in **Hermes** and want multi-agent execution without leaving the session
- You want **lower setup complexity** — no provider accounts needed, just `claude` / `codex exec` / `opencode` on PATH
- You need **kanban-centric project management** driving the execution flow
- You want **opus-level review** on every Gate and Stream without paying for it in both GSD's model budget and a separate Claude Code subscription
- Your team's **review workflow** maps to Gate → Stream → Review → Merge cycles that kanban tracks

### See Also

- [[gsd-2-ai-vibe-coding-framework]] — GSD-2 standalone agent framework

## Complementary Use

Both can be used together:
- Use **Blueprint (planning-coach)** for structured PRD → SRS → Milestone creation
- Use **GSD-2** to autonomously execute individual milestones with full observability and cost tracking
- Or use **Blueprint (phase-runner)** to execute milestones with full agent heterogeneity

The key architectural difference: **Blueprint is an orchestrator of agents; GSD-2 is an agent with extensions.**
