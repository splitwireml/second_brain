---
updated: 2026-04-17
title: Scrapling technical research
source: https://github.com/D4Vinci/Scrapling`
type: article
---

# Scrapling technical research

Date: 2026-04-13
Subject: Scrapling functionality, anti-bot behavior, architecture, AI/MCP integration, and comparison to Scrapy and Firecrawl

## Sources examined

### Official Scrapling sources
- GitHub repo: `https://github.com/D4Vinci/Scrapling`
- `README.md`
- `docs/fetching/choosing.md`
- `docs/fetching/dynamic.md`
- `docs/fetching/stealthy.md`
- `docs/parsing/adaptive.md`
- `docs/ai/mcp-server.md`
- `docs/spiders/architecture.md`
- `pyproject.toml`
- `scrapling/engines/static.py`
- `scrapling/engines/_browsers/_stealth.py`
- `scrapling/cli.py`
- `scrapling/spiders/result.py`

### External comparison sources
- Firecrawl docs: `https://docs.firecrawl.dev/introduction.md`
- Scrapy docs: `https://docs.scrapy.org/en/latest/intro/overview.html`

## High-confidence findings

1. Scrapling is a Python scraping framework/SDK, not a hosted scraping API by default.
2. It combines three layers:
   - HTTP fetcher based on `curl_cffi`
   - browser fetchers based on Playwright / Patchright
   - Scrapy-like spider framework with pause/resume and export
3. Its standout feature is adaptive element relocation: save an element once, then later relocate the same element after DOM changes using similarity matching backed by SQLite storage.
4. It does handle Cloudflare Turnstile / interstitial pages in its stealth browser mode, with both docs claims and implementation in `_cloudflare_solver()`.
5. It is browser-based for dynamic and stealth modes, using Playwright APIs and Patchright, with options for Chromium, real Chrome, or CDP.
6. It can also make normal HTTP requests and API calls directly through `get/post/put/delete` methods with JSON bodies, query params, cookies, headers, proxies, and retries.
7. Its LLM-friendly angle is real but limited in scope: it focuses on pre-filtering content before handing it to an LLM, markdown/text extraction, ad/tracker blocking, and sanitizing hidden prompt-injection content. It is not a token-compressed response protocol for every scrape result.
8. It has both SDK and server modes:
   - Python SDK/library
   - CLI
   - MCP server over stdio or HTTP
   - Docker image for the MCP server
9. Structured export is supported for spider output via JSON and JSONL. The library itself does not appear to ship a dedicated tabular/CSV schema extraction engine.

## Question-by-question answers

### 1) Is it similar to Scrapy or Firecrawl?

It is closer to Scrapy in architecture, and closer to Firecrawl in LLM-facing output goals.

- Similar to Scrapy:
  - Scrapling explicitly documents a "Scrapy-like Spider API"
  - It has `Spider`, `Request`, `Response`, scheduler, concurrency controls, deduplication, pause/resume, and crawl export
  - The docs include a direct "Comparison with Scrapy" table
- Similar to Firecrawl:
  - It can return markdown/text instead of raw HTML
  - It has an MCP server for AI tools
  - It emphasizes LLM-ready extraction and reducing irrelevant tokens before sending content to AI

Key difference:
- Scrapy = crawler framework first
- Firecrawl = hosted API/service first
- Scrapling = local Python framework/SDK first, with optional MCP/server surfaces layered on top

### 2) What measures does it take to bypass bot protection? Does it handle Cloudflare?

Confirmed anti-bot measures in docs/code:
- real browser user-agent generation
- Playwright/Patchright browser automation
- use of real Chrome when available
- CDP connection to real browsers
- proxy support and proxy rotation
- Google referer by default (`https://www.google.com/`)
- WebRTC leak blocking
- canvas-noise fingerprint defense
- WebGL enabled by default because some WAFs expect it
- DNS-over-HTTPS to avoid DNS leaks when using proxies
- ad/tracker blocking to reduce noise
- Cloudflare challenge detection and solving in stealth mode

Cloudflare handling: yes, confirmed.
- Docs claim `StealthyFetcher` can bypass Turnstile / interstitial challenges.
- `_cloudflare_solver()` in `scrapling/engines/_browsers/_stealth.py` detects challenge type, waits through managed challenges, locates Turnstile widgets, clicks verification boxes, and retries recursively if the challenge is still present.

Important limitation:
- The README explicitly says Scrapling handles Cloudflare Turnstile, but points to Hyper Solutions for Akamai, DataDome, Kasada, and Incapsula enterprise-grade antibot tokens. So Scrapling is not claiming universal antibot bypass across all major WAFs on its own.

### 3) What is the website watching feature? Is this an AI integrated scraper that watches the HTML?

Confirmed: there is no first-class "website watcher" or always-on monitoring feature documented in the code/docs I examined.

What likely caused the confusion:
- Scrapling's parser "learns from website changes"
- the adaptive feature stores an element's properties and later relocates it after the page structure changes

