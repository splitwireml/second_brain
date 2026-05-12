---
title: Multi-Agent Kanban Orchestration
created: 2026-05-05
updated: 2026-05-05
type: concept
tags: [orchestration, ai-agent, multi-agent, workflow-automation]
sources: [raw/articles/xarticle-hermes-kanban-turns-multi-agent-work-into-a-real-b-2051443615768228062.md]
related_entity: [[hermes-kanban]]
author: [[neo-ai-forecast]]
---

# Multi-Agent Kanban Orchestration

A multi-agent coordination pattern where work is expressed as a durable task board with named profiles, dependency links, and run history — rather than ephemeral parent-child function calls. Each task persists as a first-class row in a SQLite database, surviving context compression, crashes, and restarts.

## Core Idea

Standard multi-agent workflows collapse all subagent work back into a single parent response. This works for short, synchronous tasks but breaks down when:

- A worker blocks and needs to surface why
- A reviewer rejects an implementation and the next run needs to know what failed
- A process crashes mid-run and someone needs to reclaim the task
- A human wants to inspect progress without reading agent logs

Kanban orchestration solves this by making task state external and durable — not trapped inside a chat context window.

## Mechanism

1. **Tasks are assigned to named profiles** (e.g. `researcher`, `writer`, `backend-dev`, `reviewer`, `ops`). The dispatcher spawns a full worker process for each assigned task.

2. **Dependencies are explicit links** — `kanban_link` connects parent tasks to children. When a parent completes, the dependency engine promotes eligible children from `todo` → `ready`.

3. **Each attempt is a run row** — prior block reasons and crash logs are visible to the next worker, so retries don't blindly repeat failed paths.

4. **Workers interact via gated tools** — `kanban_show`, `kanban_block`, `kanban_complete`, etc. are injected into the worker's schema only when `HERMES_KANBAN_TASK` is set. Normal sessions carry no Kanban tool bloat.

## Workflow Shapes

Kanban orchestration is especially suited for:

- **Research fan-out**: multiple researcher profiles collect in parallel → analyst synthesizes → writer drafts → reviewer checks
- **Engineering pipelines**: specifier → implementer → reviewer → writer → publisher
- **Human-in-the-loop ops**: worker blocks when it needs a credential or approval; human unblocks via CLI or `/kanban unblock`
- **Fleet farming**: one specialist profile drains many similar tasks (transcripts, translations, triage)
- **Scheduled ops**: cron creates recurring tasks with idempotency keys — board becomes a durable operational journal
- **Digital twins**: named profiles (`inbox-triage`, `researcher`, `ops-review`) accumulate memory and handle recurring domains

## Key Properties

| Property | Description |
|---|---|
| Persistence | Tasks survive context compression, restarts, crashes |
| Inspectability | Run history, block reasons, comments are queryable |
| Durability | Workers are named profiles, not anonymous ephemeral calls |
| Recoverability | Crash detection + stale claim reclamation + retry history |
| Human oversight | CLI, slash commands, and dashboard for real-time board interaction |

## vs. delegate_task

`delegate_task` is a function call — parent spawns a subagent and waits for a short answer. Kanban is a durable work queue plus state machine. Use `delegate_task` when you need a quick answer. Use Kanban when work needs persistence, retry, visibility, human input, or multiple role handoffs over time.

## Related

- [[hermes-kanban]] — the entity implementing this pattern
- [[hermes-agent]] — the parent platform
- [[agent-swarm]] — alternative multi-agent pattern
- [[delegate_task]] — contrasting ephemeral subagent call pattern
