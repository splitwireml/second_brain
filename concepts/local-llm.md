---
title: "Local LLM"
created: 2026-04-18
updated: 2026-05-12
type: concept
tags: [local-llm, llm, inference, machine-learning]
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

## Related Concepts

- [[three-tier-routing-vs-turboquant-on-16gb-apple-silicon]] — 16 GB memory constraint strategies
- [[flash-moe]] — MoE architecture with local inference support
