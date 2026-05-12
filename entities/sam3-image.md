---
title: sam3-image
created: 2026-04-26
updated: 2026-04-26
type: entity
tags: [model, image-segmentation, mlx, apple-silicon, sam3, meta, interactive-segmentation]
sources: [raw/articles/huggingface-local-image-bg-removal-svg-models-2026-04-26.md]
---

# sam3-image

Native MLX port of Meta's Segment Anything Model 3 (SAM3), optimized for Apple Silicon. The most capable general-purpose interactive segmentation model on MLX.

## Overview

sam3-image brings Meta's SAM3 to Apple Silicon via MLX. Unlike dedicated background removal models, SAM3 supports interactive segmentation via text prompts, box prompts, and free-form region selection — making it suitable for both background removal and general object isolation tasks.

## Key Facts

- **Developer:** Deekshith Dade (mlx-community port)
- **Base Model:** facebook/sam3 (Meta's Segment Anything Model 3)
- **Architecture:** SAM3 with ViTDet backbone
- **Framework:** MLX (Apple Silicon native)
- **Model Size:** ~3.5 GB
- **Requirements:** macOS 13.0+, Python 3.13+, M1/M2/M3/M4
- **License:** SAM3 license (per Meta)
- **Pipeline:** Image Segmentation
- **Source:** https://huggingface.co/mlx-community/sam3-image

## Features

- **Text prompts** — describe objects to segment ("person", "car", "dog")
- **Box prompts** — draw bounding boxes to include/exclude regions
- **Interactive segmentation** — click/tap to refine masks
- **Web interface** — optional Flask-based UI at localhost:3000

## Apple Silicon Compatibility

**✅ Native MLX** — fully optimized for M1/M2/M3/M4 unified memory. Larger than u2net-mlx but provides more flexibility.

## Installation

```bash
git clone https://github.com/Deekshith-Dade/mlx_sam3.git
cd mlx-sam3
uv sync  # or pip install -e .
```

## Usage

```python
from PIL import Image
from sam3 import build_sam3_image_model
from sam3.model.sam3_image_processor import Sam3Processor

model = build_sam3_image_model()
processor = Sam3Processor(model, confidence_threshold=0.5)

image = Image.open("your_image.jpg")
state = processor.set_image(image)
state = processor.set_text_prompt("person", state)

masks = state["masks"]
boxes = state["boxes"]  # [x0, y0, x1, y1]
scores = state["scores"]
```

## Compared to Alternatives

| Model | Framework | Size | Best For |
|-------|-----------|------|---------|
| sam3-image | MLX | ~3.5GB | **Interactive segmentation**, text/box prompts |
| u2net-mlx | MLX | 176MB | Background removal only (smaller, dedicated) |
| [[rfdetr-seg-small]] | MLX | 683MB | Instance segmentation, object detection |
| [[rmbg-1-4]] | PyTorch | ~170MB | Background removal (non-MLX, most popular) |

## Related Models

- [[u2net-mlx]] — smaller, dedicated background removal
- [[rfdetr-seg-small]] — MLX instance segmentation model
- [[rmbg-1-4]] — most downloaded bg removal model (non-MLX)
