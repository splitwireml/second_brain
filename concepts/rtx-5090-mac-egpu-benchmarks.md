---
title: RTX 5090 Mac eGPU Benchmarks
created: 2026-04-13
updated: 2026-04-18
type: concept
tags: [inference, performance, apple-silicon, benchmark, llm]
sources: [raw/transcripts/2026-04-13-rtx-5090-mac-egpu.md, raw/articles/x-bookmark-2044813085358117062.md]
author: [[alex-ziskind]]
---

# RTX 5090 Mac eGPU Benchmarks

Running NVIDIA Blackwell GPUs on Apple Silicon Macs via Thunderbolt 5 + TinyGrad's TinyGPU open-source macOS driver.

## Setup

- **Host:** Mac Mini M4 Pro, 64GB RAM
- **Connection:** Thunderbolt 5 (Razer Thunderbolt 5 enclosure for 5070 Ti and 5090; USB4 dock for 5060 Ti)
- **Software:** [[tinygrad]] inference server (auto-generates GPU kernels), Docker Desktop for CUDA compiler
- **Alternative for comparison:** [[llama-cpp]] on Metal

## Key Benchmarks

### FP32 Matrix Multiplication (TFLOPS)

| GPU | Result |
|-----|--------|
| M4 Pro (Metal, internal) | 33 TFLOPS |
| RTX 5060 Ti | 22.7 TFLOPS |
| RTX 5070 Ti | ~37 TFLOPS |
| RTX 5090 | ~38 TFLOPS |

M4 Pro's integrated GPU actually outperforms the 5060 Ti on raw matmul. The 5070 Ti and 5090 show similar matmul performance due to Thunderbolt bandwidth constraints on the bus.

### LLM Token Generation (Qwen3 4B, INT4)

| Engine | Backend | tok/s | Time to First Token |
|--------|---------|-------|---------------------|
| [[llama-cpp]] | Metal (M4 Pro) | ~73.9 | 651ms |
| [[tinygrad]] | RTX 5090 TB5 | 7.39 | ~5000ms |
| [[tinygrad]] | RTX 5070 Ti TB5 | 5.5 | ~5000ms |
| [[tinygrad]] | RTX 5060 Ti TB5 | 4.6 | ~5000ms |
| [[tinygrad]] | Metal (M4 Pro) | 4.29 | ~5000ms |
| M4 Pro (baseline) | Metal | 3.66 | baseline |

NVIDIA RTX 5090 is **72% faster** than Metal on token generation (7.39 vs 4.29 tok/s) via [[tinygrad]], but [[llama-cpp]] on Metal is **10x faster** than [[tinygrad]] on the 5090.

### Larger Models (RTX 5090 only, 32GB VRAM)

| Model | tok/s |
|-------|-------|
| Qwen3 8B | 6.0 |
| Qwen3 30B MOE (active params smaller) | 6.5 |
| Llama 3.1 8B (INT8) | 7.48 |
| Qwen 2.5 14B (INT4) | 3.75 |

### Memory Bandwidth

- Observed: ~33 GB/s
- RTX 5090 rated: 1.8 TB/s
- Gap is kernel inefficiency, not Thunderbolt bottleneck (model weights stay in GPU VRAM; only a few bytes cross TB per token)

## Key Findings

1. **Works.** NVIDIA GPU compute on macOS is real for the first time since 2019. Setup takes under 5 minutes.
2. **Thunderbolt is not the bottleneck.** Once weights are loaded, token generation is GPU-internal.
3. **TinyGrad kernels are unoptimized.** 18x slower than [[llama-cpp]] on Metal. This is expected to improve.
4. **RTX 5090's 32GB VRAM enables larger models** (14B+ dense, 30B+ MOE) that won't fit in 16GB cards.
5. **For current best performance on Mac:** Use [[llama-cpp]] on Metal. For future-proofing and flexibility, watch [[tinygrad]] kernel optimizations.

## Related Concepts

- [[llm-server-throughput-optimization]] — general throughput optimization for LLM servers
- [[turboquant-kv-cache-compression]] — KV cache compression on Apple Silicon
- [[local-rag-for-coding-agents]] — local RAG patterns

## RTX 3090 Deep-Dive (Sandro + @davideciffa)

Independent confirmation via RTX 3090 on USB4 (different setup from Alex Ziskind's tests):

| Configuration | tok/s | Notes |
|---|---|---|
| llama.cpp native CUDA (RunPod) | ~baseline | Llama.cpp on native CUDA edge Metal by 22% |
| tinygrad NAK on eGPU 3090 over USB4 | ~0.74 | MoE models: 2,800 dispatches/token, GPU waits between launches |

**Key finding:** The bottleneck is NOT the cable. RTX 5090 has 1.8 TB/s memory bandwidth; tinygrad uses 28.8 GB/s. The 1.2-1.6% utilization is a kernel scheduling/fusion issue.

**MoE specific:** Qwen3-30B-A3B logs ~2,800 dispatches/token (per-expert work), resulting in 0.74 tok/s. tinygrad's AMD backend already delivers ~50 tok/s on Qwen3.5-9B on a 7900 XTX — the NAK (NVIDIA) backend has significant room to grow.

**What's shipped (the hard part):**
- Open-source NVIDIA GPU driver for macOS (Apple-signed DEXT)
- Memory manager and PCIe BAR mapping over USB4/Thunderbolt
- Compiler integration: nvcc/ptxas in Docker + NAK assembler (Docker-free alternative)
- Support: NVIDIA Ampere, Ada Lovelace, Blackwell, AMD RDNA3+

**What's left (maturity work):**
- Fused operator paths (QKV, RoPE, attention, output projection)
- MoE expert routing fused into single launches
- Quantization-aware matmul kernels per GGUF format
- KV cache layouts tuned per architecture

## References

- [[alex-ziskind]] — Blackwell eGPU benchmarks (RTX 5060 Ti, 5070 Ti, 5090)
- Sandro + @davideciffa — [RTX 3090 deep-dive](https://x.com/pupposandro/status/2044813085358117062) (11,111 chars article)
- [lucebox.com blog: eGPU myth](https://www.lucebox.com/blog/egpu-myth)
