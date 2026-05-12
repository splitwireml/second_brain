---
title: MoE Offload for 8GB Consumer GPUs
created: 2026-05-01
updated: 2026-05-05
type: concept
tags: [moe, inference, quantization, llama.cpp, local-llm, efficiency, gpu]
sources: [raw/articles/above-spec-moe-35b-rtx4060ti-2026-05-01.md]
related_entity: [[above-spec]]
---

# MoE Offload for 8GB Consumer GPUs

Running 35B+ parameter Mixture-of-Experts (MoE) models on consumer GPUs with 8 GB VRAM, specifically the RTX 4060 Ti and RTX 3070, using llama.cpp MoE offload strategies.

## Core Technique

**MoE offload** — Only the active expert parameters (typically ~3 B out of 35 B total) are loaded on the GPU at each token. The "cold" expert FFN weights are kept in system RAM and streamed as needed:

```bash
-ngl 99 -ncmoe 99
```

- `-ngl 99`: Keep all graph layers on GPU (attention + shared weights)
- `-ncmoe 99`: Offload all MoE expert FFNs to CPU/RAM

## KV Cache Strategy

- **q8_0 KV cache**: ~10 KB/token
- 200k context fits in ~2 GB VRAM with FlashAttention enabled
- This leaves room for the active 3 B params (~1.5 GB at Q4) within 8 GB

## Benchmark Results (AboveSpec, May 2026)

Hardware: RTX 4060 Ti 8 GB + 64 GB system RAM
Model: Qwen3.6-35B-A3B Q4_K_S + q8_0 KV

| Context | Tokens/sec |
|---------|-----------|
| 16k | 41 tok/s |
| 200k | 24 tok/s |

Key observations:
- **PP (Prompt Processing) barely moves**: 332 tok/s even at 200k tokens
- **TG (Token Generation) decays linearly**: attention scan over full KV is the bottleneck
- RTX 3070 8 GB performs comparably due to higher memory bandwidth (448 vs 288 GB/s) despite lower compute

## Why MoE + 8GB is the New Sweet Spot

The real bottleneck for MoE offload is **host-RAM bandwidth** — the cold expert FFNs require ~1.5 GB/token of streaming reads from DDR5. This is a bandwidth problem, not a compute problem. As long as system RAM bandwidth is sufficient:
- Only 3 B params are active per token
- 64 GB RAM provides ample headroom for offloaded experts
- 8 GB VRAM handles attention + shared weights + KV cache

## Tools

- [[llama-cpp]] with MoE offload support
- TurboQuant KV cache compression (TheTom/[@no_stp_on_snek](https://x.com/no_stp_on_snek)) for fitting larger contexts

## Related Concepts

- [[mixture-of-experts]] — General MoE architecture
- [[quantization]] — Q4_K_S and q8_0 quantization levels
- [[local-llm]] — Home/small-scale LLM inference
- [[llama-cpp]] — Inference engine used for MoE offload
