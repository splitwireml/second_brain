---
title: Firecrawl
created: 2026-04-13
updated: 2026-04-13
type: entity
tags: [tools, ai-tools, product, web-scraping]
sources: [raw/articles/scrapling-technical-research-2026-04-13.md]
---

## Overview

Firecrawl is a web data API oriented around AI workflows. Its docs position it as a single API for search, scrape, and interaction, with LLM-ready outputs such as markdown and structured JSON.

## Positioning

Compared with [[scrapling]], [[firecrawl]] is more service/API-first. Scrapling is more framework/SDK-first, while Firecrawl exposes hosted scraping/search/interact capabilities directly through an API and MCP server.

## Relationship to Scrapling

- [[scrapling]] overlaps with Firecrawl on markdown extraction, AI/MCP workflows, and LLM-oriented outputs
- [[scrapling-vs-scrapy-vs-firecrawl]] compares the two systems in architecture and use case

## Role in Agent Web Stack

In [[theahmadosman]]'s three-stage "Agent Web Stack," Firecrawl serves as the **extraction** layer (stage 2) — handling known-URL scrape and crawl after [[searxng]] finds candidates and before [[camoufox]] is needed as a browser fallback.

## Best fit

- Hosted web data access
- AI-agent workflows needing one API surface
- Markdown/JSON extraction without building crawler infrastructure yourself
- Stage 2 in the [[agent-web-stack]] pipeline

## Products

### Fire-PDF (2026-04-14 announced)

Rust-based PDF parsing engine integrated into the Firecrawl API:

- **5x faster** PDF-to-markdown conversion vs prior Firecrawl pipeline
- **400ms/page** neural layout classification — detects regions individually
- **Table extraction** → full markdown; **formula preservation** in LaTeX
- **Zero config** — automatic path selection per page
- Auto-applied to all PDFs sent through the Firecrawl API as of 2026-04-14
- A 216-page financial report processes in ~83 seconds (unverified)
- Open-source Rust library claimed; **no public repo found** at announcement time (2026-04-14) — searched all 43 firecrawl GitHub org repos, zero matches for `fire-pdf` or `FirePDF`
- Notable open questions: scanned/OCR document support, coordinate metadata for chunking pipelines, visual anchoring

Sources: `raw/articles/firecrawl-fire-pdf-rust-parser-2026-04-15.md`

## Sources

- `raw/articles/scrapling-technical-research-2026-04-13.md`
- `raw/articles/firecrawl-fire-pdf-rust-parser-2026-04-15.md`
