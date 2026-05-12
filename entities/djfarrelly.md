---
title: Dan Farrelly | Inngest.com
created: 2026-05-10
updated: 2026-05-10
type: entity
tags: [person, content-creator, x-creator, ai-infra, orchestration, inngest]
sources: [raw/articles/xarticle-djfarrelly-2052779234234380479.md]
---

# Dan Farrelly | Inngest.com

X creator (@djfarrelly). Co-founder of Inngest, a durable execution platform for AI agents.

## Background

Dan Farrelly posts on X about AI agent infrastructure, orchestration patterns, and durable execution. His central thesis: agent frameworks are coupling traps, and the real architectural layer that matters is durable orchestration primitives (steps, events, state, retries, observability).

## Key Work

### "Background agents are here. Your orchestration isn't ready." (2026-05-08)

Full X Article (2052779234234380479): 194 likes, 19 RTs.

Core arguments:
- Agent frameworks (LangGraph, CrewAI, AutoGen) are bets on which pattern wins — when patterns shift, you rewrite
- The five durable primitives: durable steps, persistent external state, parallel work coordination, event-driven control flow, structured execution observability
- Next pattern shift: synchronous chat agents → asynchronous background agents
- Three-layer stack: orchestration (stable), agent (fluid, 3-6mo), model (volatile, monthly)
- Sandboxes solve compute layer, not orchestration — they can't tell you which steps completed

## Published Concepts

- [[durab]] — Durable Orchestration Primitives concept (this article)
- Related: Inngest's agent patterns documentation (agent loops, HITL, delegation)

## Links

- X: https://x.com/djfarrelly
- Inngest: https://inngest.com