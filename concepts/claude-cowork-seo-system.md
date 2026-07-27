---
title: "Claude Cowork SEO System"
created: 2026-03-25
updated: 2026-07-27
type: concept
tags: [tools, agent, local-seo, marketing, monetization]
sources: [raw/articles/bloggersarvesh-chief-of-seo-claude-cowork-2026-03-25.md, raw/articles/bloggersarvesh-claude-cowork-seo-2037158013921042794.md, raw/articles/bloggersarvesh-claude-seo-100k-month-playbook-2032130279494853118.md, raw/articles/alventra-marketing-claude-prompts-2026-07-27.md]
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

## Eight-audit bootstrap sequence (March 2026 follow-up)

A later source from [[bloggersarvesh]] compresses the broader system into eight audits and makes execution order the main operating rule:

1. **Foundation:** GBP category audit, then attributes audit.
2. **Listing:** services-section optimization, then GBP description testing.
3. **Reviews:** competitor review teardown and a response-template system.
4. **Content engine:** GBP posting calendar and photo audit.
5. **Execution:** post consistently, upload photos weekly, and respond to every review.

The source's proposed cadence is week 1 foundation, week 2 listing, week 3 reviews, week 4 content, and week 5 onward execution. It says Claude should gather and structure evidence while a human decides which signals matter commercially and what action to take. ^[raw/articles/bloggersarvesh-claude-seo-100k-month-playbook-2032130279494853118.md]

## Public website extension: 22-prompt library

The public Alventra page publishes a longer version of the system as "Top 22 Claude Prompts For SEO." It preserves the same context-first architecture but makes the interfaces, input files, output formats, and audit thresholds explicit. The page's first 20 prompts map onto the existing table above; prompts 21 and 22 add deep on-page and backlink-gap workflows. ^[raw/articles/alventra-marketing-claude-prompts-2026-07-27.md]

### Context bootstrap and handoffs

Before prompting, the operator loads a folder containing business name, address, phone, website, GBP URL, service areas, target keywords, current GBP details, and one GBP file per competitor. A separate prompt-library file is kept for each SEO task. Claude Cowork uses that context while Chrome/Google Maps and the GBP, SEMrush, Search Console, Ahrefs, Wikidata, Rich Results Test, WordPress, and analytics surfaces supply evidence. The intended output is usually a spreadsheet or prioritized action list, not generic prose. ^[raw/articles/alventra-marketing-claude-prompts-2026-07-27.md]

### Prompt 21 — detailed on-page SEO audit

The site supplies an exact audit prompt for one target URL and keyword. It benchmarks against the top five Google results and requires:

- title under 60 characters, keyword-led with a hook;
- meta description under 155 characters, natural keyword use and CTA;
- short keyword-bearing URL slug, with a redirect/301 decision when wrong;
- exactly one intent-matched H1 and a corrected H2/H3 outline;
- first-100-word, paragraph-length, keyword-usage, entity-coverage, thin-section, fluff, and CTA analysis;
- image counts/alt text/file names, internal and external links, LocalBusiness/Article/FAQ/Breadcrumb/Review schema, Open Graph/Twitter cards, word-count gap, table of contents, and featured-snippet opportunities;
- a scorecard plus a WordPress/Gutenberg fix checklist with exact click paths, copy to paste, time, and High/Medium/Low impact.

The prompt explicitly bans generic advice and tells the agent to report blocked, paywalled, or JavaScript-rendered evidence instead of guessing. ^[raw/articles/alventra-marketing-claude-prompts-2026-07-27.md]

### Prompt 22 — backlink-gap audit

The site also supplies an Ahrefs workflow for estimating the page-level referring-domain target for a keyword. It starts in Ahrefs Keywords Explorer with country set to the United States, records KD, US/global volume, traffic potential, and the top 10 organic SERP rows, then drills into five normal competitor pages. Each backlink report is scoped to Exact URL and filtered to dofollow, one link per domain, English, all platforms, sorted by DR. ^[raw/articles/alventra-marketing-claude-prompts-2026-07-27.md]

The required analysis captures referring-page URL, domain, DR, anchor text, first-seen date, link type, page backlinks, page-level referring domains, and organic traffic. It buckets referring domains into DR 70+, 50–69, 30–49, and 0–29; reports mean and median referring domains; sets a target from the median plus a 10–15% buffer; checks PBN/paid-link/expired-domain patterns; and returns the 15 domains linking to at least two competitors. The prompt also specifies 3–5 second pacing between competitor drill-downs, a 60-second retry after rate limits, no CSV exports unless requested, screenshots per competitor, and stop conditions for fewer than five usable results, KD above 80, or structurally uncompetitive branded SERPs. ^[raw/articles/alventra-marketing-claude-prompts-2026-07-27.md]

### Version drift

The X Article labels the stack a 20-part system, while the public page labels it 22 prompts. The website's later 12-week usage order still enumerates prompts 1–20 and does not place prompts 21–22, so the expanded count is confirmed as a source version but its execution placement remains unspecified. The page's ranking, speed, review-effect, and revenue outcomes are source claims, not independently verified results. ^[raw/articles/alventra-marketing-claude-prompts-2026-07-27.md]

## Evidence and caveats

- **Source-confirmed:** the article contains the eight prompts, their ordering, example Chrome/GBP research instructions, and the weekly rollout.
- **Likely:** sequencing foundational profile data before ongoing content is a sensible operational simplification of the larger 20-prompt system.
- **Unverified source claims:** $100k/month in 90 days, ranking changes within days, review-response ranking effects, photo performance percentages, and hundreds of thousands in client revenue. These are not treated as established results here.

## Related Concepts

- [[prompt-engineering-patterns]] — general prompt templates; this is a domain-specific SEO variant
- [[paperclip-orchestrator]] — AI agents managing multi-brand workflows; similar orchestration concept but different domain
- [[ai-freelancer-200-hour-guide]] — selling AI services at $200/hr; this system is a concrete offering in that model
- [[company-naming-playbook]] — brand/naming strategy; GBP description optimization is local-brand-adjacent
- [[claude-cowork]] — the Chrome extension tool this runs inside
- [[claude-cowork-b2b-lead-scraping]] — different use case of the same Claude Cowork tool for B2B lead generation
