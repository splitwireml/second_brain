---
title: Jev
created: 2026-09-22
updated: 2026-09-22
type: entity
tags: [model, inference, ai, product]
sources: [raw/articles/sydney-runkle-x-article-2100754364545761643.md]
---

# Jev

**Jev** is TypeSafe AI's early-access System One model: it accepts natural-language or structured state plus named questions, then returns typed decisions and calibrated probabilities rather than generated text. TypeSafe's official documentation exposes it through the `jev-latest` API model and `POST https://api.typesafe.ai/v1/systemone`. The source positions it as a fast decision layer inside an agent harness, not as the model that performs open-ended reasoning or generation.^[raw/articles/sydney-runkle-x-article-2100754364545761643.md]

## Confirmed interface

- A request supplies `state`, `model`, and a `questions` map; the documented question types are **Choice**, **Score**, and binary **Noul**.
- Multiple questions over the same state are evaluated independently and in parallel in one request; answers retain probabilities/confidence where applicable.
- The LangChain integration is `TypeSafeClassifier` from `langchain-typesafe`; `.invoke()` accepts strings, structured JSON, or LangChain messages. LangChain documents routing, model selection, and tool-safety decisions as intended uses.

## Harness role

Jev separates cheap, typed policy decisions from an LLM's generative work. The source's concrete placements are: choose a cheaper model for direct lookups/extraction/localized changes, escalate architecture or high-stakes work, and risk-gate a `bash` tool call before execution via `AutoModeMiddleware`. This is an implementation layer inside [[model-agnostic-agent-harness]], complementary to [[system-one-models]] and [[ai-cost-optimization]].^[raw/articles/sydney-runkle-x-article-2100754364545761643.md]

## Evidence boundaries

**Confirmed:** TypeSafe documents the System One request/response shape, `jev-latest`, the three question types, and a hosted API; LangChain documents `TypeSafeClassifier` and its decision-focused integration.

**Source/company claims, not independently benchmarked here:** Jev is reported as up to 200× faster and 400× lower cost than comparable LLM classification. TypeSafe's release post describes 40×–200× faster end-to-end response time for comparable System One-shaped queries, but this ingest does not establish the source's 400× cost figure or task-quality parity.

**Not a replacement:** Jev does not generate text. A complete agent still needs a generative/reasoning model, explicit policy criteria, and testable tool boundaries.

## Related

- [[system-one-models]]
- [[model-agnostic-agent-harness]]
- [[ai-cost-optimization]]
- [[sydney-runkle]]

## References

- TypeSafe release: https://typesafe.ai/blog/introducing-system-one-models-and-jev
- TypeSafe quickstart: https://docs.typesafe.ai/introduction/quickstart
- LangChain integration: https://docs.langchain.com/oss/python/integrations/providers/typesafe
