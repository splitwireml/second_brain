---
title: Vision-Language Models (VLM)
created: 2026-04-14
updated: 2026-04-16
type: concept
tags: [vision-language, llm, model, computer-vision, research]
sources: [raw/articles/liquid-ai-lfm2-5-vl-450m-model-card-2026-04-16.md]
---

# Vision-Language Models (VLM)

**Vision-Language Models (VLMs)** are multimodal LLMs that process both images and text, enabling capabilities like image captioning, visual question answering, and instruction following from visual inputs.

## Architecture

Typical VLM architecture:
- **Vision encoder** — processes images into token representations (e.g. CLIP ViT, SigLIP)
- **LLM backbone** — text-only decoder that accepts visual tokens interleaved with text tokens
- **Projection/alignment layer** — maps visual features into the LLM's embedding space

## Examples

- [[hy-embodied-0-5]] — Embodied VLM with MoT architecture for robotics/VLA
- [[lfm2-5-vl-450m]] — Liquid AI VLM; SigLIP2 vision encoder + LFM2.5-350M backbone; bounding box prediction, function calling
- GPT-4V, Claude Vision, Gemini Vision
- LLaVA, CogVLM, Yi-VL

## Vision Encoders

Key vision encoder families used in VLMs:
- **CLIP ViT** — original contrastive vision-language training
- **SigLIP** — sigmoid loss CLIP variant (Google); better scaling properties than InfoNCE-based CLIP
- **SigLIP2** — second-generation SigLIP; used in [[lfm2-5-vl-450m]]; NaFlex variant is 86M params, 12 layers
- **DINOv2** — self-supervised ViT variant; used in some open VLMs

## VLM vs VLA

VLMs output text. [[vla-robotics]] models extend VLMs by also outputting physical actions for robot control.

## See Also

- [[hy-embodied-0-5]]
- [[embodied-ai]]
- [[vla-robotics]]
- [[tencent]]
