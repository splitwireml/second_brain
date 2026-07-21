---
title: Qwen
created: 2026-04-14
updated: 2026-07-16
type: entity
tags: [model, chinese-ai, qwen, vision, ai-research, training]
sources: [raw/articles/thread-NVIDIAAI-2077061428998013279.md]
---

# Qwen

Alibaba's open-source LLM model family. Covers text models (Qwen3, Qwen2.5), coding models (Qwen2.5-Coder), vision-language models (QVQ), and specialized variants. Licensed under Apache 2.0. Available in sizes from 0.5B to 72B+ parameters.

The NVIDIA AI thread names Qwen3-VL-2B as the vision model in a source-described autoresearch experiment: a coding agent trained it to count colored stars and reportedly raised accuracy from 25% to 96.9%. The result is retained as a source claim rather than an independently verified benchmark.^[raw/articles/thread-NVIDIAAI-2077061428998013279.md]

## Related Models

- [[qwen2-5-coder-0-5b]] — 0.5B coding model; base for lightweight coding fine-tunes
- [[qwen3-6-27b]] — 27B dense flagship coding model
- [[qwen3-6-35b-a3b]] — Qwen3 MoE 35B / 27B active
- [[qwen3-8b-opus-reasoning]] — 8B reasoning-specialized model distilled from Claude Opus
- [[qwen-image-layered]] — image-layer decomposition model

## Related

- [[lightweight-coding-assistants]] — lightweight coding category that includes Qwen2.5-Coder-0.5B base
- [[huggingmodels]] — primary distribution channel for Qwen model releases
- [[nvidia-ai]] — source account for the Qwen3-VL-2B training demonstration
