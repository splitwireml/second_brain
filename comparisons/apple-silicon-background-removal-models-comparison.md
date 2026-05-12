---
title: "Apple Silicon Background Removal Models: MLX vs PyTorch vs ONNX"
created: 2026-04-26
updated: 2026-05-07
type: comparison
tags: [comparison, apple-silicon, mlx, background-removal, image-segmentation, svg, gguf, onnx]
sources: [raw/articles/huggingface-local-image-bg-removal-svg-models-2026-04-26.md, users/mali/research/local-bg-removal-svg-models-2026-05-07/report.md]
---

# Apple Silicon Background Removal Models: MLX vs PyTorch

Comparing the landscape of image background removal models that run on Apple Silicon Macs — separating native MLX implementations from PyTorch/MPS alternatives. Extended with GGUF, image-to-SVG, and broader model formats.

## Quick Verdict

| Goal | Recommendation |
|------|---------------|
| Native MLX, smallest | [[u2net-mlx]] — 176MB, dedicated bg removal |
| Best overall quality | [[withoutbg]] Focus — ONNX pipeline, best hair/fur edges |
| Best open license | [[birefnet]] — MIT, 961K/mo downloads |
| Native MLX, most capable | [[sam3-image]] — 3.5GB, interactive |
| Image-to-SVG locally | Qwen2VL-2B GGUF (experimental) or mask + Potrace pipeline |
| GGUF vision model | ✅ Now exists — [[qwen2vl-2b-png-to-svg-gguf]] (experimental) |

---

## Comparison Matrix

| Model | Framework | Apple Silicon | Size | Monthly Downloads | License | Commercial? |
|-------|-----------|---------------|------|-----------------|---------|-------------|
| [[u2net-mlx]] | **MLX** | ✅ Native | 176MB | N/A | Apache 2.0 | ✅ |
| [[sam3-image]] | **MLX** | ✅ Native | 3.5GB | N/A | Apache 2.0 | ✅ Via Meta |
| rfdetr-seg-small | **MLX** | ✅ Native | 683MB | 30 | Apache 2.0 | ✅ |
| rfdetr-seg-large | **MLX** | ✅ Native | 1.2GB | 13 | Apache 2.0 | ✅ |
| [[rmbg-1-4]] | PyTorch/ONNX | ⚠️ Via MPS | ~170MB | **919K** | CC BY-NC | ❌ |
| [[rmbg-2-0]] | PyTorch/ONNX | ⚠️ Via MPS | ~170MB | 601K | CC BY-NC | ❌ |
| [[birefnet]] | PyTorch | ⚠️ Via MPS | ~400MB | 961K | MIT | ✅ |
| [[withoutbg]] Focus | **ONNX** | ✅ arm64 Docker + PyPI | ~320MB | N/A (GitHub) | Apache 2.0 | ✅ |
| CLIPSeg | Transformers | ⚠️ Via MPS | ~100MB | 926K | Apache 2.0 | ✅ |

---

## MLX-Native Models (True Apple Silicon Optimization)

### [[u2net-mlx]] — Smallest, Best for Background Removal
- **Size:** 176MB (quantized)
- **Architecture:** U-2-Net (Universal U-Net)
- **Purpose:** Dedicated background removal
- **Strengths:** Smallest footprint, native MLX, fast inference
- **Weaknesses:** Not general-purpose segmentation
- **Best for:** Applications specifically targeting background removal on Apple Silicon

### [[sam3-image]] — Most Capable, Interactive
- **Size:** ~3.5GB
- **Architecture:** SAM3 with ViTDet backbone
- **Purpose:** General interactive segmentation
- **Strengths:** Text prompts, box prompts, point prompts, interactive refinement
- **Weaknesses:** Large size, Python 3.13+ required
- **Best for:** When you need flexible segmentation beyond pure background removal

### rfdetr-seg-small/large — Real-Time Instance Segmentation
- **Size:** 683MB (small) / 1.2GB (large)
- **Architecture:** DINOv2 + Deformable DETR decoder
- **Strengths:** Instance segmentation, 38 FPS (small) on M4 Max, real-time capable
- **Weaknesses:** Not dedicated to background removal
- **Best for:** Object detection + segmentation workflows needing speed

---

## PyTorch/MPS Models (Mac CPU/GPU, Not MLX-Native)

These run on Apple Silicon via PyTorch's MPS (Metal Performance Shaders) backends — they work but aren't MLX-optimized.

### [[rmbg-1-4]] — Highest Quality, Most Popular
- **Downloads:** 915K/month (top bg removal model on HuggingFace)
- **Architecture:** IS-Net (enhanced)
- **Strengths:** Highest quality, most battle-tested, PyTorch/ONNX/Transformers.js
- **Weaknesses:** CC BY-NC license (non-commercial only; commercial license from BRIA AI required)
- **Best for:** Non-commercial projects, research, prototyping

