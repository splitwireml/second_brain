---
title: "buyer-simulation"
created: 2026-04-27
updated: 2026-04-27
type: concept
tags: [marketing, conversion, sales, buyer-persona, testing]
sources: [raw/articles/xarticle-how-to-find-fix-whats-killing-your-sales-with-the--2047668468904808531.md]
related_entity: [[ole-lehmann]]
author: [[ole-lehmann]]
---
# buyer-simulation

Technique of simulating buyer personas reviewing sales copy (landing pages, emails, ads) to identify where conversion breaks down.

## Concept

Instead of A/B testing (which takes weeks and requires significant traffic), buyer simulation uses AI to model how different buyer types react to each section of sales copy. Each persona represents a distinct reason people don't convert:

- **Broken fundamentals** — Shut-up-and-take-my-Money Buyer bounces
- **Missing credibility** — Skeptic needs proof
- **Weak value justification** — Price-Conscious Buyer can't see ROI
- **Unclear positioning** — Confused Visitor doesn't understand the offer
- **No differentiation** — Comparison Shopper asks "why not alternatives?"

## Section-by-Section Analysis

The key differentiator is that buyers narrate their internal monologue *at each section*, revealing the exact moment interest dies. When 3/5 buyers bounce at the same section, that's the primary leak.

## Implementation

[[buy-or-bounce]] is a concrete implementation by [[ole-lehmann]] as a Claude skill. The upstream inspiration is [[simgym]] by Shopify.

## Related

- [[buy-or-bounce]] (implementation)
- [[simgym]] (inspiration)
- [[ole-lehmann]] (author)
