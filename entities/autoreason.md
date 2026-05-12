---
title: Autoreason
created: 2026-04-14
updated: 2026-04-14
type: entity
tags: [oss-ai, method, agent, llm]
sources: [raw/papers/autoreason.tex, raw/papers/autoreason-readme.md]
---

# Autoreason

An iterative LLM self-refinement method developed by [SHL0MS](https://github.com/shl0ms) and the Hermes Agent team, published by [Nous Research](https://github.com/NousResearch/autoreason). Extends [Karpathy's autoresearch](/autoresearch) beyond objective metrics to subjective domains where no ground-truth fitness function exists.

## Overview

Autoreason structures each refinement iteration as a three-way tournament between:
- **A (incumbent)** — the current version, unchanged
- **B (adversarial revision)** — a fresh agent revises A based on a separate critic's findings
- **AB (synthesis)** — a third agent merges the strongest elements of A and B

A blind panel of 3 fresh agents ranks all three via [Borda count](https://en.wikipedia.org/wiki/Borda_count), with the incumbent winning ties. Convergence requires the incumbent to survive $k=2$ consecutive passes.

## Core Design

The key insight is that "do nothing" must be a first-class option. Standard critique-and-revise loops never decline to make changes — they accumulate [scope drift](https://en.wikipedia.org/wiki/Feature_creep) unchecked. Autoreason's judge panel filters out regressions.

Every role (critic, author B, synthesizer, judges) uses a fresh isolated agent with no shared context. This prevents [authorship bias](https://en.wikipedia.org/wiki/Confirmation_bias) where an agent that wrote version A will defend it.

## Key Findings

1. **Generation-evaluation gap is the mechanism.** Self-refinement fails because evaluation is harder than generation. Autoreason bridges this gap with external judges. The advantage peaks at **mid-tier models** (Haiku 3.5, Gemini Flash) where the gap is widest, and diminishes at both extremes:
   - Llama 8B: too weak to generate diverse alternatives (wins 1/3 tasks)
   - Sonnet 4.6: strong enough to self-evaluate, external judges add little
   - **Haiku 3.5: perfect 42/42 Borda sweep** — all refinement baselines degraded its outputs below single-pass

2. **Scope constrains the improvement space.** On unconstrained tasks, Sonnet 4.6's synthesis (AB) dominated and the loop never converged. Scope constraints (fixed facts, word budgets) restored convergence and quality — the same model went from last place to first.

3. **Recovery, not first-attempt improvement.** Autoreason doesn't help models get things right the first time. Its value is in structured analysis of *why* an approach failed, followed by targeted revision. In competitive programming (150 CodeContests problems), this recovery mechanism was statistically significant ($p=0.041$).

4. **CoT judges should be the default.** Adding "think step by step" to the judge prompt reduced convergence passes 3x on Task 1, with no architecture changes.

## Results Summary

| Setting | Autoreason | Best Baseline | Notes |
|---------|-----------|---------------|-------|
| Sonnet 4.6, code (private) | 77% | 73% (single) | +4pp |
| Haiku 3.5, code (private) | 40% | 38% (single) | +2pp; +8pp vs best-of-6 |
| Haiku 3.5, writing | 42/42 | 33.7 (single) | Perfect sweep; baselines degraded |
| Sonnet 4.6, constrained writing | 1st | 2nd | Scope constraint reverses failure |

## Relationship to Autoresearch

[Autoresearch](/autoresearch) uses an objective metric (val_bpb) as the fitness function for iterative ML experimentation. Autoreason replaces the objective metric with a **subjective fitness function constructed through blind evaluation** — the same way science uses peer review where math can use proofs. The three-way A/B/AB tournament is the core extension that makes subjective domains tractable.

## Implementation

The [GitHub repo](https://github.com/NousResearch/autoreason) includes the full paper (autoreason.tex), experiment trajectories, and all prompts. The method is implemented as part of the Hermes Agent codebase.
