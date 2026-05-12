---
title: LFM2.5-VL-450M
created: 2026-04-16
updated: 2026-04-16
type: entity
tags: [model, llm, vision-language, oss-ai]
sources: [raw/articles/liquid-ai-lfm2-5-vl-450m-model-card-2026-04-16.md]
related_entity: [[liquid-ai]]
---

# LFM2.5-VL-450M

**LFM2.5-VL-450M** is Liquid AI's vision-language model with ~450M total parameters (350M LLM backbone + 86M vision encoder). It processes images and text for captioning, visual QA, object detection, and function calling.

## Overview

Built on [[lfm2-5-350m]] as the LLM backbone and SigLIP2 NaFlex as the vision encoder, LFM2.5-VL-450M is the refreshed version of LFM2-VL-450M with improved instruction following, multilingual vision understanding (8 languages), and new capabilities.

## Architecture

- **LLM backbone**: [[lfm2-5-350m]] — 350M params, 16 layers (10 LIV conv + 6 GQA), 1024 hidden, 16 heads / 8 KV, 6656 intermediate, RoPE (1M theta)
- **Vision encoder**: SigLIP2 NaFlex — 86M params, 12 layers, 768 hidden, 256 patches of 16×16
- **Projection**: GELU projector, 2048 hidden size
- **Context**: 32,768 tokens; vocab 65,536
- **Image processing**: native 512×512 max, tiling up to 10 tiles, thumbnail encoding for global context

## Key Capabilities

1. **Enhanced instruction following** on vision and language tasks
2. **Multilingual vision understanding** — Arabic, Chinese, French, German, Japanese, Korean, Portuguese, Spanish
3. **Bounding box prediction** — grounded visual understanding on RefCOCO-M (81.28%)
4. **Function calling** — text-only input via chat template tools interface
5. **User-tunable image tokens** — 32–256 tokens at inference without retraining

## Benchmarks

See [[vision-language-models]] for a broader comparison across VLMs.

### Vision Benchmarks

| Benchmark | LFM2.5-VL-450M | LFM2-VL-450M | SmolVLM2-500M |
|---|---|---|---|
| MMStar | 43.00 | 40.87 | 38.20 |
| RealWorldQA | 58.43 | 52.03 | 49.90 |
| MMBench | 60.91 | 56.27 | 52.32 |
| POPE | 86.93 | 83.79 | 82.67 |
| MMVet | 41.10 | 33.85 | 29.90 |
| MM-IFEval | 45.00 | 33.09 | 11.27 |
| RefCOCO-M (bbox) | 81.28 | — | — |

### Language Benchmarks

| Benchmark | LFM2.5-VL-450M | LFM2-VL-450M |
|---|---|---|
| GPQA | 25.66 | 23.13 |
| MMLU Pro | 19.32 | 17.22 |
| IFEval | 61.16 | 51.75 |
| BFCLv4 | 21.08 | — |

## Deployment

Supported by: [[vllm]], [[sglang]], Transformers (v5.1+), llama.cpp (GGUF), ONNX, MLX (Apple Silicon).

## See Also
- [[liquid-ai]]
- [[lfm2-5-350m]]
- [[vision-language-models]]
- [[vllm]]
- [[sglang]]
