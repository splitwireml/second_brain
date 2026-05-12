---
title: Parameter-Efficient Fine-Tuning (PEFT)
created: 2026-04-16
updated: 2026-04-16
type: concept
tags: [training, llm, efficiency]
sources: []
---

## Overview

PEFT (Parameter-Efficient Fine-Tuning) refers to techniques that adapt a pre-trained language model to a downstream task by updating only a small subset of parameters, rather than full fine-tuning. This dramatically reduces compute, memory, and storage costs while maintaining competitive performance.

## Core Methods

- **LoRA (Low-Rank Adaptation)** — inject trainable rank-decomposition matrices into each attention layer; only the decomposition matrices are updated
- **QLoRA** — Quantized LoRA; quantizes the frozen base model to 4-bit NF4 to reduce memory further
- **AdaLoRA** — adaptive rank allocation for LoRA based on importance
- **LoRA-FA** — LoRA with frozen base model + frozen adapter; reduces active parameters
- **Prefix tuning** — trainable continuous prefixes prepended to attention heads
- **Prompt tuning** — trainable soft prompts at the input layer

## Why PEFT Instead of Full Fine-Tuning?

| | Full Fine-Tune | LoRA / PEFT |
|--|--|--|
| Parameters updated | 100% | 0.1–5% |
| GPU memory | Very high | Low |
| Storage per task | Full model copy | Adapter only |
| Catastrophic forgetting | Common | Minimal |

## Relationship to Training-Free

[[training-free]] methods (like zero-shot inference with CLIP or SAM) require no fine-tuning at all. PEFT is the middle ground: you do update weights, but efficiently. When zero-shot or few-shot prompting isn't enough (task is too far from pre-training), PEFT is the right tool.

## Related Concepts

- [[training-free]] — the opposite end: no weight updates at all
- [[quantization]] — often combined with PEFT (QLoRA); reducing precision to save memory
- [[llm]] — PEFT is primarily applied to LLMs
