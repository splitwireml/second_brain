---
title: System One Models
created: 2026-09-22
updated: 2026-09-22
type: concept
tags: [model, inference, agent, workflow, architecture]
sources: [raw/articles/sydney-runkle-x-article-2100754364545761643.md, raw/articles/thread-matthewcanham-2102077098756280413.md]
related_entity: [[jev]]
author: [[sydney-runkle]]
---

# System One Models

A **System One model** is a non-generative decision component: it evaluates a supplied state against typed questions and returns structured answers with probabilities/confidence. It belongs beside, not inside, the generative LLM loop: the LLM handles ambiguous reasoning and language production; the decision model makes frequent, constrained routing or policy calls. TypeSafe's [[jev]] is the source's concrete implementation.^[raw/articles/sydney-runkle-x-article-2100754364545761643.md]

## Decision contract

The contract is explicit: send shared `state` plus a named `questions` map, then consume typed outputs. The documented Jev shapes are:

- **Choice** — choose among supplied criteria and return option probabilities plus confidence.
- **Score** — place input on ordered criteria with a continuous score, distribution, and confidence.
- **Noul** — return the probability that a binary statement is true.

Because independent questions reuse the same state and execute in parallel, the pattern can avoid serial LLM calls for every small decision. The application—not the classifier—owns thresholds, escalation, and the action that follows.

## Local product-decision workflow

Canham's explainer makes the decision surface explicit: send `model: "jev-latest"`, shared `state`, and a `questions` object; each named question declares a `type`, `instructions`, and `criteria`. Jev returns `answers` keyed by question. This is a source-described interface, not independently validated API documentation.^[raw/articles/thread-matthewcanham-2102077098756280413.md]

The article's exact Noul example sends `food_complaint` with `type: "noul"`, the instruction `Does this review express dissatisfaction with the food itself?`, and true/false criteria distinguishing taste/temperature/quality complaints from queue/service complaints. For state `Waited twenty minutes, but the hotdog was worth it. Would come back if the queue was shorter.`, it shows `noul: 0.04`. The Choice example sends `main_topic`, with `type: "choice"`, instructions to select the primary focus, and `queue`, `food`, `service`, and `other` criteria; it shows `choice: "queue"`, probabilities `0.80`, `0.15`, `0.03`, `0.02`, and `confidence: 0.60`. The source says Choice supports up to 255 options.^[raw/articles/thread-matthewcanham-2102077098756280413.md]

For Score, the source sends `overall_satisfaction` with `type: "score"`, the instruction `How satisfied is this customer with their overall experience? Consider both positive and negative comments.`, and five ordered criteria from Very dissatisfied through Very satisfied. It shows `score: 2.1` plus a `probabilities` distribution of `0: 0.05`, `1: 0.15`, `2: 0.50`, `3: 0.25`, `4: 0.05`; separately, it describes Score as rating against a scale of 2 to 10 levels. Those example values, prompt strings, fields, and model name are preserved as source-specific contract details rather than generalized guarantees.^[raw/articles/thread-matthewcanham-2102077098756280413.md]

The source's hotdog-review workflow therefore separates food dissatisfaction from queue/service complaints, categorizes the primary topic, and scores overall satisfaction before application code chooses the next action. It proposes the same contract for cancellation risk, shipment delays, student misconceptions, unowned meeting commitments, player hints, specialist-team routing, tutorial selection, game-character replies, museum-guide selection, recipe substitutions, bug disruption, travel fit, product-hypothesis support, character-voice drift, and game-hint revealingness. It contrasts the Jev example with `gpt-5.6 Luna` over 60 feedback items; a thread reply mentions `Opus 5` processing six pages versus Jev sorting/checking 300 web pages in 18 seconds for two cents. These are source/reply claims, not benchmark evidence.^[raw/articles/thread-matthewcanham-2102077098756280413.md]

This is a decision sidecar, not a chatbot: it does not replace generative reasoning or implement a product action. The article gives no model size, training-data, calibration, reliability, task-quality, or benchmark-method details; its 20–200× speed and 40–400× cost ranges are source claims only. It names ChatGPT, Claude, Grok, and Kimi as text-generating LLM examples. Thread replies explicitly question confidence, verification, model size, and long-running state, reinforcing that thresholds, escalation, and evaluation remain application responsibilities.^[raw/articles/thread-matthewcanham-2102077098756280413.md]


## Agent-harness placements

1. **Model routing:** classify task complexity; send direct lookups, extraction, and localized changes to a fast model while escalating architecture/high-stakes work to a more capable one.
2. **Tool-risk gate:** classify a proposed action before a tool executes; block or require escalation when the policy says it is unsafe.
3. **Operational triage:** classify urgency, team ownership, severity, or skip/route decisions from the agent's existing state.

This refines [[model-agnostic-agent-harness]]: its loop/checks layer can contain a specialized decision sidecar rather than spending a full LLM call on every route or gate. It is also a remote-service counterpart to [[three-tier-local-model-routing]]; both reserve expensive generative reasoning for work that needs it.

## Evidence layers

**Confirmed:** TypeSafe documents the API's typed-question contract and parallel evaluation; LangChain documents `TypeSafeClassifier` as a runnable for request routing, model choice, and tool-safety decisions.

**Likely:** this architecture reduces latency and cost when an agent has many narrow, repeatable decisions with auditable criteria.

**Speculative / source-company claims:** calibrated probabilities are sufficiently reliable to automate a particular risk policy; the claimed 200× speed and 400× cost advantage transfer to a specific workload. Thresholds, false-positive/false-negative costs, adversarial inputs, and outcome quality still need workload-specific evaluation.

## Related

- [[jev]]
- [[model-agnostic-agent-harness]]
- [[three-tier-local-model-routing]]
- [[ai-cost-optimization]]
- [[sydney-runkle]]
- [[matthewcanham]]
