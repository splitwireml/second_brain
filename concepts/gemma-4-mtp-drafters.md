---
title: Gemma 4 MTP Drafters
created: 2026-05-06
updated: 2026-06-11
type: concept
tags: [llm, inference, google, optimization]
sources: [raw/articles/google-multi-token-prediction-gemma-4.md, raw/articles/thread-analogalok-2064282424532672841.md]
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

## Consumer GPU field note

A June 2026 thread by [[analogalok]] adds a practical deployment datapoint: Gemma 4 12B QAT plus a separate MTP assistant GGUF can sustain roughly 20+ tok/sec decode and 700+ tok/sec prefill on an RTX 4060 8 GB card when paired with llama.cpp flags tuned for speculative drafting. The notable implementation detail is architectural rather than benchmark-only: unlike Qwen variants that bake MTP heads into one GGUF, Gemma 4 uses a separate drafter model, which keeps the VRAM overhead low while still yielding a reported 25-40% decode uplift.

## Example llama.cpp flags

```bash
-m gemma-4-12B-it-qat-UD-Q4_K_XL.gguf \
--spec-type draft-mtp \
--spec-draft-n-max 4 \
--spec-draft-p-min 0.7 \
--spec-draft-model gemma-4-12B-it-qat-assistant-MTP-Q8_0.gguf \
-c 48000 -ngl 38 -v
```

Related: [[speculative-decoding]], [[gemma-4]], [[analogalok]].
