---
updated: 2026-04-15
type: raw
title: Liquid AI LFM2.5-VL-450M Model Card
created: 2026-04-16
source: https://huggingface.co/LiquidAI/LFM2.5-VL-450M
---

# LFM2.5-VL-450M

Source: https://huggingface.co/LiquidAI/LFM2.5-VL-450M

## Overview

LFM2.5-VL-450M is Liquid AI's refreshed vision-language model, built on an updated backbone LFM2.5-350M and tuned for stronger real-world performance. It is a general-purpose VLM with enhanced instruction following, improved multilingual vision understanding, bounding box prediction, and function calling support.

## Key Specs

- **LM Backbone**: LFM2.5-350M (350M params, 16 layers: 10 LIV conv + 6 GQA, 1024 hidden, 6656 intermediate, 16 heads / 8 KV)
- **Vision encoder**: SigLIP2 NaFlex shape-optimized, 86M params, 12 layers, 768 hidden, 256 patches of 16×16
- **Context length**: 32,768 tokens
- **Vocabulary size**: 65,536
- **Languages**: English, Arabic, Chinese, French, German, Japanese, Korean, Portuguese, Spanish
- **Native resolution**: 512×512 max without upscaling; preserves non-standard aspect ratios
- **Tiling**: non-overlapping 512×512 patches + thumbnail encoding for global context
- **Image tokens**: min 32, max 256 (user-tunable at inference)
- **Max tiles**: 10
- **Generation params**: temperature=0.1, min_p=0.15, repetition_penalty=1.05
- **License**: LFM1.0 (proprietary)

## Benchmarks

### Vision

| Benchmark | LFM2.5-VL-450M | LFM2-VL-450M | SmolVLM2-500M |
|---|---|---|---|
| MMStar | 43.00 | 40.87 | 38.20 |
| RealWorldQA | 58.43 | 52.03 | 49.90 |
| MMBench (dev en) | 60.91 | 56.27 | 52.32 |
| MMMU (val) | 32.67 | 34.44 | 34.10 |
| POPE | 86.93 | 83.79 | 82.67 |
| MMVet | 41.10 | 33.85 | 29.90 |
| BLINK | 43.92 | 42.61 | 40.70 |
| InfoVQA (val) | 43.02 | 44.56 | 24.64 |
| OCRBench | 684 | 657 | 609 |
| MM-IFEval | 45.00 | 33.09 | 11.27 |
| MMMB | 68.09 | 54.29 | 46.79 |
| CountBench | 73.31 | 47.64 | 61.81 |
| RefCOCO-M | 81.28 | - | - |

### Language

| Benchmark | LFM2.5-VL-450M | LFM2-VL-450M | SmolVLM2-500M |
|---|---|---|---|
| GPQA | 25.66 | 23.13 | 23.84 |
| MMLU Pro | 19.32 | 17.22 | 13.57 |
| IFEval | 61.16 | 51.75 | 30.14 |
| Multi-IF | 34.63 | 26.21 | 6.82 |
| BFCLv4 | 21.08 | - | - |

## Format Variants

- **Native** (Transformers, vLLM, SGLang)
- **GGUF** (llama.cpp)
- **ONNX** (cross-platform)
- **MLX** (Apple Silicon: 4bit, 5bit, 6bit, 8bit, bf16)

## Inference Frameworks

- Transformers (v5.1+)
- vLLM (GPU)
- SGLang (GPU)
- llama.cpp (CPU)

## Fine-Tuning

- Unsloth SFT (LoRA)
- TRL SFT (LoRA)