---
title: HY-World 2.0
created: 2026-04-23
updated: 2026-04-23
type: entity
tags: [model, oss-ai, computer-vision, reconstruction]
sources: [raw/articles/tencent-hy-world-2-0-model-card-2026-04-23.md]
related_entity: [[tencent]]
---

# HY-World 2.0

**HY-World 2.0** is Tencent's open-source multi-modal world model framework for **3D world generation** and **3D world reconstruction** — the first open-source state-of-the-art 3D world model. Released April 15, 2026 by the [[tencent]] HY Vision Team.

## Overview

HY-World 2.0 accepts diverse input modalities — text, single-view images, multi-view images, and videos — and produces persistent 3D world representations (meshes / 3D Gaussian Splattings) that are directly importable into game engines (Blender, Unity, Unreal Engine, Isaac Sim).

Unlike video world models (Genie 3, Cosmos, HY-World 1.5) that produce pixel-level videos which "vanish once playback ends," HY-World 2.0 generates real 3D assets that persist permanently and support real-time rendering on consumer GPUs.

## Two Core Capabilities

### World Generation (text / single image → 3D world)
Four-stage pipeline:
1. **Panorama Generation** — HY-Pano 2.0 generates 360° panorama
2. **Trajectory Planning** — WorldNav plans navigable camera paths
3. **World Expansion** — WorldStereo 2.0 expands panorama into 3D space
4. **World Composition** — WorldMirror 2.0 + 3DGS produces final navigable 3D world

### World Reconstruction (multi-view images / video → 3D)
Powered by **WorldMirror 2.0**, a unified feed-forward model that simultaneously predicts in a single forward pass:
- 3D point clouds (world coordinates)
- Per-view depth maps (camera frame)
- Surface normals (camera coordinates)
- Camera poses (c2w) and intrinsics
- 3DGS attributes (means, scales, rotations, opacities, SH coefficients)

## Model Zoo

### WorldMirror Series (Reconstruction)

**WorldMirror 2.0** (~1.2B params, released April 2026)
- Vision backbone: DINOv2 ViT-Large with registers
- Config: embed_dim=1024, depth=24, num_heads=16, patch_size=14
- Key features: Normalized RoPE (flexible resolution), depth mask prediction, FSDP + BF16 multi-GPU inference
- Input: multi-view images or video (50K–500K pixels per view)
- Output: depth, normals, camera poses, point clouds, 3DGS

**WorldMirror 1.0** (~1.2B params, 2025) — legacy predecessor

### Coming Soon
- **HY-PanoGen** — text/image → 360° panorama
- **WorldStereo 2.0** — panorama → navigable 3DGS
- **WorldNav** — trajectory planning

## Benchmarks

### WorldStereo 2.0 — Camera Control
WorldStereo 2.0 outperforms SEVA, Gen3C, and the original WorldStereo across all camera metrics:

| Method | RotErr ↓ | TransErr ↓ | ATE ↓ | Q-Align ↑ | CLIP-I ↑ |
|--------|----------|------------|-------|-----------|----------|
| SEVA | 1.690 | 1.578 | 2.879 | 3.232 | 77.16 |
| Gen3C | 0.944 | 1.580 | 2.789 | 3.353 | 82.33 |
| WorldStereo | 0.762 | 1.245 | 2.141 | 4.149 | 89.05 |
| **WorldStereo 2.0** | **0.492** | **0.968** | **1.768** | **4.205** | **89.43** |

### WorldMirror 2.0 — Point Map Reconstruction (H + all priors)
Best results with high resolution + all camera/depth priors:

| Dataset | Accuracy ↓ | Completeness ↓ |
|---------|------------|----------------|
| 7-Scenes | 0.012 | 0.016 |
| NRGBD | 0.015 | 0.016 |
| DTU | 0.554 | 0.771 |

## Usage

**Python API:**
```python
from hyworld2.worldrecon.pipeline import WorldMirrorPipeline

pipeline = WorldMirrorPipeline.from_pretrained('tencent/HY-World-2.0')
result = pipeline('path/to/images')
```

**CLI:**
```bash
python -m hyworld2.worldrecon.pipeline --input_path path/to/images

# Multi-GPU
torchrun --nproc_per_node=2 -m hyworld2.worldrecon.pipeline \
    --use_fsdp --enable_bf16
```

**Gradio App:**
```bash
python -m hyworld2.worldrecon.gradio_app
```

## Key Differences: Video vs 3D World Models

| | Video World Models | HY-World 2.0 |
|--|---|---|
| Output | Pixel videos (non-editable) | Real 3D assets (meshes/3DGS) |
| Playable Duration | Limited (<1 min) | Unlimited |
| 3D Consistency | Poor (flickering, artifacts) | Native |
| Real-Time Rendering | Per-frame inference, high latency | Consumer GPU, real-time |
| Controllability | Weak | Precise, physics-based |
| Inference Cost | Accumulates with interaction | One-time generation |
| Engine Compatibility | ✗ | ✓ Blender/UE/Isaac |

## Open-Source Status

- ✅ Technical Report (HY_World_2_0.pdf)
- ✅ WorldMirror 2.0 code + model weights
- ⬜ Full World Generation inference code (WorldNav + World Composition)
- ⬜ HY-Pano 2.0 model + code (HunyuanWorld 1.0 as interim)
- ⬜ WorldStereo 2.0 model + code (WorldStereo as interim)

## Related

- [[tencent]] — parent company
- [[3dgs]] — 3D Gaussian Splatting output format
- [[hy-embodied-0-5]] — Tencent's embodied AI model (same org/team)