So:
- it is not continuously watching HTML by itself
- it is not an autonomous monitoring daemon by default
- it does not use AI for adaptive relocation; docs explicitly say the relocation happens "without AI"

What it actually does:
- on one run, you save element fingerprints/properties
- on a later run, if the selector breaks, Scrapling searches for the most similar element using stored attributes/text/path/sibling/parent features

### 4) Does it keep running as a service doing HTML scans on websites?

Not by default.

Confirmed behaviors:
- one-off fetchers for single requests
- persistent sessions that keep browser state alive across multiple requests
- spiders that run crawls until completion
- MCP server that stays up and accepts tool calls

What is not confirmed:
- a built-in scheduled website monitoring daemon or polling service
- built-in change-detection service that keeps scanning sites unattended forever

So the answer is: it can be used in a long-running system you build, but it is not itself a website-monitoring SaaS/service by default.

### 5) What does it mean by also being able to scrape APIs?

Confirmed from code:
- the HTTP fetcher supports `get`, `post`, `put`, `delete`
- request args include `json`, `data`, `params`, headers, cookies, proxies, retries
- browser sessions can also capture XHR/fetch responses via `capture_xhr`

So "scrape APIs" means two practical things:
1. call JSON endpoints directly like a normal HTTP client
2. load a site in a browser and capture the underlying XHR/fetch API calls that power the frontend

This is useful when the site UI is just a wrapper over JSON endpoints.

### 6) Is this browser based scraping that uses something like Playwright or Browser Use?

Yes for dynamic/stealth modes, no for static mode.

Confirmed:
- `DynamicFetcher` uses Playwright APIs with Chromium/Chrome/CDP
- `StealthyFetcher` also uses Playwright-style APIs and imports Patchright for stealth browser execution
- docs repeatedly say page automation uses Playwright's `Page` API

Not found:
- any dependency on Browser Use

So the correct framing is:
- static mode = HTTP-level scraping via `curl_cffi`
- dynamic/stealth mode = Playwright/Patchright browser automation

### 7) Does it have LLM friendly responses that don't kill tokens?

Partly yes.

Confirmed LLM-friendly features:
- markdown/text extraction instead of raw HTML
- CSS-selector targeting so only relevant page regions are passed to the model
- MCP server explicitly marketed around lowering token usage
- `ai-targeted` extraction path in CLI
- prompt-injection sanitization of hidden content
- ad/tracker blocking in browser tools

Not confirmed:
- any universal token-compression format for all responses
- a special compact DOM schema comparable to a dedicated "browser for LLMs" representation

So the precise answer is:
- yes, it has LLM-oriented extraction and filtering
- no, it is not fundamentally a token-minimization protocol across every scraping workflow

### 8) Does it run as a server? Is it an SDK?

Both.

Confirmed forms:
- Python package / SDK (`pip install scrapling`)
- CLI (`scrapling ...`)
- MCP server (`scrapling mcp` or `scrapling mcp --http`)
- Docker image for the MCP server

The MCP server can run:
- stdio transport for Claude Desktop / Claude Code / Cursor-style integrations
- streamable HTTP on host/port (default port 8000 in docs)

### 9) Does it have capabilities of structured data scraping into tabular or JSON file?

Confirmed:
- spider results can be yielded as Python dicts
- `ItemList.to_json(path)`
- `ItemList.to_jsonl(path)`
- targeted extraction returns structured lists of selected elements in MCP examples

Not confirmed in examined sources:
- built-in CSV export
- built-in dataframe/table abstraction
- schema-driven extractor that automatically normalizes page content into columns without user logic or LLM help

So:
- JSON/JSONL export = yes
- tabular output = indirectly yes if you yield row dicts yourself, but not as a dedicated built-in table engine

## Architecture summary

Scrapling is best understood as four layers:

1. Parsing layer
   - selector engine
   - CSS/XPath/text/regex queries
   - adaptive relocation via stored element fingerprints

2. HTTP layer
   - `curl_cffi` sessions
   - browser impersonation and stealthy headers
   - JSON/API request support

3. Browser layer
   - Playwright/Patchright-driven dynamic and stealth fetchers
   - automation hooks
   - XHR capture
   - Cloudflare solver

4. Crawl / AI layer
   - Scrapy-like spider framework
   - item export to JSON/JSONL
   - MCP server for AI tools
   - markdown/text extraction and sanitization for token efficiency

## Bottom line

If you want:
- a local Python scraping framework with browser + HTTP + crawler + adaptive selector recovery -> Scrapling is strong
- a Scrapy replacement with stronger built-in browser/stealth tooling -> Scrapling is meaningfully closer to that category
- a hosted web-data API like Firecrawl -> Scrapling is not that by default, though its MCP server makes it feel closer in AI workflows
- an always-on website watcher/change tracker SaaS -> not built in

## Recommended wiki updates
- update [[scrapling]] with architecture, anti-bot details, AI/MCP positioning, and limitations
- create comparison page vs [[scrapy]] and [[firecrawl]]
- create entity pages for [[scrapy]] and [[firecrawl]] as comparison anchors