---
title: Claude Code Plugin System
created: 2026-05-18
updated: 2026-06-14
type: concept
tags: [agent-delegation, claude-code, hooks, json-rpc, plugin-system, slash-commands, subagents]
sources: []
related_entity: [[openai-codex-plugin-cc]]
---

## Plugin Directory Structure

A Claude Code plugin is a directory under `.claude-plugin/` with a `marketplace.json` at root.

```
.openai-codex-plugin/
├── .claude-plugin/
│   └── marketplace.json              # Registry: name, version, plugin source path
└── plugins/codex/
    ├── commands/                     # Slash command definitions (*.md)
    │   ├── review.md
    │   ├── adversarial-review.md
    │   ├── rescue.md
    │   ├── setup.md, status.md, result.md, cancel.md
    ├── agents/                       # Subagent definitions (*.md)
    │   └── codex-rescue.md
    ├── hooks/
    │   └── hooks.json                # SessionStart, SessionEnd, Stop hook registrations
    ├── skills/
    │   ├── codex-cli-runtime/        # Skill for calling codex-companion.mjs
    │   └── gpt-5-4-prompting/         # Prompt tightening helper
    ├── scripts/                      # Runtime Node executables
    │   ├── codex-companion.mjs       # Main CLI
    │   ├── app-server-broker.mjs     # Unix socket broker
    │   ├── session-lifecycle-hook.mjs
    │   └── stop-review-gate-hook.mjs
    ├── schemas/
    │   └── review-output.schema.json
    └── lib/                          # 15 shared modules
        ├── app-server.mjs            # CodexAppServerClient
        ├── app-server-protocol.d.ts  # RPC method + type defs
        ├── codex.mjs                # Turn capture, thread management
        ├── broker-lifecycle.mjs
        ├── state.mjs, job-control.mjs, tracked-jobs.mjs
        └── render.mjs, git.mjs, prompts.mjs, args.mjs, fs.mjs, workspace.mjs
```

## Slash Command Definition

Each `commands/*.md` has YAML frontmatter + markdown body:

```yaml
---
description: Run a Codex code review against local git state
argument-hint: '[--wait|--background] [--base <ref>] [--scope auto|working-tree|branch]'
disable-model-invocation: true
allowed-tools: Read, Glob, Grep, Bash(node:*), Bash(git:*), AskUserQuestion
---
```

The body is the prompt that runs when the command fires. `$ARGUMENTS` is the raw user input. `$CLAUDE_PLUGIN_ROOT` points to the plugin directory.

## Subagent Delegation (`Agent` tool)

The key delegation mechanism uses the `Agent` tool with `subagent_type`:

```yaml
# commands/rescue.md frontmatter
allowed-tools: Bash(node:*), AskUserQuestion, Agent
---

# Body calls:
Agent({ subagent_type: "codex:codex-rescue", prompt: "$ARGUMENTS" })
```

The subagent definition:

```yaml
# agents/codex-rescue.md
name: codex-rescue
model: sonnet
tools: Bash
skills:
  - codex-cli-runtime
  - gpt-5-4-prompting
```

The subagent is a thin forwarder with zero independent reasoning — one `Bash` call to the companion script, return stdout verbatim.

## JSON-RPC Protocol

### Transport: Two Modes

`CodexAppServerClient` in `app-server.mjs` has two transport implementations:

**Spawned mode**: Spawns `codex app-server` as a child process with stdio pipes. Direct 1:1 connection.

**Broker mode**: Connects to a Unix domain socket broker (`app-server-broker.mjs`) that multiplexes multiple clients through one Codex app server. Only one request runs at a time; concurrent requests get `BROKER_BUSY_RPC_CODE = -32001`.

### RPC Methods

Defined in `app-server-protocol.d.ts`:

| Method | Purpose |
|---|---|
| `initialize` | Handshake — client info, capabilities, opt-out list |
| `thread/start` | Start a new Codex thread |
| `thread/resume` | Resume an existing thread |
| `thread/name/set` | Name a thread |
| `thread/list` | List threads |
| `review/start` | Run a review (targets: `uncommittedChanges`, `baseBranch`) |
| `turn/start` | Send a prompt turn |
| `turn/interrupt` | Interrupt an active turn |

Server→client notifications: `turn/completed`, `item/agentMessage/delta`, `item/reasoning/summaryTextDelta`, etc.

### Turn Capture

`runAppServerTurn()` in `codex.mjs` captures the full turn lifecycle:

```
turn/start → [item/reasoning/* delta events] → [item/agentMessage/delta events] → turn/completed
```

Returns:
- `finalMessage` (string)
- `touchedFiles` (array of ThreadItem)
- `reasoningSummary` (string[])
- `stderr`
- `threadId`, `turnId`

`runAppServerReview()` is specialized for review tasks — uses `review/start` protocol method instead of `turn/start`.

## Job Tracking

Jobs persisted as JSON files in `{workspace}/.codex-companion/jobs/{jobId}.json`:

```typescript
interface JobRecord {
  id: string;           // "task-abc123"
  kind: "task" | "review" | "adversarial-review";
  kindLabel: "rescue" | "review" | "adversarial-review";
  title: string;
  workspaceRoot: string;
  threadId: string;    // Codex thread ID for resumption
  turnId: string;
  status: "queued" | "running" | "completed" | "cancelled" | "failed";
  phase: string;
  pid: number | null;
  logFile: string;
  request: object;
  completedAt: string | null;
}
```

Background tasks: spawned as detached processes (`detached: true, stdio: 'ignore'`) running `codex-companion.mjs task-worker --job-id ...`.

## Review Gate Hook

Optional Stop-time review gate registered in `hooks/hooks.json`:

```json
{
  "Stop": [{
    "hooks": [{
      "type": "command",
      "command": "node \"${CLAUDE_PLUGIN_ROOT}/scripts/stop-review-gate-hook.mjs\"",
      "timeout": 900
    }]
  }]
}
```

When Claude Code's main turn fires a `Stop`, the hook triggers a Codex review of the previous assistant message. If the review finds issues, the stop is blocked and Claude re-enters the turn to address them first.

## Key Design Insights

1. **Thin forwarding layers** — `codex:codex-rescue` subagent does zero independent reasoning. Shapes the prompt, calls companion script once, returns stdout unchanged.

2. **Stateless plugin, stateful runtime** — Plugin has no state; job tracking, thread IDs, progress are persisted to disk. Plugin reload doesn't lose in-progress Codex work.

3. **Broker enables sharing** — Unix socket broker means Claude Code and user's own `codex` CLI share the same app server instance, same auth, same workspace. Only one turn runs at a time per broker.

4. **Review vs. task as protocol variation** — `/codex:review` maps to `review/start` (built-in Codex reviewer). `/codex:adversarial-review` maps to `turn/start` with custom adversarial prompt — goes through general turn flow, not the review pipeline.

5. **Structured output via schema** — Adversarial review uses `outputSchema: readOutputSchema(REVIEW_SCHEMA)` to force Codex to return machine-parseable JSON with `{ summary, findings: [...] }`.

## Related
- [[openai-codex-plugin-cc]] — related entity from frontmatter; explicit cross-link
