---
title: Speculative Decoding
created: 2026-05-06
updated: 2026-05-06
type: concept
tags: [inference, llm, optimization]
sources: [raw/articles/google-multi-token-prediction-gemma-4.md]
---

# Speculative Decoding

A family of inference optimization techniques that decouple token generation from verification, using a lightweight **drafter** model to propose tokens that a larger **target** model then verifies in parallel.

## Core Principle

Standard LLMs generate text autoregressively — one token at a time, each depending on all previous tokens. This is inefficient because the same computation is applied to predicting obvious continuations (e.g., "Actions speak louder than… → words") as to complex logical reasoning.

Speculative decoding pairs:
- A **heavy target model** (the quality guarantee)
- A **lightweight drafter** (the speed source)

The drafter runs ahead and proposes a sequence of tokens faster than the target model could generate them. The target model then verifies the entire draft in a single parallel forward pass. If the draft is accepted, the application outputs the full drafted sequence in the time it would normally take to generate a single token.

## Variants

### MTP (Multi-Token Prediction)
Lightweight autoregressive drafter. Draft tokens sequentially (each depends on the previous), but the drafter is fast enough that the total time per token is still much less than the target model alone. Used in [[gemma-4-mtp-drafters]] (up to 3× speedup).

### EAGLE (Early Exit Guide for Efficient LLM Inference)
Autoregressive drafter like MTP. Used in [[pflash-speculative-prefill]] as the speculative prefill component.

### Block Diffusion
Draft an entire block of tokens in a **single parallel pass** (no sequential dependency within the block). Used in [[block-diffusion-speculative-decoding]] (DFlash) — up to 6× speedup on Qwen3-8B, ~2.5× faster than EAGLE-3.

## Relationships to Other Concepts

- [[gemma-4-mtp-drafters]] — concrete MTP implementation by Google for Gemma 4
- [[block-diffusion-speculative-decoding]] — block diffusion variant of speculative decoding
- [[pflash-speculative-prefill]] — speculative prefill for TTFT reduction (complements decode-phase speculative decoding)
- [[turboquant-kv-cache-compression]] — complementary optimization: reduces memory bandwidth pressure via KV cache quantization
- [[inference-kernel-optimization]] — hand-written GPU kernels for maximum inference efficiency
- [[llm-server-throughput-optimization]] — broader inference serving stack

## References

- [*Fast Inference from Transformers via Speculative Decoding*](https://arxiv.org/abs/2211.17192) (Google researchers, 2022)
