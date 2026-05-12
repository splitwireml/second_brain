---
title: Three-Way Tournament Self-Refinement
created: 2026-04-14
updated: 2026-04-14
type: concept
tags: [method, llm, agent]
sources: [raw/papers/autoreason.tex]
related_entity: [[autoreason]]
author: [[shl0ms]]
---

# Three-Way Tournament Self-Refinement

The core architectural pattern in [autoreason](/autoreason): instead of a linear critique-and-revise loop, each iteration produces three competing candidates evaluated by a blind panel. "Do nothing" (keeping the incumbent) is a first-class option alongside adversarial revision and synthesis.

## The Three Candidates

**A (incumbent)** — the current document as-is. Preserves what works. Anchors the evaluation.

**B (adversarial revision)** — a fresh agent revises A based on a separate critic's findings. The critic identifies problems only; the revision agent fixes them. No drafting history prevents [authorship bias](https://en.wikipedia.org/wiki/Confirmation_bias).

**AB (synthesis)** — a third fresh agent receives A and B with randomized labels and produces a merge, taking the strongest elements of each. Randomized labeling prevents the synthesizer from favoring A or B by position.

## Why Three Candidates?

A two-way A vs B tournament would work, but B tends to be too adversarial — it removes too much and judges prefer the incumbent by default, causing premature convergence. AB provides a middle path: the synthesizer can preserve A's strengths while incorporating B's corrections. Both B and AB are necessary; removing either collapses the tournament to trivial incumbency (see [component ablation in autoreason](/autoreason#component-ablation)).

The three-way structure also prevents [sycophancy](https://en.wikipedia.org/wiki/Social_desirability_bias): if the judge only sees A and B, and both were produced by the same system with similar biases, the comparison is uninformative. Adding AB creates genuine three-way competition.

## Blind Evaluation via Borda Count

Judges receive A, AB, B with randomized labels and rank them: 3 points for first, 2 for second, 1 for third. [Borda count](https://en.wikipedia.org/wiki/Borda_count) over 3 judges (6 total points available) gives finer-grained preferences than majority vote, which would produce frequent three-way ties.

Conservative tiebreak: the incumbent (A) wins ties. This is load-bearing — without it, A would win fewer ties and the loop would be less stable.

## Fresh Isolated Agents Per Role

Every role (critic, author B, synthesizer, each judge) is a fresh agent with no shared context. This is critical for preventing:

- **Authorship bias**: an agent that wrote A will defend it even while "incorporating feedback"
- **Prompt bias contamination**: judges that saw the critique prompt would be primed to find problems
- **Session context drift**: accumulated context that primes future passes in unintended directions

## Convergence Criterion

The incumbent survives $k=2$ consecutive passes. $k=1$ terminates prematurely (94% of runs saw subsequent displacement in early experiments). $k=3$ fails to converge on 24% of trajectories at 2x cost. Empirically, Elo ratings plateau by pass 5-10 regardless.

## Relationship to Other Concepts

- Extends [Karpathy's autoresearch](/autoresearch) — replaces objective val_bpb fitness function with subjective Borda-based evaluation
- Addresses [LLM self-correction unreliability](/huang2023) (Huang et al. 2023) — external judges provide the feedback that self-correction lacks
- Related to [LLM-as-Judge](/zheng2023) literature — fresh isolated agents mitigate position bias and self-preference bias
- The bloat/prune oscillation is a signal of [scope underdetermination](https://en.wikipedia.org/wiki/Underdetermined_system) — when the task doesn't specify desired output scope, the loop oscillates between "comprehensive" (AB adds detail) and "focused" (B strips back)
