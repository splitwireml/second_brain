---
title: RMBG-2.0
created: 2026-04-26
updated: 2026-04-26
type: entity
tags: [model, background-removal, image-segmentation, bria-ai, pytorch, onnx, transformers-js]
sources: [raw/articles/huggingface-local-image-bg-removal-svg-models-2026-04-26.md]
---

# RMBG-2.0

[[bria-ai]]'s next-generation background removal model — significantly improved over [[rmbg-1-4]], with a new architecture and enhanced accuracy.

## Overview

RMBG-2.0 is BRIA AI's updated state-of-the-art background removal model. It maintains the same training philosophy (legally licensed dataset, bias mitigation, content safety) while improving segmentation quality across all image categories.

## Key Facts

- **Developer:** [[bria-ai]]
- **Architecture:** Not publicly disclosed (improved over v1.4's IS-Net foundation)
- **Framework:** PyTorch, ONNX, Transformers.js, ComfyUI nodes
- **Model Size:** ~170 MB (similar to v1.4)
- **License:** CC BY-NC 4.0 (non-commercial); commercial license available from BRIA AI
- **Downloads/month:** 454,177
- **Likes:** 1,160
- **Pipeline:** Image Segmentation
- **Source:** https://huggingface.co/briaai/RMBG-2.0

## Availability Options

| Option | Quality | Commercial License | GPU Infrastructure | Setup Time |
|--------|---------|-------------------|-------------------|------------|
| Self-Hosted (HuggingFace) | ✅ RMBG-2.0 | ❌ Requires agreement | ❌ You manage | Hours |
| Bria API | ✅ RMBG-2.0 | ✅ Included | ✅ Managed | Minutes |

## Apple Silicon Compatibility

Not MLX-native. Same compatibility as [[rmbg-1-4]] — runs on Mac via PyTorch MPS or ONNX/CoreML.

## Compared to RMBG-1.4

| Dimension | RMBG-1.4 | RMBG-2.0 |
|-----------|-----------|----------|
| Monthly downloads | 915K | 454K |
| Architecture | IS-Net enhanced | New ( undisclosed) |
| Accuracy | Established SOTA | Improved over v1.4 |
| License | CC BY-NC | CC BY-NC |
| ComfyUI support | Via custom nodes | Native |

## Related Models

- [[rmbg-1-4]] — established predecessor
- [[birefnet]] — MIT-licensed alternative
- [[u2net-mlx]] — MLX-native Apple Silicon option
