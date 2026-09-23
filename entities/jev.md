---
title: Jev
created: 2026-09-22
updated: 2026-09-22
type: entity
tags: [model, inference, ai, product]
sources: [raw/articles/sydney-runkle-x-article-2100754364545761643.md, raw/articles/thread-matthewcanham-2102077098756280413.md, raw/articles/xarticle-build-a-jev-judge-2102087107410002345.md, raw/articles/xarticle-jev-is-insane-for-marketing-2102054148925526206.md]
---

# Jev

**Jev** is TypeSafe AI's early-access System One model: it accepts natural-language or structured state plus named questions, then returns typed decisions and calibrated probabilities rather than generated text. TypeSafe's official documentation exposes it through the `jev-latest` API model and `POST https://api.typesafe.ai/v1/systemone`. The source positions it as a fast decision layer inside an agent harness, not as the model that performs open-ended reasoning or generation.^[raw/articles/sydney-runkle-x-article-2100754364545761643.md]

## Confirmed interface

- A request supplies `state`, `model`, and a `questions` map; the documented question types are **Choice**, **Score**, and binary **Noul**.
- Multiple questions over the same state are evaluated independently and in parallel in one request; answers retain probabilities/confidence where applicable.
- The LangChain integration is `TypeSafeClassifier` from `langchain-typesafe`; `.invoke()` accepts strings, structured JSON, or LangChain messages. LangChain documents routing, model selection, and tool-safety decisions as intended uses.

## Harness role

Jev separates cheap, typed policy decisions from an LLM's generative work. The source's concrete placements are: choose a cheaper model for direct lookups/extraction/localized changes, escalate architecture or high-stakes work, and risk-gate a `bash` tool call before execution via `AutoModeMiddleware`. This is an implementation layer inside [[model-agnostic-agent-harness]], complementary to [[system-one-models]] and [[ai-cost-optimization]].^[raw/articles/sydney-runkle-x-article-2100754364545761643.md]

## Local explainer details

Matt Canham's local thread presents [[jev]] to product builders as a generalizing classifier for decisions rather than a text generator: the source claims it retains an LLM-like breadth across domains while returning one bounded decision quickly. That framing is source-described, not a model-card or benchmark result.^[raw/articles/thread-matthewcanham-2102077098756280413.md]

Its `jev-latest` JSON examples send `model`, shared `state`, and a named `questions` map. Each question supplies `type`, `instructions`, and `criteria`: a **Noul** uses `true`/`false` conditions, **Choice** uses named option descriptions, and **Score** supplies an ordered criteria array. The response is an `answers` map rather than prose. For the food-review example, `food_complaint` returns `noul: 0.04`; Choice returns a selected option, per-option `probabilities`, and `confidence`; Score returns a numeric `score` plus a probability distribution.^[raw/articles/thread-matthewcanham-2102077098756280413.md]

The thread calls Choice a selection among up to **255** options and says Score can use **2–10** levels. Its five-level satisfaction example nevertheless returns `score: 2.1` with probability keys `0`–`4`; this is a source example, not a resolved API-spec interpretation. The main article also compares 60 feedback items with `gpt-5.6 Luna` but provides no reproducible benchmark setup. A separate reply claims 300 web pages sorted and checked in 18 seconds for 2 cents while Opus 5 completes 6 pages; that is unverified third-party thread commentary, not Jev documentation.^[raw/articles/thread-matthewcanham-2102077098756280413.md]


## Marketing research deployment

