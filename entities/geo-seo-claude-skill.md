---
title: geo-seo-claude-skill
created: 2026-04-14
updated: 2026-04-14
type: entity
tags: [seo, ai-tools, agent]
sources: [raw/articles/zubair-trabzada-geo-seo-claude-2026-04-14.md]
related_entity: [[zubair-trabzada]]
---

A Claude Code skill (6,019 stars, MIT) that optimizes websites for AI-powered search engines — ChatGPT, Claude, Perplexity, Gemini, and Google AI Overviews — while maintaining traditional SEO foundations. GEO-first, SEO-supported.

## Architecture

- 13 sub-skills under `skills/` covering: audit, citability, crawlers, llms.txt, brand mentions, platform optimization, schema, technical SEO, content E-E-A-T, reports, prospect CRM, proposals, and monthly delta tracking
- 5 parallel subagents under `agents/` for simultaneous multi-dimensional analysis
- Python scripts for scoring, scanning, and PDF generation
- JSON-LD schema templates for organization, local business, article/author, software/SaaS, product, and website searchaction

## Key Claims

| Metric | Value |
|--------|-------|
| GEO services market | $850M+ (projected $7.3B by 2031) |
| AI-referred traffic growth | +527% year-over-year |
| AI traffic conversion rate vs organic | 4.4x higher |
| Gartner: search traffic drop by 2028 | -50% |
| Brand mentions vs backlinks for AI | 3x stronger correlation |
| Marketers investing in GEO | Only 23% |

## Citability Scoring

Optimal AI-cited passages are 134–167 words, self-contained, fact-rich, and directly answer questions. This is a concrete content-length heuristic that differs from traditional SEO word-count thinking.

## GEO Score Weights

| Category | Weight |
|----------|--------|
| AI Citability & Visibility | 25% |
| Brand Authority Signals | 20% |
| Content Quality & E-E-A-T | 20% |
| Technical Foundations | 15% |
| Structured Data | 10% |
| Platform Optimization | 10% |

## Relationship to Existing Wiki Pages

- [[llm-seo]] — Both target AI-mediated discovery; GEO-SEO-Claude is a concrete tool for execution while llm-seo is the broader strategic layer
- [[topical-authority-seo]] — E-E-A-T signal generation in the GEO-SEO tool maps to topical authority building
- [[programmatic-seo]] — Different focus: geo-seo-claude targets citation-readiness per page, not page volume at scale
- [[prompt-engineering-patterns]] — Content optimization heuristics in geo-seo-claude overlap with content-writing prompt patterns
