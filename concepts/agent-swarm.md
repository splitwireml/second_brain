---
title: Agent Swarm
created: 2026-05-04
updated: 2026-05-04
type: concept
tags: [ai-agent, multi-agent, architecture, coordination]
sources: [raw/articles/thread-defileo-2050656413006053793.md]
related_entity: [[moonshot-ai]]
---

# Agent Swarm

Multi-agent architecture pattern where a **coordinator agent** spins up dozens or hundreds of **sub-agents** working in parallel, each handling a piece of a larger task, with results reported back to and merged by the coordinator.

## Key Distinction from Single-Agent AI

Most AI systems operate as a single worker handling one task at a time sequentially. Agent swarm architectures fundamentally change this by enabling:

- **Parallel execution**: hundreds of sub-agents simultaneously
- **Specialized roles**: each sub-agent handles a specific slice of the task
- **Coordinated synthesis**: main agent merges outputs into a coherent result

## Spec-Driven Prompting

The critical unlock for agent swarms is treating prompts not as instructions but as **specifications** (spec-driven prompting):

- Write a 2-3 page markdown file defining data to collect, valid sources, output format, conflict resolution rules
- The swarm executes against the spec while the user works on something else
- Prompts written at the wrong abstraction level cause the "fragile" behavior incorrectly attributed to swarms

## Examples

- **Web agency**: 5 sub-agents scraping Google Maps/Yellow Pages, evaluating site quality, generating mockups, drafting outreach, producing market analysis — all in one 40-minute prompt
- **Data scraping**: Regional batch agents validating 1,500+ rows against live sources in parallel
- **Code optimization**: 12-hour autonomous run with 1,000+ tool calls, 4,000+ lines modified across 12 strategies

## Implementations

- **[[kimi-k2.6]]** — 300 sub-agents, 4,000 coordinated steps (from K2.5's ~100 sub-agents, ~1,300 steps)

## Related

- [[kimi-k2.6]] — Primary implementation
- [[moonshot-ai]] — Publisher of swarm-capable models
- [[defileo]] — Author who documented the swarm architecture for K2.6