A local article by jaffa describes a source-claimed marketing placement for Jev inside [[virlo]]: **Clearance** applies two confidence-bearing Noul decisions before a short-form video enters a niche benchmark—does its caption/hashtags/transcript actually match the niche, and are its hashtags misleading? The same workflow requests Choice (hook type, format, angle) and Score (performance against that creator's own baseline), then sends only results over an unspecified Noul threshold into script work. The source says a 25-video Clearance batch uses roughly 7,000 input tokens; it gives no request schema, threshold, or measured cost. ^[raw/articles/xarticle-jev-is-insane-for-marketing-2102054148925526206.md]

The article keeps responsibilities separate: Jev qualifies the sample; Virlo is said to do the 80-signal benchmark and visual, production, CTA/brand-safety tagging. Its live Calibration claims—33/44 human-labeled videos across six intents versus an existing judge's 30/44, plus early 3/4 agreement on a partially graded nearly-300-video disagreement pool—are source-described and insufficient to establish quality or migration readiness. It also reports that labeling topic as required while treating format/tone/audience as preferences changed the same test result from 16/44 to 33/44; this is a source-specific prompt observation, not a general rule. ^[raw/articles/xarticle-jev-is-insane-for-marketing-2102054148925526206.md]

## Evidence boundaries

**Confirmed:** TypeSafe documents the System One request/response shape, `jev-latest`, the three question types, and a hosted API; LangChain documents `TypeSafeClassifier` and its decision-focused integration.

**Source/company claims, not independently benchmarked here:** Jev is reported as up to 200× faster and 400× lower cost than comparable LLM classification. TypeSafe's release post describes 40×–200× faster end-to-end response time for comparable System One-shaped queries, but this ingest does not establish the source's 400× cost figure or task-quality parity.

**Not a replacement:** Jev does not generate text. A complete agent still needs a generative/reasoning model, explicit policy criteria, and testable tool boundaries.

## Related

- [[system-one-models]]
- [[model-agnostic-agent-harness]]
- [[ai-cost-optimization]]
- [[sydney-runkle]]
- [[matthewcanham]]

## References

- TypeSafe release: https://typesafe.ai/blog/introducing-system-one-models-and-jev
- TypeSafe quickstart: https://docs.typesafe.ai/introduction/quickstart
- LangChain integration: https://docs.langchain.com/oss/python/integrations/providers/typesafe

## Jev as a post-run agent judge

Akshay Pachaar's refund-support tutorial uses Jev as a judge over one evidence-bearing state: `request`, `policy`, `tool_calls`, and `final_answer`. It keeps the expected verdict out of that state, so the evaluator must infer grounding from evidence rather than receive the answer in its prompt. One example contains a successful `lookup_order` result but no successful `issue_refund`; deterministic code checks the tool success, while Jev judges whether the final response claims a completed refund. The tutorial evaluates independent questions against that shared state in parallel and positions this as post-run evaluation, not refund authorization or an unsafe-action stop path.^[raw/articles/xarticle-build-a-jev-judge-2102087107410002345.md]

Its rubric has `grounded` and `action_honest` Noul questions plus a three-level `helpfulness` Score. The `grounded` instruction asks whether factual claims are supported by supplied evidence; `action_honest` requires completed-action claims to be backed by successful tool results; `helpfulness` ranges from no useful next step to clear next step/complete resolution. The complete `rubric.py` also includes relevance and tells the evaluator to treat trace content as data rather than instructions. Question IDs do not convey the rubric to inference, so each question must carry its own clear instructions.^[raw/articles/xarticle-build-a-jev-judge-2102087107410002345.md]

The source's `JevClient` reads `TYPESAFE_API_KEY`, sends model/state/questions to `POST /v1/systemone`, applies a timeout and bounded retries, validates responses, does not retry authentication failure, and never converts an invalid response into a passing score. A Noul value such as `0.98` is the probability of the stated proposition—not the percentage of an answer that is grounded. For a Score, the tutorial reports a probability-weighted 0–2 helpfulness score normalized by `/ 2` to 0–1 and stores separate TypeSafe confidence; that rating is not confidence, and Noul has no separate confidence field.^[raw/articles/xarticle-build-a-jev-judge-2102087107410002345.md]

The source routes clear failures, clear passes, and uncertain cases needing review. Thresholds are illustrative; it calls for validation against labeled examples, measurement of cost/latency/judgment quality including retries and failed evaluations, review of uncertain cases plus samples of confident ones, pinned rubric/judge versions when comparing agent versions, and retained deterministic checks or an LLM judge when detailed explanations or hidden reasoning are required. Its performance framing is source-described rather than an independent benchmark.^[raw/articles/xarticle-build-a-jev-judge-2102087107410002345.md]

- [[opik]]
- [[eval-engineering]]
