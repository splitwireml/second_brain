---
title: Local LLM Size Tradeoffs
created: 2026-06-07
updated: 2026-07-24
type: concept
tags: [inference, benchmark, local-llm, optimization, hardware]
sources: [raw/articles/thread-0xSero-2080003696885154280.md]
related_entity: [[running-local-llms-practical-guide]]
---

# Local LLM Size Tradeoffs

Tradeoffs between model size, quality, speed, and memory for local LLM deployment. The 2026-07-22 [[0xsero]] thread makes the tradeoff concrete with a source-reported hardware ladder rather than a universal ranking.

## Source-Reported Hardware Ladder

- **4–8 GB:** [[nanbeige]]; suggested for lightweight tagging work.
- **8–24 GB:** [[bonsai-27b]]; claimed ternary compression of Qwen3.6-27B, with fit disputed by replies.
- **24–96 GB:** [[qwen3-6-27b]] Thinking Cap.
- **96–192 GB:** [[laguna-s-2-1]].
- **192–384 GB:** [[motif]].

The replies are part of the evidence: practical fit depends on quantization variant, KV-cache/context overhead, tool-calling quality, licensing, and whether the hardware is a single GPU, unified-memory Mac, or multi-device setup. A bucketed recommendation is therefore a starting point for testing, not a verified benchmark table. ^[raw/articles/thread-0xSero-2080003696885154280.md]

## Related

- [[running-local-llms-practical-guide]] — memory math, runtimes, model selection, and optimization layers.
- [[qwen3-6-consumer-gpu-tuning]] — Qwen3.6-specific offloading and KV-cache tuning.
- [[1-bit-bonsai-bitnet-fine-tuning]] — existing 1-bit/ternary compression context.
- [[0xsero]] — source author of the hardware ladder.
