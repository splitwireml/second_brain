---
title: LTX-2.3
created: 2026-04-16
updated: 2026-04-16
type: entity
tags: [model, video-generation, generative-models, video, audio, open-source, diffusion, architecture]
sources: [raw/articles/lightricks-ltx-2-3-2026-04-16.md]
related_entity: [[lightricks]]
---

# LTX-2.3

## Overview

LTX-2.3 is a DiT-based audio-video foundation model developed by [[lightricks]]. It generates synchronized video and audio within a single model — both can be produced together or independently (e.g., video-only, audio-only). It is a significant update to the earlier LTX-2 model with improved audio and visual quality and enhanced prompt adherence.

## Model Variants

| Variant | Description |
|---------|-------------|
| ltx-2.3-22b-dev | Full 22B model, trainable in bf16 |
| ltx-2.3-22b-distilled | 8-step distilled version, CFG=1 |
| ltx-2.3-22b-distilled-1.1 | v1.1 distilled — different aesthetic, improved audio |
| ltx-2.3-22b-distilled-lora-384 | LoRA for full model (384-res) |
| ltx-2.3-22b-distilled-lora-384-1.1 | LoRA for v1.1 distilled |
| ltx-2.3-spatial-upscaler-x2-1.1 | x2 spatial upscaler for latents |
| ltx-2.3-spatial-upscaler-x1.5-1.0 | x1.5 spatial upscaler for latents |
| ltx-2.3-temporal-upscaler-x2-1.0 | x2 temporal upscaler (higher FPS) |

## Key Capabilities

- **Joint audio-video generation** in a single model
- **Modality combinations:** image-to-video, text-to-video, video-to-video, image-text-to-video, audio-to-video, text-to-audio, video-to-audio, audio-to-audio, and cross-combinations (e.g., image-text-to-audio-video)
- **Languages:** English, German, Spanish, French, Japanese, Korean, Chinese, Italian, Portuguese
- **Diffusers library support** (coming soon)
- **ComfyUI support** via built-in LTXVideo nodes in ComfyUI Manager
- **Fully trainable** base (dev) model
- **LoRA/IC-LoRA training** can take less than an hour

## Technical Constraints

- Resolution (W×H) must be divisible by **32**
- Frame count must be divisible by **8 + 1** (i.e., 9, 17, 25, 33...)
- Non-divisible inputs: pad with -1, then crop to desired size
- Requires Python >= 3.12, CUDA > 12.7, PyTorch ~= 2.7

## Limitations

- Not a factual information model
- May amplify societal biases
- Prompt following heavily influenced by prompting style
- Audio without speech may be lower quality

## Availability

- **Demo:** [LTX Studio Playground](https://app.ltx.studio/ltx-2-playground/i2v)
- **API:** [console.ltx.video](https://console.ltx.video/playground/)
- **Local:** GitHub.com/Lightricks/LTX-2 (ComfyUI or PyTorch codebase)

## Related

- [[seedance-2-0]] — related video generation model
- [[makeugc]] — AI UGC ad platform using video generation
- [[open-higgsfield-ai]] — lists LTX Lipsync and LTX-Video as providers
