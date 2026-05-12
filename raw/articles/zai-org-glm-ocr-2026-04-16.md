---
updated: 2026-04-17
title: GLM-OCR — Hugging Face Model Card
source: https://huggingface.co/zai-org/GLM-OCR
type: arxiv
---

# GLM-OCR — Hugging Face Model Card

**Source:** https://huggingface.co/zai-org/GLM-OCR
**Organization:** Z.ai (zai-org)
**License:** MIT
**Accessed:** 2026-04-16

---

## Introduction

GLM-OCR is a multimodal OCR model for complex document understanding, built on the GLM-V encoder–decoder architecture. It introduces Multi-Token Prediction (MTP) loss and stable full-task reinforcement learning to improve training efficiency, recognition accuracy, and generalization. The model integrates the CogViT visual encoder pre-trained on large-scale image–text data, a lightweight cross-modal connector with efficient token downsampling, and a GLM-0.5B language decoder. Combined with a two-stage pipeline of layout analysis and parallel recognition based on PP-DocLayout-V3, GLM-OCR delivers robust and high-quality OCR performance across diverse document layouts.

**Key Features:**
- **State-of-the-Art Performance**: Score of 94.62 on OmniDocBench V1.5, ranking #1 overall. SOTA across major document understanding benchmarks including formula recognition, table recognition, and information extraction.
- **Optimized for Real-World Scenarios**: Robust performance on complex tables, code-heavy documents, seals, and challenging real-world layouts.
- **Efficient Inference**: Only 0.9B parameters. Supports deployment via vLLM, SGLang, and Ollama.
- **Easy to Use**: Fully open-sourced with comprehensive SDK and inference toolchain.

## Architecture

- **Visual Encoder:** CogViT, pre-trained on large-scale image–text data
- **Cross-modal Connector:** Lightweight with efficient token downsampling
- **Language Decoder:** GLM-0.5B
- **Layout Pipeline:** PP-DocLayout-V3 (two-stage: layout analysis + parallel recognition)
- **Training:** Multi-Token Prediction (MTP) loss + stable full-task reinforcement learning

## Performance

- OmniDocBench V1.5: **94.62** (#1 overall)
- SOTA on formula recognition, table recognition, information extraction
- Speed: 1.86 pages/second (PDF), 0.67 images/second

## Deployment Options

| Runtime | Command |
|---------|---------|
| vLLM | `vllm serve zai-org/GLM-OCR --allowed-local-media-path / --port 8080` |
| SGLang | `python -m sglang.launch_server --model zai-org/GLM-OCR --port 8080` |
| Ollama | `ollama run glm-ocr` |
| Transformers | `AutoModelForImageTextToText` from `transformers` |

## Supported Languages

zh, en, fr, es, ru, de, ja, ko

## Technical Report

- arXiv: https://arxiv.org/abs/2603.10910

## SDK

- GitHub: https://github.com/zai-org/GLM-OCR
- API Docs: https://docs.z.ai/guides/vlm/glm-ocr
- Community: WeChat, Discord