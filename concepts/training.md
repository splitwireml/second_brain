---
title: Training
created: 2026-04-16
updated: 2026-04-16
type: concept
tags: [training, deep-learning, llm]
sources: []
---

## Overview

Training refers to the process of updating neural network weights to minimize a loss function on a dataset. In the context of LLMs and vision models, it encompasses pre-training (learning language/vision representations from large-scale data), fine-tuning (adapting to a specific task), and the various parameter-efficient variants.

## Key Concepts

### Pre-training
- **Language model pre-training** — next-token prediction on large text corpora
- **Vision-language pre-training** — aligned image-text pairs (CLIP, ALIGN)
- **Self-supervised** — masked autoencoding (BERT, MAE) or contrastive learning

### Fine-tuning
- **Full fine-tuning** — update all parameters; expensive for large models
- **PEFT ([[peft]])** — update only adapter/prefix parameters (LoRA, QLoRA, prefix tuning)
- **RLHF / DPO** — reinforcement learning from human feedback or direct preference optimization

### Distributed Training
- **Data Parallel (DP/DDP)** — same model across GPUs, different data batches
- **Tensor Parallel (TP)** — model layers split across GPUs within a node
- **Pipeline Parallel (PP)** — model layers split across GPUs across nodes
- **FSDP (Fully Sharded Data Parallel)** — shards model weights, optimizer, gradients across GPUs

## Relationship to Other Concepts

- [[peft]] — parameter-efficient training; the practical alternative to full fine-tuning
- [[quantization]] — often applied after or during training to reduce serving cost
- [[efficiency]] — training efficiency (FLOPs utilization) is a core research area
