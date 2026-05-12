---
title: TurboQuant — KV Cache Compression for LLMs
created: 2026-04-11
updated: 2026-04-13
type: concept
tags: [inference, quantization, optimization, llm]
sources: [raw/transcripts/2026-04-11-After This, 16GB Feels Different.md, raw/articles/x-bookmarks-2026.md]
author: [[alex-ziskind]]
---

**Presented by** [[alex-ziskind]] in "After This, 16GB Feels Different" (2026-04-11).

# TurboQuant — KV Cache Compression for LLMs

## Overview

TurboQuant is a Google's research technique that applies quantization to the KV cache of LLMs, compressing it by up to 6x while maintaining output quality and sometimes improving inference speed. It addresses the memory bottleneck that quantization of model weights alone cannot solve — the KV cache grows linearly with context length and resides in GPU/SoC memory alongside the model weights.

## Background: The KV Cache Problem

When an LLM generates text, it doesn't re-read the entire conversation from scratch for every token. Instead it stores **key-value pairs (KV cache)** — mathematical summaries of every token already processed — inside memory alongside the model weights. This cache grows with every token and can consume gigabytes at long context lengths.

Standard quantization (Q8, Q4, Q3, Q2) compresses the model weights but leaves the KV cache untouched. A 9B parameter model at Q8 is ~10 GB on disk, but running it with a 131K context window on 16 GB Mac Mini fails — the KV cache alone consumes the remaining memory.

## How TurboQuant Works

Unlike weight quantization which compresses the static model weights, **TurboQuant compresses the KV cache dynamically** as tokens are processed. It uses per-token scalar quantization with learned scaling factors.

**Variants (aggressiveness):**
- **Turbo 4** — 1.9x KV cache compression (conservative)
- **Turbo 3** — 2.5x compression
- **Turbo 2** — 4x compression (most aggressive)

**Symmetric vs Asymmetric:**
- **Symmetric** — same Turbo level applied to both K and V heads (original approach, poor quality at high compression)
- **Asymmetric** — Q8 for K (key) heads + Turbo level for V (value) heads — recovers quality while maintaining compression

The asymmetric approach (Q8-K + Turbo-V) was suggested by Tom Turney and dramatically improved quality in benchmarks.

## Experimental Results (Alex Ziskind, M4 Mac Mini / M5 Max MacBook Pro)

### Context Window Scaling on 16GB Mac Mini (Qwen 3.5 9B Q8)
| Context | Q8 KV Cache | Turbo 3 KV Cache | Savings |
|---------|-------------|-------------------|---------|
| 32K | ~growing | ~growing | ~2x more usable |
| 65K | OOM crash | fits | 2x context |
| 131K | crashes | 3.6 GB spare | 2x more usable |

Loading Q8 at 131K context crashes the 16GB Mac Mini. Turbo 3 runs the same model at 131K with headroom to spare.

### Speed: M5 Max MacBook Pro
At short context lengths, TurboQuant is slightly slower (~1-4%). But at **depth 32K context**, Q8 decode speed drops from ~54 tok/s to ~37 tok/s (33% degradation) while **TurboQuant stays flat at ~44 tok/s** — recovering the performance curve. The M5 Max is memory-bandwidth bound at long contexts; compressing the KV cache reduces memory bandwidth pressure, offsetting the decompression cost.

On the Mac Mini (compute-bound), the flat-speed benefit was not observed — matrix multiplications dominate over KV cache reads.

### Quality: Needle-in-Haystack (Mac Mini)
| Config | 1K | 4K | 8K | 16K | 32K |
|--------|-----|-----|-----|------|-----|
| Q8 | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |
| Symmetric Turbo 3 | 1/3 | 0/3 | 0/3 | 0/3 | 0/3 |
| Asymmetric Q8-K + Turbo 3-V | 3/3 | 3/3 | 3/3 | 3/3 | 3/3 |

Symmetric application causes severe quality degradation. Asymmetric application recovers quality completely.

## Implementation Status

- **Not yet in llama.cpp mainline** — community fork by Tom Turney (TurboQuant Plus) implements it as a llama.cpp fork
- **VLLM** — reportedly working on integration
- **LM Studio** — will get it once llama.cpp mainlines it
- **Apple Silicon** — works; M5 Max shows speed benefits, M4/M5 Mac Minis are compute-bound so speed benefit is minimal but context headroom improves dramatically

## Relationship to Weight Quantization

TurboQuant is **orthogonal and complementary** to weight quantization:
- Weight quantization (Q8, Q4, Q3) compresses the static model on disk and in memory
- TurboQuant compresses the dynamic KV cache during inference
- They can be combined: e.g., Qwen 3.5 9B at Q4 weights + Turbo 3 KV cache = fits in 16GB with 131K context

## Key Takeaways

1. **Asymmetric (Q8-K + Turbo-V)** is the only reliable configuration — symmetric modes degrade quality severely
2. **Best for memory-constrained systems** — 16GB Macs, mobile SoCs; less benefit on systems with >64GB
3. **Qwen 3.5 models respond best** on Apple Silicon — other models vary widely
4. **Speed benefit appears at long contexts on bandwidth-bound hardware** (M5 Max) but not on compute-bound hardware (Mac Mini)
5. **Standard 4-bit weight quantization is still the floor** — going below Q4 for weights causes output quality issues (loops, garbage)

## See Also

- [[llm-server-throughput-optimization]] — Alex Ziskind's earlier video on llama.cpp multi-instance throughput optimization
- [[1-bit-bonsai-bitnet-fine-tuning]] — 1-bit weight quantization for extreme memory reduction
- [[vibevoice]] — VibeVoice uses 7.5 Hz tokenization to reduce effective token count, achieving similar KV cache reduction goals via a different approach
- [[insanely-fast-whisper]] — Flash Attention 2 + chunking for speed; different optimization vector
- [[three-tier-local-model-routing]] — complementary architecture pattern for deciding which workloads should stay local in the first place
- [[three-tier-routing-vs-turboquant-on-16gb-apple-silicon]] — comparison of system-level routing versus KV-cache compression on 16 GB Apple Silicon
