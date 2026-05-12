---
title: GRPO
created: 2026-05-04
updated: 2026-05-04
type: concept
tags: [method, rl, optimization]
sources: [raw/articles/thread-akshay-pachaar-2049916107923034300-2026-04-30.md]
related_entity: [[berkeley]]
---

## Definition

GRPO (Group Relative Policy Optimization) is a reinforcement learning method for LLMs that uses policy gradients on scalar group-relative rewards. It groups responses, computes a baseline from the group mean, and applies advantage normalization. Widely used for fine-tuning LLMs on reasoning, code generation, and agentic tasks.

## How It Works

GRPO collects multiple rollout trajectories per prompt, computes a scalar reward for each, and updates model weights via policy gradient backprop — treating the reward as the learning signal. The key mechanism is group-relative advantage: instead of comparing to a global baseline, each trajectory is scored against the group's average.

## Tradeoffs

- **Can add new capabilities** to a base model (unlike GEPA which only changes prompts)
- **High rollout requirements** — tens of thousands needed to converge
- **Expensive** — significant GPU compute cost
- **Scalar feedback loses information** — full 5,000-token traces reduced to +1/-1

## Compared to GEPA

GEPA (Generative Evolutionary Prompt Algorithm) targets the same problem space but uses natural language reflection on full traces instead of scalar rewards. GEPA achieves 10 points higher on the same benchmark at 35× fewer rollouts and no GPU cost. The two are increasingly combined in hybrid recipes like BetterTogether and mmGRPO.

- [[gepa]] — prompt optimization method that competes with and complements GRPO
