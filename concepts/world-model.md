---
title: World Model
created: 2026-04-23
updated: 2026-04-23
type: concept
tags: [worldmodel, embodied-ai]
sources: [raw/articles/tencent-hy-world-2-0-model-card-2026-04-23.md]
related_entity: [[hy-world-2-0]]
---

# World Model

A **world model** is an AI system that learns a predictive internal representation of a physical or virtual environment — enabling reasoning about how the world evolves, what actions lead to what outcomes, and how to navigate or manipulate the environment.

## World Models vs Video Generation

Traditional video generation models produce pixel-level outputs that "watch a movie" — the output is passive, non-interactive, and ephemeral. World models, by contrast, produce structured 3D representations that:

1. **Persist** — the world exists beyond playback
2. **Are editable** — geometry and appearance can be modified
3. **Support real-time rendering** — consumer GPU, no per-frame inference cost
4. **Are physics-compatible** — collision detection, accurate lighting
5. **Are engine-importable** — work with Blender, Unity, Unreal, Isaac Sim

| | Video World Models | 3D World Models |
|--|---|---|
| Output | Pixel videos | 3D assets (mesh/3DGS) |
| Playable Duration | Limited | Unlimited |
| 3D Consistency | Poor | Native |
| Rendering Cost | Accumulates | One-time generation |
| Engine Import | ✗ | ✓ |
| Controllability | Weak | Precise |

## HY-World 2.0 as a 3D World Model

HY-World 2.0 is the first **open-source state-of-the-art** 3D world model. Its key innovations:

- **World Generation** — text/single image → navigable 3DGS via a 4-stage pipeline (panorama → trajectory → expansion → composition)
- **World Reconstruction** — multi-view video → 3DGS in one forward pass via WorldMirror 2.0
- **First open-source SOTA** — comparable to closed-source methods like Marble

## Related Concepts

- [[hy-world-2-0]] — the canonical open-source 3D world model
- [[embodied-ai]] — world models for physical robot reasoning and control
- [[hy-embodied-0-5]] — Tencent's embodied foundation model (related team/org)
- [[3dgs]] — the 3D representation format used by HY-World 2.0
