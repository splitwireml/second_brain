---
title: Quantization (1.25-bit)
created: 2026-04-29
updated: 2026-04-29
type: concept
tags: [quantization, inference, efficiency, model]
sources: [raw/articles/hy-mt1.5-1.8b-1.25bit-tencent-2026-04-29.md]
related_entity: [[hy-mt1.5-1.8b-1.25bit]]
---

# Quantization (1.25-bit)

Extreme low-bit quantization technique reducing model memory footprint to ~13% of full precision while maintaining accuracy.

## Definition

1.25-bit quantization is an extreme form of quantization where model weights are compressed to approximately 1.25 bits per parameter. This is near the theoretical minimum for representing numerical values (essentially 1-bit with a small amount of residual precision to preserve signal fidelity). For comparison, typical quantization levels:

- FP16: 16 bits per parameter (baseline)
- INT8: 8 bits per parameter (50% size)
- 1.67-bit: ~79% size reduction (prior art)
- 1.25-bit: ~92% size reduction from FP16 (3.3GB → 440MB in Hy-MT1.5-1.8B)

## Mechanism

The 1.25-bit approach used by [[hy-mt1.5-1.8b-1.25bit]] drops memory from 3.3GB (FP16) to 440MB — a 7.5× compression ratio. Tencent claims this achieves 25% smaller size and ~10% speed improvement over the prior 1.67-bit approach with no accuracy loss.

## Tradeoffs

- **Memory savings**: 7.5× reduction enables mobile deployment
- **Speed**: smaller weights → less memory bandwidth → faster inference
- **Accuracy risk**: extreme quantization typically degrades quality; claimed no loss here
- **Compatibility**: requires specialized inference kernels for 1.25-bit arithmetic

## Related Concepts

- [[inference]] — the execution context where quantization matters
- [[efficiency]] — parameter/computational efficiency goals
- [[mobile-inference]] — target deployment for [[hy-mt1.5-1.8b-1.25bit]]

## Related Entities

- [[hy-mt1.5-1.8b-1.25bit]] — the model using 1.25-bit quantization
- [[tencent]] — the company behind this quantization approach
- [[local-llm]] — broader context of on-device model deployment