---
title: Website Cloning
created: 2026-05-10
updated: 2026-05-10
type: concept
tags: [tools, workflow, ai, design]
sources: [raw/articles/recreate-website-2053516030098452858.md]
related_entity: [[voxyz_ai]]
author: [[voxyz_ai]]
---

# Website Cloning

Website cloning is the practice of taking an existing website's design structure as a skeleton and rebuilding it with your own content. The key insight is not to copy directly but to use the skeleton framework and inject your own content.

## The Pipeline

From [[voxyz_ai]]'s method:

1. **GPT Images 2** — generate concept art to lock visual direction fast
2. **Tripo API** — 3D model generation (600 free credits on signup)
3. **Gemini (AI Studio)** — reference image + video → website prototype in one shot
4. **Claude + Codex** — design review, detail polish, API integration

## Base Layer Theory

Once you have a base with clear UI/UX direction, any subsequent model respects that visual direction automatically. Colors stay locked, layout holds, style doesn't drift.

Without a base, going straight to Claude or Codex from scratch results in clashing styles because each model improvises.

## Gemini's Role

Gemini's strength is visual perception (accepts video input, not just images), not coding ability. The workflow:
- Visual in, visual out — lay the base
- Max 2 refinement rounds, then export code
- Switch to Claude/Codex for detail polish

## The Flow

1. Decide what your business needs to display (content first, then find skeleton)
2. Find a design you like and deconstruct it
3. Generate concept art with GPT Images to lock direction
4. One shot through Gemini for website base
5. Max 2 refinement rounds, then switch models

## Key Prompt Pattern

> "Image is the single source of truth for visuals. Video is the single source of truth for interactions. Don't invent anything outside these two references."

## Related Concepts

- [[ai-design-pipeline]] — broader AI-driven design pipeline
- [[vibe-coding]] — the broader paradigm
- [[gemini]] (Google AI Studio) — used for visual base creation via video + image input
- [[claude-code]] — used for final polish and deployment
