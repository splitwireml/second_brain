---
title: llama.cpp
created: 2026-04-13
updated: 2026-04-14
type: entity
tags: [oss-ai, inference, open-source, llm]
sources: [raw/transcripts/2026-04-13-rtx-5090-mac-egpu.md]
---

# llama.cpp

Open-source C/C++ LLM inference engine with highly optimized GPU kernels. Central reference point for comparing [[tinygrad]]'s performance.

## Overview

Llama.cpp is the de facto standard for local LLM inference, known for hand-tuned GPU kernels across Metal, CUDA, and other backends. Written in C/C++ for maximum performance and portability.

## Performance Context (from [[alex-ziskind]] benchmarks)

On M4 Pro Mac Mini, same test (Qwen3 4B via LlamaBenchy):

| Engine | Backend | tok/s | Time to First Token |
|--------|---------|-------|---------------------|
| Llama.cpp | Metal | ~73.9 | 651ms |
| TinyGrad | NVIDIA RTX 5090 (Thunderbolt 5) | ~7.39 | ~5000ms |
| TinyGrad | Metal | ~4.29 | ~5000ms |

Llama.cpp is **10x faster** than TinyGrad running NVIDIA GPU over Thunderbolt, and **18x faster** than TinyGrad on Metal for this workload.

The performance gap is attributed to:
- Fused quantization-aware matrix multiplies
- Optimized KV cache management
- Thousands of contributor-hours of hand-tuned kernels

## Memory-Mapped Oversized Models

Current llama.cpp server docs explicitly document `--mmap` / `--no-mmap` and note that memory mapping is enabled by default. That matters beyond load time: it is the enabling mechanism behind patterns like [[three-tier-local-model-routing]], where a base-memory Apple Silicon box can keep a large quantized model on local storage and use it as a heavy preprocessing or fallback tier.

This does not independently verify any single benchmark claim from X/Twitter operators, but it does confirm that mmap-backed serving is a first-class llama.cpp capability rather than an undocumented hack.

## Relationship to Other Entities

- [[tinygrad]] — competing inference engine; TinyGrad auto-generates kernels, llama.cpp hand-tunes
- [[rtx-5090-mac-egpu-benchmarks]] — benchmark concept page with full comparison data between TinyGrad on NVIDIA eGPU and llama.cpp on Metal
- [[alex-ziskind]] — primary benchmarking source for these comparisons
- [[three-tier-local-model-routing]] — routing pattern that uses llama.cpp as the heavy local tier via mmap-backed model loading

## References

- [github.com/ggerganov/llama.cpp](https://github.com/ggerganov/llama.cpp)
