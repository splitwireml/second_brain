---
title: Training-Free
created: 2026-04-16
updated: 2026-04-16
type: concept
tags: [training-free, deep-learning, efficiency]
sources: []
---

## Overview

Training-free methods are AI/ML techniques that achieve strong performance without any fine-tuning or task-specific gradient updates. They rely on pre-trained models, zero-shot capabilities, prompting strategies, or architectural inductive biases rather than updating weights.

## Examples

- **Zero-shot classification** — CLIP, GPT-4V: classify inputs into arbitrary label sets without fine-tuning
- **Zero-shot segmentation** — SAM (Segment Anything Model): segment any class without training on it ([[segmentation]])
- **Prompt-based navigation** — language-conditioned policies in robotics that generalize without RL fine-tuning
- **In-context learning** — LLMs solve new tasks from few-shot examples without weight changes
- **Training-free architecture search** — e.g., BigNAS, once-for-all networks that elude separate training per deployment setting

## Relationship to Fine-Tuning

Training-free is the opposite end of the spectrum from full fine-tuning and LoRA. When training-free works, it saves:
- GPU hours
- Annotation cost
- Overfitting risk on small datasets

When it doesn't work (task is too far from pre-training distribution), then PEFT methods like [[peft]] LoRA / QLoRA become relevant.

## Related Concepts

- [[segmentation]] — SAM is the canonical training-free segmentation model
- [[sam3-ai-box]] — a training-free workflow built on SAM
- [[zero-shot]] — the broader capability of generalizing without training
- [[efficiency]] — training-free methods often have efficiency benefits
