---
title: Hermes Kanban
created: 2026-05-05
updated: 2026-05-05
type: entity
tags: [ai-agent, orchestration, nous-research, multi-agent]
sources: [raw/articles/xarticle-hermes-kanban-turns-multi-agent-work-into-a-real-b-2051443615768228062.md]
related_concepts: [[multi-agent-kanban-orchestration]]
author: [[neo-ai-forecast]]
---

# Hermes Kanban

SQLite-backed durable task board built into [Hermes Agent]([[hermes-agent]]). Turns multi-agent work from invisible function calls into an inspectable, persistent coordination layer with named worker profiles, dependency tracking, retry history, and human-in-the-loop support.

## What It Is

Hermes Kanban solves the visibility problem in standard multi-agent setups. In a typical fork-and-join pattern, subagents run inside a parent context — their state, failures, and handoffs are invisible. Kanban makes every task a first-class durable row in a SQLite database, with run history, comments, and dependency links that survive context compression, crashes, and restarts.

Default board location: `~/.hermes/kanban.db`

Multi-board support (one database per project/repo/client):
```
~/.hermes/kanban/boards/<slug>/kanban.db
```

## Board Model

- **Board** — isolated queue per project or domain
- **Task** — unit of work with title, body, assignee, priority, tenant, status
- **Link** — parent-to-child dependency between tasks
- **Comment** — durable human or agent notes
- **Run** — one worker attempt on a task
- **Workspace** — where the worker operates
- **Dispatcher** — loop that promotes and claims ready work

## Task Statuses

```
triage → todo → ready → running → blocked → done → archived
```

- **triage**: raw ideas
- **todo**: dependency-waiting
- **ready**: eligible to run
- **running**: claimed by a worker
- **blocked**: needs human input or credential
- **done**: completed
- **archived**: old tasks

## Named Profiles

Tasks are assigned to Hermes profiles (e.g. `researcher`, `writer`, `backend-dev`, `reviewer`, `ops`). When the dispatcher picks up a ready task, it spawns that profile as a full worker process with its own identity, memory, skills, toolsets, and operating context. This is different from anonymous subagent calls — the worker is persistent and accountable.

## Dispatcher Location

The dispatcher runs inside the Hermes gateway by default (`hermes gateway start`), waking every 60 seconds to:
1. Reclaim stale claims
2. Detect crashed workers
3. Promote dependency-satisfied tasks
4. Claim ready tasks atomically
5. Spawn the assigned profile
6. Pin the worker to the correct board

Old standalone daemon mode (`hermes kanban daemon --force`) is deprecated.

## Human Interfaces

1. **CLI**: `hermes kanban list`, `hermes kanban show`, `hermes kanban comment`, `hermes kanban unblock`, `hermes kanban stats`
2. **Slash commands in chat**: `/kanban list`, `/kanban create`, `/kanban --board <slug> list`
3. **Dashboard**: `hermes dashboard` → Kanban tab with columns, filters, drag-and-drop, run history, and live task events

## Worker Tool Interface

Workers use dedicated `kanban_*` tools inside their own process (not shell commands):
```
kanban_show, kanban_complete, kanban_block, kanban_heartbeat,
kanban_comment, kanban_create, kanban_link
```

These tools only appear when `HERMES_KANBAN_TASK` is set — normal Hermes sessions carry no Kanban schema bloat.

## Retry and Failure Handling

Each task attempt is stored as a run row. Retried tasks inherit prior run history (block reasons, crash logs, etc.) so workers don't repeat failed paths. Tasks that repeatedly fail to spawn eventually auto-block with the last error (`spawn_failed` → `gave_up`), rather than looping silently.

## Key Difference from delegate_task

- `delegate_task`: function call — parent waits for a short answer back
- `Kanban`: durable work queue + state machine — work persists, retries, and survives context compression

## Related

- [[hermes-agent]] — the parent platform
- [[multi-agent-kanban-orchestration]] — the coordination pattern this enables
- [[neo-ai-forecast]] — author of the source article
