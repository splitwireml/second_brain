---
title: LLM
created: 2026-04-16
updated: 2026-04-16
type: concept
tags: [llm, deep-learning]
sources: []
---

## Overview

LLM (Large Language Model) refers to a neural network trained on large-scale text data with billions of parameters, capable of understanding and generating natural language, code, and other modalities. GPT-4, Claude 3/4, Gemini, Llama, and Mistral are examples.

## Core Properties

- **Autoregressive generation** — predicts next token given previous context
- **In-context learning** — generalizes to new tasks from few-shot examples without weight updates
- **Emergent capabilities** — reasoning, code generation, tool use appear at scale
- **Scaling laws** — performance improves predictably with model size, data, and compute

## Key Techniques

- **Architecture** — transformer decoder-only; attention mechanisms; RoPE positional encoding
- **Training** — pre-training on web-scale text; fine-tuning with SFT, RLHF, DPO
- **Serving** — quantization ([[quantization]]), batching, KV cache optimization, speculative decoding
- **Long context** — attention approximations (FlashAttention), NTK-aware scaling, position interpolation

## Related Concepts

- [[quantization]] — essential for efficient LLM serving
- [[peft]] — parameter-efficient fine-tuning for task adaptation
- [[training]] — pre-training and fine-tuning mechanics
- [[efficiency]] — inference optimization techniques
