---
title: Three-Tier Local Model Routing
created: 2026-04-14
updated: 2026-04-14
type: concept
tags: [agent, inference, optimization, method]
sources: [raw/articles/leopardracer-mac-mini-35b-local-routing-2026-04-14.md]
related_entity: [[leopardracer]]
author: [[leopardracer]]
---

# Three-Tier Local Model Routing

## Definition

Three-Tier Local Model Routing is an agent architecture pattern where local models are split by job shape rather than by brand loyalty to one model. A small fast model handles ubiquitous low-stakes classification, a mid-tier model handles summarization/compression, and a large local model handles heavy preprocessing and degraded-mode fallback. A frontier cloud model remains the primary reasoning engine for complex or sensitive work.

## Core idea

The pattern rejects two common mistakes:

- sending everything to the expensive cloud model
- forcing one local model to cover every task

Instead, it routes by task economics and latency tolerance.

## Tier structure from the source

### 1. Fast tier

Runs on every incoming message.

Typical jobs:
- intent/type classification
- urgency labeling
- cheap skip/route decisions

Primary requirement: latency.

### 2. Primary tier

Used when language understanding matters but full frontier reasoning is unnecessary.

Typical jobs:
- message compression before cloud inference
- email preprocessing
- short summary generation
- intermediate operational text transforms

Primary requirement: decent quality at modest cost.

### 3. Heavy tier

Large local model used sparingly.

Typical jobs:
- compressing a full day's operational signals into a planning brief
- memory consolidation or clustering
- overnight degraded-mode operational fallback
- absorbing outages or rate limits from the cloud tier

Primary requirement: local availability and broader capability, not perfect quality.

### 4. Cloud tier

The source keeps Claude as the main reasoning engine. Local routing exists to protect cloud capacity, not to eliminate it.

## Why the pattern works

### Cost

Pre-classification and pre-compression reduce unnecessary cloud calls and shrink prompt payloads before they hit the expensive model. In the source, this is the real savings mechanism, which makes it an extension of [[ai-cost-optimization]] rather than a separate idea.

### Latency

Strict classification does not need long chain-of-thought. Disabling reasoning mode on small local models can turn an unusably slow classifier into a sub-second routing component.

### Resilience

When the cloud model is rate-limited or unavailable, a large local tier can keep operational tasks moving. The local model is not expected to match frontier quality; it only needs to preserve minimum viable system function.

### Hardware leverage

The heavy tier becomes practical when paired with [[llama-cpp]] and memory mapping. That makes oversized MoE models more usable on constrained Apple Silicon systems than naive RAM math suggests, especially for workloads where not all parameters are active per token.

## Evidence layers

### Confirmed

- [[leopardracer]] published a detailed source post describing this routing pattern on 2026-04-13.
- llama.cpp server docs document `--mmap`, supporting the general feasibility of SSD-backed memory mapping.
- arXiv paper `2312.11514` ("LLM in a flash") exists and supports the broader idea of limited-memory inference backed by storage.
- Ollama's gemma4 page currently advertises small multimodal variants, supporting the plausibility of small-model routing for mixed media inputs.

### Likely

- This pattern is strongest in always-on agent systems with many cheap-but-frequent classification and compression tasks.
- The economic gain comes more from avoiding unnecessary frontier-model usage than from replacing frontier reasoning outright.
- The pattern is especially attractive on Apple Silicon mini/server boxes where power, cost, and unified memory make always-on local inference practical.

### Source claims not independently verified

- The exact 30-40% reduction in Claude sessions claimed by the author.
- The exact 15x token savings on daily signal compression.
- The exact decode speeds and zero-swap behavior on the author's machine.
- The superiority of the author's specific Gemma-vs-Qwen benchmark outcomes outside that environment.

### Speculative

- A single model family can eventually cover all three local tiers without quality regressions.
- Most agent operators will get similar gains without redesigning task boundaries and safety bypass rules.

## Safety and routing rules

The source includes an important rule: some message classes should bypass local routing entirely and go straight to the cloud model. The cited examples are work-related, money-related, deployment, and publishing tasks, plus very short ambiguous messages. That matters because routing mistakes on small models are cheap technically but expensive operationally.

## Why it matters

This pattern turns local inference from a hobby benchmark into infrastructure. It gives local models a clear role inside an agent system:

- classify first
- compress before expensive reasoning
- keep a larger local fallback for outages
- let the cloud model spend its budget on genuinely hard work

It complements [[llm-server-throughput-optimization]] by solving a different problem: throughput optimization scales one inference server harder, while three-tier routing changes which tasks hit which model at all.

It also complements [[ai-cost-optimization]] by adding an architectural cost lever on top of token filtering and cashback.

## Related pages

- [[leopardracer]] — source author
- [[ai-cost-optimization]] — cost reduction via fewer cloud calls and smaller prompts
- [[llama-cpp]] — mmap-capable heavy-tier inference engine
- [[llm-server-throughput-optimization]] — scaling local inference capacity once routing decisions are made
- [[turboquant-kv-cache-compression]] — complementary KV-cache optimization for long-context local inference
- [[three-tier-routing-vs-turboquant-on-16gb-apple-silicon]] — comparison of architecture-layer routing versus low-level memory compression on 16 GB Macs
- [[hermes-agent]] — adjacent agent system where local preprocessing and fallback layers are relevant

## References

- Raw source: `raw/articles/leopardracer-mac-mini-35b-local-routing-2026-04-14.md`
- Original tweet: https://x.com/leopardracer/status/2043631410045452360
- arXiv: https://arxiv.org/abs/2312.11514
- llama.cpp server docs: https://raw.githubusercontent.com/ggml-org/llama.cpp/master/tools/server/README.md
- Ollama gemma4 page: https://ollama.com/library/gemma4
