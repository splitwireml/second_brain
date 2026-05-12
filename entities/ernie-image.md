---
title: Ernie Image
created: 2026-04-23
updated: 2026-04-26
type: entity
tags: [oss-ai, diffusion, image-generation, chinese-ai, baidu, comfyui]
sources:
  - type: transcript
    path: raw/transcripts/2026-04-23-Ernie-Image-AI-ComfyUI.md
  - type: article
    path: raw/articles/huggingmodels-ernie-image-2046273468120158637.md
related_entity: [[baidu]]
---

# Ernie Image

Open-source image generation model from [[baidu]]. An 8B parameter diffusion transformer supporting multi-language text rendering and complex prompt adherence. Available in base and Turbo variants.

## Key Facts

- **Parameters:** 8B (diffusion transformer)
- **Variants:** Base model (50 sampling steps), Turbo model (8 sampling steps)
- **Text Encoder:** Mistral 3 (3B params)
- **VAE:** Flux2 VAE
- **Text Rendering:** Multi-language support (highlighted strength)
- **ComfyUI Support:** Native from launch day

## Capabilities

### Strengths

- **Text rendering:** Excellent, especially for comic styles, speech bubbles, and multi-language text
- **Layout/structure:** Strong prompt adherence for comic panels, posters, app mockups
- **Anime styles:** Clean aesthetic results
- **Prompt adherence:** Complex text prompts handled well via text encoder + language model

### Weaknesses

- **Photorealism:** Not competitive with Z-Image Turbo; skin textures can become oversaturated or reptilian when detailed skin texture keywords are added
- **Text placement in comics:** Hit-or-miss; requires multiple seed attempts

## Ernie Image vs Z-Image Turbo

Benchmarks show similar overall performance. Z-Image Turbo is stronger on photorealism aesthetics. Ernie Image excels at text rendering and comic/anime styles.

## Files Required (ComfyUI)

1. Diffusion model — `Ernie Image Turbo`
2. Text encoder — Mistral 3 3B
3. Prompt enhancer — Ernie Image Prompt Enhancer Safe Tensors
4. VAE — Flux2 VAE

## See Also

- [[ernie-image-vs-z-image-turbo]] — side-by-side comparison with Z-Image Turbo
- [[baidu]] — parent company
- [[benji-ai-playground]] — YouTube benchmarks
