---
title: Google Gemma 4 - Drafter Explained
created: 2026-05-07
updated: 2026-05-07
type: entity
tags: [google, llm, ml, inference, oss-ai, model]
sources: [raw/articles/google-gemma-4-drafter-explained-2051694045869879749.md]
---

# Google Gemma 4 - Drafter Explained

X Article by [[google-gemma]] (@googlegemma) providing a detailed technical explainer of how the Gemma 4 MTP (Multi-Token Prediction) drafters work.

## Summary

The article covers:
- **Speculative decoding**: Using a smaller drafter model to predict multiple tokens ahead, verified in parallel by the target model
- **Multi-Token Prediction (MTP) head**: The drafter component that generates draft tokens using the target model's hidden states
- **Target Activations**: Draft model uses final activations from the target model, concatenated with token embeddings and down-projected to drafter dimensions
- **KV Cache Sharing**: Draft model cross-attends to the target model's KV cache instead of building its own
- **Efficient Embedder**: For E2B/E4B models, sparse clustering technique in the LM Head identifies likely token clusters to reduce computation
- The draft model for Gemma 4 E2B has ~76M parameters, 4 layers, and 256 input embedding size

## Relationships

- Part of the [[gemma-4]] model family
- Related concept: [[gemma-4-mtp-drafters]]
- Related technique: [[speculative-decoding]]
- Source: [x.com/googlegemma/status/2051694045869879749](https://x.com/googlegemma/status/2051694045869879749)

## See Also

- [[gemma-4-mtp-drafters]] (concept)
- [[speculative-decoding]] (concept)
- [[block-diffusion-speculative-decoding]] (concept)
- [[gemma-4]] (entity)
- [[google]] (entity)
