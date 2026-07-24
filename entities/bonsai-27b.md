---
title: Bonsai-27B
created: 2026-07-24
updated: 2026-07-24
type: entity
tags: [llm, model, quantization, inference, local-llm, hardware]
sources: [raw/articles/thread-0xSero-2080003696885154280.md]
---

# Bonsai-27B

“Bonsai-27B” is the local source’s label for a claimed ternary compression of [[qwen3-6-27b]], placed in the 8–24 GB hardware tier. The post claims a roughly 4 GB VRAM footprint, but replies dispute the practical fit: one says the q1_0 variant does not fit 4 GB, another reports needing 12 GB, and another prefers a higher-bit quant at 16–24 GB. Treat the fit and quality claims as source-reported and contested.

## Identity Boundary

The existing [[1-bit-bonsai-bitnet-fine-tuning]] page documents PrismML Bonsai models, including an 8B binary-compressed family. This page keeps the source’s “Bonsai-27B” label separate until the relationship between the two names is independently established.

## Related

- [[qwen3-6-27b]] — the model named as the compression base.
- [[1-bit-bonsai-bitnet-fine-tuning]] — existing Bonsai/BitNet compression context.
- [[local-llm-size-tradeoffs]] — constrained-hardware model selection.
- [[0xsero]] — source author.
