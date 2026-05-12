---
title: GEPA
created: 2026-05-04
updated: 2026-05-04
type: concept
tags: [method, optimization, prompt-engineering, research]
sources: [raw/articles/thread-akshay-pachaar-2049916107923034300-2026-04-30.md]
related_entity: [[akshay-pachaar]]
author: [[akshay-pachaar]]
---

## Definition

GEPA (Generative Evolutionary Prompt Algorithm) is a prompt optimization method for compound AI systems that uses natural language reflection on full rollout traces instead of scalar rewards. Published July 2025 (arXiv:2507.19457), accepted to ICLR 2026. Implemented as a first-class optimizer in [[dspy]], with cookbooks from Hugging Face and OpenAI.

## Core Mechanism

GEPA replaces GRPO-style scalar rewards with a **feedback function μ_f** that returns both a score *and* a natural language description of what happened. The reflection model reads the full rollout trace (reasoning steps, tool calls, errors, judge rationales — all ~5,000 tokens) and writes a new prompt. The new prompt is tested on the same 3 examples; if it improves, it replaces the candidate.

**Key distinction from GRPO:** GRPO reduces a 5,000-token rollout to a single +1/-1 bit. GEPA preserves the full information content of the trace and lets an LLM read it.

## Algorithm

1. Pick a candidate prompt set from the population (Pareto sampling)
2. Pick a module to mutate (round-robin)
3. Sample 3 examples from training set
4. Run rollouts, collect traces + feedback from μ_f
5. Reflect: feed traces + feedback to reflection LLM → new prompt
6. Accept/reject: rerun on same 3 examples

No gradients. No PPO. No KL penalties. Budget-driven.

## Pareto Selection

GEPA uses Pareto-based parent selection (borrowed from quality-diversity optimization). Unlike greedy selection which picks the best-average candidate every time (collapsing to local optima), Pareto selection keeps anyone best at at least one task and weights selection by how many tasks they win. This preserves diverse strategies that can later recombine.

## vs. GRPO

| | GEPA | GRPO |
|---|---|---|
| What changes | Prompts | Model weights |
| Feedback | Full trace + natural language | Scalar (+1/-1) |
| Rollouts needed | 35× fewer | Many thousands |
| GPU required | No | Yes |
| What it can fix | Prompt quality | Capabilities + prompt |

GEPA beats GRPO by 10 points on the same benchmark at 35× fewer rollouts and under $1,000 vs $40,000. GEPA cannot add new capabilities to a base model — fine-tune when the model can't do the task at all.

## Tooling

- [[dspy]] — first-class `dspy.GEPA` optimizer
- [[grpo]] — reinforcement learning method GEPA competes with and complements
- [[dspy]] — framework where GEPA is implemented as a first-class optimizer
- [[prompt-engineering-patterns]] — broader prompt engineering patterns
