---
title: Agent Swarm
created: 2026-05-04
updated: 2026-06-11
type: concept
tags: [agent, ai-agent, multi-agent, architecture, coordination]
sources: [raw/articles/thread-defileo-2050656413006053793.md, raw/articles/xarticle-youre-not-slow-youre-single-threaded-a-complete-gu-2059320043478081976.md]
related_entity: [[moonshot-ai]]
---

# Agent Swarm

Multi-agent architecture pattern where a **coordinator agent** spins up dozens or hundreds of **sub-agents** working in parallel, each handling a piece of a larger task, with results reported back to and merged by the coordinator.

## Key Distinction from Single-Agent AI

Most AI systems operate as a single worker handling one task at a time sequentially. Agent swarm architectures fundamentally change this by enabling:

- **Parallel execution** — many independent subtasks run at once instead of waiting in one queue
- **Specialized roles** — each sub-agent handles a specific slice of the task
- **Coordinated synthesis** — the main agent merges outputs into a coherent result
- **Memory isolation** — workers keep scoped context so early findings do not get pushed out of a single giant thread

## Why Single-Agent Loops Stall

Rohit's framing is useful even outside Kimi: the real bottleneck is often not model IQ but a single-threaded layout.

- **Time fails first** — fifty independent subtasks run 50× slower in series than in parallel.
- **Memory fails second** — one context window becomes one overloaded desk.
- **Handoffs stay manual** — the human becomes project manager for the machine, splitting work and ferrying outputs between chats.

A swarm removes the human from most of that glue work by making coordination its own first-class job.

## Spec-Driven Prompting

The critical unlock for agent swarms is treating prompts not as instructions but as **specifications**:

- Write a markdown brief defining the job, valid sources, output format, and conflict rules.
- Let the orchestrator turn that brief into worker assignments.
- Re-run weak slices surgically rather than restarting the whole job.

Prompts written at the wrong abstraction level cause the “fragile” behavior often blamed on swarms.

## Examples

- **Web agency** — sub-agents scrape directories, evaluate sites, generate mockups, draft outreach, and summarize the market in parallel.
- **Data scraping** — regional or company-level workers validate large datasets against live sources simultaneously.
- **Code optimization** — many search / implementation strategies run side by side while the coordinator keeps the best edits.
- **Competitive research** — one orchestrator decomposes dozens of companies or sources into independent worker jobs and returns a finished folder instead of a single long chat reply.

## Implementations

- **[[kimi-k2.6]]** — 300 sub-agents, 4,000 coordinated steps
- **[[claude-sub-agent-pattern]]** — coordinator + specialist worker pattern in Claude-centric stacks

## Related

- [[kimi-k2.6]] — primary high-scale implementation in the current wiki
- [[moonshot-ai]] — publisher of swarm-capable models
- [[defileo]] — author who first documented the K2.6 swarm architecture in the wiki
- [[rohit]] — later source emphasizing throughput, memory, and handoff bottlenecks
