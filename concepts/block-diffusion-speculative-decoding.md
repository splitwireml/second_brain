---
title: Block Diffusion Speculative Decoding
created: 2026-04-16
updated: 2026-04-16
type: concept
tags: [inference, optimization, llm]
sources: [raw/articles/z-lab-dflash-2026-04-16.md]
related_entity: [[dflash]]
---

# Block Diffusion Speculative Decoding

A speculative decoding technique that uses a block diffusion model to draft an entire sequence of tokens in a **single parallel forward pass**, rather than autoregressively (token by token).

## The Problem with Prior Approaches

Standard LLM inference is sequential — each token depends on all previous tokens. Speculative decoding缓解 this by having a small "draft" model propose tokens, which the target model then verifies in parallel. Accepted tokens are retained; rejected tokens trigger a rollback.

Existing draft methods — including EAGLE-3 — draft **autoregressively**, meaning each proposed token depends on the previous one. This limits practical speedups to ~2-3× because the draft stage itself becomes sequential.

## How Block Diffusion Changes It

A **block diffusion draft model** generates a full block of tokens (e.g., 16 tokens) in a single forward pass — no sequential dependency within the block. The target model then verifies the entire block in parallel.

The key innovation: removing the sequential draft bottleneck means the speedup is determined by the acceptance rate of the block, not the draft speed.

Results from [[dflash]]:
- Up to **6× lossless acceleration** on Qwen3-8B
- ~2.5× faster than EAGLE-3 (which drafts autoregressively)

## Relationship to Other Concepts

- [[llm-server-throughput-optimization]] — block diffusion is one technique in the broader inference optimization toolkit
- [[turboquant-kv-cache-compression]] — complementary optimization: TurboQuant compresses the KV cache (memory/speed), block diffusion accelerates drafting (compute/speed)
- [[three-tier-local-model-routing]] — routing decisions could leverage faster speculative decoding to shift more inference to local models

## Implementation Notes

- Requires a trained block diffusion draft model paired with a target model
- [[dflash]] provides pretrained draft models for Qwen3.5, Qwen3-Coder, Llama-3.1, GPT-OSS, and Kimi-K2.5
- Serving backends: [[sglang]] (recommended), [[vllm]] (nightly), Transformers (Qwen3/LLaMA only), MLX (Apple Silicon)
- vLLM integration requires nightly build with `--extra-index-url https://wheels.vllm.ai/nightly`

### Related Concepts

- [[pflash-speculative-prefill]] — speculative prefill that reduces TTFT by 10× using a small draft model to select only important tokens before the target model prefills; complements block diffusion speculative decoding for the decode phase
- [[inference-kernel-optimization]] — hand-written CUDA kernels for maximum inference efficiency; related to PFlash's CUDA kernel approach
