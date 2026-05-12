---
title: Flash-MoE
created: 2026-04-16
updated: 2026-04-16
type: concept
tags: [inference, moe, apple-silicon, efficiency, llm]
sources: [raw/articles/danveloper-flash-moe-qwen-397b-2026-04-16.md]
related_entity: [[dan-woods]]
author: [[dan-woods]]
---

# Flash-MoE

A system for running large Mixture-of-Experts (MoE) models entirely from flash storage — never loading them into DRAM — by exploiting Apple's unified memory architecture and hardware caches. Implemented by [[dan-woods]] in Objective-C and Metal Shading Language.

## Core Thesis

Based on Apple's "LLM in a Flash" paper (arXiv:2312.11514): for MoE models where expert weights dominate total parameters, only a small fraction of weights are active per token. If weight blocks are small enough and SSD bandwidth is high enough, they can be streamed from disk on demand rather than held in memory.

## Technical Details

### Hardware Substrate (M3 Max MacBook Pro)

- **Unified memory:** CPU and GPU share the same physical memory space — no bus-hopping between storage and compute
- **Copper-wired SSD controller:** CPU, GPU, and SSD on a single chip with direct copper interconnects
- **M3 Max sequential SSD reads:** ~17.5 GB/s (3x faster than the M1 Max numbers Apple published in the LLM in a Flash paper)
- **Unified memory architecture:** GPU-visible memory accessible by the CPU without copies

### MoE Sparsity Exploitation

- Qwen 3.5 397B has 512 experts per layer, activates 10 per token
- **K=4 pruning** found viable: no quality degradation; K=3 causes immediate collapse (suggests routing distributes critical computation across exactly 4 experts)
- Result: <2% of expert weights needed per token
- **2-bit requantization** of expert weights: RMSE 0.001–0.003 per layer (negligible quality loss), cuts storage from 209 GB to 120 GB

### Three-Command-Buffer GPU Pipeline

Streams expert weights from disk while the GPU is still computing — CPU pre-loads next layer's experts during current layer execution. No Python, no ML framework in the hot path.

### The Counterintuitive Cache Finding

> Deleting the 9.8 GB Metal LRU expert cache and letting macOS handle caching made everything **38% faster**.

The application-level GPU-visible cache pages forced Apple's hardware memory compressor to work at 60,000–130,000 decompressions/second, burning 1–2 GB/s of memory bandwidth on housekeeping. Removing the cache dropped decompressions to near zero. Theme: **trust the hardware, get the software out of the way.**

### MoE Routing Indeterminacy

Non-deterministic MoE routing makes cache optimization harder than dense models — can't pre-fetch the next layer's experts because you don't know which experts the router will select. Dense models with predictable weight access patterns may actually be better suited for flash streaming since you can pre-fetch deterministically.

## Performance

| Metric | Value |
|--------|-------|
| Sustained throughput | 5.7 tok/s |
| Max token throughput | 7.07 tok/s |
| Resident memory | 5.5 GB |
| Current SSD utilization | Barely being touched |
| Theoretical ceiling (M3 Max, SSD-limited) | 18.6 tok/s |
| Projected M4 Max (no software changes) | ~8 tok/s |

M4 Max SSD bandwidth ~25 GB/s (~20% generation-over-generation improvement). Within 2–3 hardware generations: 10+ tok/s on 400B models on a laptop becomes baseline.

## Generalizability

The approach extends to any MoE model where expert weights dominate total parameters. DeepSeek-V3 (671B total, 37B active) is the most obvious next candidate.

## Relationship to Other Concepts

- [[mixture-of-experts]] — Flash-MoE exploits MoE sparsity to make flash-weight-streaming viable
- [[llm-server-throughput-optimization]] — Same general theme of maximizing hardware utilization
- [[turboquant-kv-cache-compression]] — Related compression theme, but different mechanism (KV cache vs. weight streaming)
- [[three-tier-local-model-routing]] — Different architecture for running large models on constrained hardware

## References

- [flash-moe GitHub](https://github.com/danveloper/flash-moe) (3,641 stars)
- [Apple LLM in a Flash paper — arXiv:2312.11514](https://arxiv.org/pdf/2312.11514)
