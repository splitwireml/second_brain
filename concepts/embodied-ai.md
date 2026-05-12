---
title: Embodied AI
created: 2026-04-14
updated: 2026-04-14
type: concept
tags: [embodied-ai, robotics, vision-language, agent, reasoning]
sources: [raw/articles/tencent-hy-embodied-0-5-model-card-2026-04-14.md]
---

# Embodied AI

**Embodied AI** refers to AI systems that perceive, reason about, and interact with physical environments through sensors (cameras, lidar) and actuators (robot limbs, grippers). Unlike purely text-based LLMs, embodied AI must understand 3D spatial relationships, physical object properties, and action consequences.

## Key Capabilities

- **Spatial-temporal visual perception** — Understanding how scenes evolve over time
- **Physical reasoning** — Predicting object behavior and affordances
- **Action planning** — Generating sequences of actions to achieve goals
- **闭环反馈** — Closed-loop feedback from environment

## Relation to VLMs

General-purpose [[vision-language-models]] (VLMs) excel at image captioning and QA but lack physical understanding. Embodied AI bridges this gap by training on:
- >100 million embodied interaction data points
- Robot action trajectories
- 3D spatial relationships

[[hy-embodied-0-5]] was specifically designed to serve as the "brain" (cognitive engine) for Vision-Language-Action (VLA) pipelines in physical robots.

## Benchmark Domains

Typical embodied AI benchmarks include:
- Robotic manipulation success rates
- Navigation accuracy in unseen environments
- Physical reasoning puzzles
- Long-horizon task completion

## See Also

- [[hy-embodied-0-5]]
- [[vla-robotics]]
- [[vision-language-models]]
- [[tencent]]
