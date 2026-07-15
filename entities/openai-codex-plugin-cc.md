---
title: openai/codex-plugin-cc
type: entity
tags: [agent-delegation, claude-code, codex, json-rpc, openai, plugin]
aliases: [codex-plugin-cc, openai/codex-plugin-cc]
created: 2026-05-18
updated: 2026-05-18
source: https://github.com/openai/codex-plugin-cc
stars: 18965
license: Apache-2.0
language: JavaScript
summary: "Use OpenAI Codex from inside Claude Code for code review and task delegation."
related_to: [Claude-Code, OpenAI-Codex, Claude-Code-Plugin-System]
---

## Overview

OpenAI's official plugin that lets Claude Code users invoke OpenAI Codex directly from their Claude Code workflow. Created 2026-03-30, 18.9k stars, Apache-2.0 license.

## Quick Install

```bash
/plugin marketplace add openai/codex-plugin-cc
/plugin install codex@openai-codex
/reload-plugins
/codex:setup
```

## Commands

| Command | Purpose |
|---|---|
| `/codex:review` | Read-only Codex review of uncommitted changes or branch diff |
| `/codex:adversarial-review` | Steerable challenge review with custom focus text |
| `/codex:rescue` | Delegate a task to Codex (investigate, fix, continue) |
| `/codex:status` | Check running/completed job status |
| `/codex:result` | Fetch stored output of a finished job |
| `/codex:cancel` | Cancel an active background Codex job |
| `/codex:setup` | Check Codex install/auth status, manage review gate |

## Key Files

- `plugins/codex/scripts/codex-companion.mjs` — Main CLI entry point (setup, review, task, status, result, cancel, task-worker, cancel)
- `plugins/codex/scripts/app-server-broker.mjs` — Unix socket broker that multiplexes clients through one Codex app server
- `plugins/codex/scripts/lib/app-server.mjs` — CodexAppServerClient (Spawned + Broker transport modes)
- `plugins/codex/scripts/lib/app-server-protocol.d.ts` — JSON-RPC 2.0 method definitions
- `plugins/codex/scripts/lib/codex.mjs` — Turn capture, thread management, review execution
- `plugins/codex/commands/rescue.md` — Delegation command (uses Agent tool with subagent_type: codex:codex-rescue)
- `plugins/codex/agents/codex-rescue.md` — Thin forwarding subagent (zero independent reasoning)
- `plugins/codex/hooks/hooks.json` — Stop hook for optional review gate

## Runtime Architecture

- **Direct mode**: Spawns `codex app-server` as child process, communicates via stdio JSON-RPC
- **Broker mode**: Unix domain socket broker (`app-server-broker.mjs`) shares one Codex app server across multiple clients
- **Protocol**: JSON-RPC 2.0 over stdio or Unix socket — methods: `thread/start`, `thread/resume`, `review/start`, `turn/start`, `turn/interrupt`
- **Auth**: Uses local `codex` CLI auth (same account as user's own Codex install)

## Delegation Flow

```
Claude Code user → /codex:rescue investigate the flaky test
  → rescue.md command (checks for resumable threads via AskUserQuestion)
  → Agent tool with subagent_type: "codex:codex-rescue"
  → codex-rescue subagent (model: sonnet, tools: Bash, skills: codex-cli-runtime)
  → codex-cli-runtime skill
  → Bash: node "${CLAUDE_PLUGIN_ROOT}/scripts/codex-companion.mjs" task "investigate the flaky test"
  → CodexAppServerClient.request("thread/start", ...) → Codex app server
  → Result streamed back via turn/completed notifications
  → stdout returned verbatim to user
```

## Job Tracking

Jobs stored as JSON in `{workspace}/.codex-companion/jobs/{jobId}.json`:
- Fields: id, kind, title, threadId, turnId, status, pid, logFile, request payload
- Background tasks spawned as detached processes running `task-worker` subcommand
- `/codex:status` polls job files; `/codex:result` reads stored payload