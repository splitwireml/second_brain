---
title: AI Cost Optimization
created: 2026-04-12
updated: 2026-07-15
type: concept
tags: [tools, monetization, optimization]
sources: [raw/articles/noisyb0y1-ai-cost-optimization-2026-04-10.md, raw/articles/thread-VaibhavSisinty-2071243569814491579.md, raw/articles/xarticle-building-against-the-big-labs-that-are-trying-to-e-2076767931053294017.md]
---

# AI Cost Optimization

Reducing the effective cost of AI tool usage through token efficiency and subscription cashback. Covers two dimensions: minimizing token burn per session, and recovering spend via cashback on subscriptions already being paid.

## Token Efficiency

### Input Token Reduction

The primary waste source in AI coding sessions is terminal output noise: logs, progress bars, ANSI codes, passing test output. A typical 30-minute Claude Code session burns ~150K tokens, most of which carry no useful information.

**[[rtk-rust-token-killer]]** sits between terminal and AI, filtering and deduplicating raw command output before it enters the context window. Achieves ~70% input token reduction (150K → 45K tokens per session).

**[[caveman-claude-skill]]** reduces Claude's response verbosity by 65–87% through modes that strip filler, articles, and explanatory fragments.

Combined: input tokens -70%, output tokens -75%. Effective cost per session drops ~80%.

### Session-Level Practices

- **Edit over Reply**: Each follow-up message re-loads entire conversation context. Message 30 costs 31x more than message 1. Editing the original message replaces the exchange rather than accumulating it.
- **Batch questions**: One multi-part prompt costs one context load vs. three separate loads.
- **Projects for repeated files**: Upload once (~75K tokens), not per-session (~375K tokens across 5 sessions).

## Subscription Cashback

**[[bleap]]** is a self-custodial finance app offering 20% cashback on AI subscriptions (Claude Pro, ChatGPT Plus, Gemini Advanced) via its card. Max subscription ($100/mo) generates $20/mo back ($240/yr).

## Architectural Offloading

A newer cost lever is to move routine preprocessing off the frontier model entirely. [[three-tier-local-model-routing]] adds a third dimension to cost optimization:

- small local models classify or discard low-value messages before a paid model sees them
- mid-tier local models compress long inputs before they hit the expensive context window
- a larger local fallback handles degraded-mode operational work during outages or rate limits

This does not eliminate cloud usage. It preserves cloud budget for the tasks that actually need frontier reasoning.

### Provider Router + Prompt Compression

The Vaibhav Sisinty / OmniRoute thread adds a fourth cost lever: keep the client configuration fixed while a local router decides which upstream provider handles the request and whether prompt compression should happen before the expensive model sees the payload. In this framing, cost control is not only about smaller prompts or better local models. It is also about abstraction at the API boundary.

**Confirmed from the bookmark:** the tool is presented as a single localhost endpoint (`http://localhost:20128/v1`, `model: auto`) for Claude Code, Cursor, Codex, Cline, and related coding clients.^[raw/articles/thread-VaibhavSisinty-2071243569814491579.md]

**Source claims not independently verified:** the author claims up to 95% token-cost reduction and 1.6 billion free tokens per month, while replies in the same thread push back that compression and auto-routing can hide quality failures until edge cases surface.^[raw/articles/thread-VaibhavSisinty-2071243569814491579.md]

This makes provider-layer routing a useful extension of [[ai-cost-optimization]], but not yet a confirmed replacement for direct quality testing or workload-specific evaluation.

### Provider-Margin Arbitrage (AI Video)

A parallel cost-reduction vector applies to AI API costs when the provider adds significant margin. [[frederikfeldt-seedance-pricing]] documents a case: Seedance 2.0 hosted platforms charge $0.25–0.37/second, while raw ByteDance API reportedly costs ~$0.10/second — a 2.5–3.7× markup for the convenience of a hosted UI.

The hosted platforms' value proposition is the model zoo (30+ models, full creative suite). For operators who need only one model, paying for the entire bundle is pure waste. The arbitrage exists wherever a platform wraps a metered API in a bundled product.

### Domain-Specific Harness Economics

The [[shortcut]] case study adds a workload-level cost lever: optimize the complete harness for a narrow domain instead of paying the context and tool-call tax of a general-purpose agent. The article reports 37 versus 61 tool calls per spreadsheet task and 3.7M versus 7.1M input tokens against Claude for Excel, alongside claims of 40% lower cost and 17% higher accuracy on Shortcut's internal finance evals. These are source-reported measurements, not independently audited here. ^[raw/articles/xarticle-building-against-the-big-labs-that-are-trying-to-e-2076767931053294017.md]

The broader pattern is to keep a stable task harness while routing subproblems to the best-fit model: the source describes using different models for general spreadsheet work, image/PDF perception, cost-sensitive tasks, and a smaller in-house worker model. Cost optimization therefore includes context design, tool economy, and model selection—not only prompt compression or cheaper inference. ^[raw/articles/xarticle-building-against-the-big-labs-that-are-trying-to-e-2076767931053294017.md]

## Effective Cost Math

| Scenario | Monthly Cost | Token Efficiency | Cashback | Net Annual |
|----------|-------------|-----------------|----------|-------------|
| Unoptimized | $100/mo | 0% | $0 | $1,200 |
| Optimized | $100/mo | -70% (RTK) + -75% (Caveman) | +$20/mo (Bleap) | $960 spend, $240 back = $720 effective |

Same subscriptions. 3x more output per dollar. $240+/year recovered.

## Related Entities

- [[rtk-rust-token-killer]] — input token filter for AI coding sessions
- [[caveman-claude-skill]] — Claude response compression
- [[bleap]] — AI subscription cashback card
- [[omniroute]] — provider-router layer for coding clients, prompt compression, and failover abstraction
- [[shortcut]] — domain-specific spreadsheet agent used as a harness/cost case study

## Related Concepts

- [[llm-server-throughput-optimization]] — server-side inference optimization
- [[turboquant-kv-cache-compression]] — KV cache quantization for context length
- [[three-tier-local-model-routing]] — routing architecture that reduces cloud calls before token costs are incurred
