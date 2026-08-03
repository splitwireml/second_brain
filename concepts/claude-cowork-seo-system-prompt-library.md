---
title: "Claude Cowork SEO System: Prompt Library"
created: 2026-08-03
updated: 2026-08-03
type: concept
tags: [seo, local-seo, claude-cowork, browser-automation, prompt-engineering, workflow, tools]
sources: [raw/articles/bloggersarvesh-chief-of-seo-claude-cowork-2026-03-25.md, raw/articles/bloggersarvesh-claude-cowork-seo-2037158013921042794.md, raw/articles/bloggersarvesh-claude-seo-100k-month-playbook-2032130279494853118.md, raw/articles/alventra-marketing-claude-prompts-2026-07-27.md]
---

# Claude Cowork SEO System: Prompt Library

## Scope

This is the operational appendix for [[claude-cowork-seo-system]]. It preserves the reusable inputs, exact thresholds, browser/tool surfaces, output schemas, and execution constraints for prompts 1–20. Repeated sales copy and outcome claims are omitted; source mechanics are retained. Prompts are source-described workflows, not independently validated SEO instructions.

## Bootstrap: load context before any audit

The public version's bootstrap prompt preserves these fields:

```text
Here is everything you need to know about my business before we start any SEO work. Reference this every time I ask you to run an audit, build a strategy, or analyze competitors. Never ask me for this information again.

BUSINESS BASICS: Business name: [your business name]
Address: [full address]
Phone: [phone number]
Website: [website URL]
Google Business Profile: [GBP URL]
Years in business: [X years]
Team size: [solo / small team / large team]

SERVICES + MARKET: Primary service: [what you do]
Secondary services: [service 2], [service 3], [service 4]
Service areas: [city 1], [city 2], [city 3], [city 4], [city 5]
Target customer: [who your best customer is]
Average job value: [$X]

SEO GOALS: Top 5 keywords I want to rank for: [keyword 1] ... [keyword 5]
Keywords I currently rank for: [keywords]
Keywords I should rank for but don't: [keywords]

CURRENT STANDINGS: Google reviews: [count], [rating], [new reviews/month]
GBP monthly views: [impressions if known]
Monthly website traffic: [visits if known]
Current map pack status: [ranking/not ranking]
Biggest SEO problem right now: [one honest sentence]

COMPETITORS: [name] - [GBP URL] - [website] - [known advantage]
[repeat for three competitors]

WHAT I'VE ALREADY TRIED: [agency, DIY, tools, outcomes, failures]

HOW I WANT YOU TO WORK: Prioritize quick wins. For each recommendation give impact
(high/medium/low) and expected time to see results. Use spreadsheet format for
comparisons. When unsure, say so; do not guess. Use this as the base for everything.
```

The source also specifies one file per competitor, uploaded GBP details, and one prompt-library file per task. The March setup adds a practical access prerequisite: activate the Cowork Chrome extension and keep Ahrefs or SEMrush plus the relevant Search Console property logged in. ^[raw/articles/bloggersarvesh-chief-of-seo-claude-cowork-2026-03-25.md] ^[raw/articles/alventra-marketing-claude-prompts-2026-07-27.md]

## Part 1 — Google Business Profile

### Prompt 1 — GBP category audit

**Browser/input:** Google Maps; three target queries such as `[service] in [city]`; the business GBP and three competitor GBPs.

```text
Search the three target keywords in Google Maps. For each search, record the Map Pack businesses. Open each competitor GBP and extract the primary and every secondary category. Output one spreadsheet tab per keyword with business name, primary category, secondary categories, star rating, review count, and ranking position. Highlight categories competitors have that I lack. Rank additions by the number of top competitors sharing them: all three = table stakes; one competitor = differentiation opportunity.
```

**Artifact:** category matrix plus prioritized add/change list. The source's reasoning is pattern detection across categories and Map Pack positions; the claim that one added category changed rankings quickly remains source-reported. ^[raw/articles/bloggersarvesh-chief-of-seo-claude-cowork-2026-03-25.md]

### Prompt 2 — GBP attributes audit

**Browser/input:** own GBP plus three competitors.

```text
Extract every visible attribute/tag from each listing, including ownership, estimates, appointments, accessibility, availability, payment, and any other displayed attribute. Output a yes/no matrix with attribute name and one column for my listing plus each competitor. Separate attributes shared by all competitors, shared by two of three, and present in only one. For every missing attribute, estimate likely ranking impact and whether it affects click-through rate.
```

