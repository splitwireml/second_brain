---
title: Triverra
created: 2026-07-20
updated: 2026-07-20
type: entity
tags: [brand, product, ai-tools, ai-agent, website]
sources: [raw/articles/triverra-ai-travel-companion-hero-prompt.md]
---

# Triverra

Triverra is a source-provided AI travel companion brand represented by a full-viewport React/Tailwind landing-hero specification. The prompt positions the product as creating travel plans tailored to a user's preferences, budget, and pace. The requested UI copy includes “8370+ trips planned” and a “4.9” rating; these are prompt-specified marketing claims, not independently verified product facts.

## Landing hero specification

- Slow-motion looping travel video background at `0.8x` playback and `1.02` scale.
- Floating glassmorphic navbar with desktop navigation, register CTA, shared-layout active dot, and a mobile drawer.
- Centered headline: “Dream deeper. Travel farther.”
- Primary and secondary CTAs with masked vertical text swaps and dual-arrow cross-fades.
- Ambient motion across the content column, plus staggered entrance animations.
- Responsive breakpoints for desktop, tablet, and mobile layouts.

## Implementation constraints

The source requires a self-contained client component using React, `framer-motion`, `lucide-react`, Tailwind CSS, and the Gantari font. It explicitly protects existing sections, requires rendering the new section after them, preserves exact arrow-color filters, and forbids global resets or font changes outside the section.

The asset URLs in the supplied text are truncated placeholders (`…`), so the source is a design/implementation brief rather than a directly runnable artifact. ^[raw/articles/triverra-ai-travel-companion-hero-prompt.md]

## Related

- [[ai-travel-companion-landing-hero]] — concept distilled from the brief
- [[ai-cinematic-website-design]] — adjacent premium motion-heavy web pattern
- [[landing-page-ai-workflow]] — specificity-first AI landing-page prompting
- [[ui-design]] — interface and interaction-design context
