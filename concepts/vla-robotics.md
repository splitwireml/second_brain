---
title: Vision-Language-Action (VLA) Robotics
created: 2026-04-14
updated: 2026-04-14
type: concept
tags: [robotics, vla, embodied-ai, agent, vision-language]
sources: [raw/articles/tencent-hy-embodied-0-5-model-card-2026-04-14.md]
---

# Vision-Language-Action (VLA) Robotics

**Vision-Language-Action (VLA)** is a paradigm for robotic control where a single model processes visual input and language instructions to generate physical actions for robot control.

## How VLA Works

```
Vision Input → [VLA Model] → Action Output
Language Instruction ↗
```

Unlike separate perception/planning/control stacks, VLA end-to-end models like [[hy-embodied-0-5]] directly output:
- Joint velocity commands
- End-effector target positions
- Discrete action tokens

## VLA vs Other Paradigms

| Paradigm | Input | Output | Example |
|----------|-------|--------|---------|
| VLM | Vision + Text | Text | GPT-4V, [[hy-embodied-0-5]] |
| VLA | Vision + Text | Actions | [[hy-embodied-0-5]], RT-2 |
| RHLF | Vision | Actions | Classical robotics |

## [[hy-embodied-0-5]] as VLA Brain

HY-Embodied-0.5 is explicitly designed to serve as the cognitive engine ("brain") for VLA pipelines. It outputs reasoning that can be translated into robot actions by downstream control systems.

## See Also

- [[hy-embodied-0-5]]
- [[embodied-ai]]
- [[vision-language-models]]
- [[tencent]]
