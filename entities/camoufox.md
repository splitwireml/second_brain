---
title: Camoufox
created: 2026-04-15
updated: 2026-04-25
type: entity
tags: [tools, ai-tools, open-source, browser-automation]
sources: [raw/articles/theahmadosman-agent-web-stack-2026-04-15.md]
---

## Overview

Camofox is a browser automation framework, the successor/fork of [camoufox](https://github.com/mjdixy/camoufox). Used as the browser fallback layer in agent web stacks — handles JavaScript-heavy pages and interactive elements that HTTP-based scraping cannot capture.

## Role in Agent Web Stack

In [[theahmadosman]]'s "Agent Web Stack," Camofox serves as the **browser fallback** layer — the third and final stage:

```
[[searxng]] (candidate discovery) → [[firecrawl]] (known-URL scrape) → Camofox (JS/interaction)
```

When SearXNG fails to extract content and Firecrawl cannot handle JavaScript-rendered pages, Camofox launches a real browser to interact with the page.

## Key Properties

- **Anti-detection** — built-in stealth mode to evade bot detection (Cloudflare, PerimeterX, etc.)
- **Firefox-based** — uses Firefox with custom anti-fingerprinting configurations
- **Headless or visible** — runs headless by default but supports visible browser for debugging
- **Python API** — `pip install camoufox` with a sync and async API
- **Session persistence** — maintains cookies and local storage across sessions

## Relationship to Other Tools

- Complements [[searxng]] (meta-search) and [[firecrawl]] (HTTP scraping) in a three-stage agent web pipeline
- [[scrapling]] overlaps functionally (adaptive web scraping with Cloudflare handling) but is primarily HTTP-framework-based; Camofox is a real-browser solution
- Contrast with Playwright/Selenium — Camofox is specifically hardened against anti-bot systems
- [[theahmadosman]] uses the phrase "Camofox: browser fallback for JS/interaction" — the key differentiator is JS rendering and interaction that HTTP tools cannot handle

## Sources

- `raw/articles/theahmadosman-agent-web-stack-2026-04-15.md`
- github.com/mjdixy/camoufox (or relevant fork)
