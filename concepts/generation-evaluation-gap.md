---
title: Generation-Evaluation Gap
created: 2026-04-14
updated: 2026-04-14
type: concept
tags: [llm, method, training]
sources: [raw/papers/autoreason.tex]
related_entity: [[autoreason]]
---

# Generation-Evaluation Gap

The central theoretical claim in [autoreason](/autoreason): self-refinement fails because **generation and evaluation are different tasks**, and evaluation is often harder. A model that can produce a good output cannot necessarily recognize whether its own output is good.

This gap is the necessary condition for autoreason's value. When the gap is wide, external evaluation helps. When it narrows, external evaluation becomes redundant.

## Evidence from Model Tiering

The [autoreason](/autoreason) paper tests autoreason across 5 model tiers and finds a clear pattern:

| Model | AR Advantage | Explanation |
|-------|-------------|-------------|
| Llama 8B | None (AR wins 1/3) | Too weak to generate diverse alternatives |
| Gemini Flash | Moderate (+5pp) | Gap is wide |
| **Haiku 3.5** | **Maximum (+8.3pp)** | **Gap is widest; baselines degrade** |
| Sonnet 4 | Moderate (+5.4pp) | Gap still significant |
| Sonnet 4.6 | Minimal (+0-4pp) | Gap narrow; self-evaluation sufficient |

## Haiku 4.5: The Transition Point

Haiku 4.5 is the clearest evidence for the gap theory. With Sonnet 4.6 judges:
- Public tests: autoreason +4pp over single-pass (75% vs 71%)
- **Private tests: autoreason equals single-pass (60% vs 60%)** — advantage vanishes entirely
- Critique-and-revise no longer degrades (was 35% vs 38% single for Haiku 3.5)

The model crossed the threshold where its own evaluation capability is sufficient. The generation-evaluation gap has narrowed to the point where structured external evaluation adds nothing on held-out tests.

## The Destruction Effect at Weak Models

With Haiku 3.5, standard self-refinement baselines *degraded* outputs below the unrefined single-pass:
- Conservative: 17/42 avg Borda vs single-pass 33.7
- Critique-and-revise: 16.3 vs 33.7 (degraded 52%)
- Harsh critic: 15.3 vs 33.7

The mechanism: Haiku cannot assess whether deletions improve or damage the output. Each pass is a coin flip between improvement and degradation, and the coin is biased toward degradation. Autoreason's judge panel rejects passes that lose content quality — this is the evaluation capability the base model lacks.

## Connection to Literature

Huang et al. (2023) showed LLMs cannot self-correct reasoning without external feedback. Autoreason provides that external feedback through the judge panel. The generation-evaluation gap is the theoretical framing for *why* external feedback is necessary and *when* it matters most.

## Practical Implication

> Match your refinement architecture to the model's position on the capability curve.

For mid-tier models (where the gap is wide): use structured multi-candidate evaluation like autoreason. For frontier models (where the gap is narrow): simple methods suffice. For weakest models: invest in generation quality first.