**Artifact:** table-stakes, strong-recommendation, and differentiator lists. “Baseline requirement” is the source's operating interpretation, not an independently verified ranking rule. ^[raw/articles/bloggersarvesh-claude-seo-100k-month-playbook-2032130279494853118.md]

### Prompt 3 — competitor review teardown

**Browser/input:** three competitor GBPs; the source specifies the last 50 reviews per competitor.

```text
For each competitor, extract total reviews, average rating, reviews in the last 30/60/90 days, top five mentioned services, top five neighborhoods/cities, staff names, recurring complaints or negative themes, and customer phrases worth eliciting in future reviews. Compare review velocity to my GBP and add a separate tab stating the monthly review pace needed to catch the leading competitor and the estimated time at that pace.
```

**Artifact:** review-velocity target, language inventory, and complaint map. The repeated source insight is to evaluate recency/velocity rather than total count alone; its ranking-effect language is source-described. ^[raw/articles/bloggersarvesh-claude-cowork-seo-2037158013921042794.md]

### Prompt 4 — review response strategy

**Browser/input:** own and competitor GBPs; last 30 owner responses per listing.

```text
Measure response rate, estimated response time, service/location mentions, average response length, tone, negative-review handling, and any visible engagement pattern. Compare my strategy with competitors. Then write a complete response-template system: three variations each for 5-star, 4-star, 3-star, and 1–2-star reviews. Use service + city language naturally; 4-star responses acknowledge the gap and invite a return; 3-star responses take accountability and offer resolution; 1–2-star responses are empathetic and non-defensive. Keep each template 40–80 words and human-sounding.
```

**Artifact:** response benchmark and 12 templates. The sources present review responses as a repeatable under-one-minute operating system; the ranking claim is not independently verified. ^[raw/articles/bloggersarvesh-chief-of-seo-claude-cowork-2026-03-25.md]

### Prompt 5 — GBP posts strategy

**Browser/input:** own and competitor GBPs; visible post history for the last 90 days.

```text
Record total posts, average posts/week, post types (offer/update/event/product), images, CTA buttons, topics, seasonal patterns, and visible engagement. Compare my listing with competitors. Build an eight-week calendar at 2–3 posts/week using seasonal promotions, before/after projects, neighborhood-specific posts, review highlights, team spotlights, and educational problem-solving posts. Each post needs a target keyword, 100–150 words, a CTA, and an image description. Write weeks 1–4 in full and outline weeks 5–8.
```

**Artifact:** competitor cadence table plus 8-week calendar. The later 90-day refinement adds recurring coverage across 8–10 neighborhoods/month as a source-described local-relevance tactic. ^[raw/articles/bloggersarvesh-claude-cowork-seo-2037158013921042794.md]

### Prompt 6 — services-section optimization

**Browser/input:** own/competitor GBPs and own website.

```text
Extract every service, description, service grouping, description structure, and shared-vs-unique service from each competitor. Compare the GBP services section with the website: services on the site but absent from GBP, GBP services without descriptions, and descriptions weaker than competitors. Write a description for every core service: 2–3 sentences, 40–60 words, primary service keyword, one service area, a concrete benefit, and natural business language.
```

**Artifact:** service comparison, website-to-GBP gap list, and paste-ready descriptions. ^[raw/articles/alventra-marketing-claude-prompts-2026-07-27.md]

### Prompt 7 — GBP description optimization

**Browser/input:** own/competitor GBP descriptions.

```text
Extract full descriptions and compare character count, primary/secondary keywords, service areas, trust signals, unique selling points, CTA, and tone. Identify common competitor elements, unclaimed opportunities, and my distinctive elements. Write three versions under 750 characters: keyword-focused, conversion-focused, and trust-focused. Include the supplied target keywords and service areas. Test variants sequentially rather than treating one description as permanent.
```

**Artifact:** description comparison and three variants. The source proposes a 30-day test cadence; ranking/call outcomes are not independently measured here. ^[raw/articles/bloggersarvesh-claude-cowork-seo-2037158013921042794.md]

### Prompt 8 — GBP photo audit

**Browser/input:** own/competitor photo sections.

```text
Record total photos, estimated additions in the last 30 and 90 days, photo types, quality, stock-photo indicators, people/faces, local landmarks/neighborhoods, and average weekly upload rate. Build an eight-week plan with exact weekly quantity, shot list, location/purpose, before/after versus team/truck/completed-install priorities, keyword-and-location naming convention, and geotagging instructions. The public version asks for a plan that beats the top competitor's velocity by 50%; avoid generic office photos.
```