### [[rmbg-2-0]] — Next-Generation
- **Downloads:** 454K/month
- **Architecture:** Improved over v1.4 (specific architecture not disclosed)
- **Strengths:** Better edge quality and fine detail than v1.4
- **Weaknesses:** Same CC BY-NC license restriction
- **Best for:** Projects prioritizing quality over v1.4

### [[birefnet]] — Best Open License
- **Downloads:** 848K/month (2nd most downloaded)
- **Architecture:** BiRefNet (Bilateral Reference Network)
- **Tasks:** Background removal, salient object detection, camouflaged object detection
- **Strengths:** MIT license (fully open commercial use), multi-task capability
- **Weaknesses:** Not MLX-native
- **Best for:** Commercial projects needing background removal

---

## Image-to-SVG on Apple Silicon

### The Core Problem

**No end-to-end neural image-to-SVG model runs on Apple Silicon.** The fundamental issues:

| Barrier | Detail |
|---------|--------|
| Model size | Only dedicated img2svg (Qwen2.5-VL-32B) needs 64GB+ VRAM |
| No GGUF ports | No vision-to-SVG model has been quantized to GGUF |
| No dedicated research | No community has produced a purpose-built raster-to-SVG MLX model |

### What Exists (And Doesn't Work)

| Model | Format | Size | Problem |
|-------|--------|------|---------|
| svg-hub/qwen-2.5vl-32b-img2svg | PEFT LoRA | 6.5GB | Needs 64GB+ VRAM |
| svg-hub/qwen-2.5vl-32b-text2svg | PEFT LoRA | 6.5GB | Same — text→SVG only |
| thesantatitan/qwen-svg-sft | Qwen3-8B LoRA | ~8B | Text→SVG only, not image→SVG |

### GGUF Vision Gap

GGUF (llama.cpp quantization) powers local text models on Apple Silicon — but vision models have almost no GGUF ecosystem:

| Search | Results |
|--------|---------|
| `gguf+vision`, `gguf+multimodal`, `gguf+image` | 0 results |
| `segmentation+gguf`, `background+removal+gguf` | 0 results |
| `u2net+gguf`, `sam+gguf` | 0 results |
| `llava+gguf`, `vlm+gguf` | 0 results |

Florence-2 (microsoft/Florence-2-large, 954K downloads) is the most capable open vision model but has no GGUF port and produces text outputs, not SVG paths.

### Practical Working Pipeline

The proven local approach is a **mask → vectorize pipeline**:

```
Raster Image → Background Removal → Edge Processing → Potrace → SVG
```

**Stage 1 — Background removal** (any of):
- [[u2net-mlx]] — native MLX, 176MB
- [[rmbg-1-4]] — highest quality, PyTorch/MPS
- [[sam3-image]] — most flexible, MLX

**Stage 2 — Edge/mask processing**:
- OpenCV Canny edge detection
- Otsu thresholding for binary masks
- Morphological ops to clean edges

**Stage 3 — Vectorization**:
- **Potrace** — `brew install potrace`, then `potrace mask.bmp -s -o output.svg`
- **Inkscape** CLI — `inkscape --export-filename=output.svg input.png --export-type=svg`
- **svgtrace** (Python) — programmatic Potrace wrapper

---

## Verdict by Use Case

| Use Case | Recommendation |
|----------|---------------|
| Background removal, smallest MLX | [[u2net-mlx]] |
| Background removal, highest quality | [[rmbg-1-4]] |
| Background removal, commercial use | [[birefnet]] |
| Interactive segmentation | [[sam3-image]] |
| Real-time instance segmentation | rfdetr-seg-small |
| Image-to-SVG on Apple Silicon | Mask → Potrace pipeline (no neural solution) |
| Neural image-to-SVG (any platform) | Qwen2.5-VL-32B (64GB+ VRAM) — not Apple Silicon viable |

---

## Sources
- https://huggingface.co/mlx-community/sam3-image
- https://huggingface.co/themindstudio/u2net-mlx
- https://huggingface.co/mlx-community/rfdetr-seg-small-fp32
- https://huggingface.co/mlx-community/rfdetr-seg-large-fp32
- https://huggingface.co/briaai/RMBG-1.4
- https://huggingface.co/briaai/RMBG-2.0
- https://huggingface.co/ZhengPeng7/BiRefNet
- https://huggingface.co/svg-hub/qwen-2.5vl-32b-img2svg-ckpt-1500
- https://huggingface.co/svg-hub/qwen-2.5vl-32b-text2svg-ckpt-3500
- https://huggingface.co/thesantatitan/qwen-svg-sft-new-rank128-deepseek
- https://huggingface.co/microsoft/Florence-2-large
