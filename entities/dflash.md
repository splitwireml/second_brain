---
title: DFlash
created: 2026-04-16
updated: 2026-04-16
type: entity
tags: [oss-ai, inference, optimization]
sources: [raw/articles/z-lab-dflash-2026-04-16.md]
related_entity: [[z-lab]]
---

# DFlash

Lightweight block diffusion model for speculative decoding. Drafts an entire block of tokens in a single parallel forward pass, then the target LLM verifies them in parallel. Achieves up to **6× lossless acceleration** on Qwen3-8B — nearly 2.5× faster than EAGLE-3.

**Paper:** arXiv:2602.06036
**GitHub:** 1,252 stars (as of 2026-04-16)
**Organization:** [[z-lab]]

## How It Works

Standard LLM inference is sequential — every token depends on the previous one. Speculative decoding uses a small draft model to propose tokens, verified in parallel by the target model. Prior methods like EAGLE-3 draft **autoregressively** (token by token), capping speedups at ~2-3×.

DFlash uses **block diffusion** to draft a full block of tokens in **one parallel forward pass**, removing the sequential draft bottleneck.

## Supported Target Models

| Model | Draft Model |
|---|---|
| Qwen3.5-4B / 9B / 27B / 35B-A3B | z-lab/Qwen3.5-*-DFlash |
| **Qwen3.6-27B** | **z-lab/Qwen3.6-27B-DFlash** — Qwen3.6-27B with diffusion-based speculative decoding; announced April 30 2026 via HuggingFace |
| Qwen3-Coder-Next / 30B-A3B | z-lab/Qwen3-Coder-*-DFlash |
| gpt-oss-20b / 120b | z-lab/gpt-oss-*-DFlash |
| Llama-3.1-8B-Instruct | z-lab/LLaMA3.1-8B-Instruct-DFlash-UltraChat |
| Kimi-K2.5 (preview) | z-lab/Kimi-K2.5-DFlash |

## Serving Backends

- **[[sglang]]** — production serving recommended
- **[[vllm]]** — nightly build required
- **Transformers** — Qwen3 and LLaMA-3.1 only
- **MLX** — Apple Silicon support

## Apple Silicon Heterogeneous Acceleration (2026-04-15)

DFlash is being ported to MLX targeting **ANE + GPU simultaneous execution** on Apple Silicon M-series chips. The approach exploits the M-series unified memory architecture to run the Neural Engine and GPU in parallel for heterogeneous acceleration. See [[mlx-ane-gpu-heterogeneous-acceleration]].

## Relationship to Other Concepts

- [[llm-server-throughput-optimization]] — DFlash is a specific technique within the broader inference optimization space
- [[turboquant-kv-cache-compression]] — complementary: TurboQuant compresses KV cache, DFlash accelerates token drafting
