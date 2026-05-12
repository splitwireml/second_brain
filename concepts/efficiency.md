---
title: Efficiency
created: 2026-04-16
updated: 2026-04-16
type: concept
tags: [efficiency, optimization]
sources: []
---

## Overview

Efficiency in AI/ML refers to maximizing the useful compute, memory, or parameter utilization of a model relative to its cost. It spans inference optimization, training efficiency, and parameter efficiency — all focused on doing more with less.

## Dimensions

### Inference Efficiency
- **Latency** — time to produce first token / complete output
- **Throughput** — tokens per second (critical for multi-agent workloads)
- **Memory footprint** — VRAM/RAM required to serve a model

### Training Efficiency
- **FLOPs utilization** — actual vs theoretical compute during training
- **Sample efficiency** — how much data is needed to reach a performance target
- **Catastrophic forgetting avoidance** — maintaining performance on old tasks while learning new ones

### Parameter Efficiency
- How much performance can be extracted per trainable parameter (see [[peft]])

## Key Techniques

- **Quantization** — reduce weight precision (FP16 → INT8 → INT4); see [[quantization]]
- **Batching** — increase throughput by batching concurrent requests
- **KV cache optimization** — reduce redundant computation in autoregressive decoding
- **Speculative decoding** — use small draft model to speculatively generate, verify with large model
- **Sparse attention / flash attention** — reduce attention computation complexity

## Relationship to Other Concepts

- [[quantization]] — the primary efficiency technique for reducing memory and increasing speed
- [[training-free]] — efficiency via avoiding training altogether
- [[training]] — efficiency in the training regime
- [[peft]] — parameter efficiency in fine-tuning
