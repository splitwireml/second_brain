---
title: vLLM CUDA Graph OOM Avoidance
created: 2026-04-27
updated: 2026-04-27
type: concept
tags: [inference, optimization, vllm, cuda]
sources: [raw/articles/thread-TheAhmadOsman-2048608672348045540.md]
related_entity: [[theahmadosman]]
author: [[theahmadosman]]
---

## Definition

A vLLM inference optimization technique that avoids out-of-memory (OOM) errors from CUDA Graph compilation without sacrificing the performance gains of graph-based execution. Instead of falling back to eager mode with `--enforce-eager`, the approach temporarily reduces context window size to allow CUDA Graphs to compile and cache, then restores full context on restart.

## The Problem

vLLM may recommend `--enforce-eager` when CUDA Graphs fail to compile due to insufficient VRAM. Eager mode avoids OOM but eliminates CUDA Graph performance gains, which can significantly hurt throughput.

## The Solution

1. **Lower `--max-model-len`** — e.g., reduce to 4K tokens
2. **Let CUDA Graphs compile** — compilation succeeds with reduced context; graphs are cached by `torch.compile`
3. **Restart vLLM** with the cached graphs
4. **Raise `--max-model-len` back up** — cached graphs persist, full context restored

Result: keep CUDA Graph performance gains without hitting OOM.

## Why It Works

CUDA Graphs capture and replay GPU operations as a single optimized execution graph. The compilation step requires enough VRAM to build the graph representation. By temporarily reducing the maximum sequence length, the compilation workspace fits in memory. Once cached, the graphs can handle larger contexts because the replay phase has different memory characteristics than the capture phase.

## Commands

```bash
# Step 1: compile with reduced context
vllm serve <model> --max-model-len 4096

# Step 2: restart with full context (graphs cached)
vllm serve <model> --max-model-len <original>
```

## Related

- [[vllm]] — high-throughput inference engine with PagedAttention and CUDA Graph support
- [[inference-kernel-optimization]] — low-level GPU kernel optimization; CUDA Graphs are one optimization lever
- [[gpu-kernel-learning-path]] — learning curriculum for GPU optimization including serving engine internals
