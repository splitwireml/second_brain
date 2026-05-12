---
title: GLM-OCR
created: 2026-04-16
updated: 2026-04-16
type: entity
tags: [ocr, document-understanding, multimodal, vision-language, open-source, inference]
sources: [raw/articles/zai-org-glm-ocr-2026-04-16.md]
related_entity: [[zai-org]]
---

# GLM-OCR

GLM-OCR is a multimodal OCR model for complex document understanding, built by [[zai-org]] on the GLM-V encoder–decoder architecture. At only **0.9B parameters**, it achieves #1 on OmniDocBench V1.5 (94.62) and SOTA on formula recognition, table recognition, and information extraction benchmarks.

## Overview

- **Organization:** [[zai-org]] (Z.ai)
- **Architecture:** GLM-V (CogViT visual encoder + GLM-0.5B decoder)
- **Parameters:** 0.9B
- **License:** MIT
- **Languages:** zh, en, fr, es, ru, de, ja, ko
- **Technical Report:** [arXiv:2603.10910](https://arxiv.org/abs/2603.10910)
- **SDK:** [github.com/zai-org/GLM-OCR](https://github.com/zai-org/GLM-OCR)

## Key Features

- **State-of-the-Art Performance:** 94.62 on OmniDocBench V1.5, ranking #1 overall; SOTA on formula recognition, table recognition, and information extraction
- **Real-World Robustness:** Complex tables, code-heavy documents, seals, and diverse layouts
- **Efficient Inference:** Supports [[vllm]], [[sglang]], and Ollama deployment — 1.86 pages/sec (PDF), 0.67 images/sec
- **Two-Stage Pipeline:** PP-DocLayout-V3 for layout analysis, then parallel recognition

## Architecture

- **Visual Encoder:** CogViT, pre-trained on large-scale image–text data
- **Cross-modal Connector:** Lightweight with efficient token downsampling
- **Language Decoder:** GLM-0.5B
- **Layout Pipeline:** PP-DocLayout-V3 (layout analysis → parallel recognition)
- **Training:** Multi-Token Prediction (MTP) loss + stable full-task RL

## Deployment

| Runtime | Notes |
|---------|-------|
| [[vllm]] | `vllm serve zai-org/GLM-OCR --port 8080` |
| [[sglang]] | `python -m sglang.launch_server --model zai-org/GLM-OCR --port 8080` |
| Ollama | `ollama run glm-ocr` |
| Transformers | `AutoModelForImageTextToText` from `transformers` |

## Related

- [[vllm]] — high-throughput LLM inference engine, supports GLM-OCR deployment
- [[sglang]] — high-throughput LLM inference engine, supports GLM-OCR deployment
- [[vision-language-models]] — VLMs process images + text; GLM-OCR as a specialized document-understanding VLM
- [[zai-org]] — the organization behind GLM-OCR
