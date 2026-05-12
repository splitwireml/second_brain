---
title: "Claude Cowork SEO System"
created: 2026-03-25
updated: 2026-03-25
type: concept
tags: [marketing, agent, tools, monetization]
sources: [raw/articles/bloggersarvesh-chief-of-seo-claude-cowork-2026-03-25.md]
---

# Claude Cowork SEO System

## Overview

A 20-prompt system built inside [[claude-cowork]] (Chrome extension) that automates a complete local SEO audit for home services businesses. Created by [[bloggersarvesh]] and offered as a service through [[alventra-marketing]].

## Core Thesis

The key differentiator is **business context loading** — feeding Claude a permanent file with the business's NAP data, competitor GBP URLs, target keywords, and service areas *once*, so every subsequent prompt operates from real data instead of generic advice.

Without context loading: prompts return generic, unhelpful output.
With context loading: every prompt feels written specifically for that business.

## Architecture

### Pre-work: Context File
A single file per business containing:
- Business name, address, phone, website, GBP URL
- Service areas (5 cities), target keywords
- Current Google standings (reviews, GBP views, map pack status)
- 3 competitors with GBP URLs
- SEO history (what's been tried)

This file is referenced by every subsequent prompt.

### Part 1: GBP Audit (Prompts 1–8)

| # | Prompt | What it does |
|---|--------|-------------|
| 1 | GBP category audit | Map pack competitor category analysis |
| 2 | GBP attributes audit | Attribute gaps vs competitors |
| 3 | Competitor review teardown | Velocity, sentiment, keyword patterns |
| 4 | Review response strategy | Template system with keyword-rich responses |
| 5 | GBP posts strategy | 8-week content calendar |
| 6 | Services section optimization | Keyword-rich descriptions |
| 7 | GBP description optimization | 3 versions (ranking/conversion/balanced) |
| 8 | GBP photo audit | Photo types, upload cadence |

### Part 2: Website (Prompts 9–13)

| # | Prompt | What it does |
|---|--------|-------------|
| 9 | Keyword gap analysis | GSC data, page 2 opportunities |
| 10 | Money page audit | Ranking page optimization |
| 11 | Service + city page builder | Location-specific page generator |
| 12 | Google Search Console analysis | Page 2 keyword sprint (30-day) |
| 13 | Review sentiment analysis | Emotional language extraction for copy |

### Part 3: Backlinks + Authority (Prompts 14–16)

| # | Prompt | What it does |
|---|--------|-------------|
| 14 | Competitor backlink audit | Authority link mapping via Ahrefs |
| 15 | Local citation audit | NAP consistency across directories |
| 16 | Local search intent mapping | Keyword stage categorization (4 stages) |

### Part 4: Content + Tracking (Prompts 17–20)

| # | Prompt | What it does |
|---|--------|-------------|
| 17 | Content gap analysis | SEMrush Content Gap tool |
| 18 | Entity optimisation | Google Knowledge Graph / schema markup |
| 19 | Competitor GBP posting pattern analysis | Forensic posting cadence analysis |
| 20 | Monthly SEO performance report | 5-minute executive summary |

## Key Insights

1. **Context loading is the moat** — the setup file is what separates this from pasting prompts blindly
2. **Review velocity > review count** — a business getting 15/month beats one with 200 total but no new reviews
3. **Page 2 keywords are the cheapest wins** — positions 11–20 need one title tag change to break through
4. **GBP posting is asymmetric** — most competitors post inconsistently; consistent posting immediately differentiates
5. **Entity optimization compounds** — Knowledge Panel, schema markup, and entity signals age well and are resilient to algorithm updates

## 90-Day Rollout Plan

| Weeks | Focus |
|-------|-------|
| 1–2 | Context loading + GBP categories + attributes |
| 3–4 | Reviews + GBP posts + response templates |
| 5–8 | Services, description, photos + website page audit |
| 9–12 | Backlinks + citations + search intent + content gaps |

## Related Concepts

- [[prompt-engineering-patterns]] — general prompt templates; this is a domain-specific SEO variant
- [[paperclip-orchestrator]] — AI agents managing multi-brand workflows; similar orchestration concept but different domain
- [[ai-freelancer-200-hour-guide]] — selling AI services at $200/hr; this system is a concrete offering in that model
- [[company-naming-playbook]] — brand/naming strategy; GBP description optimization is local-brand-adjacent
- [[claude-cowork]] — the Chrome extension tool this runs inside
- [[claude-cowork-b2b-lead-scraping]] — different use case of the same Claude Cowork tool for B2B lead generation