**Artifact:** photo-velocity comparison and shot calendar. The suggested steady cadence of 3–5 photos/week and the percentage claims are source claims, not validated platform rules. ^[raw/articles/bloggersarvesh-chief-of-seo-claude-cowork-2026-03-25.md]

## Part 2 — Website

### Prompt 9 — keyword-gap audit

```text
In SEMrush Keyword Gap, compare my domain with three competitors. Keep keywords where competitors rank 1–20 and I do not. Filter to monthly volume 100–2,000, local-intent terms containing a city/service/near-me/emergency/best/local signal, and KD under 40. For the top 20, record volume, KD, competitor positions, whether an existing page can be optimized, and whether a new page is required. Sort by opportunity score and add Action Required = Optimize existing page or Create new page.
```

The output is a prioritized spreadsheet, not a generic keyword dump. ^[raw/articles/bloggersarvesh-claude-cowork-seo-2037158013921042794.md]

### Prompt 10 — money-page audit

```text
In Google Search Console, use the last three months of queries and pages. For every page, map ranking keywords, average position, impressions, clicks, and whether the match is intentional. Identify high-value positions 4–15, high-impression/low-click pages, zero-ranking pages, and cannibalization. Produce quick wins for this week, medium-effort rebuilds for next month, and new pages for 90 days. Include current position, target position, expected time, and exact on-page changes.
```

The April capture contains malformed URL fragments around this prompt; this structured version preserves the recoverable task requirements and the public page's clean version. ^[raw/articles/alventra-marketing-claude-prompts-2026-07-27.md]

### Prompt 11 — service + city page builder

```text
Inventory existing service-plus-city combinations on the site. For every missing combination, write: title under 60 characters, meta description under 155, natural H1, 100-word local opening, 150-word city-specific why-us section, 200-word service/process section, city review placeholder, three city-specific FAQs, phone CTA, exact URL slug, three internal-link targets, and two relevant citation/directories.
```

The source's examples include `[service] + [city]`, `[service] near [city]`, and `best [service] in [city]`. Avoid treating the source's “one page per city guarantees ranking” language as a verified rule. ^[raw/articles/bloggersarvesh-claude-cowork-seo-2037158013921042794.md]

### Prompt 12 — Search Console page-2 sprint

```text
Export 90 days of Search Console data. Find every keyword in positions 11–20 with at least 100 impressions/month. For each ranking page, check title inclusion, H1 inclusion, first-100-word inclusion, word count, internal links, and current meta description. Build a 30-day sprint: week 1 title/H1, week 2 thin-page additions for pages under 500 words, week 3 exact internal links, week 4 meta rewrites for high-impression/low-CTR pages. Write the exact replacement copy for every fix.
```

This is the source's page-2 “goldmine” workflow; the traffic/ranking payoff is source-described. ^[raw/articles/alventra-marketing-claude-prompts-2026-07-27.md]

### Prompt 13 — review sentiment analysis

```text
Read the last 100 reviews for three competitors and my GBP. Extract the top 20 emotional words, top 10 outcomes, top five pre-service fears/frustrations, recommendation phrases, and language present in 5-star but not 3-star reviews. Compare emotional gaps. Rewrite my GBP description, homepage headline/subheadline, review-request script, and three website social-proof statements using the observed customer language.
```

The source positions this as conversion-language extraction, not merely sentiment scoring. ^[raw/articles/bloggersarvesh-claude-cowork-seo-2037158013921042794.md]

## Part 3 — Backlinks and authority

### Prompt 14 — competitor backlink audit

```text
In Ahrefs Site Explorer, inspect each competitor's full backlink profile. Filter to dofollow, linking-domain DR >= 20, linking-domain traffic >= 100/month, and non-sitewide links. Find domains linking to all three competitors, two, or one. For high-priority opportunities record domain/URL, DR, site type, how the competitor earned the link, realistic acquisition chance, and an outreach strategy. Build a 90-day plan: five easiest directory/citation/association links, five medium local-news/sponsor/guest-post links, and five authority links. Include contact method and complete outreach email.
```

The later public audit (prompt 22) uses a stricter page-level Exact URL workflow and is preserved separately in [[claude-cowork-seo-advanced-audits]]. ^[raw/articles/bloggersarvesh-claude-cowork-seo-2037158013921042794.md]

### Prompt 15 — local citation audit

