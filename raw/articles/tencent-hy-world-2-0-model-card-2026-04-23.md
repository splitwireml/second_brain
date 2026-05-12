---
title: HY-World 2.0 — Tencent Multi-Modal 3D World Model
created: 2026-04-23
updated: 2026-04-23
type: raw
tags: [model, worldmodel, 3d, reconstruction, generation, tencent, oss-ai]
sources: []
---

# HY-World 2.0 — Raw Source Metadata

**URL:** https://huggingface.co/tencent/HY-World-2.0
**Downloaded:** 2026-04-23
**Verified:** Full README.md + DOCUMENTATION.md fetched via curl

## Source Files

- README.md (21,336 bytes) — primary model card
- DOCUMENTATION.md (20,076 bytes) — detailed API/CLI reference
- HY-WorldMirror-2.0/config.json (842 bytes)
- HY-WorldMirror-2.0/README.md (352 bytes)
- Technical Report: https://3d-models.hunyuan.tencent.com/world/world2_0/HY_World_2_0.pdf
- GitHub: https://github.com/Tencent-Hunyuan/HY-World-2.0

## Key Facts

- **Released:** April 15, 2026
- **Organization:** Tencent (HY Vision Team)
- **Pipeline tag:** image-to-3d
- **License:** Tencent HY-World 2.0 Community License (EU disallowed)
- **Languages:** English, Chinese
- **Siblings:** model.safetensors (5,053,553,272 bytes / ~4.7GB)

## WorldMirror 2.0 Config

- Model size: large
- Vision backbone: dinov2_vitl14_reg (DINOv2 ViT-Large with registers)
- Embed dim: 1024
- Patch size: 14
- Image size: 518
- Num heads: 16
- Depth: 24
- MLP ratio: 4.0
- GS dim: 256
- Normalized RoPE: true
- Num register tokens: 4
- BF16: disabled by default
- Condition strategy: token, pow3r, token

## Model Zoo

| Model | Description | Params | Date | Status |
|-------|-------------|--------|------|--------|
| WorldMirror 2.0 | Multi-view/video → 3D reconstruction | ~1.2B | 2026 | ✅ Released |
| WorldMirror 1.0 | Multi-view/video → 3D reconstruction (legacy) | ~1.2B | 2025 | ✅ Released |
| HY-PanoGen | Text/image → 360° panorama | — | Coming Soon | ⬜ |
| WorldStereo 2.0 | Panorama → navigable 3DGS world | — | Coming Soon | ⬜ |
| WorldNav | Trajectory planning | — | Coming Soon | ⬜ |

## Benchmark Highlights (WorldStereo 2.0 — Camera Control)

| Method | RotErr ↓ | TransErr ↓ | ATE ↓ | Q-Align ↑ | CLIP-IQA+ ↑ | Laion-Aes ↑ | CLIP-I ↑ |
|--------|----------|------------|-------|-----------|-------------|-------------|----------|
| SEVA | 1.690 | 1.578 | 2.879 | 3.232 | 0.479 | 4.623 | 77.16 |
| Gen3C | 0.944 | 1.580 | 2.789 | 3.353 | 0.489 | 4.863 | 82.33 |
| WorldStereo | 0.762 | 1.245 | 2.141 | 4.149 | 0.547 | 5.257 | 89.05 |
| **WorldStereo 2.0** | **0.492** | **0.968** | **1.768** | **4.205** | 0.544 | **5.266** | **89.43** |

## WorldMirror 2.0 Reconstruction Accuracy (H + all priors)

| Dataset | Accuracy ↓ | Completeness ↓ |
|---------|------------|----------------|
| 7-Scenes | 0.012 | 0.016 |
| NRGBD | 0.015 | 0.016 |
| DTU | 0.554 | 0.771 |
