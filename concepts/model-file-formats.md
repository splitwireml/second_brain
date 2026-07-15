---
title: Model File Formats
created: 2026-05-19
updated: 2026-05-19
type: concept
tags: [llm, ai, local-llm, open-source]
sources: [raw/articles/xarticle-04-what-a-model-actually-includes-2055347680147312810.md]
---

## Overview

Model file formats define how model weights, metadata, and associated data are packaged and stored on disk. The same underlying model can be distributed in different formats.

## Common Formats

### Safetensors
- Common in Hugging Face ecosystem
- Stores tensors safely and efficiently
- Used for training, fine-tuning, framework-based inference
- Typically paired with separate config and tokenizer files

### GGUF (GPT General Unified Format)
- Common for llama.cpp-style local inference
- Optimized for local runtimes
- Often includes quantization (Q4_K_M, Q5_K_M, etc.)
- Usually packages weights, metadata, tokenizer into one file

### Runtime-specific packaging
- Ollama model packages
- Other local inference system formats
- May bundle everything needed for specific applications

## Format vs Quality

A common beginner mistake: treating GGUF and safetensors as quality indicators. They are packaging formats — they tell you how the model is stored, not how smart it is. Quality depends on the underlying model, quantization level, runtime, prompt formatting, and settings.

## Matching Format to Runtime

- Python frameworks → typically load safetensors
- llama.cpp → usually wants GGUF
- Desktop apps → hide format details but depend on one underneath

The format must be supported by your runtime. Using the wrong format means the model cannot be loaded.

## Related Concepts

- [[local-llm]] — Format choice matters for local deployment
- [[model-architecture]] — Architecture determines format compatibility
- [[chat-template]] — Template may be embedded in model files

## Sources

^[raw/articles/xarticle-04-what-a-model-actually-includes-2055347680147312810.md]