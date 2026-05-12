---
title: Vibe Coding
created: 2026-04-11
updated: 2026-04-11
type: concept
tags: [vibe-coding, llm, tools]
sources: []
---

## Overview

Vibe coding is a workflow paradigm where a developer describes what they want in natural language and an AI tool (Claude Code, Cursor, Lovable, v0, Open-Lovable) builds the implementation. The human reviews, iterates, and steers — but does not write code directly.

## Key Distinctions

| Tool | What it produces | Human role |
|------|-----------------|------------|
| [[lovable-dev]] | Full React/web apps | Prompt + review |
| [[open-lovable]] | Open-source alternative to Lovable | Prompt + review |
| Cursor | IDE with AI pair programmer | Pair programming |
| Claude Code | CLI agent for autonomous coding | Orchestration + review |

## Related Concepts

- [[prompt-engineering-patterns]] — the prompting techniques that make vibe coding effective
- [[ai-cost-optimization]] — cost management when running vibe coding at scale
