---
title: Premortem Claude Prompting
created: 2026-05-03
updated: 2026-05-03
type: concept
tags: [method, agent]
sources: [raw/articles/ole-lehmann-premortem-claude-2026-05-02.md]
author: [[ole-lehmann]]
---

# Premortem Claude Prompting

## Definition

A prompting technique that flips the frame on AI advice by asking an agent to diagnose a future failure rather than evaluate a plan's viability. Instead of "is this a good plan?", the user says "it's 6 months from now and this is already dead — tell me how it died."

The technique is adapted from Daniel Kahneman's pre-mortem concept (from *Thinking, Fast and Slow*), where project leaders imagine a project has already failed and work backward to identify why.

## How It Works

1. User states their plan or decision
2. Prompt: *"it's 6 months from now and this is already dead. tell me how it died."*
3. Claude (or any capable LLM) identifies failure modes — each with a full failure story and early warning signs
4. A synthesis extracts:
   - Most likely failure
   - Most dangerous failure
   - Single biggest hidden assumption
   - Revised plan with gaps closed

## Why It Works

LLMs are trained to be helpful — they find reasons to say yes to plans. A premortem inverts the reward signal: the premise already says the plan failed, so optimism is disabled and the model shifts to adversarial analysis.

## Key Claims (Source)

- Daniel Kahneman (Nobel-winning psychologist behind *Thinking, Fast and Slow*) called it his single most valuable decision-making technique
- Google, Goldman Sachs, and Procter & Gamble all use premortems before major launches
- [[building-effective-agents]] paper from Anthropic touches on related adversarial prompting patterns
- [[ole-lehmann]] published a Claude skill implementing this as a reusable workflow

## Four-Part Synthesis Structure

The output of a good premortem includes:

| Element | Description |
|---------|-------------|
| Failure stories | Each failure mode explained as a narrative with cause and effect |
| Early warning signs | Observable signals that each failure is beginning |
| Hidden assumptions | The single most critical untested assumption |
| Revised plan | Original plan with failure-mode mitigations baked in |

## Relationship to Buy-or-Bounce

Both [[buy-or-bounce]] and premortem are [[ole-lehmann]] prompting methods that flip the model's default optimistic framing. Buy-or-Bounce simulates buyers reviewing copy; premortem simulates future failure reviewing strategy.

## Related Concepts

- [[buy-or-bounce]] — buyer simulation for conversion copy (same author)
- [[buyer-simulation]] — general concept of simulating audiences to stress-test output
- [[prompt-engineering-patterns]] — the broader prompting technique category
- [[vibe-coding-in-production]] — related production deployment anti-pattern framing
- [[building-effective-agents]] — Anthropic's canonical agent design paper
