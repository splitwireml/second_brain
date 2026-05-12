---
title: "Deep Agents Evals"
created: 2026-04-11
updated: 2026-04-11
type: concept
tags: [agent, evaluation]
sources: [raw/articles/x-bookmarks-2026.md, raw/articles/x-bookmarks-weekly.md]
---

# How We Build Evals for Deep Agents

## Source

Viv (`@Vtrivedy10`) on X — thread on building evaluation frameworks for deep/compound AI agents.

## Overview

Deep agents — agents that compose multiple capabilities over long horizon tasks — require fundamentally different evaluation approaches than single-turn or simple sequential agents.

## Key Challenges

1. **Credit assignment** — which step in a 50-step agentic trace caused the eventual failure?
2. **Partial success** — an agent can be "mostly right" in a way that's hard to score binary pass/fail
3. **Environment diversity** — agents behave differently across codebase styles, domain contexts, tool availability
4. **Human evaluation cost** — the traces that matter most (complex, multi-step) are the most expensive to have humans label

## Common Approaches

### Synthetic Evals
Generate eval cases programmatically using LLMs (e.g., ask GPT-4 to generate challenging agent tasks)

### Unit Test Adherence
Use existing unit/integration tests as ground-truth — does the agent's code change pass the suite?

###_checkpoint Scoring
Evaluate at intermediate steps in the agentic trace (every N steps), not just the final outcome.

### Weighted Rubrics
Define a rubric of subtasks; each has a weight; final score is weighted sum. Enables partial credit.

## Relevance to This Wiki

Building reliable AI agents (like those in [[vibe-kanban-agent-spawning]], [[paperclipai-paperclip]], [[gsd-2-ai-vibe-coding-framework]]) requires systematic evals. The evaluation infrastructure is often the bottleneck to shipping agentic products.

## See Also

- [[vibe-kanban-agent-spawning]] — agent spawning that would benefit from evals
- [[paperclipai-paperclip]] — production agent deployment where evals are critical
- [[gsd-2-ai-vibe-coding-framework]] — vibe coding agents needing eval frameworks
- [[research-code-agent-cli-automation]] — CLI agents and their evaluation challenges
