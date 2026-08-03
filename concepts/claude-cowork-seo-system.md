---
title: "Claude Cowork SEO System"
created: 2026-03-25
updated: 2026-08-03
type: concept
tags: [tools, agent, ai-agent, local-seo, seo, marketing, browser-automation, workflow, prompt-engineering]
sources: [raw/articles/bloggersarvesh-chief-of-seo-claude-cowork-2026-03-25.md, raw/articles/bloggersarvesh-claude-cowork-seo-2037158013921042794.md, raw/articles/bloggersarvesh-claude-seo-100k-month-playbook-2032130279494853118.md, raw/articles/alventra-marketing-claude-prompts-2026-07-27.md]
---

# Claude Cowork SEO System

## What this page contains

A source-reconciled description of Sarvesh Shrivastava's Claude Cowork local-SEO system for home-services businesses. The page keeps the architecture, source differences, execution order, human boundary, and evidence limits here; the complete operational prompt cards are in [[claude-cowork-seo-system-prompt-library]] and the later 22-prompt extension is in [[claude-cowork-seo-advanced-audits]].

The raw captures remain immutable. This page is the derived technical artifact, not a replacement for the source text.

## Source map and version history

| Version | Source | What it contributes |
|---|---|---|
| March 25, 2026 | `bloggersarvesh-chief-of-seo-claude-cowork-2026-03-25.md` | Context loading, logged-in Chrome-tool access, eight detailed GBP audits, human decision boundary, and the five-week execution loop. |
| April 19, 2026 | `bloggersarvesh-claude-cowork-seo-2037158013921042794.md` | The fuller 20-prompt stack: GBP, website, backlink/authority, content, entity, posting-pattern, and reporting work. |
| July 20, 2026 | `bloggersarvesh-claude-seo-100k-month-playbook-2032130279494853118.md` | Same-author eight-audit refinement, review-velocity target, baseline/differentiator framing, and explicit Claude-versus-human boundary. |
| July 27, 2026 | `alventra-marketing-claude-prompts-2026-07-27.md` | Public 22-prompt version, complete context bootstrap, exact thresholds and filters, detailed on-page audit, and detailed backlink-gap audit. |

### Source-integrity note

The first March raw capture changes mid-prompt during the photo audit and then restarts overlapping 20-prompt material. The April raw capture also contains malformed embedded URL/HTML fragments in several later prompt blocks. These are capture defects, not silently repaired raw content. Where the later public page supplies the same missing operational detail, this derived cluster uses that corroborating version and preserves the version drift explicitly.

## Core thesis

**Context loading is the system's moat.** Claude receives a persistent business context once, then uses browser-connected tools to collect evidence and produce prioritized execution artifacts. The intended difference is not “better prompting” in isolation; it is a durable handoff from business facts to repeatable audits.

Without the context file, the sources say Claude returns generic SEO advice. With it, the same prompt can operate on the business's NAP data, service areas, competitors, keywords, reviews, GBP state, prior work, and current performance.

## Runtime architecture

### 1. Persistent context layer

Load a folder or project context containing:

- business name, full address, phone, website, and GBP URL;
- years in business, team size, primary and secondary services, service areas, target customer, and average job value;
- top target keywords, current rankings, missing target keywords, review count/rating/velocity, GBP views, website traffic, map-pack status, and the biggest current SEO problem;
- one file per competitor with name, GBP URL, website, and known reason they are winning;
- current GBP categories, attributes, photos, services, and descriptions;
- SEO history: agency/DIY work, tools used, what worked, and what failed;
- one prompt-library file per SEO task.

The context instruction is: use this information for every audit, strategy, and competitor analysis; do not ask for it again; prioritize quick wins; report impact and expected time; use spreadsheet output for comparisons; state uncertainty instead of guessing.

### 2. Browser evidence layer

The March source's setup sequence is explicit: install and activate the Claude Cowork Chrome extension; keep Ahrefs or SEMrush logged in; keep the relevant Google Search Console property logged in; then let Cowork open tabs and collect live evidence. The public version adds Google Maps/GBP, Wikidata, Rich Results Test, WordPress/Gutenberg, Google Analytics, and the relevant SEO surfaces as task-specific interfaces.

The agent's normal handoff is:

`persistent context → Chrome/Google/SEO-tool evidence → spreadsheet or structured notes → prioritized action list → human commercial decision → implementation → monthly measurement`

### 3. Human decision layer

Claude gathers, compares, structures, drafts, and detects gaps. The operator still chooses revenue-relevant keywords, interprets local-market context, checks whether a competitor's advantage is actually offline proof or community presence, approves changes, and executes or supervises them. The sources do not support treating Cowork as an autonomous ranking system.

## The 20-prompt system

