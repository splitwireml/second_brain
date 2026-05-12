---
title: Google Maps B2B Lead Generation with Claude Code
created: 2026-04-15
updated: 2026-04-15
type: concept
tags: [lead-gen, outbound, b2b, web-scraping, claude-code, automation, monetization]
sources: [raw/articles/levikmunneke-google-maps-lead-gen-2026-04-15.md]
related_entity: [[levikmunnke]]
---

## Definition

A four-layer automated B2B lead generation system that uses Claude Code to scaffold the entire stack: Maps Data API (RapidAPI) for listings by zip code → Python email scraper for website contact pages → dedup + cleaning pipeline → Flask dashboard for export.

## Architecture

The system is built in four independent layers:

1. **Maps Data API** — RapidAPI "maps data" by alexanderxbx ($3–$19/mo); returns business name, address, phone, website URL, rating, review count, category, coordinates for a keyword + location
2. **Email Scraper** — Python requests + BeautifulSoup; regex extract from raw HTML, checks /contact and /about pages, thread pool of 20; skips generic emails (info@, hello@, support@) unless nothing else found
3. **Dedup + Cleaning Pipeline** — removes nulls, duplicates, personal email domains (gmail, yahoo, hotmail, outlook, aol), closed businesses, 404s; normalizes to E.164 phone format; outputs clean_leads.csv and flagged_leads.csv
4. **Flask Dashboard** — search form, job queue with progress bars, database stats, filtered CSV export, filter by min rating/review count/has email/category

## Zip Code Strategy

The key insight: Google Maps caps results per keyword+location query at a few hundred. The fix is iterating across all ~32,000 US zip codes. A national run for a niche category (HVAC, roofing, landscaping) yields:

- 800k–1.2M raw listings before dedup
- 400k–700k unique businesses after dedup
- 35–50% yield a scrapeable email → 140k–200k verified email addresses
- 60–70% drop after cleaning → 40k–80k clean B2B leads

Full national run: 12–24 hours at 10 concurrent threads.

## Cost Math

| Component | Cost |
|-----------|------|
| Maps Data API (RapidAPI) | $3–$19/mo |
| Email scraper (Python, free) | $0 |
| Cleaning pipeline (Python, free) | $0 |
| Flask dashboard (free) | $0 |
| **Total** | **$3–$25/mo** |

vs. ZoomInfo at ~$15,000/year ($1,250/mo) with 40% bounce rates.

Derived cost: ~$0.50 per 1,000 verified leads.

## Key Claims

- **265M+ Google Maps business listings** — Likely; widely cited but unverified independently
- **800k–1.2M raw listings per national niche run** — Unverified; derived from zip code coverage math
- **35–50% email scrape rate** — Plausible; typical business website contact page rate
- **$0.50/1,000 verified leads** — Derived estimate based on $25/mo cost and 40k–80k output

## Relationship to Other Concepts

The methodology is adjacent to several other systems in the wiki:

- [[claude-cowork-seo-system]] — also uses Claude Code to scaffold a tool pipeline for a non-technical operator
- [[x-organic-b2b-sales]] — the outbound destination: the CSV produced by this pipeline feeds cold outreach sequences
- [[claude-mcp-linkedin-outreach-automation]] — alternative outreach channel (LinkedIn vs. email) using similar enrichment patterns
- [[programmatic-seo]] — similar scale-out strategy: iterate across a large combinatorial space (zip codes / keywords) to generate volume

## Open Questions

- RapidAPI "maps data" by alexanderxbx — not independently confirmed to exist or function as described
- Actual lead quality and deliverability rates not independently verified
- Blocklist (gmail/yahoo personal domains) may drop valid small business contacts using personal addresses
