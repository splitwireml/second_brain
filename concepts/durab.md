---
title: Durable Orchestration Primitives
created: 2026-05-10
updated: 2026-05-10
type: concept
tags: [agents, orchestration, durable-execution, background-agents, framework-trap, inngest]
sources: [raw/articles/xarticle-djfarrelly-2052779234234380479.md]
related_entity: [[djfarrelly]]
related_concepts:
  - agent-orchestration-patterns
  - multi-agent-kanban-orchestration
  - agent.md
  - company-brain
  - agent-swarm
author: [[djfarrelly]]
---

# Durable Orchestration Primitives

The thesis: there's a layer that doesn't change as agent patterns evolve. **Durable orchestration** — steps, events, state, retries, observability — underlies every pattern (ReAct, planning, multi-agent, etc.). If you have this layer covered, changing agent patterns is easier. Get it wrong, every pattern shift is a rewrite or a migration.

## Core Argument: The Framework Trap

Agent frameworks aren't libraries. They're bets on which agent pattern wins. When the pattern shifts, you don't refactor; you rewrite:

- **LangGraph** — encodes graph-based control flow as the paradigm
- **CrewAI** — encodes role-based agents
- **AutoGen** — encodes conversational multi-agent (now in maintenance mode as Microsoft shifted to Microsoft Agent Framework)

When Anthropic published their agent patterns guide, it invalidated assumptions baked into half the frameworks. Their advice: start with raw LLM APIs and avoid frameworks that obscure prompts and responses.

The problem isn't abstraction — it's **coupling**. Abstract the primitives: steps, retries, state. Don't abstract the topology.

## The Five Primitives

These appear underneath every pattern:

1. **Durable steps** — work checkpoints so an error mid-loop doesn't lose 40 minutes of progress
2. **Persistent external state** — survives process crashes and deployments
3. **Parallel work coordination** — fan-out/fan-in, parallel tool calls, sub-agent delegation
4. **Event-driven control flow** — pause and wait for a signal (e.g. Human-in-the-loop, cancellation) without holding a connection open
5. **Structured execution observability (traces)** — every step and every decision, inspectable

These primitives encode **execution guarantees**, not agent patterns. You compose them into whatever pattern you need today and recompose when the pattern changes tomorrow.

## The Background Agent Gap

The next major pattern shift: from synchronous chat agents to asynchronous background agents. This is where most infrastructure falls apart.

Background agents need:
- **Long-running execution with crash recovery** — can't live in Lambda with 5-minute timeout or in-memory on a single process
- **Multi-step observability** — trace every LLM call, tool invocation, decision point, sub-agent delegation
- **Event-driven control flow** — sleep and be woken up without blocking a thread
- **Lifecycle controls** — status, cancellation, scheduling, inspection

## Sandboxes vs. Orchestration

Sandbox providers solve a different problem — they answer "where does the agent run?" They're a runtime snapshot, not a workflow snapshot. They can't tell you which steps completed or where to resume without re-executing work that already succeeded.

The orchestration layer should sit **above** the sandboxes, managing the lifecycle of sandboxes and retaining state.

## Three-Layer Stack

| Layer | Stability | Changes |
|-------|-----------|---------|
| **Orchestration** (stable) | Multi-year decision | Doesn't change when agent patterns change |
| **Agent** (fluid) | 3-6 months | Application code on durable primitives |
| **Model** (volatile) | Monthly | Single line change, not architecture change |

## Key Insight

Patterns change faster than ever. They're all compositions. Frameworks encode a fixed topology and struggle to adapt. **Composable primitives** don't have that same issue.

When you have `step.run()`, `step.invoke()`, `step.waitForEvent()`, and `step.sleep()`, you can build things that don't fit neatly into any existing taxonomy.

> "You can't recompose what you can't see." — teams with strong orchestration and observability iterate faster.

## Related

- [[djfarrelly]] — author; co-founder of Inngest
- [[agent-orchestration-patterns]] — four multi-agent patterns (sequential, fan-out, hierarchical, reflexive); this concept is the durable foundation beneath those patterns
- [[multi-agent-kanban-orchestration]] — durable task board approach; shares the durability thesis but focuses on Kanban-style persistence rather than step primitives
- [[company-brain]] — related thesis: shared operational state layer for agents; durable orchestration is the infrastructure foundation for company brain
- [[agent.md]] — general AI agent concept; this extends it with the durable execution layer thesis