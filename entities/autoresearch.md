---
title: Autoresearch
created: 2026-04-12
updated: 2026-07-16
type: entity
tags: [llm, marketing, method, ai-research, training, agent]
sources: [raw/articles/ericosiu-autoresearch-ai-copy-testing-2026-04-12.md, raw/articles/thread-NVIDIAAI-2077061428998013279.md]
---

# Autoresearch

AI copy testing loop adapted from Karpathy's autonomous ML experiments. Generates 50+ variants, scores them via simulated expert panel in ~8 minutes — without needing live traffic. First phase of a two-phase optimization pipeline (autoresearch pre-launch, autogrowth post-launch).

## Agent-steered ML experiments

The NVIDIA AI thread shows the same propose → run → evaluate → decide pattern applied to model training: a coding agent received a goal and a five-hour time budget, used NeMo RL, NeMo Gym, and reusable skills to build the environment, train and evaluate a vision model, and propose the next experiment while a researcher steered priorities. Qwen3-VL-2B reportedly improved colored-star counting accuracy from 25% to 96.9%; this metric remains source-reported, not independently verified.^[raw/articles/thread-NVIDIAAI-2077061428998013279.md]

## Related Concepts

- [[autoresearch-ai-copy-testing]] — the full copy testing concept that uses autoresearch as its core loop
- [[loop-engineering]] — bounded agent loops with explicit budgets and verification
- [[human-in-the-loop]] — researcher steering at the outer loop rather than per-action approval
- [[nvidia-ai]] — source account for the NeMo RL/Gym training demonstration
- [[qwen]] — model family containing the source-described Qwen3-VL-2B
- [[ai-workflow-setup-service]] — selling AI automation workflows; autoresearch is a deliverable within this service
