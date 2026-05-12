---
title: help.ai — threaded AI step follow-ups
created: 2026-04-16
updated: 2026-04-16
type: concept
tags: [idea, ai-tools]
sources: []
---

# help.ai — Threaded Step Follow-Ups

> Shelled 2026-04-16. UX pattern, not a moat. Money sync — would require venture capital to compete with incumbents who already have context window and user base.

## The Idea

An AI chat platform where each step of a multi-step AI answer gets its own threaded follow-up, instead of everything living in one linear conversation. Recursive threading — sub-steps can also be followed up on.

**Problem it solves:** People ask AI for help, get a multi-step answer, then ask follow-ups on individual steps. This creates context rot — the conversation pollutes the context window with tangential threads about steps 1, 2, 5, 8 while trying to debug step 3.

## Assessment (why shelved)

1. **No moat** — this is a UX pattern, not a defensible product. OpenAI or Anthropic could ship threaded-step follow-ups as a feature toggle tomorrow.
2. **Money sync** — competing requires VC funding. Incumbents already own the context window infrastructure and user base.
3. **Technical ambiguity** — unclear how "steps" are identified. Structured AI output vs. post-processing layer to break apart wall-of-text responses.

## Potential Revisit Conditions

- An incumbent ships this pattern and validates demand (free market research)
- A lightweight browser extension or plugin approach could capture users without building a full platform
- Someone demonstrates that context-window efficiency from threading translates to measurable cost savings

## Related

- [[ai-cost-optimization]] — context rot contributes to wasted tokens
- [[caveman-claude-skill]] — another approach to reducing token waste through compression rather than threading
