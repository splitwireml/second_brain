---
title: The HIVE Claude Code Architecture
created: 2026-06-11
updated: 2026-06-11
type: concept
tags: [claude-code, workflow, orchestration, subagents, agent]
sources: [raw/articles/xarticle-the-ai-agent-stack-the-creator-of-claude-code-uses-2064292484856041558.md]
related_entity: [[claude-code]]
author: [[av1dlive]]
---

# The HIVE Claude Code Architecture

A reconstructed operating model for Claude Code built around three composable layers: local loops, cloud routines, and parallel swarms.

## Three tiers

1. **Local loops** — live-session `/loop` jobs for continuous daytime work.
2. **Routines** — `/schedule`-driven durable jobs in Anthropic's cloud for overnight or off-laptop execution.
3. **Swarms** — `/batch` plus dynamic workflows for large one-shot fan-out across many subagents.

The article's point is not that any one primitive is novel on its own, but that the real system emerges when the three are composed into one architecture.

## Operational details worth keeping

The source highlights Boris Cherny's public framing that "my job is to write loops" and turns that into a reproducible builder's guide: custom `.claude/loop.md` behavior, reusable slash commands, recurring maintenance loops for PRs and issue triage, and an overnight layer that keeps work progressing when the operator is away.

## Why this concept matters

This is a useful bridge between simple single-session prompting and full autonomous-agent mythology. It translates Claude Code features into an actual operating cadence with boundaries, persistence windows, and scale-up paths.

## Related

- [[claude-code]]
- [[dynamic-workflows-in-claude-code]]
- [[agent-swarm]]
