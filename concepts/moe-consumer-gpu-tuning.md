---
title: MoE Consumer GPU Tuning
created: 2026-05-03
updated: 2026-05-03
type: concept
tags: [local-llm, inference, moe, optimization]
sources: [raw/articles/qwen3-6-35b-rtx4070-12gb-iam-shanmukha-2026-05-01.md]
related_entity: [[qwen3-6-35b-a3b]]
author: [[iam-shanmukha]]
---

# MoE Consumer GPU Tuning

## Definition

Techniques for running large Mixture-of-Experts (MoE) language models on consumer-grade GPUs with limited VRAM (8-12GB), using quantization, KV cache compression, and llama.cpp flag tuning to achieve usable throughput at long context lengths.

## Key Techniques

### MoE Expert Activation Control

The `-ncmoe` flag in llama-server controls how many MoE experts are activated per token. Lower values reduce VRAM usage at the cost of speed:

- `ncmoe 60` — maximum throughput, ~8GB VRAM on RTX 4070 12GB
- `ncmoe 25` — balanced, ~4GB VRAM, still fast
- Lower values possible with proportional speed reduction

### KV Cache Quantization

Qwen models tolerate aggressive KV cache quantization without significant quality loss:
- `--cache-type-k q8_0 --cache-type-v q8_0` — q8_0 KV cache
- Q4_K cache quality is close to q8_0 on Qwen models specifically
- Enables 128K+ context on 12GB VRAM cards

### Flash Attention

`-fa` flag enables Flash Attention, significantly speeding up attention computation at long contexts with minimal quality impact.

### Fit-Target Parameter

`--fit-target 256` as an alternative to `-ngl 999` — lets the inference engine auto-tune layer placement across VRAM and system RAM, reported to achieve 80+ tok/s on RTX 4070 with IQ4_XS quantization.

## Benchmark Reference

[[iam-shanmukha]] benchmark on RTX 4070 12GB + 64GB RAM:
- Qwen3.6-35B-A3B GGUF Q4_K_M at 60 tok/s, 128K context
- llama-server with `-ngl 999 -ncmoe 25 -fa --cache-type-k q8_0 --cache-type-v q8_0 -c 131072`

[[above-spec]] benchmark on RTX 4060 Ti 8GB:
- 35B MoE at 41 tok/s at 16K context, 24 tok/s at 200K context

## Relationship to Other Concepts

- [[local-llm]] — the broader goal of running LLMs without cloud dependency
- [[moe-offload-8gb-gpu]] — related 35B MoE + 8GB VRAM work (RTX 4060 Ti)
- [[llm-server-throughput-optimization]] — multi-instance llama.cpp throughput optimization
- [[quantization]] — the compression technique making this possible
- [[qwen3-6-35b-a3b]] — the specific model these techniques target
