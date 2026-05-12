---
title: HY-Embodied-0.5
created: 2026-04-14
updated: 2026-04-14
type: entity
tags: [model, llm, moe, vision-language, robotics, oss-ai]
sources: [raw/articles/tencent-hy-embodied-0-5-model-card-2026-04-14.md]
---

# HY-Embodied-0.5

**HY-Embodied-0.5** is a suite of embodied foundation models developed by [[tencent]] (Tencent Robotics X × HY Vision Team). It features a **Mixture-of-Transformers (MoT)** architecture and comes in two sizes: a 2B variant optimized for edge deployment and a 32B variant for complex reasoning.

## Architecture

The model uses an innovative **Mixture-of-Transformers (MoT)** architecture with latent tokens for modality-specific computing. Key config details:

| Parameter | Value |
|-----------|-------|
| Hidden size | 2048 |
| Layers | 32 |
| Attention heads | 16 |
| KV heads | 4 |
| Head dim | 128 |
| Intermediate size | 6144 |
| Vocab size | 120,818 |
| Max position | 262,144 |
| dtype | bfloat16 |

The **MoT-2B variant** contains **4B total parameters** but requires only **2.2B activated parameters** during inference — achieved through sparse mixture-of-experts routing in the vision pathway.

## Variants

- **MoT-2B**: 2 billion activated parameters, 4B total (sparse). Designed for edge deployment and real-time robotics.
- **MoT-32B**: 32 billion parameters. Achieves frontier-level performance comparable to Gemini 3.0 Pro.

## Training

- **Data**: >100 million embodied and spatial-specific data points
- **Tokens**: >200 billion tokens corpus
- **Method**: Self-evolving post-training with large-to-small on-policy distillation (32B → 2B)

## Capabilities

- Spatial-temporal visual perception
- Complex embodied reasoning (prediction, interaction, planning)
- Vision-Language-Action (VLA) pipeline integration
- Step-by-step chain reasoning

## Performance

- MoT-2B outperforms state-of-the-art models of similar size across **16 benchmarks**
- 32B variant achieves frontier-level performance comparable to **Gemini 3.0 Pro**

## Usage

```python
from transformers import AutoModelForImageTextToText, AutoProcessor
model = AutoModelForImageTextToText.from_pretrained("tencent/HY-Embodied-0.5", torch_dtype=torch.bfloat16)
```

Requires transformers version from specific commit (not yet merged to main):
```bash
pip install git+https://github.com/huggingface/transformers@9293856c419762ebf98fbe2bd9440f9ce7069f1a
```

## See Also

- [[tencent]]
- [[mixture-of-transformers]]
- [[embodied-ai]]
- [[vision-language-models]]
- [[vla-robotics]]
