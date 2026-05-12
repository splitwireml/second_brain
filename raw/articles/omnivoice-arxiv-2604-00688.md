---
updated: 2026-04-17
title: OmniVoice Paper Summary
source: https://arxiv.org/html/2604.00688v1
type: arxiv
---

# OmniVoice Paper Summary

**Source:** https://arxiv.org/html/2604.00688v1
**Title:** OmniVoice: Towards Omnilingual Zero-Shot Text-to-Speech with Diffusion Language Models
**Authors:** Han Zhu, Lingxuan Ye, Wei Kang, Zengwei Yao, Liyong Guo, Fangjun Kuang, Zhifeng Han, Weiji Zhuang, Long Lin, Daniel Povey (Xiaomi Corp.)
**Date:** 2026

## Abstract Highlights

- 600+ languages supported
- 581k-hour multilingual dataset curated entirely from open-source data
- State-of-the-art performance on Chinese, English, and multilingual benchmarks
- Discrete NAR architecture with diffusion language model objective

## Architecture Details

### Core Design
- **Single-stage NAR** — directly maps text to multi-codebook acoustic tokens
- **Bidirectional Transformer backbone** initialized from Qwen3-0.6B
- **8-codebook acoustic tokens** via Higgs-audio tokenizer
- **Full-codebook random masking** strategy

### Key Innovations
1. **Full-codebook Random Masking** — stochastic masking across all codebooks (vs per-layer masking in prior work)
2. **LLM Initialization** — first NAR TTS to benefit from LLM weight initialization

### Why Single-Stage
- Two-stage cascaded systems suffer from:
  - Error propagation (semantic errors degrade acoustic quality)
  - Information bottlenecks (low-bitrate semantic representations lose detail)
- Single-stage bypasses both issues

## Training Details

- **Data:** 581k hours, open-source multilingual data
- **Initialization:** Pre-trained Qwen3-0.6B LLM weights
- **Objective:** Discrete masked diffusion
- **Classifier-free guidance** used in log-softmax space

## Memory Requirements (from GitHub issues)

## See Also

- [[omnivoice-huggingface-2026]] — OmniVoice HuggingFace summary
- [[vibevoice]] — VibeVoice — related open-source voice AI
- [[omnivoice-vs-vibevoice-comparison]] — OmniVoice vs VibeVoice comparison


- Model weights: ~1.2 GB (float16)
- Total inference: ~6-8 GB (float16)
- Whisper ASR adds ~0.5 GB for auto-transcription
- On 7.6 GB GPU: works with `expandable_segments:True` flag