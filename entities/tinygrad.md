---
title: TinyGrad
created: 2026-04-13
updated: 2026-04-18
type: entity
tags: [oss-ai, inference, framework, open-source]
sources: [raw/transcripts/2026-04-13-rtx-5090-mac-egpu.md, raw/articles/x-bookmark-2044813085358117062.md]
---

# TinyGrad

[[alex-ziskind]]'s entity page for coding agents and local LLM inference.

## Overview

TinyGrad is an open-source deep learning framework by [TinyCorp](https://github.com/tinygrad) that prioritizes simplicity and hackability. Best known for writing the first open-source NVIDIA GPU driver for macOS (TinyGPU), enabling NVIDIA Blackwell GPUs to run on Apple Silicon Macs over Thunderbolt.

## Key Products

### TinyGPU

Open-source macOS kernel extension (kext) that provides direct GPU access for NVIDIA and AMD GPUs over Thunderbolt/USB4. No NVIDIA drivers or Linux required. Approved by Apple for macOS.

- **Website:** tinygrad.org
- **Setup:** Single curl command + system extension approval + Docker Desktop (for NVIDIA CUDA compiler or AMD HIP compiler)
- **Installation time:** Under 5 minutes

### TinyGrad Framework

Deep learning framework with auto-generated GPU kernels. The inference server runs entirely on the external GPU with no server overhead.

## Performance on Apple Silicon eGPU

Based on [[alex-ziskind]]'s benchmarks (RTX 5060 Ti, 5070 Ti, 5090 via Thunderbolt 5 on M4 Pro Mac Mini):

| GPU | FP32 Matmul (TFLOPS) | Qwen3 4B tok/s | Notes |
|-----|---------------------|----------------|-------|
| M4 Pro (Metal, internal) | 33 | 3.66 | Baseline |
| RTX 5060 Ti (Thunderbolt 5) | 22.7 | 4.6 | 16GB VRAM |
| RTX 5070 Ti (Thunderbolt 5) | ~37 | 5.5 | 16GB VRAM |
| RTX 5090 (Thunderbolt 5) | ~38 | 6.0 | 32GB VRAM |

**Memory bandwidth observed:** ~33 GB/s (5090 capable of 1.8 TB/s) — kernel optimization is the bottleneck, not Thunderbolt.

**Llama.cpp vs TinyGrad:** Llama.cpp with hand-tuned Metal kernels is 10x faster than TinyGrad on the same Metal backend. TinyGrad auto-generates kernels from a general-purpose compiler vs. Llama.cpp's thousands of contributor-hours of hand-tuned kernels.

## Relationship to llama.cpp

TinyGrad and [[llama-cpp]] are both inference engines but take opposite approaches:
- **Llama.cpp:** Hand-tuned, platform-specific kernels (Metal, CUDA, CPU); years of optimization
- **TinyGrad:** Auto-generated kernels via compiler; prioritizes hackability over raw performance

The TinyGrad team considers this a feature, not a bug — the hard part (driver, compiler pipeline, memory manager) is done; kernel optimization will follow.

## References

- [tinygrad.org](https://tinygrad.org)
- [TinyGPU macOS driver announcement](https://x.com/__tinygrad__/status/2039213719155310736)
- [[rtx-5090-mac-egpu-benchmarks]] (full benchmark data)
