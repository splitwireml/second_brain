---
title: Alex Ziskind
created: 2026-04-11
updated: 2026-04-11
type: entity
tags:
  - person
sources:
  - raw/transcripts/2026-04-11-After This
  - 16GB Feels Different.md
  - raw/transcripts/2026-04-11-Your-local-LLM-is-10x-slower.md
---

# Alex Ziskind

## Overview

Alex Ziskind is a content creator focused on local LLM inference, Apple Silicon optimization, and practical AI deployment. His channel covers benchmarking, quantization, hardware-specific tuning, and tool tutorials for running LLMs efficiently on consumer hardware — particularly Apple Silicon Macs.

## Content Themes

- **Quantization** — weight quantization (Q8, Q4, Q3, Q2), KV cache compression, GGUF formats
- **Apple Silicon** — MLX, MPS, memory management, Metal performance
- **llama.cpp** — multi-instance deployment, throughput optimization, server configurations
- **Benchmarks** — real-world tok/s measurements across hardware, context length scaling, needle-in-haystack quality tests

## Known Videos in Wiki

| Video | Topic | Date |
|-------|-------|------|
| [Your local LLM is 10x slower than it should be](https://www.youtube.com/watch?v=dQw4w9WgXcQ) | llama.cpp multi-instance + nginx throughput optimization | 2026-04-11 |
| [After This, 16GB Feels Different](https://youtu.be/XLlQDfhyBjc) | TurboQuant KV cache compression on Apple Silicon | 2026-04-11 |

## Technical Approach

Alex's methodology:
- **In-machine benchmarks** — measures actual tok/s on real hardware rather than claimed benchmarks
- **Context depth scaling** — tests performance at 4K, 8K, 16K, 32K, 65K, 131K context lengths
- **Quality testing** — uses needle-in-haystack to verify output quality at compression
- **Real-world context** — accounts for OS memory usage, KV cache behavior, system memory pressure

## Relationships

- References **Qwen 3.5** model family extensively as testbed for Apple Silicon benchmarks
- Uses **Bartowski's quantizations** (popular community quantizer) for weight quantization tests
- Covers **Tom Turney's TurboQuant Plus** fork of llama.cpp

## Related Concepts

- [[llm-server-throughput-optimization]] — his earlier video on llama.cpp throughput optimization
- [[turboquant-kv-cache-compression]] — his April 2026 video on KV cache quantization
- [[three-tier-routing-vs-turboquant-on-16gb-apple-silicon]] — comparison page connecting his 16 GB Apple Silicon optimization work to a newer agent-routing pattern

## Related Entities

- [[vibevoice]] — separate voice AI work; Alex covers Apple Silicon ASR optimization
