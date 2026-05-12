---
title: Gemma 4 MTP Drafters
created: 2026-05-06
updated: 2026-05-06
type: concept
tags: [inference, google, llm, optimization]
sources: [raw/articles/google-multi-token-prediction-gemma-4.md]
related_entity: [[gemma-4]]
---

# Gemma 4 MTP Drafters

Multi-Token Prediction (MTP) drafters are lightweight speculative decoding companions for the [[gemma-4]] model family, delivering up to **3× speedup** with no degradation in output quality or reasoning logic.

## Overview

Standard LLM inference is memory-bandwidth bound — the processor spends most of its time moving billions of parameters from VRAM to compute units just to generate a single token. This under-utilizes compute and creates high latency, especially on consumer hardware.

MTP drafters solve this by pairing each Gemma 4 model with a specialized lightweight drafter model. The drafter runs ahead, predicting several future tokens in the time the target model would take to process one. The target model then verifies all drafted tokens in a single parallel pass.

## Key Architectural Details

1. **KV cache sharing**: Draft models share the target model's KV cache — they don't recalculate context the larger model has already computed
2. **Efficient embedder clustering**: For E2B and E4B edge models (where final logit calculation is a bottleneck), an efficient clustering technique in the embedder further accelerates generation
3. **No quality degradation**: The primary [[gemma-4]] model retains final verification, ensuring identical frontier-class reasoning and accuracy

## Hardware-Specific Behavior

| Hardware | Observation |
|----------|-------------|
| Apple Silicon (26B MoE) | Batch size 1 has routing challenges; batch sizes 4–8 unlock ~2.2× speedup |
| Nvidia A100 | Similar gains with increased batch size |

## Relationship to Other Techniques

- **[[speculative-decoding]]**: MTP drafters are a specific implementation of speculative decoding (drafter + target verification)
- **[[block-diffusion-speculative-decoding]]** (DFlash): Both are speculative decoding techniques. DFlash drafts an entire block in a single parallel pass. MTP drafts autoregressively (multiple forward passes, but each is faster than one target model pass). DFlash can reach 6× speedup; MTP reaches 3×.
- **[[pflash-speculative-prefill]]**: Speculative prefill reduces TTFT (time to first token); MTP drafters accelerate token generation after the first token
- **[[turboquant-kv-cache-compression]]**: Complements MTP — compression reduces memory bandwidth pressure; MTP reduces the number of decode steps needed

## References

- Paper: [*Fast Inference from Transformers via Speculative Decoding*](https://arxiv.org/abs/2211.17192) (Google researchers, 2022)
- Technical explainer: [In-depth architecture breakdown](https://x.com/googlegemma/status/2051694045869879749) (X/Google Gemma)
- Documentation: [ai.google.dev/gemma/docs/mtp/overview](https://ai.google.dev/gemma/docs/mtp/overview)
