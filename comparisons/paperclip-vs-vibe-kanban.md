---
title: Paperclip vs Vibe Kanban
created: 2026-04-10
updated: 2026-04-10
type: comparison
tags: [orchestration, agent, comparison]
sources: [raw/articles/paperclipai-technical-research-2026-04-10.md, raw/articles/paperclip-vs-vibe-kanban-agent-spawning-agent-control-comparison-2026-04-10.md, concepts/paperclipai-paperclip, concepts/vibe-kanban-agent-spawning]
---

# Paperclip vs Vibe Kanban — Agent Control Architecture Comparison

## Quick Summary

Both orchestrate multiple AI coding agents (Claude Code, Codex, OpenCode) from a dashboard. Paperclip is a **business control plane** (budgets, org charts, approval gates). Vibe Kanban is a **parallel coding agent runner** (git worktrees, kanban, PR review).

## Key Differences

| | Paperclip | Vibe Kanban |
|--|-----------|-------------|
| **Language** | TypeScript/Node.js | Rust (backend) |
| **Agent abstraction** | TypeScript adapter packages | Rust trait + `enum_dispatch` |
| **Spawn model** | `runChildProcess()` Promise | `tokio::process::Command` |
| **Exit detection** | Process exit + timeout | Dual-mode: `oneshot` + `try_wait()` polling |
| **Claude Code reliability** | Works (stdout parsed after exit) | **BROKEN** — sessions stuck forever (bug #2495) |
| **Workspace isolation** | Experimental (env vars + git worktree) | Native Rust git worktree manager |
| **Skills injection** | Tmpdir symlinks per-run | Worktree `.claude/skills/` per-task |
| **Agent communication** | Issue/comment + @-mentions | Kanban card state + WebSocket |
| **Human approval gates** | Yes (board + approvals) | PR review after-the-fact |
| **Cost tracking** | Built-in (per-agent token budgets) | **Not built-in** |
| **Org chart / company model** | Yes | No |
| **Hermes support** | Plugin adapter (`@henkey/hermes-paperclip-adapter`) | Via custom executor RFC |
| **Primary use case** | Run an AI company | Parallelize coding agents |

## Architecture Deep Dive

### Spawning
- **Paperclip:** Node.js `child_process` spawn, Promise-based, `stream-json` parsed after exit. Supports `--resume` for session continuity. OpenCode uses HTTP server pattern.
- **Vibe Kanban:** Rust `tokio::process::Command`, `AsyncGroupChild` for process groups. ACP harness for JSON-RPC agents. Only Codex has reliable exit signaling.

### Exit Detection
- **Paperclip:** Relies on process termination or `timeoutSec` kill. Simple but effective for agents that exit.
- **Vibe Kanban:** Dual-mode — `oneshot` channel (if executor supports it) or OS polling every 250ms. Claude Code returns `exit_signal: None` — sessions hang forever.

### Workspace Isolation
- **Paperclip:** Introduced as experimental feature in v2026.403.0. Workspace lifecycle managed via env vars (`PAPERCLIP_WORKSPACE_*`). Agent controls workspace runtime.
- **Vibe Kanban:** Git worktree isolation is native and mature. Each task gets a branch + worktree. Cleanup is `git worktree remove --force`.

### Session Resume
- **Paperclip:** `sessionId` stored in DB, passed back via `--resume` CLI flag on next heartbeat.
- **Vibe Kanban:** `spawn_follow_up()` takes `session_id`, uses Codex `thread_fork` for continuation.

## See Also

- [[paperclipai-paperclip]] — Paperclip orchestration platform
- [[vibe-kanban-agent-spawning]] — Vibe Kanban agent spawning architecture

## Related

- [[paperclipai-paperclip]] — Paperclip standalone
- [[vibe-kanban-agent-spawning]] — Vibe Kanban standalone
- [[research-code-agent-cli-automation]] — Claude Code, Codex, OpenCode CLI interfaces
