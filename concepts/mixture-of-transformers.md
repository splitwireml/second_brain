---
title: Mixture-of-Transformers (MoT)
created: 2026-04-14
updated: 2026-04-14
type: concept
tags: [architecture, moe, vision-language, efficiency, llm]
sources: [raw/articles/tencent-hy-embodied-0-5-model-card-2026-04-14.md]
---

# Mixture-of-Transformers (MoT)

**Mixture-of-Transformers (MoT)** is a sparse architecture variant used in [[hy-embodied-0-5]] that applies mixture-of-experts principles specifically to the vision/encoding pathway, enabling high-resolution visual processing without proportional compute cost.

## How It Works

Unlike traditional MoE applied to FFN layers, MoT in HY-Embodied uses latent tokens for **modality-specific computing** — separating vision tokens into different processing routes based on content type (spatial, temporal, semantic).

Key advantage: A model with **4B total parameters** can activate only **2.2B parameters per forward pass** while maintaining dense-model-quality visual representations.

## Comparison to Standard MoE

| Aspect | Standard MoE (FFN-based) | MoT (Vision Pathway) |
|--------|------------------------|---------------------|
| Sparsity location | FFN layers | Vision encoder pathway |
| Experts | Typically 8-256 FFN experts | Latent token routing |
| Active params | K/N of total | Subset via routing |
| Use case | Language models | Vision-language models |

## Implemented In

- [[hy-embodied-0-5]] — Uses MoT with latent token routing for fine-grained visual perception

## See Also

- [[hy-embodied-0-5]]
- [[mixture-of-experts]]
- [[vision-language-models]]
