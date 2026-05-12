---
title: Scrapy
created: 2026-04-13
updated: 2026-04-13
type: entity
tags: [tools, open-source, web-scraping, automation]
sources: [raw/articles/scrapling-technical-research-2026-04-13.md]
---

## Overview

Scrapy is the canonical Python crawling framework for structured web scraping. Its architecture centers on spiders, requests, responses, scheduling, deduplication, and export pipelines.

## Positioning

Based on the Scrapling docs' own architecture notes, [[scrapling]] is notably closer to Scrapy than to hosted scraping APIs because Scrapling includes a Scrapy-like spider API, scheduler, session routing, concurrency controls, and pause/resume support.

## Relationship to Scrapling

- [[scrapling]] explicitly documents a Scrapy-like spider API and includes a direct comparison table
- [[scrapling-vs-scrapy-vs-firecrawl]] compares the two systems in architecture and use case

## Best fit

- Large crawl jobs
- Framework-style scraping pipelines
- Custom extraction logic and export flows

## Sources

- Official Scrapy docs reviewed indirectly via technical research in `raw/articles/scrapling-technical-research-2026-04-13.md`
