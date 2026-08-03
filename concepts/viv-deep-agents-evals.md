---
title: "Deep Agents Evals"
created: 2026-04-11
updated: 2026-08-03
type: concept
tags: [agent, evaluation]
sources: [raw/articles/x-bookmarks-2026.md, raw/articles/x-bookmarks-weekly.md, raw/articles/xarticle-how-to-become-an-applied-ai-engineer-2074519552277336571.md, raw/articles/xarticle-eval-engineering-build-the-gate-that-lets-your-age-2083540339147567268.md]
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

## Outcome and trajectory grading

[[eyad-khrais]]'s applied AI engineering guide makes the evaluation split concrete: grade the final outcome separately from the trajectory that produced it. A production agent can reach the right final answer while taking a dangerous path, such as touching a forbidden field or attempting payment before approval. Deterministic checks should catch safety violations in the tool-call log, while model judges or rubrics score judgment calls such as escalation quality or reasoning adequacy.

## Eval-engineering gate

Hanako's six-step course adds a component-level repair lens to the outcome/trajectory split: evaluate end to end for task success, trajectory for loops, redundant calls, and wasted steps, and components for which retriever, tool, or sub-agent failed. Its starter metrics are faithfulness to returned tool evidence, tool-parameter accuracy, and task completion against a real signal rather than the agent's own claim. The article's judge-bias figures, version-pinning rule, and blast-radius lanes are source-described and unverified here. ^[raw/articles/xarticle-eval-engineering-build-the-gate-that-lets-your-age-2083540339147567268.md]

The proposed gate also mines complete production traces for eval cases: clean baselines, user corrections, empty or duplicated tool calls, and external timeouts. A verifier is tested with one clearly correct and one plausible wrong result before it is trusted, and objectively checkable conditions go to code rather than a model judge. This makes [[eval-engineering]] the operational companion to this page's deep-agent evaluation framework. ^[raw/articles/xarticle-eval-engineering-build-the-gate-that-lets-your-age-2083540339147567268.md]

## Relevance to This Wiki

Building reliable AI agents (like those in [[vibe-kanban-agent-spawning]], [[paperclipai-paperclip]], [[gsd-2-ai-vibe-coding-framework]]) requires systematic evals. The evaluation infrastructure is often the bottleneck to shipping agentic products.

## See Also

- [[vibe-kanban-agent-spawning]] — agent spawning that would benefit from evals
- [[paperclipai-paperclip]] — production agent deployment where evals are critical
- [[gsd-2-ai-vibe-coding-framework]] — vibe coding agents needing eval frameworks
- [[research-code-agent-cli-automation]] — CLI agents and their evaluation challenges
