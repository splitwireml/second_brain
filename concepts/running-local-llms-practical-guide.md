---
title: "Running Local LLMs: From First Run to Fine-Tuned"
created: 2026-05-09
updated: 2026-05-09
type: concept
tags: [local-llm, inference, quantization, apple-silicon, nvidia, fine-tuning, gguf, kv-cache]
sources: [raw/articles/xarticle-running-local-llms-from-first-run-to-fine-tuned-2053217139369095252.md]
related_entity: [[michaelzguo]]
---

# Running Local LLMs: From First Run to Fine-Tuned

Comprehensive practical guide covering the five layers of local LLM deployment: hardware (memory bandwidth as the real metric), memory math (weights + KV cache + overhead), runtime (Ollama vs llama.cpp), model selection (quantization, MoE, prompt templates), and optimization (Flash Attention, KV cache quantization, imatrix, speculative decoding).

## Five Layers Framework

1. **Hardware** — Memory bandwidth (not FLOPS) is the real constraint for local inference; Apple Silicon unified memory and NVIDIA consumer GPUs compared
2. **Memory Math** — Total memory = weights + KV cache + runtime overhead; context size is the hidden memory variable; Q4 as sweet spot (~0.5 bytes/param)
3. **Runtime** — Ollama (simple, automatic chat templates) vs llama.cpp (full control: --jinja, --flash-attn, --ctx-size, --n-gpu-layers)
4. **Model Selection** — Reading GGUF filenames (base/instruct/chat, quantization level, K-quants, MoE A3B suffix); prompt template sensitivity
5. **Optimization** — Core parameters (num_ctx, num_gpu, num_batch), Flash Attention, KV cache quantization, imatrix importance-guided quantization, speculative decoding, MTP

## Key Insights

- A Q4 8B model outperforms an FP16 3B model on most everyday tasks — bigger architecture at lower quantization beats smaller at FP16
- MoE memory requirement based on total parameters (all weights load), but compute based on active parameters only
- For local agent use and tool calling, latency and instruction-following stability often matter more than benchmark rankings
- TPS measures speed, not quality — test on actual tasks: instruction following, long context, code, hallucination

## Source

[X Article by @Michaelzsguo](https://x.com/Michaelzsguo/status/2053217139369095252) — Sat May 09 2026 (190 likes, 32 RTs)
