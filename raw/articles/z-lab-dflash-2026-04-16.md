---
updated: 2026-04-17
title: 'DFlash: Block Diffusion for Flash Speculative Decoding'
source: https://github.com/z-lab/dflash
type: github
---

# DFlash: Block Diffusion for Flash Speculative Decoding

**URL:** https://github.com/z-lab/dflash
**Source:** GitHub README + Z Lab project page
**Date:** 2026-04-16
**Type:** research/summary

## Overview

DFlash is a lightweight block diffusion model designed for speculative decoding, enabling efficient and high-quality parallel drafting of token sequences. It achieves up to 6× lossless acceleration on Qwen3-8B — nearly 2.5× faster than EAGLE-3.

## Key Facts

- **Authors:** Jian Chen, Yesheng Liang, Zhijian Liu (Z Lab)
- **Paper:** arXiv:2602.06036
- **GitHub:** 1,252 stars
- **Created:** 2026-01-04
- **Last push:** 2026-04-14
- **Language:** Python

## Technical Core

### The Problem

Standard LLM inference is sequential — every token depends on the previous one. This creates a bottleneck.

### Speculative Decoding

A small draft model proposes tokens, then the target LLM verifies them in parallel. EAGLE-3 and similar approaches draft **autoregressively** (token by token), capping speedups at ~2-3×.

### DFlash Innovation

DFlash uses a **block diffusion model** to draft an entire block of tokens in a **single parallel forward pass**. This breaks the sequential bottleneck at the draft stage.

Key claim: up to **6× lossless acceleration** on Qwen3-8B, nearly **2.5× faster than EAGLE-3**.

## Supported Models

| Model | DFlash Draft Model |
|---|---|
| Kimi-K2.5 (Preview) | z-lab/Kimi-K2.5-DFlash |
| Qwen3.5-4B | z-lab/Qwen3.5-4B-DFlash |
| Qwen3.5-9B | z-lab/Qwen3.5-9B-DFlash |
| Qwen3.5-27B | z-lab/Qwen3.5-27B-DFlash |
| Qwen3.5-35B-A3B | z-lab/Qwen3.5-35B-A3B-DFlash |
| Qwen3-Coder-Next | z-lab/Qwen3-Coder-Next-DFlash |
| Qwen3-Coder-30B-A3B | z-lab/Qwen3-Coder-30B-A3B-DFlash |
| gpt-oss-20b | z-lab/gpt-oss-20b-DFlash |
| gpt-oss-120b | z-lab/gpt-oss-120b-DFlash |
| Qwen3-4B (non-thinking) | z-lab/Qwen3-4B-DFlash-b16 |
| Qwen3-8B (non-thinking) | z-lab/Qwen3-8B-DFlash-b16 |
| Llama-3.1-8B-Instruct | z-lab/LLaMA3.1-8B-Instruct-DFlash-UltraChat |

Coming soon: Qwen3.5-122B-A3B, Qwen3.5-397B-A17B, GLM-5.1

## Backends

| Backend | Install | Notes |
|---|---|---|
| Transformers | `uv pip install -e ".[transformers]"` | Qwen3 and LLaMA-3.1 only |
| SGLang | `uv pip install -e ".[sglang]"` | Production serving |
| vLLM | Requires nightly build | Integration in progress |
| MLX | `pip install -e ".[mlx]"` | Apple Silicon |

## Architecture

Block diffusion draft model + target LLM verification. The draft model generates a block of tokens in a single parallel pass, then the target model accepts/rejects each token in parallel.

## Citations

```bibtex
@article{chen2026dflash,
  title   = {{DFlash: Block Diffusion for Flash Speculative Decoding}},
  author  = {Chen, Jian and Liang, Yesheng and Liu, Zhijian},
  journal = {arXiv preprint arXiv:2602.06036},
  year    = {2026}
}
```

## Acknowledgements

Thanks to dcw02, gongy, and Modal Labs team for SGLang support; benchislett at NVIDIA for vLLM integration.