```text
Search the exact business name across Google Business Profile, Yelp, Bing Places, Apple Maps, Facebook, BBB, Angi, HomeAdvisor, Thumbtack, Houzz, Yellow Pages, Manta, Foursquare, Superpages, Citysearch, and relevant industry directories. For each, record existence, exact name, address, phone, URL, duplicates, rating, and review count. Flag NAP inconsistencies, prioritize repairs, list missing high-value directories, and create a monthly maintenance checklist.
```

The source treats NAP consistency as a verification concern; the stated ranking and 30-day improvement effects remain source claims. ^[raw/articles/alventra-marketing-claude-prompts-2026-07-27.md]

### Prompt 16 — local search-intent map

```text
In SEMrush, pull niche/service-area keywords with volume >= 20/month. Classify each as Stage 1 problem-unaware, Stage 2 problem-aware, Stage 3 solution-aware, or Stage 4 ready-to-hire. For each stage calculate keyword count, combined volume, average KD, and top 10 keywords. Route Stage 4 to service pages/GBP, Stage 3 to comparison/FAQ pages, Stage 2 to educational content, and Stage 1 to problem-identification content. Select five Stage 4 targets for the next 90 days with exact actions.
```

The four-stage taxonomy and destination mapping are source mechanics; the claimed 5–10× conversion difference is not verified. ^[raw/articles/bloggersarvesh-claude-cowork-seo-2037158013921042794.md]

## Part 4 — Content, entity, and tracking

### Prompt 17 — content-gap analysis

```text
In SEMrush Content Gap, compare my domain with three competitors. Keep competitor-ranking terms missing from my site, volume 50–500/month, question words, and problems my service solves. Select the top 20. Classify into problem-awareness, solution-comparison, and local-service content. For each write an SEO title, URL slug, secondary keywords, questions, recommended word count, internal links, CTA, and a 200-word brief. Prioritize problem-awareness topics first.
```

### Prompt 18 — entity optimization

```text
Check whether the business has a Google Knowledge Panel, whether it exists on Wikidata, what schema is present in the Rich Results Test, and whether quoted brand searches show consistent name/address/phone data. Produce complete LocalBusiness JSON-LD, an authoritative-presence/claim list (Wikipedia only if eligible, Crunchbase, LinkedIn, associations), brand-mention/anchor guidance, and a knowledge-panel action plan.
```

The public source frames knowledge-graph, AI-overview, and resilience outcomes as claims; the actual deliverable is the audit and implementation plan. ^[raw/articles/alventra-marketing-claude-prompts-2026-07-27.md]

### Prompt 19 — competitor GBP posting-pattern analysis

```text
For every visible competitor GBP post, record exact date/time, weekday, post type, word count, image, CTA and CTA text, topic/service, neighborhood/city, price/offer, hashtags, and formatting. Output one spreadsheet row per post. Analyze weekday/time/type/topic/season/month patterns and gaps. Build a market-specific cadence with days, times, types, topic mix, and the first four weeks of full copy.
```

This is more forensic than prompt 5: prompt 5 builds a calendar from a 90-day summary; prompt 19 reconstructs the visible history row by row. ^[raw/articles/alventra-marketing-claude-prompts-2026-07-27.md]

### Prompt 20 — monthly SEO performance report

```text
Read Google Search Console, GBP insights, and GA4 if available. Compare the last 30 days with the previous 30 days. Include organic clicks, impressions, CTR, average position, top/improving/declining queries, winning/losing pages, GBP views, branded/discovery queries, calls, directions, website clicks, photo views, review change, organic sessions, conversion rate, landing pages, and bounce rate. Produce a one-page report with three wins, three problems, one next action, and whether GBP calls rose or fell.
```

The source's measurement principle is to connect search work to calls and revenue rather than traffic vanity metrics; attribution implementation is not specified. ^[raw/articles/alventra-marketing-claude-prompts-2026-07-27.md]

## Shared output and safety rules

- Use spreadsheets/tables for competitor comparisons and preserve the raw evidence behind every recommendation.
- Report blocked, paywalled, JavaScript-rendered, unavailable, or rate-limited evidence instead of guessing.
- Keep source-observed facts, recommendations, and promotional outcomes separate.
- Treat exact thresholds as this source's operating defaults, not universal SEO laws.
- Have a human approve category changes, copy, links, entity claims, and publication.

## Related

- [[claude-cowork-seo-system]]
- [[claude-cowork-seo-advanced-audits]]
- [[claude-cowork]]
- [[prompt-engineering-patterns]]
- [[local-seo]]
- [[human-in-the-loop]]
