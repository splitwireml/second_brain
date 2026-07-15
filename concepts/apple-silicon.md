---
title: Apple Silicon
created: 2026-05-31
updated: 2026-06-14
type: concept
tags: [inference, apple-silicon, gpu, hardware, local-llm, mlx]
sources: []
related_entity: [[apple]]
---

# Apple Silicon

Apple's ARM-based SoC family (M1/M2/M3/M4 series) designed for ML workloads. Key for local LLM inference due to unified memory architecture.

## Key Advantages for Local LLM Inference

- **Unified memory**: CPU and GPU share memory — no PCIe bandwidth bottleneck for large model weights
- **Metal GPU**: High compute throughput for matrix operations
- **ANe (Neural Engine)**: Dedicated ML accelerator for specific inference tasks
- **Power efficiency**: Can run inference quietly without thermal throttling

## Key Frameworks

- [[mlx]] — Apple's own ML framework for Metal GPU acceleration
- llama.cpp with Metal backend — GGUF model inference

## Related Concepts

- [[mlx]] — ML framework for Apple Silicon
- [[apple-silicon-inference]] — inference on Apple Silicon
- [[apple-silicon-embedding-pipeline]] — embeddings on Apple Silicon
- [[local-llm]] — running LLMs locally
- [[quantization]] — GGUF quantization for Apple Silicon

## Related
- [[apple]] — related entity from frontmatter; explicit cross-link
