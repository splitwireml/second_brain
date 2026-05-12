---
title: "buy-or-bounce"
created: 2026-04-27
updated: 2026-04-27
type: entity
tags: [method, ai-skill, sales, conversion, claude-skill]
sources: [raw/articles/xarticle-how-to-find-fix-whats-killing-your-sales-with-the--2047668468904808531.md]
related_entity: [[ole-lehmann]]
---
# buy-or-bounce

Claude skill that simulates 5 different buyer personas reading landing pages, emails, ads, or any sales copy to identify where conversion breaks down.

Built by [[ole-lehmann]] as a free alternative to Shopify's SimGym.

## The 5 Buyer Personas

1. **Shut-up-and-take-my-Money Buyer** — Has the problem, has the money, actively shopping. If they bounce, fundamentals are broken.
2. **Skeptic** — Been burned before. Looking for proof: numbers, case studies, guarantees.
3. **Price-Conscious Buyer** — Doing the math on ROI the entire time. Needs value to clearly exceed cost.
4. **Confused Visitor** — Can't tell what the offer is or if it's for them. Most common and most fixable problem.
5. **Comparison Shopper** — Evaluating alternatives. Asks "Why this and not that?"

## How It Works

1. Paste landing page/email/ad copy
2. Skill parses into sections
3. All 5 buyers walk through narrating their internal monologue section-by-section
4. Outputs: conversion score, friction map, prioritized fixes with specific rewrites

## Origin

Inspired by Shopify's SimGym — which runs hundreds of simulated shoppers through merchant storefronts in real cloud browsers. buy-or-bounce implements the same concept as a Claude skill, running in ~3 minutes for free.

## Related

- [[ole-lehmann]] (author)
- [[buyer-simulation]] (technique/concept)
- [[simgym]] (upstream inspiration)
