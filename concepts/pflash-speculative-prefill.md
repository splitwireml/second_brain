---
title: PFlash Speculative Prefill
created: 2026-05-01
updated: 2026-05-01
type: concept
tags: [inference, optimization, efficiency, llm, local-llm, gpu]
sources: [raw/articles/pflash-cuda-prefill-speedup-2026-05-01.md]
related_entity: [[dflash]]
author: [[pupposandro]]
---

# PFlash Speculative Prefill

A C++/CUDA speculative prefill system that achieves **10× faster time-to-first-token (TTFT)** on long-context LLM inference compared to vanilla [[llama-cpp]], by using a small in-process drafter to select only the tokens that matter before the target model prefills.

## How It Works

PFlash stacks two algorithms:

1. **Cross-Family Speculative Prefill** (Liu et al / SambaNova, ICLR 2026): A small draft model (Qwen3-0.6B BF16) runs over the full prompt and scores per-token importance via attention. The top-scoring spans are kept (keep_ratio=0.05); the rest are dropped. The target model then prefills only ~6.5K tokens at 128K context instead of the full 128K.

2. **FlashPrefill CUDA port** (Fan et al, 2026): 4 hand-written CUDA kernels (mean_K, score, select, sparse_fwd) plus Block-Sparse-Attention (BSA) from mit-han-lab for the sparse attention forward. This makes the drafter itself fast enough at 128K that it doesn't become the bottleneck.

No Python, Triton, or PyTorch runs in the inference loop.

## Benchmark Results

On Qwen3.6-27B Q4_K_M / RTX 3090 (single-shot):

| Context | PFlash TTFT | llama.cpp TTFT | Speedup |
|---------|-------------|----------------|---------|
| 128K    | 24.8s       | ~257s          | 10.4×   |
| 64K     | 13.5s       | 134.95s        | 10.0×   |

Decode after prefill runs at ~74 tok/s via [[dflash]] speculative decode.

Quality is preserved: NIAH (Needle-in-a-Haystack) retrieval succeeds at every tested context from 32K to 128K with keep_ratio=0.05.

## Architecture

PFlash sits on top of [[dflash]] (block diffusion speculative decoding daemon). The drafter (1.3GB) + dflash daemon (15GB + 3GB + 3GB) don't fit in 24GB VRAM on RTX 3090, so a park/unpark protocol swaps them in/out of VRAM (~3s overhead per request).

## Relationship to Other Concepts

- [[block-diffusion-speculative-decoding]] — PFlash uses speculative prefill to reduce target prefill cost; dflash handles the block diffusion spec decode after
- [[llama-cpp]] — PFlash's comparison baseline; vanilla llama.cpp prefill is O(S²)
- [[dflash]] — PFlash sits in front of dflash for the decode phase
- [[inference-kernel-optimization]] — PFlash uses hand-written CUDA kernels (4 total) for maximum efficiency

## Technical Notes

- Drafter: Qwen3-0.6B BF16 loaded in-process with the target via custom ggml graph
- BSA kernel: FA-2 derived sm_80+ from mit-han-lab/Block-Sparse-Attention
- keep_ratio=0.05 keeps ~6.5K tokens at 128K source length
- DFLASH_FP_ALPHA=0.85 block-selection threshold (0.99 = stricter, ~1s faster at 128K with small quality loss)