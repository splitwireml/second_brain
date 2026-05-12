---
title: Codex Lead Database Pipeline
created: 2026-05-03
updated: 2026-05-03
type: concept
tags: [codex, outbound, web-scraping, local-business]
sources: [raw/articles/levikmunneke-codex-lead-database-2026-04-30.md]
---

# Codex Lead Database Pipeline

Using Codex CLI as a lead generation scraping engine — targeting 260M+ Google Maps business listings instead of fatigued Apollo/Lusha/Zoominfo contact pools. By [[levikmunneke]].

## The Stack

1. **OpenAI Codex CLI** — writes, debugs, and runs Python scripts autonomously from plain English prompts
2. **RapidAPI Google Maps Places endpoint** — $5-15/mo for 10,000+ requests; scrapes business name, address, phone, website, rating, reviews, lat/lng, place ID
3. **Python environment** — laptop or $7/mo VPS

**Total monthly cost: under $25** vs $99/mo for Apollo.

## Three-Prompt Pipeline

### Prompt 1 — Google Maps Scraper
Describe: query + city + max_results → clean CSV with proper headers, exponential backoff, duplicate skip by place ID.

### Prompt 2 — Website Enricher
Takes maps CSV → crawls each business website (up to 5 pages) → extracts emails, phones, page title, meta description, HTTPS, load speed, mobile responsiveness, copyright year, conversion signals.

### Prompt 3 — Signal Extractor
Adds a "signal" column: one specific, observable problem per business. E.g.:
- "no website attached to google profile"
- "site loads in 8.4 seconds, killing mobile conversions"
- "copyright year is 2019 — site likely abandoned"

The signal becomes the opening line of a cold email.

## The Math

- 5 categories × 10 cities × 500 businesses = 25,000 raw leads
- ~60% enriched with usable email = 15,000 contactable leads
- 800 sends/day across 30-40 warmed inboxes
- Reply rate: 3-7% (hyper-specific signals) vs 0.5-1.5% (generic Apollo)
- **Result: ~450 replies, ~67 booked discovery calls per outbound run**
- Infrastructure cost: under $400/mo all-in
- One closed retainer at $3-5k pays for the year

## Why Maps Beats Apollo

Apollo/Lusha/Zoominfo data is saturated — every agency owner buys the same 50,000 contacts. Local businesses (dentists, contractors, gym owners) aren't on those platforms and are "wide open" to outbound.

Google Maps has 260M+ business listings sitting completely untouched.

## The Email That Writes Itelf

Generic Apollo cold email:
> "hey john, hope your week is going well. i help dentists like yourself generate more new patient appointments through paid ads."

Signal-driven Codex email:
> "hey john — noticed your google profile doesn't have a website attached, and the place id matches an old wix site that's been down for months. built you a free landing page mockup for [business name] — want me to send it over?"

## Implementation Timeline (One Afternoon)

- Hour 1: Codex CLI install + login
- Hour 2: RapidAPI key + test endpoint in Postman
- Hour 3: Codex builds maps scraper → test CSV output
- Hour 4: Codex builds website enricher → test on sample CSV
- Hour 5: Codex builds signal extractor → review signals
- Morning after: run full pipeline → start sending by Friday

## Raw Source

- `raw/articles/levikmunneke-codex-lead-database-2026-04-30.md`
