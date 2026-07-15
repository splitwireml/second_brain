---
title: mlx
created: 2026-04-28
updated: 2026-06-14
type: concept
tags: [inference, apple-silicon, framework, local-llm, ml]
sources: []
related_entity: [[apple-silicon]]
---
# MLX

Apple's ML framework for Apple Silicon (M1/M2/M3/M4 chips). Enables efficient running of LLMs and ML models on local Macs with Metal GPU acceleration.

## Key Capabilities

- **Metal GPU acceleration**: Unified memory architecture allows running large models without multi-GPU setup
- **Efficient LLM inference**: Supports GGUF quantized models via llama.cpp backend
- **Local embedding pipelines**: [[apple-silicon-embedding-pipeline]] uses MLX for embedding generation

## Related Concepts

- [[local-llm]] — MLX as a key infrastructure choice for local LLM inference
- [[apple-silicon-inference]] — Apple Silicon inference more broadly
- [[quantization]] — GGUF/QAT quantization enables large models on Apple Silicon
- [[llm]] — LLM inference fundamentals

## Related
- [[apple-silicon]] — related entity from frontmatter; explicit cross-link
