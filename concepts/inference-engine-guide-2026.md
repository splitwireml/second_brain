---
title: Inference Engine Guide 2026
created: 2026-05-20
updated: 2026-05-20
type: concept
tags: [llm, inference, gpu, local-llm, optimization]
sources: [raw/articles/inference-engine-guide-2026-2057183854444843202.md]
---

## Definition

The software layer that turns hardware (GPU, CPU, unified memory) into usable LLM inference. Not "the model" — the traffic cop, memory manager, kernel dispatcher, scheduler, cache accountant, parallelism planner, and API surface.

## One-Page Decision Guide

| Hardware | Engine |
|---|---|
| Laptop/edge/odd | llama.cpp |
| Mac-first | MLX / MLX-LM |
| Single RTX 3090/4090/5090 | ExLlamaV2 |
| 2-4+ NVIDIA/CUDA GPUs | ExLlamaV3 |
| General production | vLLM |
| Long-context/MoE/routing | SGLang |
| NVIDIA max performance | TensorRT-LLM |
| Cluster orchestration | NVIDIA Dynamo |

## Key Principle

Pick hardware strategy, workload shape, and serving model first. The engine follows.

## Workload Phases

- **Prefill** — reads prompt, builds KV cache; compute-intensive
- **Decode** — generates one token at a time; memory-bandwidth-bound

Decode speed tracks memory bandwidth more than peak compute.

## Real Bottlenecks

1. Memory bandwidth (not just VRAM size) — VRAM determines fit, bandwidth determines speed
2. KV cache growth — long context can run out even when weights fit
3. Interconnect — multi-GPU communication cost (NVLink vs PCIe)
4. Scheduler quality — batching, prefill/decode sharing, starvation avoidance
5. Runtime overhead — CUDA graphs, kernel fusion, sampling, tokenizer

## DO NOT USE

- Ollama (not recommended for production)
- llama.cpp / Ollama on multi-GPU setups (use vLLM or ExLlamaV3 instead)

## Benchmarking Rules

Never compare engines using only single-user tok/s. Measure: TTFT, TPOT, p50/p95/p99, cost per 1M tokens, KV cache hit rate. Separate prefill from decode. Test with realistic concurrency.

## Related

- [[local-llm]]
- [[llm-inference-optimization]]