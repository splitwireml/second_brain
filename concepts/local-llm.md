---
title: "Local LLM"
created: 2026-04-18
updated: 2026-05-12
type: concept
tags: [llm, inference, local-llm, machine-learning]
sources: [raw/articles/xarticle-running-local-llms-2053217139369095252.md]
---

# Local LLM

Self-hosted language model deployment on consumer or on-premises hardware, eliminating API costs and cloud dependencies.

## Definition

Running LLMs locally on personal hardware (typically consumer GPUs, Apple Silicon Macs, or dedicated inference boxes) rather than calling cloud-hosted APIs. Key properties: privacy-preserving, no per-token billing, latency取决于硬件, and requires model quantization/compression for consumer hardware constraints.

## Key Techniques

- [[quantization]] — reducing bit-width precision (GGUF, GPTQ, AWQ, MLX)
- [[llama-cpp]] — CPU/GPU inference engine with broad hardware support
- [[vibevoice]] — MLX-based speech models for Apple Silicon
- [[void-model-mlx]] — MLX-optimized transformer for Apple Silicon

## Related Entities

- [[vibevoice]] — MLX-based speech models for Apple Silicon
- [[omnivoice]] — Xiaomi multilingual TTS, 600+ languages
- [[supertonic-3]] — CPU-only ONNX TTS, 31 languages
- [[void-model-mlx]] — MLX-optimized transformer for Apple Silicon
