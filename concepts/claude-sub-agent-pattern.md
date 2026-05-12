---
title: Claude Sub-Agent Pattern
created: 2026-05-12
updated: 2026-05-12
type: concept
tags: [ai-agent, claude, sub-agent, orchestration, multi-agent, architecture]
sources: [raw/articles/xarticle-KeshWelch-2052486245218177361.md, raw/articles/thread-defileo-2050656413006053793.md, concepts/agent-swarm.md, concepts/agent-orchestration-patterns.md]
related_entity: [[KeshWelch, defileo, kimi-k2.6]]
author: [[KeshWelch]]
---

# Claude Sub-Agent Pattern

A multi-agent architecture pattern where a **coordinator agent** (typically Claude Opus) manages multiple specialized sub-agents, each handling a distinct domain or task type. The coordinator routes work, synthesizes results, and maintains coherent state across the agent system.

## Core Architecture

```
┌─────────────────────────────────────────────┐
│         Coordinator Agent (Claude Opus)       │
│  - Persistent memory of all tasks/entities   │
│  - Routes work to specialized sub-agents    │
│  - Synthesizes outputs, ensures nothing     │
│    falls through the cracks                 │
└──────────────┬──────────────────────────────┘
               │
       ┌───────┴───────┬─────────┬─────────┐
       ▼               ▼         ▼         ▼
   ┌────────┐    ┌──────────┐ ┌───────┐ ┌──────────┐
   │Sub-Agent│    │Sub-Agent │ │Sub-   │ │Sub-Agent │
   │  Type 1 │    │  Type 2  │ │Agent 3│ │  Type N  │
   └────────┘    └──────────┘ └───────┘ └──────────┘
```

## Key Properties

| Property | Description |
|---|---|
| **Specialization** | Each sub-agent has one focused job with explicit rules |
| **Autonomy boundaries** | Sub-agents know what they can do autonomously vs. what needs human approval |
| **Coordinator sovereignty** | The coordinator doesn't do the work itself—it routes and synthesizes |
| **Spec-driven prompts** | Sub-agents execute against detailed specs, not one-liners |

## Pattern Variants

### 5-Sub-Agent Pattern (Chief of Sales)
From [[KeshWelch]]'s Chief of Sales architecture:
1. **Inbound responder** — Speed-to-lead, <90 second response
2. **Follow-up sequencer** — Post-call custom follow-ups from transcript
3. **CRM autopilot** — Updates, stage progression, contact refresh
4. **Enrichment + brief writer** — LinkedIn, funding, tech stack signals
5. **Knowledge base / FAQ** — Answers prospect questions in rep's voice

### Agent Swarm Pattern (Kimi K2.6)
- **300 sub-agents** working in parallel
- **4,000 coordinated steps** per run
- Coordinator spins up dozens/hundreds working simultaneously
- Each handles a regional batch or specialized slice
- Results reported back and merged by coordinator

### Kanban Orchestration Pattern (Hermes)
- Tasks are durable rows in SQLite, not ephemeral parent-child calls
- Named profiles for workers (`researcher`, `writer`, `backend-dev`, `reviewer`)
- Dependencies are explicit links between tasks
- Block reasons and crash logs visible to next worker for retry logic

## Spec-Driven Prompting

The critical unlock for sub-agent systems is treating prompts as **specifications**:

```
Instead of: "scrape all dentists in Toronto"
Write:       2-3 page markdown defining:
             - What data to collect (name, address, website status, etc.)
             - What counts as valid source
             - What sources are acceptable
             - Output format requirements
             - Conflict resolution rules
```

The swarm executes against the spec while you work on something else.

## Architecture Layering

From the Chief of Sales architecture (7-layer):

1. **Orchestrator** — Claude Opus at center with persistent memory
2. **Integrations** — Gmail/CRM/calendar/Gong/Slack/enrichment tools
3. **Sub-agents** — Specialized prompts with explicit autonomy rules
4. **Rep workspace** — Slack channel per segment with action posts
5. **Closer flow** — Daily feed of calls, recoveries, pending proposals
6. **Human approval gate** — Draft mode for first 2 weeks
7. **Measurement** — Metrics tracking for continuous tuning

## Orchestration vs. Delegation

| Pattern | Use Case | Behavior |
|---|---|---|
| **delegate_task** | Quick answer needed | Ephemeral parent-child call, waits for short answer |
| **Sub-agent pattern** | Work needs persistence, retry, visibility, multiple handoffs | Coordinator manages durable tasks with state |

## Metrics Impact (Sales Example)

| Metric | Before | After |
|---|---|---|
| Speed-to-lead | 17 hours | 90 seconds |
| Reply-to-booking | 31% | ~60% |
| Show rate | 35% | ~60% |
| Close rate | 22% | ~30% |
| **Combined multiplier** | — | **~4.7x pipeline** |

## Related Concepts

- [[agent-swarm]] — Coordinator + parallel sub-agent pattern with 300 agents
- [[agent-orchestration-patterns]] — Four patterns: Sequential Pipeline, Parallel Fan-Out, Hierarchical Supervisor-Worker, Reflexive Self-Correcting
- [[chief-of-sales-ai-agent-architecture]] — KeshWelch's 7-layer sales-specific implementation
- [[hermes-agent-personal-multi-agent-architecture]] — 4-agent crew with specialized roles
- [[multi-agent-kanban-orchestration]] — Durable task board pattern for multi-agent coordination
- [[kimi-k2.6]] — Reference implementation with 300 sub-agents
- [[defileo]] — Author who documented the swarm architecture for K2.6

## Sources

- [Claude Opus, $10m chief of sales - KeshWelch](https://x.com/i/status/2052486245218177361) — 2026-05-07; 102 likes
- [The power of Kimi K2.6 most people are sleeping on - Defileo](https://x.com/defileo/status/2050656413006053793) — 2026-05-02; 210 likes