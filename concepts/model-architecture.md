---
title: Model Architecture
created: 2026-05-19
updated: 2026-05-19
type: concept
tags: [llm, ai, architecture, local-llm]
sources: [raw/articles/xarticle-04-what-a-model-actually-includes-2055347680147312810.md]
---

## Overview

**Model architecture** defines the structural design of a neural network — the shape of the model before any learning occurs. It specifies how neurons and layers are arranged and connected, determining how data flows through the network during inference.

## Components

Key architecture parameters include:
- **Number of layers** — Depth of the model
- **Hidden size** — Dimensionality of intermediate representations
- **Attention heads** — Number of attention mechanisms in transformers
- **Vocabulary size** — Total tokens the model can recognize
- **Context length** — Maximum input sequence length supported
- **Positional encoding method** — How position information is injected

## Why Architecture Matters

Two models with identical parameter counts can have completely different architectures and behave differently. A runtime cannot load model weights correctly unless it understands the architecture those weights were trained in.

The weights are not independent floating numbers — they are structured parameters attached to a specific architectural template.

## Related Concepts

- [[local-llm]] — The domain where architecture becomes practical
- [[model-weights]] — Weights only make sense within an architecture
- [[tokenizer]] — Tokenizer must match the model's vocabulary size

## Sources

^[raw/articles/xarticle-04-what-a-model-actually-includes-2055347680147312810.md]