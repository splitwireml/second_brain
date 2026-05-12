---
title: ai-design-workflow
created: 2026-04-30
updated: 2026-04-30
type: concept
tags: [ai-design, design, workflow, agent, brand, content]
sources: [raw/articles/claude-design-brand-workflow-nateherk-2026-04-30.md]
related_entity: [[claude-design]]
author: [[nate-herk]]
---

# AI Design Workflow

End-to-end brand-building pipeline: brainstorm in Claude chat → execute in [[claude-design]] → ship via [[claude-code]] + Vercel. Author: [[nate-herk]].

## Three-Surface Pipeline

1. **Plan in chat** — Regular Claude.ai for mission, audience, color palette, typography, logo concepts, voice and tone. Produces a markdown spec before opening Design. Keeps Design sessions for execution only.
2. **Execute in Design** — Build from locked design system: pitch decks, landing pages, mobile app prototypes, brand guidelines docs, animated videos. Uses all three editing surfaces (edit tool, draw tool, tweaks panel) to minimize prompting.
3. **Ship from Code** — Export zip → drop into [[claude-code]] → push to GitHub → connect Vercel → deploy in 60 seconds.

## Design System as Glue

A [[claude-design]] design system holds colors, typography hierarchy, spacing rules, button styles, hover states, badges, tags, cards, input fields, and icon set. The Design.md spec becomes the source of truth for every downstream asset. On team plans it shares across the org.

Inputs can be: URL + GitHub repo (scrapes brand DNA), or for new brands: logo PNG + markdown concept doc + button feel notes.

The verifier agent self-checks renders and fixes issues before the user sees them — the killer feature of [[claude-design]].

## Quota Management

- Weekly limits are separate from regular Claude and Claude Code usage
- Brainstorming in Design burns session unnecessarily — plan first in chat
- Edit in canvas (click, draw, tweaks panel) uses zero prompting budget
- Switch to Sonnet 4.6 for tweaks; reserve Opus 4.7 for planning
- Export to [[claude-code]] when quota hits; progress transfers as a zip
- Design systems from full GitHub repos consume far more tokens than logo + markdown spec

## Deliverables in One Pipeline

1. Investor pitch deck (slide deck mode + brand markdown + chat outline)
2. Landing page (high-fidelity, skipped wireframes — knew layout already)
3. Brand guidelines doc (two minutes from design system)
4. Mobile app prototype (multiple screens, dark mode, straight to high-fidelity)
5. Launch video (HyperFrames skill for motion graphics and scene transitions)

All outputs land in the same visual world because they all pull from one design system.

## Related Entities

- [[claude-design]] — The design execution surface; canvas-based GUI with verifier agent
- [[nate-herk]] — Author; documented the full Tally brand build
- [[claude-code]] — The code execution surface; receives Design exports and deploys to Vercel

## Related Concepts

- [[landing-page-ai-workflow]] — Overlapping theme: AI-driven landing page creation with vibe-coding principles and design-to-code handoff
- [[vibe-coding-in-production]] — Eric Mishra's framework for responsible vibe coding; overlaps on design agent workflows