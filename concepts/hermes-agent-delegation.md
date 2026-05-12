---
title: "Hermes Agent Delegation"
created: "2026-05-09"
updated: 2026-05-10
type: "concept"
tags: [hermes-agent, multi-agent, delegation, orchestration, agentic-ai]
sources: [raw/articles/xarticle-neoaiforecast-2051591568696782935.md]
related_entity: [[hermes-agent]]
author: [[neo-ai-forecast]]
---

## Summary

Hermes Agent's multi-agent delegation feature allows a parent agent to spin up focused child agents, assign each a scoped task, collect their results, and produce a cleaner final answer. This makes Hermes feel less like a chatbot and more like an actual agent runtime.

## Key Concepts

### The Delegation Model

The core principle is **task decomposition into workstreams**: research, planning, implementation, debugging, writing, verification, and synthesis each become isolated child-agent jobs rather than competing for a single context window.

**Parent agent = project lead**
**Subagents = focused specialists**

The parent decides what needs to happen, sends independent tasks to child agents, and receives their final results without flooding its own working memory with every intermediate step.

### Control Surfaces

Hermes defaults to **controlled delegation**:
- Child agents are typically **leaf workers** — they do their assigned job and report back
- They are **not allowed to recursively spawn** infinite agent trees
- Deeper orchestration is an **explicit operator choice**, not hidden behavior

For advanced users, `max_spawn_depth: 2` and `role="orchestrator"` can unlock deeper agent trees.

### When to Delegate

A good rule: delegate when the task needs **2+ of these**:
1. Independent research (multiple sources/docs/claims to verify)
2. Different expert lenses (security, performance, UX, architecture, etc.)
3. Large code/document review (too much context for one pass)
4. Parallel options (competing approaches to evaluate)
5. Final synthesis (one polished answer after multiple investigations)
6. Lower context pollution (keep parent focused on decisions, not raw details)

### Practical Example: Code Review Team

```plaintext
Review this branch like a small engineering team.
Use separate workstreams:
1. One subagent checks correctness and edge cases.
2. One subagent checks security-sensitive areas.
3. One subagent checks tests and coverage gaps.
4. Then synthesize the top issues into a prioritized action plan.
```

Each subagent stays focused in its own isolated context. The final answer is cleaner because the work underneath was cleaner.

## Why This Matters

**Normal chatbots** operate a single conversational loop: ask → answer → correct → try again.

**Hermes** is closer to an operating layer for agentic work. The shift is from "chat with a model" to "operate an agent."

This is the difference between:
- Answer generators (one model trying to do everything)
- Managed workflows (structured task decomposition and result synthesis)

## The Bigger Picture

The future of AI agents is not one giant chatbot with a bigger context window. It will look more like **runtimes** with:

- memory
- skills
- tools
- schedules
- profiles
- messaging surfaces
- model routing
- subagent delegation
- operator controls

## Related

- [[hermes-agent]] — the agent this delegation feature belongs to
- [[multi-agent-kanban-orchestration]] — durable task-board coordination for multi-agent work
- [[hermes-memory-architecture]] — Tony Simons' 11-layer memory stack including delegation patterns
- [[context-os]] — layered infrastructure approach to agent memory
- [[personal-ai-agent-architecture]] — personal AI agent setups
- [[vmiss]] — 4-agent Hermes setup (related multi-agent pattern)