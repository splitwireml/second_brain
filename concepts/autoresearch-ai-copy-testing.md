---
title: Autoresearch — AI-Powered Copy Testing System
created: 2026-04-12
updated: 2026-04-13
type: concept
tags: [marketing, method, monetization]
sources: [raw/articles/ericosiu-autoresearch-ai-copy-testing-2026-04-12.md]
related_entity: [[autoresearch]]
---

**Core method:** [[autoresearch]] — AI copy testing loop adapted from Karpathy's autonomous ML experiments.

# Autoresearch — AI Copy Testing

## Overview

Autoresearch is an AI-driven copywriting optimization system that generates, scores, and evolves 50+ content variants in minutes using a simulated expert panel — without live traffic. It adapts Andrej Karpathy's autonomous ML experiment loop (propose → run → measure → decide → repeat) to marketing copy: landing pages, email sequences, ad creative, and form pages.

The system has two phases:

1. **Autoresearch (pre-launch):** Generate 50+ variants → score with expert panel → evolve winners → ship at 85+ score
2. **Autogrowth (post-launch):** Take winner as control → generate 3-5 mutations → split real traffic → measure conversions → promote real winners, kill real losers → repeat weekly

## Core Mechanism: Simulated Expert Panel

Each variant is scored by a 5-person simulated expert panel, each with a distinct viewpoint and scoring rubric:

| Expert | Lens | Question |
|--------|------|----------|
| CMO at $50M B2B | Stopping scroll | "Would this make me stop scrolling?" |
| Skeptical founder | Credibility | "Do I believe this?" |
| Conversion rate optimizer | Clarity | "Is this clear and action-driving?" |
| Senior copywriter | Differentiation | "Is this compelling and differentiated?" |
| ROI-obsessed CEO | Decision | "Would I put this on my site?" |

Each scores 0-100. The average is the variant's panel score. Results are decisive: original headlines scoring 61.6 placed dead last against alternatives scoring 89.8.

## The Evolution Loop

```
Round 1: Generate 10 variants → Expert panel → Top 3 advance
Round 2: Cross-breed top 3 → 15 combinations → Score → Top 5 advance
Round 3–N: Evolve top performers → Score → Repeat
```

Six rounds on a landing page hero section: 51 variants, score 62 → 87 in 8 minutes. 54 variants across 7 rounds on a form page: score 57 → 86.

## Key Findings from Form Optimization

- **Phone number field position:** Moving from position 3 to 8 improved completion likelihood score by 27 points. Early phone fields create friction; late phone fields feel like a small addition after 7-field investment.
- **CTA specificity:** "Get Started" scored 14 points lower than "Book My Free Strategy Call." Specificity about what happens next wins.
- **Thank-you copy:** "Your request has been received... 1-2 business days" scored 25 points lower than "Done. Our team reviews every submission personally. Expect a direct reply within 1 business day, not a nurture sequence." The phrase "not a nurture sequence" resonates strongly.

## Five Primary Use Cases

1. **Landing pages** — Headlines, CTAs, subheadlines, problem statements
2. **Cold email campaigns** — Subject lines, opening lines; kill losers on day 3 with real open/reply data
3. **Ad creative** — Generate 20+ variants, panel-score, deploy top 5 to Meta/LinkedIn, let the platform algorithm validate
4. **Content hooks** — Score X post hooks before publishing; 65 vs 90 panel score = 2,000 vs 200,000 impressions
5. **Pricing and positioning** — Test "$10K/month" vs "less than one junior hire" vs "starting at $333/day" framing

## Economics

- ~$2 in API calls per full run
- 8 minutes of compute time
- Zero designer or developer time
- Zero waiting for traffic

Compared to traditional A/B: 2 weeks of live traffic with 50% of visitors on the losing variant.

## Relationship to Karpathy's Autoresearch

Andrej Karpathy published a 630-line Python script (March 2026) that autonomously ran 50 ML experiments overnight — no human intervention. The pattern is identical: propose a change, run the experiment, measure the result, decide what to try next. Autoresearch for copy applies this same loop to conversion copy instead of model weights.

## Related Concepts

- [[prompt-engineering-patterns]] — The prompt templates used to generate variants and drive expert panel scoring
- [[hermes-agent-market-claims]] — Marketing claims analysis; relates to AI-generated copy credibility
- [[ai-workflow-setup-service]] — Selling AI automation workflows; autoresearch is a deliverable within this service
- [[ai-freelancer-200-hour-guide]] — Monetization context; copy testing as a $200/hr freelance offering
- [[company-naming-playbook]] — Brand/copy framing techniques; complementary to variant generation
- [[ai-job-search-automation]] — Same autonomous loop pattern applied to job search; parallel implementation of the propose→score→evolve→decide cycle

## Sources

- `raw/articles/ericosiu-autoresearch-ai-copy-testing-2026-04-12.md`
