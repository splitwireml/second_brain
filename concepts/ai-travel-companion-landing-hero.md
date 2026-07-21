---
title: AI Travel Companion Landing Hero
created: 2026-07-20
updated: 2026-07-20
type: concept
tags: [ai-tools, ai-agent, design, ui-design, website, landing-page, animated-websites, framer-motion, conversion, ai-design]
sources: [raw/articles/triverra-ai-travel-companion-hero-prompt.md]
related_entity: [[triverra]]
---

# AI Travel Companion Landing Hero

An AI travel companion landing-hero pattern that combines a full-viewport cinematic video, glassmorphic navigation, concise travel positioning, and interaction-heavy CTAs. The [[triverra]] brief is the source example; it specifies implementation values rather than reporting an observed or tested build.

## Pattern components

1. **Atmosphere:** dark looping travel video, slowed to `0.8x`, with a subtle scale-up and white type.
2. **Navigation:** responsive glass pill on desktop, a backdrop-blurred drawer on mobile, and a shared-layout active-state dot.
3. **Hierarchy:** a supporting AI-travel badge, two-line editorial headline, two CTAs, social proof, and a short explanatory footer.
4. **Micro-interactions:** staggered fade-up entrances, ambient whole-column float, masked duplicate-label text swap, and dual-arrow cross-fade.
5. **Constraint density:** exact Tailwind values, easing curves, breakpoints, CSS filters, asset referrer policy, and build-safety rules are supplied so a coding agent has less visual ambiguity.

## Evidence and limits

**Confirmed from the supplied brief:** the requested stack is React, framer-motion, lucide-react, and Tailwind CSS; the hero is responsive; the video playback rate, typography, CTA effects, and integration safeguards are explicitly specified. ^[raw/articles/triverra-ai-travel-companion-hero-prompt.md]

**Not established by the source:** whether Triverra exists as a deployed product, whether the listed trip/rating figures are true, whether the assets resolve, and whether the component has been built or verified. The source includes truncated asset URLs, so implementation still requires real asset values and runtime checks.

## Design implication

This is a concrete example of the specificity principle in [[prompt-engineering-patterns]]: the prompt describes behavior, values, responsive states, and integration boundaries instead of asking for a generic “premium” hero. It sits at the intersection of [[ai-cinematic-website-design]] and [[landing-page-ai-workflow]].

## Related

- [[triverra]]
- [[ai-cinematic-website-design]]
- [[landing-page-ai-workflow]]
- [[above-the-fold-design]]
- [[prompt-engineering-patterns]]
- [[ui-design]]
