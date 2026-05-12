---
title: Qwen3-6-35B-A3B
created: 2026-05-03
updated: 2026-05-03
type: entity
tags: [llm, qwen, moe, model, open-source, chinese-ai]
sources: [raw/articles/qwen3-6-35b-rtx4070-12gb-iam-shanmukha-2026-05-01.md]
related_entity: [[iam-shanmukha]]
---

# Qwen3-6-35B-A3B

Mixture-of-Agents 35B model by Alibaba Qwen team (35B total / A3B = 3 experts, ~27B active parameters). Open-weight, Apache 2.0.

## Key Specifications

- **Architecture**: MoE with 3 experts (A3B = 3 active of N experts)
- **Total parameters**: 35B
- **Active parameters**: ~27B per expert activation
- **Quantization**: Q4_K_M, Q4_K_XS, IQ4_XS all viable on consumer GPUs
- **Context**: Up to 262K (reported working at full context on RTX 4070 12GB + 64GB system RAM)
- **Speed**: Up to 60 tok/s on RTX 4070 12GB VRAM with proper llama-server flags

## Consumer GPU Benchmarks

| GPU | VRAM | Quant | Speed | Context |
|-----|------|-------|-------|---------|
| RTX 4070 | 12GB | Q4_K_M | ~60 tok/s | 128K |
| RTX 4070 | 12GB | Q4_K_XL | ~60 tok/s | 128K |
| RTX 4070 | 12GB | IQ4_XS | 80+ tok/s | 128K |
| RTX 4060 Ti | 8GB | Q4_K_M | ~41 tok/s | 16K |
| RTX 4060 Ti | 8GB | Q4_K_M | ~24 tok/s | 200K |

## Key llama-server Flags

From [[iam-shanmukha]] benchmarks:
- `-ngl 999` — load all layers to GPU
- `-ncmoe 25` (or 60) — MoE expert activation count, controls VRAM usage; lower = less VRAM, lower speed
- `-fa` — Flash Attention
- `--cache-type-k q8_0 --cache-type-v q8_0` — KV cache quantization; Qwen models tolerate Q4_K quality close to q8_0
- `--fit-target 256` — alternative to `-ngl 999`; reported 80+ tok/s with IQ4_XS on RTX 4070
- `-c 131072` — 128K context

## Related

- [[qwen3-6-27b]] — dense 27B variant; same family, different architecture
- [[dflash]] — z-lab diffusion-based speculative decoding; Qwen3.6-27B-DFlash variant
- [[local-llm]] — consumer GPU inference
- [[moe-offload-8gb-gpu]] — related 35B MoE on 8GB consumer GPU work
- [[llm-server-throughput-optimization]] — llama.cpp multi-instance throughput techniques
