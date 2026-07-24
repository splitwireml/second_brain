---
title: Qwen3-6-27B
created: 2026-04-22
updated: 2026-07-24
type: entity
tags: [llm, model, chinese-ai, open-source, qwen]
sources: [raw/articles/alibaba-qwen-qwen3-6-27b-2046939764428009914.md, raw/articles/qwen3-6-35b-rtx4070-12gb-iam-shanmukha-2026-05-01.md, raw/articles/thread-0xSero-2080003696885154280.md]
related_entity: [[minimax]]
---

# Qwen3-6-27B

Dense, open-source 27B parameter language model by Alibaba's Qwen team. Announced April 22, 2026. Positioned as a flagship-level coding model that punches above its weight class.

## Key Claims

- **27B parameters** — dense (not MoE), runs on consumer-grade hardware
- **Coding benchmarks** — claims to surpass Qwen3.5-397B-A17B across major coding benchmarks
- **Agentic coding** — strongest capability highlighted
- **Thinking + non-thinking modes** — supports both modes
- **Apache 2.0** — fully open source

## 2026-07-22 Hardware-Fit Update

[[0xsero]] placed Qwen3.6-27B “Thinking Cap” in the 24–96 GB tier and wrote that calling Qwen’s reasoning model “Thinking Cap” improved performance by 10 basis points across benchmarks. The local thread also contains users comparing Qwen3.6 variants on 12–96 GB systems and discussing whether the model or GLM 5.2 is preferable for a four-DGX-Spark cluster. These are source-reported observations, not independent measurements.^[raw/articles/thread-0xSero-2080003696885154280.md]

## Context

Qwen3.6-27B is the latest in the Qwen3.6 series, which includes Qwen3.6-35B-A3B (Mixture of Agents with 3 experts, 35B total / 27B active per the MoA architecture). The 27B variant appears to be a dense model variant optimized for efficiency.

## Related

- [[minimax]] — related entity from frontmatter; explicit cross-link
- [[qwen3-8b-opus-reasoning]] — smaller 8B reasoning-specialized variant
- [[qwen3-6-35b-a3b]] — 35B MoE variant (35B total / 27B active); Qwen3.6 series
- [[bonsai-27b]] — source-described ternary-compressed variant/listing associated with this model
- [[minimax-m27]] — another open-weight model with agentic capabilities
- [[dflash]] — z-lab's diffusion-based speculative decoding; Qwen3.6-27B-DFlash announced April 30 2026 as a DFlash-accelerated variant
- [[llm]] — general LLM concepts

## Sources

- [Qwen Official Announcement](https://x.com/Alibaba_Qwen/status/2046939764428009914) — 1132 RT, 8007 likes
- [Hardware-fit thread](https://x.com/0xSero/status/2080003696885154280) — local source reports the Thinking Cap placement and benchmark claim
