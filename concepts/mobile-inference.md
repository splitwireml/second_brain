---
title: Mobile Inference
created: 2026-04-29
updated: 2026-04-29
type: concept
tags: [inference, efficiency, model, chinese-ai]
sources: [raw/articles/hy-mt1.5-1.8b-1.25bit-tencent-2026-04-29.md]
related_entity: [[hy-mt1.5-1.8b-1.25bit]]
---

# Mobile Inference

Running language models directly on mobile devices with no network dependency, enabled by extreme quantization and efficient kernels.

## Definition

Mobile inference refers to on-device LLM execution — no server calls, no latency, fully offline. The challenge is fitting large models into constrained mobile memory while maintaining acceptable quality and speed. [[hy-mt1.5-1.8b-1.25bit]] demonstrates this at 440MB, targeting Android phones.

## Key Constraints

| Constraint | Typical Limit | Solution |
|---|---|---|
| Memory | 2–6 GB RAM | Extreme quantization (1.25-bit) |
| Storage | 1–4 GB | Small model variants, quantized weights |
| Power | Thermal throttling | Efficient kernels, batch size limits |
| Speed | >5 tok/s for interactivity | Quantization + optimized arithmetic |

## Enabling Techniques

- **Quantization**: 1.25-bit reduces 3.3GB → 440MB ([[hy-mt1.5-1.8b-1.25bit]])
- **Small models**: 1.8B params is small enough for mobile
- **Efficient kernels**: specialized inference kernels for low-bit arithmetic
- **On-device storage**: APK distribution (Android) without server round-trips

## Relationship to Other Concepts

- [[quantization]] — the core technique enabling mobile deployment
- [[inference]] — the execution paradigm; mobile inference is a subset
- [[local-llm]] — broader on-device LLM context (includes Mac/PC, not just phones)
- [[void-model-mlx]] — Apple Silicon equivalent for on-device inference

## Real-World Example

[[hy-mt1.5-1.8b-1.25bit]] by [[tencent]]: 440MB APK, 33 languages, runs on Android without internet. This is the reference implementation for mobile inference in the wiki.

## Related Entities

- [[hy-mt1.5-1.8b-1.25bit]] — mobile translation model
- [[tencent]] — developer of mobile inference models
- [[void-model-mlx]] — Apple Silicon on-device inference counterpart