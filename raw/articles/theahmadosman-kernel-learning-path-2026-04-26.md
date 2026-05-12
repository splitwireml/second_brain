---
source: https://x.com/TheAhmadOsman/status/2048413820259832050
author: "@TheAhmadOsman"
date: 2026-04-26
type: x-article
tweet_id: "2048413820259832050"
quoted_tweet_id: "2048234466519236818"
---

# @TheAhmadOsman — How to Learn GPU Kernel Optimization

**@TheAhmadOsman** — Sun Apr 26 14:48:07 +0000 2026

---

How to go about learning all of this?

## 1st: Start with the serving engine view

- **vLLM**: PagedAttention, continuous batching, prefix caching, CUDA graphs
- **SGLang**: RadixAttention/prefix reuse, speculative decoding, MoE, structured/agent workloads
- **TensorRT-LLM**: NVIDIA peak stack, FP8/FP4, Wide-EP, disaggregated serving
- **FlashInfer**: reusable kernel/operator library for attention/GEMM/MoE/sampling

## 2nd: Go down the stack

- Triton tutorials → custom fused kernels
- CUTLASS/CuTe → Tensor Core GEMM and Blackwell/Hopper details
- FlashAttention papers → attention algorithm/kernel co-design
- PagedAttention paper → KV-cache memory management
- MoE docs → routing + grouped GEMM + all-to-all
- Nsight profiling → stop guessing

## 3rd: Do this mini-project sequence

1. Implement RMSNorm in Triton; compare to PyTorch
2. Implement fused SiLU × gate
3. Implement simple FP16 matmul; compare to cuBLAS/rocBLAS
4. Implement paged KV lookup for decode attention
5. Add FP8 KV cache with per-block scales
6. Implement toy top-k sampling on GPU
7. Implement tiny MoE dispatch + grouped GEMM
8. Integrate one custom op into vLLM or SGLang and profile end-to-end

---

Quoted tweet (2048234466519236818): "You don't 'run a model' / You run Kernels..."
