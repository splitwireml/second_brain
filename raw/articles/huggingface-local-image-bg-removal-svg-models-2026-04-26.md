---
title: HuggingFace Local Image Background Removal and SVG Models — Apple Silicon Research
created: 2026-04-26
updated: 2026-04-27
type: raw
tags: [research, huggingface, apple-silicon, mlx, background-removal, svg, image-processing, gguf]
sources: []
---

# Research: HuggingFace Local Image Background Removal and Image-to-SVG Models for Apple Silicon

**Date:** 2026-04-26
**Source:** HuggingFace model repository (huggingface.co/models), HF API
**Scope:** Image background removal and image-to-SVG conversion models with Apple Silicon / MLX support

---

## Background Removal Models — Apple Silicon / MLX Native

### MLX-Native Models (Apple Silicon)

#### 1. sam3-image (mlx-community/sam3-image)
- **Architecture:** SAM3 with ViTDet backbone (Meta's Segment Anything Model 3)
- **Framework:** MLX (Apple's machine learning framework)
- **Model Size:** ~3.5 GB
- **VRAM:** Not specified — MLX uses unified memory
- **Requirements:** macOS 13.0+, Apple Silicon (M1/M2/M3/M4), Python 3.13+
- **Features:** Text prompts, box prompts, interactive segmentation
- **License:** Apache 2.0
- **Downloads:** Not tracked
- **Source:** https://huggingface.co/mlx-community/sam3-image

#### 2. u2net-mlx (themindstudio/u2net-mlx)
- **Architecture:** U-2-Net (Universal U-Net)
- **Framework:** MLX
- **Model Size:** 176 MB (quantized)
- **VRAM:** Not specified — MLX uses unified memory
- **Purpose:** Background removal specifically
- **License:** Apache 2.0
- **Downloads:** Not tracked
- **Source:** https://huggingface.co/themindstudio/u2net-mlx

#### 3. rfdetr-seg-small-fp32 (mlx-community/rfdetr-seg-small-fp32)
- **Architecture:** DINOv2-small backbone + C2f projector + 4-layer Deformable DETR decoder + 4-block Segmentation head
- **Framework:** MLX
- **Parameters:** ~36M
- **Input Resolution:** 384x384
- **Mask Resolution:** 96x96
- **VRAM / Memory:** 683 MB peak
- **Inference (M4 Max):** ~26ms (38 FPS)
- **License:** Apache 2.0
- **Downloads:** 30/month
- **Source:** https://huggingface.co/mlx-community/rfdetr-seg-small-fp32

#### 4. rfdetr-seg-large-fp32 (mlx-community/rfdetr-seg-large-fp32)
- **Architecture:** DINOv2-small backbone + C2f projector + 5-layer Deformable DETR decoder + 5-block Segmentation head
- **Framework:** MLX
- **Parameters:** ~36M
- **Input Resolution:** 504x504
- **Mask Resolution:** 126x126
- **VRAM / Memory:** 1.2 GB peak
- **Inference (M4 Max):** ~89ms (11 FPS)
- **License:** Apache 2.0
- **Downloads:** 13/month
- **Source:** https://huggingface.co/mlx-community/rfdetr-seg-large-fp32

### Non-MLX Models (CPU/GPU, runnable on Mac)

#### 5. briaai/RMBG-1.4 (BRIA AI)
- **Architecture:** IS-Net (enhanced) — saliency segmentation model
- **Framework:** PyTorch, ONNX, Transformers.js
- **Model Size:** ~170 MB
- **Purpose:** Background removal — general purpose
- **Training Data:** 12,000 high-quality manually labeled images (legally licensed)
- **Categories Covered:** Objects (45%), People+objects/animals (25%), People (17%), Text (3%), Animals (2%)
- **Benchmark:** Balanced gender, ethnicity, disability representation
- **License:** CC BY-NC 4.0 (non-commercial); commercial license available from BRIA AI
- **Downloads:** 915,862/month (top background removal model on HuggingFace)
- **Source:** https://huggingface.co/briaai/RMBG-1.4

#### 6. briaai/RMBG-2.0 (BRIA AI)
- **Architecture:** Improved over RMBG-1.4 (specific architecture not disclosed)
- **Framework:** PyTorch, ONNX, Transformers.js
- **Purpose:** Background removal — state-of-the-art improvement over v1.4
- **License:** CC BY-NC 4.0 (non-commercial); commercial license available
- **Downloads:** 454,177/month
- **Source:** https://huggingface.co/briaai/RMBG-2.0

#### 7. ZhengPeng7/BiRefNet
- **Architecture:** BiRefNet (Bilateral Reference Network) — Dichotomous Image Segmentation
- **Framework:** PyTorch (custom birefnet library)
- **Model Size:** ~400 MB
- **Tasks:** Background removal, mask generation, salient object detection, camouflaged object detection
- **License:** MIT
- **Downloads:** 848,461/month (2nd most downloaded image segmentation model)
- **Source:** https://huggingface.co/ZhengPeng7/BiRefNet

#### 8. CIDAS/clipseg-rd64-refined
- **Architecture:** CLIPSeg (CLIP-based image segmentation)
- **Framework:** Transformers
- **License:** Apache 2.0
- **Downloads:** 926,736 (most downloaded image segmentation model overall)
- **Source:** https://huggingface.co/CIDAS/clipseg-rd64-refined

---

## Image-to-SVG Models — The Full Picture

### svg-hub/qwen-2.5vl-32b-img2svg-ckpt-1500
- **Base Model:** Qwen2.5-VL-32B-Instruct
- **Framework:** PEFT (LoRA adapter)
- **Type:** Image-to-SVG via vision-language model
- **Model Size:** ~6.5 GB total (adapter is PEFT LoRA on top of 32B base)
- **VRAM Required:** 64+ GB (32B VLM — NOT Apple Silicon feasible on most Macs)
- **Downloads:** 0 (private/limited)
- **Note:** This is the only dedicated image-to-SVG model found on HuggingFace. It requires significant GPU resources and is not practical for local Apple Silicon deployment.
- **Source:** https://huggingface.co/svg-hub/qwen-2.5vl-32b-img2svg-ckpt-1500

### svg-hub/qwen-2.5vl-32b-text2svg-ckpt-3500
- **Base Model:** Qwen2.5-VL-32B-Instruct
- **Type:** Text-to-SVG LoRA adapter
- **Same 64GB+ VRAM requirement — not viable for Apple Silicon**

### thesantatitan/qwen-svg-sft-new-rank128-deepseek
- **Base Model:** Qwen3-8B (NOT a VLM — text-only)
- **Type:** Text-to-SVG — generates SVG markup from text descriptions
- **Downloads:** 4 — essentially experimental
- **Limitation:** Generates SVG markup from text, not from raster images. Cannot convert a PNG/jpg to SVG paths.
- **Verdict:** Not applicable to raster→SVG; useful only if you want to generate SVG from scratch via prompts

### Alternative Approaches for SVG Generation

No dedicated image-to-SVG models optimized for Apple Silicon were found on HuggingFace. Alternatives include:

1. **CLIPSeg + Potrace/vectorizer pipeline** — Use CLIPSeg for masking, then vectorize with Potrace or similar
2. **Segment Anything (SAM) + path tracing** — SAM for precise masks, then trace with stroke-based SVG tools
3. **Rembg (background removal) + SVG tracer** — Remove background, then use svgtrace, Vectorizer.app, or Adobe Express
4. **Adobe Express / Vectorizer.app** — Not local; cloud-based but free tier available
5. **Inkscape / ImageTracer** — Traditional open-source bitmap-to-SVG tools, CPU-based, run locally

---

## Summary Table

| Model | Framework | Size | Apple Silicon MLX | Purpose | License | Downloads/month |
|-------|-----------|------|-------------------|---------|---------|---------------|
| sam3-image | MLX | ~3.5GB | YES (native) | Segmentation (interactive) | Apache 2.0 | N/A |
| u2net-mlx | MLX | 176MB | YES (native) | Background removal | Apache 2.0 | N/A |
| rfdetr-seg-small | MLX | ~683MB | YES (native) | Instance segmentation | Apache 2.0 | 30 |
| rfdetr-seg-large | MLX | ~1.2GB | YES (native) | Instance segmentation | Apache 2.0 | 13 |
| RMBG-1.4 | PyTorch/ONNX | ~170MB | NO (but runs on Mac CPU) | Background removal | CC BY-NC | 915K |
| RMBG-2.0 | PyTorch/ONNX | ~170MB | NO (but runs on Mac CPU) | Background removal | CC BY-NC | 454K |
| BiRefNet | PyTorch | ~400MB | NO (but runs on Mac CPU) | Background removal/Masking | MIT | 848K |
| clipseg-rd64 | Transformers | ~100MB | NO (but runs on Mac CPU) | CLIPSeg segmentation | Apache 2.0 | 926K |
| qwen-vl-img2svg | PEFT/VLM | 6.5GB+ | NO (needs 64GB+ VRAM) | Image-to-SVG | Proprietary | 0 |

---

## GGUF and Quantization — Vision Model Gap

**GGUF** (GPT-Generated Unified Format) from llama.cpp is the standard for quantizing LLMs to run locally. However, vision models have a severe GGUF gap:

| Model Type | GGUF Available? | Apple Silicon Compatible? |
|---|---|---|
| Text LLMs (Llama, Qwen, Mistral) | ✅ Yes — massive ecosystem | ✅ Yes via llama.cpp/MLX |
| Vision-Language Models (LLaVA, Qwen2-VL) | ⚠️ Very rare | ⚠️ No dedicated img2svg |
| Background Removal (RMBG, U-2-Net) | ❌ No GGUF ports found | ✅ Via PyTorch/ONNX |
| Image-to-SVG | ❌ None | ❌ No models exist |

**Searched extensively for GGUF vision models (all returned empty):**
- `gguf+vision`, `gguf+multimodal`, `gguf+image` — no results
- `segmentation+gguf`, `background+removal+gguf`, `u2net+gguf`, `sam+gguf` — no results
- `llava+gguf`, `vlm+gguf`, `moondream+gguf` — no results

**Florence-2** (microsoft/Florence-2-large, 954K downloads) is a powerful general vision model but produces text outputs, not SVG paths, and has no GGUF port.

**The fundamental issue:** Vision model quantization is far behind text model quantization. No one has yet produced a purpose-built GGUF port for any image-to-SVG model.

## Key Findings

1. **Best Apple Silicon MLX option for background removal:** u2net-mlx (176MB, dedicated background removal)
2. **Best Apple Silicon MLX option for general segmentation:** sam3-image (3.5GB, interactive, text/box prompts)
3. **Best overall (non-MLX, runs on Mac):** BRIA RMBG-1.4 (915K downloads/month, CC BY-NC)
4. **Best MIT-licensed option:** BiRefNet (848K downloads/month, fully open)
5. **Image-to-SVG on Apple Silicon:** No local solution exists — the only dedicated img2svg model (Qwen2.5-VL-32B) needs 64GB+ VRAM. Best path is a pipeline: background removal + Potrace vectorization.
6. **GGUF gap:** No GGUF-format vision model for image-to-SVG exists anywhere on HuggingFace. Vision model quantization is years behind text model quantization.
7. **Practical recommendation:** For local image→SVG on Apple Silicon: run RMBG-1.4 or u2net-mlx to get a clean RGBA mask, then pipe through Potrace for vectorization.
