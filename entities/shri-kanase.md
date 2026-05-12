---
title: Shri Kanase
created: 2026-04-20
updated: 2026-04-20
type: entity
tags: [person]
sources: [raw/articles/ecomshri-claude-reverse-engineer-ecom-ads-2045564337096737139.md]
---

# Shri Kanase

X creator [@EcomShri](https://x.com/EcomShri). Covers e-commerce competitive intelligence and Google Ads strategy.

## Source

[How to exploit Claude to reverse-engineer any $1M+/month ecom brand's entire Google Ads strategy](https://x.com/EcomShri/status/2045564337096737139) — A guide to using Claude as a competitive intelligence tool for Google Ads, extracting competitor keyword themes, ad copy patterns, Shopping feed structure, and landing page strategies from publicly available data.

## Core Method

The workflow runs in 5 steps:

1. **Pull ads from Google Ads Transparency** (adstransparency.google.com) — grab 8-12 ads mixing text and Shopping
2. **Search incognito as their customer** — 5-8 searches across brand, product, category, and comparison terms
3. **Visit landing pages** — screenshot 2-3 top landing pages and capture headline, pricing, trust signals, CTA
4. **Feed to Claude** — 3 sequential prompts: Ad/Shopping Breakdown → Landing Page Teardown → Full Strategy Synthesis
5. **Extract action items** — top 3-5 moves to implement against competitor

## What the Method Reveals

- Every active ad across search, Shopping, display, YouTube
- Shopping feed structure (titles, images, pricing, product prioritization)
- Ad copy patterns (headlines, descriptions, CTAs, emotional triggers)
- Landing page strategy and conversion elements
- Implied keyword themes

## What It Cannot See

- Exact bids/budgets
- ROAS, CTR, conversion rates
- Precise audience targeting

## Key Claim

"Every competitor spending money on Google Ads is essentially publishing their strategy for anyone who knows how to read it." Run quarterly on top 3-5 competitors to maintain sustained edge.

## Related

- [[hermes-agent]] — used as the analysis engine in this workflow
- [[claude-design-patterns]] — complementary AI design prompting patterns
