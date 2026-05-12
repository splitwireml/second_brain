---
title: Hy-MT1.5-1.8B-1.25bit
created: 2026-04-29
updated: 2026-04-29
type: entity
tags: [model, quantization, inference, efficiency, chinese-ai]
sources: [raw/articles/hy-mt1.5-1.8b-1.25bit-tencent-2026-04-29.md]
---

# Hy-MT1.5-1.8B-1.25bit

Tencent's open-source mobile translation model. 1.8B parameters quantized to 1.25-bit (440MB), running fully offline on-phone.

## Overview

Hy-MT1.5-1.8B-1.25bit is a stripped-down variant of the Hy-MT1.5 translation model family, compressed to 440MB via 1.25-bit quantization. At 1.8B parameters, it claims to match commercial translation APIs and 235B-scale models on standard benchmarks. Memory footprint drops from 3.3GB (FP16) to 440MB — 25% smaller and ~10% faster than prior 1.67-bit approaches, with no accuracy loss reported.

## Capabilities

- 33 languages, 5 dialects, 1,056 translation directions
- Minority languages: Tibetan and Mongolian included
- 30 first-place rankings in international MT competitions
- Android APK available for offline use
- HuggingFace, GitHub, and paper links provided

## Technical Details

- Parameters: 1.8B
- Quantization: 1.25-bit (essentially 1-bit with some residual precision)
- Size: 440MB (vs 3.3GB FP16)
- Speed: ~10% faster than prior 1.67-bit approach
- Deployments: Tencent products (production)

## Related

- [[tencent]] — parent company
- [[quantization]] — the core technique enabling mobile deployment
- [[mobile-inference]] — the inference paradigm this model targets
- [[local-llm]] — broader context of on-device language models