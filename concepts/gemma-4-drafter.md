---
title: Gemma 4 - Drafter Explained
created: 2026-05-07
updated: 2026-05-07
type: concept
tags: [inference, google, llm, optimization, model]
sources: [raw/articles/google-gemma-4-drafter-explained-2051694045869879749.md]
related_entity: [[google-gemma-4-drafter]]
---

# Gemma 4 - Drafter Explained

Detailed technical explainer of the Gemma 4 MTP (Multi-Token Prediction) drafters, published by [[google-gemma]] on X.

## Key Concepts

### Speculative Decoding

Standard LLM inference generates one token at a time autoregressively. Speculative decoding uses a smaller "drafter" model to predict several tokens in advance, then the larger "target" model verifies them all in parallel in a single forward pass.

### Multi-Token Prediction (MTP) Head

The drafter runs autoregressively using the target model's intermediate hidden states. A single forward pass of the target model produces one NTP token plus multiple drafter tokens — resulting in multiple tokens instead of one.

### Target Activations

To improve draft quality, the final activations of the target model are fed to the draft model. These are concatenated with the token embedding and projected down to the drafter's dimension (e.g., 1,536 → 256 for E2B). In subsequent rounds, the draft model uses its own intermediate activations.

### KV Cache Sharing

Rather than building its own KV cache, the draft model cross-attends to the target model's already-computed KV cache. For global attention, the draft reuses the target's global KV cache directly.

### Efficient Embedder

For E2B and E4B edge models, a clustering technique identifies likely token clusters in the vocabulary. The LM Head computes cluster logits first, selects the most likely clusters, then computes token logits only within those clusters — reducing computation significantly.

## Draft Model Specs

The drafter for Gemma 4 E2B has approximately:
- **76M parameters**
- **4 layers**
- **256 input embedding size** (vs 1,536 for the target E2B model)

## Relationships

- Implementation of [[speculative-decoding]]
- Related to [[gemma-4-mtp-drafters]] (broader concept)
- Part of [[gemma-4]] model family
- Related technique: [[block-diffusion-speculative-decoding]] (DFlash — parallel block drafts vs autoregressive MTP)
- Complementary to [[turboquant-kv-cache-compression]] (compression vs fewer decode steps)

## References

- X Article: [x.com/googlegemma/status/2051694045869879749](https://x.com/googlegemma/status/2051694045869879749)
- Google Blog: [Multi-Token Prediction for Gemma 4](https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/)
