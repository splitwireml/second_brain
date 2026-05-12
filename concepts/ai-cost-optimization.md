---
title: AI Cost Optimization
created: 2026-04-12
updated: 2026-04-14
type: concept
tags: [optimization, tools, monetization]
sources: [raw/articles/noisyb0y1-ai-cost-optimization-2026-04-10.md]
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

### Provider-Margin Arbitrage (AI Video)

A parallel cost-reduction vector applies to AI API costs when the provider adds significant margin. [[frederikfeldt-seedance-pricing]] documents a case: Seedance 2.0 hosted platforms charge $0.25–0.37/second, while raw ByteDance API reportedly costs ~$0.10/second — a 2.5–3.7× markup for the convenience of a hosted UI.

The hosted platforms' value proposition is the model zoo (30+ models, full creative suite). For operators who need only one model, paying for the entire bundle is pure waste. The arbitrage exists wherever a platform wraps a metered API in a bundled product.

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

## Related Concepts

- [[llm-server-throughput-optimization]] — server-side inference optimization
- [[turboquant-kv-cache-compression]] — KV cache quantization for context length
- [[three-tier-local-model-routing]] — routing architecture that reduces cloud calls before token costs are incurred
