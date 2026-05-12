---
updated: 2026-04-17
title: Tencent HY-Embodied-0.5 Model Card
source: https://huggingface.co/tencent/HY-Embodied-0.5
type: arxiv
---

# Tencent HY-Embodied-0.5 Model Card

> Source: https://huggingface.co/tencent/HY-Embodied-0.5
> Retrieved: 2026-04-14

## Raw README Content

We introduce **HY-Embodied-0.5**, a suite of foundation models tailored specifically for real-world embodied intelligence. To bridge the gap between general Vision-Language Models (VLMs) and the strict demands of physical agents, our models are engineered to excel in spatial-temporal visual perception and complex embodied reasoning (prediction, interaction, and planning).

The suite features an innovative **Mixture-of-Transformers (MoT)** architecture utilizing latent tokens for modality-specific computing, significantly enhancing fine-grained perception. It includes two primary variants: a highly efficient **2B model** for edge deployment and a powerful **32B model** for complex reasoning. Through a self-evolving post-training paradigm and large-to-small on-policy distillation, our compact MoT-2B outperforms state-of-the-art models of similar size across 16 benchmarks, while the 32B variant achieves frontier-level performance comparable to Gemini 3.0 Pro. Ultimately, HY-Embodied serves as a robust "brain" for Vision-Language-Action (VLA) pipelines, delivering compelling results in real-world physical robot control.

### Key Features

- **Evolved MoT Architecture:** The MoT-2B variant contains 4B total parameters but requires **only 2.2B activated parameters** during inference.
- **High-Quality Mixed Chain Reasoning:** On-policy distillation from 32B to 2B variant.
- **Large-Scale Embodied Pre-training:** >100 million embodied and spatial-specific data points, >200 billion tokens.
- **Stronger VLA Application:** Core cognitive engine for physical robots.

### Architecture Details (from config.json)

- Model type: hunyuan_vl_mot
- Architecture: HunYuanVLMoTForConditionalGeneration
- Hidden size: 2048
- Layers: 32
- Attention heads: 16
- KV heads: 4
- Head dim: 128
- Intermediate size: 6144
- Vocab size: 120818
- Max position: 262144
- dtype: bfloat16
- Dense list: [2048, 0]
- use_qk_norm: true
- ROPE scaling: dynamic with alpha=1000

### Hardware Requirements

- GPU: NVIDIA with at least 16GB VRAM recommended
- CPU: Supported but slower
- Memory: At least 16GB RAM
- Storage: 20GB+ free space

### Links

- Paper: https://arxiv.org/abs/2604.07430
- GitHub: https://github.com/Tencent-Hunyuan/HY-Embodied
- Tech Report: https://github.com/Tencent-Hunyuan/HY-Embodied/blob/master/hy_embodied_tech_report.pdf