---
title: Opus 4.7 Prompting Differences from 4.6
created: 2026-04-19
updated: 2026-04-19
type: concept
tags: [llm, reasoning, agent]
sources: [raw/articles/opus-47-prompting-guide-smart-ape-2045070676063649908.md]
author: [[the-smart-ape]]
---

# Opus 4.7 Prompting Differences from 4.6

Opus 4.7 punishes bad prompting more than 4.6 — using 4.6-style prompts produces worse, more expensive results.

## Key Change

Opus 4.7 has a different internal response model vs 4.6. Techniques that worked well on 4.6 can backfire on 4.7.

Specific differences identified by [[the-smart-ape]]:
- 4.7 self-verification behaves differently — outputs that were "good enough" on 4.6 are rejected or degraded
- More expensive per output when used with 4.6-style prompts
- The model is more sensitive to prompt structure and instruction clarity

## Practical Implication

Users migrating from 4.6 need to re-optimize their prompt templates. Old prompts don't transfer directly.

## Related

- [[prompt-engineering-patterns]] — general prompting techniques
- [[rtk-rust-token-killer]] — token reduction for expensive models
- [[caveman-claude-skill]] — output token compression
