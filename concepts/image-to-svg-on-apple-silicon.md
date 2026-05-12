---
title: Image-to-SVG on Apple Silicon
created: 2026-04-26
updated: 2026-04-27
type: concept
tags: [apple-silicon, svg, vectorization, image-processing, mlx, vision, gguf]
sources: [raw/articles/huggingface-local-image-bg-removal-svg-models-2026-04-26.md]
---

# Image-to-SVG on Apple Silicon

Converting raster images to SVG (vector graphics) on Apple Silicon Macs — a research gap for neural approaches; traditional tools are the practical local path as of April 2026.

## The Landscape

Image-to-SVG conversion breaks into two paradigms:

| Approach | Description | Apple Silicon Feasibility |
|---|---|---|
| **End-to-end neural** | Model directly outputs SVG paths from raster input | ❌ No viable model exists |
| **Pipeline (mask → vectorize)** | Background removal → edge detection → Potrace | ✅ Fully local, works well |
| **VLM prompting** | Use a VLM to describe/generate SVG from image | ⚠️ Qwen2.5-VL-32B only; 64GB+ VRAM |

## Dedicated Image-to-SVG Models

### svg-hub/qwen-2.5vl-32b-img2svg-ckpt-1500
- **Type:** LoRA adapter on Qwen2.5-VL-32B-Instruct (vision-language model)
- **Size:** ~6.5 GB total (32B base + adapter weights)
- **VRAM Required:** 64GB+ (full 32B Qwen2.5-VL needs hardware Apple Silicon can't provide)
- **Downloads:** 0 — essentially experimental, no community adoption
- **Verdict:** ❌ Not viable for Apple Silicon or any consumer hardware

### svg-hub/qwen-2.5vl-32b-text2svg-ckpt-3500
- **Type:** Text-to-SVG LoRA on same Qwen2.5-VL-32B base
- **Same hardware barrier as img2svg**
- **Verdict:** ❌ Same — 32B VLMs exceed Apple Silicon capacity

### thesantatitan/qwen-svg-sft-new-rank128-deepseek
- **Type:** Qwen3-8B fine-tune for SVG generation (LoRA adapter)
- **Architecture:** Text-to-SVG (generates SVG markup from text descriptions, NOT from raster images)
- **Size:** ~8B base (adapter is separate)
- **VRAM:** ~16GB for Qwen3-8B — potentially runnable on high-end Apple Silicon with quantization
- **Limitation:** This is text→SVG, not image→SVG. Cannot convert a raster image to SVG paths.
- **Verdict:** ⚠️ Interesting for SVG markup generation, but not raster-to-SVG conversion

## Broader Image-to-SVG Research

### DeepSVG (Google, arxiv:2007.11301)
- **What it is:** Hierarchical generative network for vector graphics animation; learned to generate SVG paths from scratch
- **Status:** Research paper only, no production model, no GGUF/CoreML/MLX port
- **Verdict:** ❌ Not deployable

### Im2Vec (arxiv:2102.02798)
- **What it is:** Synthesizes vector graphics without vector supervision; end-to-end raster→SVG
- **Status:** Research only, no production model
- **Verdict:** ❌ Not deployable

### MARVEL (arxiv:2110.04830)
- **What it is:** Manga/comic vectorization via deep reinforcement learning
- **Status:** Research only
- **Verdict:** ❌ Not deployable

## GGUF and Quantization: The Vision Gap

**GGUF (GPT-Generated Unified Format)** from llama.cpp is the standard for quantizing LLMs to run locally. However:

| Model Type | GGUF Available? | Apple Silicon Compatible? |
|---|---|---|
| Text LLMs (Llama, Qwen, Mistral) | ✅ Yes — massive ecosystem | ✅ Yes via llama.cpp/MLX |
| Vision-Language Models (LLaVA, Qwen2-VL) | ❌ Very limited | ⚠️ Rare, no dedicated img2svg |
| Background Removal (RMBG, U-2-Net) | ❌ No GGUF ports found | ✅ Via PyTorch/ONNX |
| Image-to-SVG | ❌ None | ❌ No models exist |

**Key finding:** There is **no GGUF-format vision model for image-to-SVG conversion** anywhere on HuggingFace. Vision quantization is far behind text model quantization.

Florence-2 (microsoft/Florence-2-large, 954K downloads) is a powerful vision foundation model (text-to-image understanding, OCR, detection) but has no SVG generation capability and no GGUF port.

## Practical Local Pipeline (Recommended)

The working local approach on Apple Silicon is a **three-stage pipeline**:

```
Raster Image → Background Removal (mask) → Vectorization (SVG paths)
```

### Stage 1: Background Removal

| Model | Format | Size | Apple Silicon |
|---|---|---|---|
| [[u2net-mlx]] | MLX | ~200MB | ✅ Native |
| [[rmbg-1-4]] | PyTorch/ONNX | ~350MB | ✅ Via Python |
| [[sam3-image]] | MLX | 3.5GB | ✅ Native |

See [[apple-silicon-local-background-removal]] for full comparison.

### Stage 2: Edge/Mask Processing

After getting a clean RGBA or mask image:
- **Canny edge detection** (OpenCV) → clean outlines
- **Otsu thresholding** → binary mask from alpha channel
- **Morphological operations** → close gaps, clean edges

### Stage 3: Vectorization

| Tool | Type | License | Quality |
|---|---|---|---|
| **Potrace** | Bitmap→SVG (Bezier fitting) | GPL | Good for logos/illustrations |
| **Inkscape** (Trace Bitmap) | GUI + CLI | GPL | Good, multiple modes |
| **ImageTracer.js** | JavaScript library | MPL 2.0 | Web-compatible |
| **svgtrace** (Python) | Potrace wrapper | MIT | Scriptable |

### Recommended Tool: Potrace

```bash
brew install potrace

# From RGBA image, extract alpha channel as PNM
convert input.png -alpha extract mask.pbm

# Vectorize
potrace mask.pbm -s -o output.svg

# Higher quality
potrace mask.pbm -s -k 2 -t 3 -o output.svg
```

## Commercial / Web-Based Alternatives

If local neural approaches are required, these hosted services work well:

| Service | Approach | Free Tier |
|---|---|---|
| **Vectorizer.ai** | AI-powered raster→SVG | 5 credits/month |
| **Adobe Express Vectorizer** | AI trace | Free with Adobe account |
| **Vectorizer.io** | Potrace-based with AI upsampling | Limited free |

These are not local but are the only viable neural image-to-SVG options for Apple Silicon today.

## Research Gap

**The core problem:** No lightweight end-to-end neural raster-to-SVG model exists that can run on Apple Silicon unified memory. The field has three distinct problems:

1. **Model size** — Existing image-to-SVG models (Qwen2.5-VL-32B) are too large for consumer hardware
2. **No quantization path** — No GGUF/CoreML ports exist for vision-to-SVG models
3. **No dedicated research** — The community has not produced a purpose-built raster-to-SVG model in GGUF/MLX format

**What would make this viable:** A ~1-3B parameter vision encoder + SVG decoder that fits in <8GB, quantized to Q4/Q5, that produces SVG paths from raster input. This does not yet exist publicly.

## Related Concepts

- [[apple-silicon-local-background-removal]] — Stage 1 of the pipeline
- [[background-removal-vs-matting]] — When to use removal vs. soft matting
- [[rmbg-1-4]] — Most capable general background removal for Apple Silicon PyTorch
- [[u2net-mlx]] — Only native MLX background removal option
