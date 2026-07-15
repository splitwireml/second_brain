---
title: OMLX
name: OMLX
type: entity
description: A specialized inference engine for Apple Silicon built on the MLX framework, featuring a two-tier KV cache system that swaps older context to SSD while keeping immediate context in unified memory.
tags: [apple-silicon, inference-engine, kv-cache, local-ai, mlx, ssd-paging]
sources:
  - type: transcript
    path: raw/transcripts/2026-05-16-OMLX.md
  - type: video
    path: raw/assets/2026-05-16-OMLX.m4a
created: 2026-05-16
updated: 2026-05-16
---

# OMLX

OMLX is a specialized inference runtime designed to maximize performance on Apple Silicon by leveraging MLX's unified memory architecture and introducing a two-tier KV cache system with SSD paging.

## Overview

OMLX addresses the memory bottleneck that limits local AI inference on Macs. Unlike generalist tools that support multiple GPU architectures, OMLX is purpose-built for Apple's unified memory design.

Content creator: [[andrus-better-stack]]

## Key Technical Features

### Unified Memory Architecture

In traditional PCs, CPU and GPU maintain separate memory pools, requiring constant data copying over the PCI bus. Apple Silicon eliminates this through unified memory — the CPU and GPU share the same physical memory.

OMLX exploits this via:
- **Zero-copy arrays**: When the GPU finishes a calculation, the CPU reads results instantly without moving data
- **Lazy computation**: Operations don't execute until the output is actually needed, allowing MLX to optimize the entire calculation graph on the fly

### Two-Tier KV Cache

The critical innovation is how OMLX manages the KV cache compared to tools like LM Studio:

| Aspect | LM Studio | OMLX |
|--------|-----------|------|
| Memory strategy | Holds entire context history in hot RAM | Two-tier: immediate context in unified memory, older context paged to SSD |
| System prompts | Kept in hot state | Frozen and swapped to SSD |
| Memory behavior | Like keeping all tabs open | Like a modern OS: pages data in/out as needed |

### SSD Paging

When older conversation history (system prompts, tool definitions) isn't needed immediately, OMLX freezes it and swaps it to the high-speed SSD. When that context is needed again, OMLX recognizes the prefix, instantly hydrates the model's brain from disk, and resumes without hallucinating or starting from scratch.

## Performance Benchmarks

Tested on MacBook M2 (32GB RAM) with Qwen 3.6 35B parameter 4-bit model building a movie search app:

| Metric | OMLX | LM Studio |
|--------|------|-----------|
| Task duration | ~20 minutes | ~35 minutes |
| Tokens/second | ~47 | ~16 |
| Cache efficiency | 89% | Lower |
| System usability during run | Full (browse, watch video) | Severely degraded |
| Context limit errors | Occasional 400 errors | None |

### The 400 Error Trade-off

OMLX occasionally hits context limit errors (400) on constrained hardware. When this happens, a `/clear` command wipes short-term memory — but unlike other tools, the computational state remains on SSD. When the model receives a new prompt to continue, OMLX instantly rehydrates from disk and picks up exactly where it left off.

## Related

- [[mlx]] — Apple's MLX framework that OMLX is built on
- [[two-tier-kv-cache]] — the memory management concept behind OMLX
- [[better-stack]] — the channel that produced this video
- [[apple-silicon-inference]] — broader context for local inference on Apple Silicon