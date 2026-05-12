---
title: GPU Kernel Learning Path
created: 2026-04-26
updated: 2026-04-26
type: concept
tags: [inference, optimization, performance]
sources: [raw/articles/theahmadosman-kernel-learning-path-2026-04-26.md]
related_entity: [[theahmadosman]]
author: [[theahmadosman]]
---

## Definition

A structured 3-stage learning curriculum for GPU kernel optimization in LLM inference, authored by [[theahmadosman]] as a follow-up to the [[inference-kernel-optimization]] thread.

## Stage 1: Serving Engine View

Start by understanding the systems that orchestrate kernel execution:

- **[[vllm]]** — PagedAttention, continuous batching, prefix caching, CUDA graphs
- **[[sglang]]** — RadixAttention/prefix reuse, speculative decoding, MoE, structured/agent workloads
- **TensorRT-LLM** — NVIDIA peak stack, FP8/FP4, Wide-EP, disaggregated serving
- **FlashInfer** — reusable kernel/operator library for attention/GEMM/MoE/sampling

## Stage 2: Down the Stack

Go deeper into the underlying primitives:

- **Triton tutorials** → custom fused kernels
- **CUTLASS/CuTe** → Tensor Core GEMM and Blackwell/Hopper architecture details
- **FlashAttention papers** → attention algorithm and kernel co-design
- **PagedAttention paper** → KV-cache memory management
- **MoE docs** → routing + grouped GEMM + all-to-all communication
- **Nsight profiling** → empirical performance measurement (stop guessing)

## Stage 3: Mini-Project Sequence

Hands-on implementation projects (in order):

1. Implement RMSNorm in Triton; compare to PyTorch
2. Implement fused SiLU × gate
3. Implement simple FP16 matmul; compare to cuBLAS/rocBLAS
4. Implement paged KV lookup for decode attention
5. Add FP8 KV cache with per-block scales
6. Implement toy top-k sampling on GPU
7. Implement tiny MoE dispatch + grouped GEMM
8. Integrate one custom op into [[vllm]] or [[sglang]] and profile end-to-end

## Relationship to [[inference-kernel-optimization]]

This learning path is the practical extension of the conceptual framework in [[inference-kernel-optimization]]. Knowing that kernels are what you actually run is the insight; knowing how to learn to build and optimize them is this path.

## Related Entities

- [[vllm]] — PagedAttention inference engine, Stage 1 reference and Stage 3 integration target
- [[sglang]] — RadixAttention inference engine, Stage 1 reference and Stage 3 integration target
- [[tinygrad]] — deep learning framework with auto-generated GPU kernels (Stage 2 context)
- [[unsloth]] — AI company with hand-tuned GPU kernels for fast inference (practical outcome context)

## Related Concepts

- [[inference-kernel-optimization]] — conceptual foundation: the model is the recipe, kernels are the actual work
- [[quantization]] — covered in Stage 3 (FP8 KV cache)
- [[mixture-of-experts]] — covered in Stage 1 (SGLang MoE) and Stage 3 (MoE dispatch mini-project)
