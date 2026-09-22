---
title: System One Models
created: 2026-09-22
updated: 2026-09-22
type: concept
tags: [model, inference, agent, workflow, architecture]
sources: [raw/articles/sydney-runkle-x-article-2100754364545761643.md]
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
