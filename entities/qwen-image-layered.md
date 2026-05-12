---
title: Qwen-Image-Layered
created: 2026-04-23
updated: 2026-04-23
type: entity
tags: [model, qwen, chinese-ai, computer-vision, multimodal, layered-image-decomposition, diffusion, open-source, oss-ai]
sources: [raw/articles/huggingface-unsloth-qwen-image-layered-gguf-2026-04-23.md]
related_entity: [[qwen3-6-27b]]
---

# Qwen-Image-Layered

Image-layer decomposition model by Alibaba's Qwen team (Qwen/Minimax/[[tencent]]?). Decomposes any image into N RGBA layers — each layer is independently editable (recolor, resize, reposition, delete) without affecting others. This physically isolates semantic/structural components, enabling high-fidelity consistent editing. Supports variable-layer decomposition (3, 4, 8 layers) and recursive decomposition (a layer can itself be further decomposed).

## Key Capabilities

- **Layered decomposition**: Any image → N independent RGBA layers
- **Inherent editability**: Edit target layer in isolation (recolor, replace, delete)
- **Elementary operations**: Resize/reposition without distortion
- **Recursive decomposition**: Layers can be further decomposed ad infinitum
- **Consistency**: Edits propagate cleanly across the full composition

## Technical Details

- **Architecture**: Diffusion-based image-to-image pipeline via Diffusers
- **Pipeline**: `QwenImageLayeredPipeline`
- **Framework**: `transformers >= 4.51.3` (Qwen2.5-VL)
- **Recommended resolution**: 640 or 1024
- **Default layers**: 4
- **CFG scale**: 4.0 with `cfg_normalize=True`
- **Inference steps**: 50
- **Languages**: English + Chinese
- **License**: Apache 2.0

## Quantization

GGUF quantized versions by [[unsloth]] available at [unsloth/Qwen-Image-Layered-GGUF](https://huggingface.co/unsloth/Qwen-Image-Layered-GGUF), using Unsloth Dynamic 2.0 methodology. Available quantizations: Q4_0, Q4_1, Q4_K_M, Q4_K_S, Q5_0, Q5_1, Q5_K_M, Q5_K_S, Q6_K, Q8_0.

## Related

- [[qwen3-6-27b]] — Qwen dense language model
- [[qwen3-8b-opus-reasoning]] — Qwen reasoning-specialized variant
- [[computer-vision]] — broader CV domain

## Sources

- [arXiv:2512.15603](https://arxiv.org/abs/2512.15603)
- [Official Blog](https://qwenlm.github.io/blog/qwen-image-layered/)
- [HuggingFace Model Card](https://huggingface.co/Qwen/Qwen-Image-Layered)
- [Demo Space](https://huggingface.co/spaces/Qwen/Qwen-Image-Layered)
