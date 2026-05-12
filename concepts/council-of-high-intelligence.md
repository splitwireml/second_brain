---
title: Council of High Intelligence
created: 2026-04-17
updated: 2026-04-17
type: concept
tags: [ai-tools, agent, orchestration, reasoning, claude-code]
sources: [raw/articles/nyk-builderz-council-high-intelligence-2026-04-17.md]
related_entity: [[nyk-builderz]]
author: [[nyk-builderz]]
---

# Council of High Intelligence

Multi-agent deliberation framework that forces multiple AI personas to disagree through structured rounds before reaching consensus. Built for Claude Code as a skill/package. 157 GitHub stars (as of 2026-04-17). CC0 licensed.

GitHub: github.com/0xNyk/council-of-high-intelligence

## What It Is

Single-agent LLMs simulate one coherent viewpoint per generation — even well-structured prompts produce one reasoning tradition dressed up as balance. The Council externalizes disagreement by spawning 11 independent Claude Code subagents, each with a distinct analytical method and explicitly declared blind spots, coordinated by a central protocol enforcer.

## Architecture

### 11 Personas (Historical Thinkers)

| Persona | Model | Method | Blind Spot |
|---------|-------|--------|------------|
| Socrates | Opus | Assumption destruction | Infinite questioning loops |
| Aristotle | Opus | Categorization & structure | Over-classifies |
| Marcus Aurelius | Opus | Moral clarity, control/distinction | Over-internalizes |
| Lao Tzu | Opus | Non-action & emergence | Dismissive of direct intervention |
| Alan Watts | Opus | Perspective dissolution | No actionable output |
| Feynman | Sonnet | First-principles debugging | Ignores social/incentive factors |
| Sun Tzu | Sonnet | Adversarial strategy | Over-focuses on competition |
| Ada Lovelace | Sonnet | Formal systems | Rigid to human messiness |
| Machiavelli | Sonnet | Power dynamics | Cynical to cooperative solutions |
| Linus Torvalds | Sonnet | Pragmatic engineering | Dismisses theoretical elegance |
| Miyamoto Musashi | Sonnet | Strategic timing | Waits too long to act |

Model split: **Opus** (depth-heavy, 5 members) and **Sonnet** (speed-critical, 6 members).

### 6 Polarity Pairs

Each pair is a structural counterweight — when one is selected, its opponent must be considered:

1. **Socrates vs Feynman** — top-down destruction vs bottom-up rebuilding
2. **Aristotle vs Lao Tzu** — categories vs emergence
3. **Sun Tzu vs Aurelius** — external game vs internal governance
4. **Ada vs Machiavelli** — formal purity vs human incentives
5. **Torvalds vs Watts** — ship it vs question the framing
6. **Musashi vs Torvalds** — perfect moment vs immediate shipping

### 3-Round Deliberation Protocol

1. **Round 1** — Parallel independent analysis (400 words max per member). Each produces: essential question, domain analysis, verdict, confidence, self-critique.
2. **Round 2** — Cross-examination (300 words max). Each member must engage at least 2 others by name, answering: who they disagree with and why; which insight strengthens their position; what changed their view; restate final position.
3. **Round 3** — Synthesis (100 words max per member). Crystallization only — no new arguments.

### Anti-Recursion Rules

Socrates can loop indefinitely. Three enforcement mechanisms:
- **Hemlock rule**: If Socrates re-asks a question already answered with evidence, coordinator forces a 50-word position statement
- **3-level depth limit**: After 3 levels of questioning, Socrates must state a position
- **2-message cutoff**: Any pair exceeding 2 messages is cut off and forced to Round 3

### Decision Rules

- 2/3 majority = consensus; dissent recorded in Minority Report
- No majority = dilemma presented to user with each position stated
- Domain expert weighting: 1.5x for the member whose domain most directly matches the problem

## Pre-Built Domain Triads

| Domain | Triad | Tension |
|--------|-------|---------|
| architecture | Aristotle + Ada + Feynman | classify → formalize → simplicity-test |
| strategy | Sun Tzu + Machiavelli + Aurelius | terrain → incentives → moral grounding |
| ethics | Aurelius + Socrates + Lao Tzu | duty → questioning → natural order |
| debugging | Feynman + Socrates + Ada | bottom-up → assumptions → formal verify |
| innovation | Ada + Lao Tzu + Aristotle | abstraction → emergence → classification |
| conflict | Socrates + Machiavelli + Aurelius | expose → predict → ground |
| complexity | Lao Tzu + Aristotle + Ada | emergence → categories → formalism |
| risk | Sun Tzu + Aurelius + Feynman | threats → resilience → empirical verify |
| shipping | Torvalds + Musashi + Feynman | pragmatism → timing → first-principles |
| product | Torvalds + Machiavelli + Watts | ship it → incentives → reframing |
| founder | Musashi + Sun Tzu + Torvalds | timing → terrain → engineering reality |

## Invocation

```bash
/council --triad architecture "should we split the monolith now or after Series B?"
/council --full "is this acquisition worth pursuing at 8x revenue?"
/council --members socrates,feynman,ada "why does our cache invalidation keep failing?"
```

Requires Claude Code CLI with agent subagent support.

## When to Use

**Use for**: complex decisions with real trade-offs — architecture choices, strategic pivots, build-vs-buy, pricing models.

**Don't use for**: questions with clear correct answers, or when a triad covers the domain. 11 members consume significant context and API cost.

## Related Concepts

- [[autoreason]] — Nous Research multi-agent tournament method; related approach to structured agent deliberation
- [[agent-teams]] — Multi-agent collaboration paradigm; relevant to council's multi-agent orchestration approach
