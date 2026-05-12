---
title: BiRefNet
created: 2026-04-26
updated: 2026-04-26
type: entity
tags: [model, background-removal, image-segmentation, salient-object-detection, pytorch, mit-license]
sources: [raw/articles/huggingface-local-image-bg-removal-svg-models-2026-04-26.md]
---

# BiRefNet

Bilateral Reference Network for dichotomous image segmentation. The most downloaded MIT-licensed image segmentation model on HuggingFace (848K monthly downloads).

## Overview

BiRefNet (Bilateral Reference Network) is a segmentation model that uses bilateral references to achieve precise object boundary delineation. It handles multiple segmentation tasks: background removal, salient object detection, camouflaged object detection, and general instance segmentation.

## Key Facts

- **Architecture:** BiRefNet (Biilateral Reference Network) — arXiv:2401.03407
- **Framework:** PyTorch (custom birefnet library)
- **Model Size:** ~400 MB
- **License:** MIT (fully open, commercial use allowed)
- **Downloads/month:** 848,461 (2nd most downloaded image segmentation model)
- **Likes:** 561
- **Pipeline:** Image Segmentation
- **Source:** https://huggingface.co/ZhengPeng7/BiRefNet

## Tasks Supported

- Background removal
- Mask generation
- Dichotomous Image Segmentation (DIS)
- Camouflaged Object Detection
- Salient Object Detection

## Apple Silicon Compatibility

Not MLX-native. Runs on Mac via PyTorch with MPS (Metal Performance Shaders) backend. While not optimized for MLX unified memory, PyTorch+MPS still leverages the GPU on Apple Silicon.

## Compared to Alternatives

| Model | License | Monthly Downloads | Best For |
|-------|---------|-----------------|---------|
| [[rmbg-1-4]] | CC BY-NC | 915K | Background removal (non-commercial limit) |
| **BiRefNet** | **MIT** | 848K | **Fully open, commercial use OK** |
| [[rmbg-2-0]] | CC BY-NC | 454K | Best accuracy (non-commercial limit) |
| CLIPSeg | Apache 2.0 | 926K | CLIP-based flexible segmentation |

## Related Models

- [[rmbg-1-4]] — most popular but non-commercial license
- [[u2net-mlx]] — MLX-native alternative
- [[sam3-image]] — MLX-native interactive segmentation
