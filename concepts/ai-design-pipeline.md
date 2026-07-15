---
title: AI Design Pipeline
created: 2026-05-10
updated: 2026-05-10
type: concept
tags: [tools, workflow, ai, design]
sources: [raw/articles/recreate-website-2053516030098452858.md]
related_entity: [[voxyz_ai]]
author: [[voxyz_ai]]
---

# AI Design Pipeline

An AI design pipeline uses multiple AI models in sequence, each playing to its strengths, to go from concept to deployed website or application.

## The Multi-Model Pipeline Pattern

From [[voxyz_ai]]'s website cloning method:

| Stage | Model | Strength | Weakness |
|-------|-------|----------|----------|
| Concept art | GPT Images 2 | Rapid visual direction | N/A |
| Base website | Gemini 3.1 Pro | Visual perception (video + image input) | Coding ability degrades after 2 rounds |
| Polish | Claude + Codex | Code quality, design refinement | N/A |

## Base Layer Theory

The core insight: lock visual direction early with a "base" that subsequent models respect. Without this, each model improvises independently, resulting in clashing styles.

```
Base layer (Gemini) → locks colors, layout, typography
Polish layer (Claude/Codex) → refines details within locked direction
```

## Two-Round Ceiling

Gemini's coding ability degrades after approximately two refinement rounds. The workflow is:
1. One shot for base
2. Max 2 focused refinement rounds
3. Export and switch to Claude/Codex for all further work

## Related Concepts

- [[website-cloning]] — the specific application of this pipeline
- [[vibe-coding]] — the broader paradigm
- gemini (Google AI Studio) — the base layer model, accepts video + image for visual fidelity
- [[claude-code]] — the polish layer
- [[ai-design-workflow]] — overlapping concept with different emphasis
