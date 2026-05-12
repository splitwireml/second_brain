---
title: RMBG-1.4
created: 2026-04-26
updated: 2026-04-26
type: entity
tags: [model, background-removal, image-segmentation, bria-ai, pytorch, onnx, transformers-js]
sources: [raw/articles/huggingface-local-image-bg-removal-svg-models-2026-04-26.md]
---

# RMBG-1.4

[[bria-ai]]'s flagship background removal model — the most downloaded image segmentation model on HuggingFace with 915K monthly downloads.

## Overview

RMBG-1.4 is a saliency segmentation model trained on 12,000+ high-quality, manually labeled, legally licensed images. It distinguishes foreground from background across diverse categories including e-commerce products, people, animals, text overlays, and advertising content.

## Key Facts

- **Developer:** [[bria-ai]]
- **Architecture:** IS-Net (enhanced) — proprietary training scheme on top of IS-Net architecture
- **Framework:** PyTorch, ONNX, Transformers.js
- **Model Size:** ~170 MB
- **License:** CC BY-NC 4.0 (non-commercial); commercial license required for business use
- **Downloads/month:** 915,862
- **Likes:** 1,966
- **Pipeline:** Image Segmentation
- **Source:** https://huggingface.co/briaai/RMBG-1.4

## Training Data Distribution

| Category | Distribution |
|----------|--------------|
| Objects only | 45.11% |
| People with objects/animals | 25.24% |
| People only | 17.35% |
| People/objects/animals with text | 8.52% |
| Text only | 2.52% |
| Animals only | 1.89% |

| Property | Distribution |
|----------|-------------|
| Photorealistic | 87.70% |
| Non-Photorealistic | 12.30% |
| Non-solid background | 52.05% |
| Solid background | 47.95% |
| Single foreground | 51.42% |
| Multiple foregrounds | 48.58% |

## Performance

Benchmarked for balanced gender, ethnicity, and people with disabilities. BRIA AI claims accuracy "rivals leading source-available models." No independent third-party benchmark scores are published on the model card.

## Apple Silicon Compatibility

Not MLX-native. Runs on Mac via:
- PyTorch with MPS backend (Metal GPU acceleration)
- ONNX with CoreML export (Apple Neural Engine)
- Transformers.js in browser/Node.js

On M1/M2/M3/M4 Macs: usable via PyTorch MPS or ONNX/CoreML, though not optimized for MLX unified memory architecture.

## Usage

```python
from transformers import pipeline

pipe = pipeline("image-segmentation", model="briaai/RMBG-1.4", trust_remote_code=True)
mask = pipe(image_path, return_mask=True)  # returns pillow mask
result = pipe(image_path)  # returns image with mask applied (transparent background)
```

## Compared to RMBG-2.0

RMBG-2.0 is a newer version with improved accuracy but same non-commercial license. v1.4 remains more widely deployed due to established ecosystem and 2x the monthly downloads.

## Related Models

- [[rmbg-2-0]] — newer version with improved accuracy
- [[birefnet]] — MIT-licensed alternative background removal model
- [[u2net-mlx]] — MLX-native alternative for Apple Silicon
- [[sam3-image]] — MLX-native interactive segmentation
