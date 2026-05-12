---
title: 3D Gaussian Splatting
created: 2026-04-23
updated: 2026-04-23
type: concept
tags: [3dgs, 3d-vision, computer-vision]
sources: [raw/articles/tencent-hy-world-2-0-model-card-2026-04-23.md]
related_entity: [[hy-world-2-0]]
---

# 3D Gaussian Splatting

**3D Gaussian Splatting (3DGS)** is a differentiable rasterization technique for representing and rendering 3D scenes as a set of oriented Gaussian primitives (ellipsoids). Each Gaussian is defined by:
- **Mean** (center position in 3D space)
- **Covariance** (scale + rotation / shape)
- **Opacity** (alpha value)
- **Spherical Harmonics (SH) coefficients** — for color/appearance

3DGS enables real-time rendering of complex scenes on consumer GPUs by avoiding the expensive neural rendering pipelines of NeRF. Scenes can be optimized from multi-view images via gradient descent, producing a point-based representation that renders via splatting (projection + alpha blending).

## Why 3DGS Matters for World Models

HY-World 2.0 outputs 3DGS as its primary 3D representation because:
- **Editable** — Gaussians can be transformed, added, removed
- **Game engine compatible** — exportable to Blender/Unity/Unreal/Isaac
- **Real-time rendering** — one-time generation cost, ~0 rendering cost thereafter
- **Persistent** — unlike pixel videos, the 3D world exists permanently

Traditional video world models (Genie 3, Cosmos) produce non-editable pixel videos with bounded playable duration. 3DGS world models produce persistent, explorable 3D worlds.

## 3DGS as Output of WorldMirror 2.0

WorldMirror 2.0 predicts these Gaussian attributes per-input-view in a single forward pass:

| Attribute | Shape | Description |
|-----------|-------|-------------|
| `means` | [B, N, 3] | Gaussian centers (3D positions) |
| `scales` | [B, N, 3] | Gaussian extents along each axis |
| `quats` | [B, N, 4] | Rotation as quaternions |
| `opacities` | [B, N] | Per-Gaussian alpha |
| `sh` | [B, N, 1, 3] | Spherical harmonics (degree 0 = color) |
| `weights` | [B, N] | Per-Gaussian confidence |

Where N = S × H × W (number of views × image height × image width).

The output `gaussians.ply` file encodes all Gaussians in a standard PLY format readable by 3DGS viewers and game engines.

## Related Concepts

- [[hy-world-2-0]] — uses 3DGS as its primary 3D output format
- [[3dgs]] (related entity/concept for splatting techniques)