| # | Area | Audit / build | Required artifact |
|---:|---|---|---|
| 1 | GBP | Category audit | Per-keyword competitor spreadsheet; missing-category priority list. |
| 2 | GBP | Attributes audit | Listing-vs-competitor matrix; table-stakes, strong-recommendation, and differentiator lists. |
| 3 | GBP | Competitor review teardown | 50-review sample, 30/60/90-day velocity, service/location/staff language, complaints, review target. |
| 4 | GBP | Review response strategy | Response-rate/tone analysis and 3 variations for each 5-, 4-, 3-, and 1–2-star case. |
| 5 | GBP | Posts strategy | Competitor 90-day pattern table and eight-week calendar; weeks 1–4 full copy, weeks 5–8 outlines. |
| 6 | GBP | Services optimization | Competitor service comparison, website-to-GBP gap list, and 40–60-word service descriptions. |
| 7 | GBP | Description optimization | Competitor gap table and three sub-750-character description variants. |
| 8 | GBP | Photo audit | 30/90-day photo comparison and eight-week shot/upload plan; public version targets beating velocity by 50%. |
| 9 | Website | Keyword gap | SEMrush competitor gap filtered to positions 1–20, volume 100–2,000, local-intent terms, KD under 40; top 20 opportunity table. |
| 10 | Website | Money-page audit | Search Console page/query analysis, positions 4–15 quick wins, high-impression/low-CTR fixes, cannibalization, 90-day action plan. |
| 11 | Website | Service + city page builder | Missing service-city inventory plus page copy, metadata, FAQ, CTA, slug, internal links, and citation targets. |
| 12 | Website | Search Console page-2 sprint | Positions 11–20 with at least 100 monthly impressions; exact title/H1/body/internal-link/meta fixes over 30 days. |
| 13 | Website | Review sentiment | Emotional words, outcomes, fears, recommendation phrases, competitor gap, and copy/review-request rewrites. |
| 14 | Authority | Competitor backlink audit | Dofollow/non-sitewide backlink profiles and 90-day opportunity/outreach plan. |
| 15 | Authority | Local citation audit | NAP/platform matrix, duplicate/inconsistency flags, correction plan, missing directories, maintenance checklist. |
| 16 | Authority | Search-intent map | Four buyer stages, volume/KD summaries, stage-specific content destinations, and five 90-day ready-to-hire targets. |
| 17 | Content | Content gap | Top 20 question/problem keywords, three intent buckets, page titles/slugs, 200-word briefs, links, and CTAs. |
| 18 | Content | Entity optimization | Knowledge-panel/Wikidata/schema/brand-consistency checks and LocalBusiness JSON-LD/entity plan. |
| 19 | Content | GBP posting-pattern analysis | Forensic date/time/type/topic/CTA table, exploitable gaps, market-specific cadence, and four weeks of copy. |
| 20 | Tracking | Monthly SEO report | Search Console, GBP, and optional GA4 month-over-month metrics; five-minute wins/problems/next-action report. |

The prompt cards preserve the detailed fields, thresholds, interfaces, outputs, and stop conditions in [[claude-cowork-seo-system-prompt-library]].

## Execution orders in the sources

### Eight-audit order

The March and July eight-audit versions are a compressed operating loop rather than a different system:

1. week 1: categories and attributes;
2. week 2: services and description;
3. week 3: review teardown and response templates;
4. week 4: GBP posts and photos;
5. week 5 onward: post, upload photos weekly, and respond to every review.

### Twenty-prompt order

The fuller version spreads the stack over 12 weeks:

- week 1: context, prompts 1–2;
- week 2: prompts 3–5;
- week 3: prompts 6–8;
- week 4: prompts 9 and 12;
- weeks 5–6: prompts 10, 11, and 13;
- weeks 7–8: prompts 14–16;
- weeks 9–10: prompts 17–19;
- weeks 11–12: prompt 20.

The later public page labels the library “22 prompts,” but its usage schedule still ends at prompt 20. Prompts 21–22 are confirmed as a later extension; their execution placement is not specified.

## Evidence layers

### Confirmed from the source text

The context schema, Cowork/browser handoffs, named tools and interfaces, prompt sequence, spreadsheet/action-list outputs, thresholds, filters, prompt 21/22 requirements, eight-audit cadence, 20-prompt cadence, and human/automation boundary are source-confirmed mechanics.

### Likely synthesis

A practical implementation can treat the context folder as a reusable project input, keep one evidence table per audit, and gate implementation on a human review of source freshness, commercial value, and access limitations. That is a coherent synthesis of the repeated workflow, not a separately tested product specification.

### Unverified source or marketing claims

Claims about ranking within days, response effects, photo percentages, 5–10× conversion differences, $100k/month in 90 days, hundreds of thousands in client revenue, and the agency's case-study outcomes remain attributed claims. They are not independent benchmarks in this wiki.

## Related concepts

- [[claude-cowork-seo-system-prompt-library]] — complete 1–20 operational prompt cards.
- [[claude-cowork-seo-advanced-audits]] — public 22-prompt extension, including the detailed on-page and backlink audits.
- [[claude-cowork]] — browser-connected Claude surface used by the system.
- [[local-seo]] — broader local-search domain.
- [[llm-seo]] — adjacent AI-mediated search visibility cluster.
- [[topical-authority-seo]] — authority/content coverage adjacent to the system's content and link work.
- [[human-in-the-loop]] — the human judgment boundary that keeps research separate from autonomous commercial decisions.
