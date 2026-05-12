---
title: vLLM
created: 2026-04-15
updated: 2026-04-27
type: entity
tags: [inference, platform, tools]
sources: [raw/articles/minimax-m27-huggingface-2026-04-15.md]
---

# vLLM

> High-throughput inference engine for LLMs. Recommended deployment target for [[minimax-m27]].

**GitHub:** [vllm-project/vllm](https://github.com/vllm-project/vllm)
**License:** Apache 2.0

vLLM is an open-source inference engine optimized for high-throughput LLM serving. It features PagedAttention (KV cache management), continuous batching, tensor parallelism, and FP8 support. Recommended for production deployments of [[minimax-m27]].

## MiniMax M2.7 Deployment (vLLM)

```bash
SAFETENSORS_FAST_GPU=1 vllm serve \
    MiniMaxAI/MiniMax-M2.7 --trust-remote-code \
    --tensor-parallel-size 4 \
    --enable-auto-tool-choice --tool-call-parser minimax_m2 \
    --reasoning-parser minimax_m2_append_think
```

**Hardware:** 220 GB for weights + 240 GB per 1M KV cache tokens. Recommended: 96G×4 GPU (400K token KV cache).

## Apple Silicon / Metal GPU Support

**vLLM does NOT support Metal GPU on Apple Silicon.** On macOS, vLLM falls back to CPU-only mode.

Evidence from `vllm/platforms/__init__.py`:
```python
is_cpu = sys.platform.startswith("darwin")  # macOS → CpuPlatform
```

`VLLM_TARGET_DEVICE` supports only `cuda` or `cpu` — no `metal` or `mps` option.
All CUDA-kernel-based acceleration (PagedAttention, continuous batching, tensor parallelism)
is unavailable on Metal.

For Apple Silicon inference with GPU acceleration:
- **`llama.cpp` + Metal** — best Apple Silicon GPU option (what [[apple-silicon-embedding-pipeline]] uses)
- **`mlx-lm`** — Apple's official MLX serving library
- **LM Studio** — GUI around llama.cpp/MLX

## Related

- [[apple-silicon-embedding-pipeline]] — LEANN + llama.cpp embedding pipeline on M4 Metal (no GPU parallelism available)
- [[minimax-m27]] — model vLLM is used to deploy
- [[sglang]] — alternative inference engine
