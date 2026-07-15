---
title: Claude Code Lead Gen
created: 2026-06-07
updated: 2026-06-11
type: concept
tags: [claude-code, lead-gen, outbound, sales, web-scraping]
sources: [raw/articles/xarticle-how-i-built-a-400m-lead-database-with-claude-code-2062312236513915351.md]
related_entity: [[levikmunneke]]
author: [[levikmunneke]]
---

# Claude Code Lead Gen

A lead-generation workflow where [[claude-code]] is used as the build-and-maintain loop for scraping public directories, normalizing records, and enriching them into custom outbound lists. The core claim is that the best lead sources are often mandatory public registries and niche directories rather than rented aggregator databases.

## Core thesis

Instead of buying the same Apollo- or ZoomInfo-style contact pools as everyone else, the operator targets sources where visibility is already intentional or legally required: licensing boards, business registries, IRS 990 data, trade associations, chambers, event rosters, and vertical-specific directories. [[claude-code]] then writes the scraper, runs it, inspects failures, and quickly repairs broken parsers when the target site changes.

## Workflow

1. **Discovery** — find verticals where public listing is mandatory or commercially useful
2. **Extraction** — use requests + BeautifulSoup for simple sites, or browser automation for JS-heavy and rate-limited sites
3. **Normalization** — dedupe across name, geography, business identity, and email/domain matches
4. **Enrichment** — append verified email, firmographic data, and buying signals
5. **Maintenance** — re-run and repair broken scrapers continuously as directory layouts change

## Why it beats bought lists

- **Higher intent quality**: public licensing or registry data already verifies role, status, or activity
- **Lower inbox saturation**: custom lists are less likely to have been blasted by dozens of other senders
- **Better economics at scale**: once list size grows, scraper infrastructure can be cheaper than seat-based data vendors
- **More durable edge**: the real moat is not one scraper but the ability to keep many scrapers alive with low maintenance overhead

## Related

- [[levikmunneke]]
- [[claude-code]]
- [[lead-gen]]
- [[web-scraping]]
- [[cold-email]]
- [[codex-lead-database-pipeline]]
