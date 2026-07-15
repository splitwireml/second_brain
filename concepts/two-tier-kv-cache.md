---
title: Two-Tier KV Cache
name: two-tier-kv-cache
created: 2026-05-16
updated: 2026-05-16
type: concept
description: A memory management strategy for LLM inference that keeps immediate context in fast unified/RAM while paging older conversation history to SSD, reducing memory pressure without losing context state.
tags: [apple-silicon, kv-cache, llm-inference, memory-management, ssd-paging]
sources: [raw/transcripts/2026-05-16-OMLX.md]
---

# Two-Tier KV Cache

A memory management approach for LLM inference runtimes that splits the KV cache into hot (immediate context) and cold (older history) tiers, using SSD paging for the cold tier to extend effective memory capacity beyond RAM limits.

## Core Problem

Running long conversations with LLMs is memory-intensive because every word of history must remain in RAM. For Macs with limited unified memory, this creates a hard ceiling on context window utilization — either you hit OOM or you truncate context and lose valuable conversation state.

## How It Works

### Tier 1: Hot (Unified Memory)
- Immediate context: recent turns, active instructions, current task state
- Kept in unified memory for maximum access speed
- GPU can read results with zero-copy

### Tier 2: Cold (SSD)
- Older conversation history: system prompts, tool definitions, earlier turns
- "Frozen" and swapped to high-speed SSD when not actively needed
- Can be instantly rehydrated when referenced by new tokens

### The Key Insight

Unlike a naive page-out where you lose state, a well-designed two-tier cache preserves the computational state on disk. When the model processes tokens that reference paged history, the system recognizes the prefix, loads the state back from SSD, and continues generation without gaps or hallucinations.

## Trade-offs

**Advantages:**
- Effective RAM extension through SSD utilization
- Background agent work doesn't block normal computer usage
- Higher throughput (tokens/second) due to better memory management

**Disadvantages:**
- Occasional context limit errors on constrained hardware
- May require manual intervention (`/clear`) to manage memory
- SSD must be high-speed (NVMe) to make paging worthwhile

## Implementation Example: OMLX

OMLX implements this on Apple Silicon using MLX's zero-copy arrays and lazy computation. The SSD paging is persistent — even when you clear a session, the computational state remains on disk and resumes instantly on the next prompt.

This is what enables OMLX to achieve ~47 tokens/second on M2 MacBook Pro while LM Studio achieves ~16 tokens/second, despite both using the same Qwen 3.6 35B 4-bit model.

## Related Concepts

- [[omlx]] — the inference engine that popularized this technique on Apple Silicon
- [[kv-cache-compression]] — related memory optimization techniques
- [[mlx]] — the underlying framework enabling zero-copy on Apple Silicon