---
title: "Background agents are here. Your orchestration isn't ready."
author: Dan Farrelly (@djfarrelly)
authorId: "133401483"
createdAt: "Fri May 08 15:54:42 +0000 2026"
type: x-article
tags: [ai-agent, orchestration, infrastructure, durable-execution, background-agents]
platform: X
id: "2052779234234380479"
likes: 192
retweets: 18
replies: 3
url: https://x.com/i/status/2052779234234380479
---
# Background agents are here. Your orchestration isn't ready.

Every six months, the "right" way to build an AI agent changes.

We went from RAG being the consensus and everyone got their vector DBs, then to ReAct. We need virtual memory to solve this 4k context problem! Wait context windows are huge now. Now Anthropic dropped a blog post - we're prompt chaining, routing, creating orchestrator-workers! Context engineering is the real work. We need a browser for this, no MCP is the future. We're building tons of specialized sub-agents with funny human-sounding roles. Nope, models got better, generic agents with great prompts are king. Wow OpenAI jumped on MCP, it's definitely the future. CLIs are it now, MCPs are out. Now we need a sandbox, but how fast can it spin up? We are making software factories. What about syncing context across agents?...

If you coupled your infrastructure to any one of these patterns, you've already rebuilt at least twice. And you'll rebuild again.

Here's the thesis: there's a layer that doesn't change. Durable orchestration: steps, events, state, retries, observability. Every pattern listed above runs on top of these same primitives.

## The framework trap

Agent frameworks aren't libraries. They're bets on which agent pattern wins. When the pattern shifts, you don't refactor; you rewrite.

LangGraph encodes graph-based control flow as the paradigm. CrewAI encodes role-based agents. AutoGen encodes conversational multi-agent. Each is optimized for one view of how agents should work, and each becomes a liability when that view changes.

When Anthropic published their agent patterns guide, it invalidated assumptions baked into half the frameworks in the ecosystem. Their explicit advice: start with raw LLM APIs and avoid frameworks that obscure prompts and responses.

The problem isn't abstraction. Abstraction is fine. The problem is coupling. Abstract the primitives: steps, retries, state. Don't abstract the topology.

## What actually stays the same

Five primitives show up underneath every pattern:

- Durable steps - work checkpoints so an error mid-loop doesn't lose 40 minutes of progress.
- Persistent external state - survives process crashes and deployments.
- Parallel work coordination - fan-out/fan-in, parallel tool calls, sub-agent delegation.
- Event-driven control flow - pause and wait for a signal (e.g. Human-in-the-loop, cancellation) without holding a connection open.
- Structured execution observability (traces) - every step and every decision, inspectable to debug specific and broad issues.

These primitives don't encode an agent pattern. They encode execution guarantees.

## The background agent gap

The next major pattern shift is already happening: from synchronous chat agents to asynchronous background agents. This is where most infrastructure falls apart, and where durable orchestration becomes non-negotiable.

Background agents need:
- Long-running execution with crash recovery. A 45-minute agent run can't live in a Lambda with a 5-minute timeout.
- Multi-step observability. When a background agent produces a bad result 30 minutes into a run, you need to trace every step.
- Event-driven control flow. Background agents need to pause and wait for external input without blocking a thread.
- Lifecycle controls. Status, cancellation, scheduling, inspection.

## What about sandboxes?

Sandbox providers solve a different problem. They operate at the compute layer — they answer "where does the agent run?" Some pause and resume the full VM state, which is powerful, but it's a runtime snapshot, not a workflow snapshot. They can't tell you which steps completed, what they returned, or where to resume without re-executing work.

The orchestration layer should sit above the sandboxes, managing the lifecycle of sandboxes and retaining state.

## The composability argument

Durable orchestration isn't just about reliability. It's about composability. The primitives compose into patterns that don't have names yet.

When you have step.run(), step.invoke(), step.waitForEvent(), and step.sleep(), you can build things that don't fit neatly into any existing taxonomy:
- Delegate to 5 sub-agents, wait for the first 3 to complete, cancel the other 2, and synthesize partial results before continuing.
- Create autoresearch-like pipeline that runs nightly evals on agent traces, and automatically updates system prompts.
- Run the same task with two different prompt strategies in parallel, wait for both to complete, score the results.

## What this looks like in practice

The orchestration layer (stable): Durable execution, step primitives, event system, state management, observability, scheduling. This is your multi-year decision.

The agent layer (fluid): How you structure LLM calls, tool use, reasoning, delegation. This changes every 3-6 months.

The model layer (volatile): Which LLM you call, which API, which provider. This changes monthly.

## Design for the rewrite

Agent topologies have a shelf life. The one you're building now won't be the one you're running in six months.

Design around it. An orchestration layer with the right primitives enables your team to adapt quickly. Let everything above it change as fast as it needs to.

Background agents aren't coming. They're here. The only question is whether your infrastructure is ready to let them run, or whether you're about to rebuild it again.