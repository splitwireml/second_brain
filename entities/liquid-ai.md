---
title: Liquid AI
created: 2026-04-16
updated: 2026-04-16
type: entity
tags: [AI-company, llm, model]
sources: [raw/articles/liquid-ai-lfm2-5-vl-450m-model-card-2026-04-16.md]
---

# Liquid AI

**Liquid AI** is an AI company building Liquid Foundation Models (LFMs) — hybrid neural network architectures optimized for on-device and edge deployment.

## Overview

Liquid AI was founded to build efficient, compact LLMs that rival much larger models while running on consumer hardware. Their LFM architecture uses a hybrid of LIV (Locally Interactive Value) convolution blocks and standard GQA transformer blocks.

## Products

### Text Models
- [[lfm2-5-350m]] — 350M parameter instruction-tuned model; 28T token training budget; best-in-class per-parameter performance
- LFM2.5-350M-Base — pre-trained base model for fine-tuning

### Vision-Language Models
- [[lfm2-5-vl-450m]] — vision-language model with SigLIP2 encoder; 450M total params; multimodal instruction following

### Format Variants
All models ship in: Native (Transformers/vLLM/SGLang), GGUF (llama.cpp), ONNX, and MLX (Apple Silicon).

## Architecture

LFM models use a hybrid architecture combining:
- **LIV convolution blocks** — locally interactive value blocks for efficient pattern recognition
- **GQA transformer blocks** — grouped-query attention for the language modeling head

The architecture is designed for sub-linear inference cost at small parameter counts.

## See Also
- [[vision-language-models]]
- [[mixture-of-experts]]
- [[vllm]]
- [[sglang]]
- [[llama-cpp]]
