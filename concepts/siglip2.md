---
title: SigLIP2
created: 2026-04-16
updated: 2026-04-16
type: concept
tags: [computer-vision, model, vision-language, architecture]
sources: [raw/articles/liquid-ai-lfm2-5-vl-450m-model-card-2026-04-16.md]
related_entity: [[liquid-ai]]
---

# SigLIP2

**SigLIP2** is Google's second-generation SigLIP vision model — a CLIP-style vision-language model for encoding images into dense token representations. Used as the vision encoder in [[lfm2-5-vl-450m]].

## Overview

SigLIP (Sigmoid Loss for CLIP) improves on standard CLIP training by using a sigmoid loss instead of InfoNCE, allowing asymmetric learned biases and better scaling properties. SigLIP2 is the successor with improved architectures and training regimes.

The **NaFlex** variant is a shape-optimized configuration used in [[lfm2-5-vl-450m]] — 86M params, 12 layers, 768 hidden, 256 patches of 16×16.

## Architecture (NaFlex variant)

- **Parameters**: 86M
- **Layers**: 12
- **Hidden size**: 768
- **Attention heads**: 12
- **Patch size**: 16×16
- **Num patches**: 256
- **Activation**: GELU with pytorch tanh approximation
- **Layer norm eps**: 1e-6

## Role in VLMs

SigLIP2 serves as the **vision encoder** in vision-language models. It converts images into visual token sequences that are projected into the LLM's embedding space via an alignment projector.

Typical VLM pipeline:
1. Image → SigLIP2 encoder → visual tokens
2. Visual tokens → projector → LLM embedding space
3. Projected tokens interleaved with text tokens → LLM backbone (e.g., [[lfm2-5-350m]])

## See Also
- [[vision-language-models]]
- [[lfm2-5-vl-450m]]
- [[lfm2-5-350m]]
- [[liquid-ai]]
- [[mixture-of-experts]] (for context on LFM architecture vs. standard ViT+LLM VLMs)
