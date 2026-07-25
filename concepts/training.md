---
title: Training
created: 2026-04-16
updated: 2026-07-25
type: concept
tags: [llm, training, deep-learning]
sources: [raw/articles/thread-leerob-2080467752897146898.md]
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

### Human analogy for model learning
Lee Robinson frames training as a human learning loop: pretraining builds broad pattern knowledge, supervised fine-tuning (SFT) supplies examples of desired behavior, and reinforcement learning (RL) uses feedback from simulated work to improve decisions. The analogy is explanatory, not a claim that models learn exactly like people. ^[raw/articles/thread-leerob-2080467752897146898.md]

### Training feedback and evaluation
Training progress needs both practice-style checks and held-out final exams. Objective checks can score verifiable outcomes, while open-ended outputs may use a rubric or LLM-as-judge; held-out tasks are necessary to distinguish generalization from memorization. ^[raw/articles/thread-leerob-2080467752897146898.md]

### Distributed Training
- **Data Parallel (DP/DDP)** — same model across GPUs, different data batches
- **Tensor Parallel (TP)** — model layers split across GPUs within a node
- **Pipeline Parallel (PP)** — model layers split across GPUs across nodes
- **FSDP (Fully Sharded Data Parallel)** — shards model weights, optimizer, gradients across GPUs

## Relationship to Other Concepts

- [[peft]] — parameter-efficient training; the practical alternative to full fine-tuning
- [[quantization]] — often applied after or during training to reduce serving cost
- [[efficiency]] — training efficiency (FLOPs utilization) is a core research area
- [[generation-evaluation-gap]] — why external evaluation matters when model self-evaluation is insufficient
- [[leerob]] — source author of the human-learning analogy
