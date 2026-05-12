---
title: "obscura vs camoufox"
created: 2026-04-25
updated: 2026-04-25
type: comparison
tags: [browser-automation, web-scraping, performance, anti-detection]
sources:
  - raw/articles/nftcps-obscura-rust-browser-2046777680792850720.md
  - raw/articles/github-h4ckf0r0day-obscura-2026-04-25.md
participants:
  - [[obscura]]
  - [[camoufox]]
---

# obscura vs camoufox

Side-by-side comparison of two headless browser engines for AI agent web automation and scraping.

## Overview

| | **obscura** | **camoufox** |
|---|---|---|
| **Language** | Rust | Python |
| **Browser engine** | Custom V8 | Firefox (Gecko) |
| **Protocol** | CDP (Puppeteer/Playwright compatible) | Playwright sync/async API |
| **Binary size** | 57 MB (single binary) | Firefox (~200 MB) + Python deps |
| **Startup** | Instant | 2-5s |
| **License** | Open source | Open source |

## Benchmarks (local testing, macOS ARM64)

| | **obscura** | **camoufox** |
|---|---|---|
| example.com (cold) | **0.12s** | 2.18s |
| Hacker News | **1.6s** | 4.3s |
| Notion (JS-heavy) | ❌ blocked | ✅ 11s |

## Feature comparison

| Feature | **obscura** | **camoufox** |
|---|---|---|
| JavaScript rendering | ✅ | ✅ |
| Anti-detection (stealth) | ✅ Built-in fingerprint randomization + tracker blocking | ✅ Firefox hardened + Playwright stealth plugin |
| Session persistence | ❌ | ✅ Cookies, localStorage across runs |
| Screenshot | ❌ CLI only (planned) | ✅ Full page + element |
| CLI mode | ✅ `fetch`, `serve`, `scrape` | ❌ Python API only |
| CDP server mode | ✅ WebSocket CDP | ❌ |
| Parallel scraping | ✅ `--scrape --concurrency N` | ✅ Via Python async |
| Headless only | ❌ | ✅ Headless or headed |
| Works on Notion | ❌ Blocked by bot detection | ✅ Full render |
| Works on Google | ❌ JS errors | ⚠️ Works but slow |
| Works on HN / static sites | ✅ Fast | ✅ Works |

## Strengths

### obscura
- **Speed** — 10-20× faster cold start, 2-3× faster page loads
- **Zero dependencies** — single binary, no Node.js, Firefox, or Python required at runtime
- **CDP compatibility** — drop-in replacement for headless Chrome in existing Puppeteer/Playwright scripts
- **Parallel scraping** — built-in `scrape` command with concurrency flag
- **Lightweight for pipelines** — ideal for high-volume, low-latency fetch pipelines where anti-bot is not a concern

### camoufox
- **Maturity** — battle-tested Firefox hardening, well-documented, active community
- **Full Playwright API** — mouse, keyboard, file uploads, downloads, multi-context
- **Notion / anti-bot sites** — successfully renders content on sites that block headless Chrome
- **Session management** — cookie and localStorage persistence across runs
- **Debugging** — headed mode for visible browser inspection
- **JavaScript execution control** — fine-grained `waitForSelector`, `waitForFunction`, `evaluate`

## Weaknesses

### obscura
- **New and unproven** — v0.1.1, limited real-world testing
- **No screenshot** — `--screenshot` flag mentioned in docs but not implemented
- **No session persistence** — each run is fresh
- **Bot detection on aggressive sites** — Notion, Google, and similar detect and block it
- **Limited API** — CLI only, no Python/JavaScript API for fine-grained control

### camoufox
- **Startup latency** — 2-5s to launch Firefox + Playwright
- **Resource heavy** — full Firefox instance, ~200 MB+ memory
- **Python dependency** — requires Python 3.9+ with camoufox installed
- **No CLI** — always requires a Python script

## Architecture

### obscura
```
obscura binary (Rust + V8)
├── Serves CDP WebSocket on port 9222
├── CLI: fetch / serve / scrape
└── Stealth mode: fingerprint randomization + 3,520 tracker domains blocked
```

### camoufox
```
Python (camoufox library)
└── Playwright (manages Firefox)
    ├── Sync API: with Camoufox() as browser: ...
    └── Async API: async with Camoufox() as browser: ...
```

## Decision matrix

| Use case | Recommendation |
|---|---|
| High-volume static/HN-style pages | **obscura** |
| Notion, Confluence, Google Docs | **camoufox** |
| CDP pipeline (existing Puppeteer scripts) | **obscura** |
| Anti-bot sites (Cloudflare, PerimeterX) | **camoufox** |
| Quick one-off CLI fetch | **obscura** |
| Interactive debugging | **camoufox** |
| JS-heavy single-page apps | **camoufox** |
| Low-latency agent loops | **obscura** |
| Session-persistent login state | **camoufox** |

## Verdict

**obscura** excels as a fast, lightweight, CLI-first browser for agent pipelines hitting accessible sites. Its CDP compatibility means existing tooling works without changes, and its single-binary distribution is ideal for containerized environments.

**camoufox** is the workhorse for anything that hits anti-bot protection or requires the full Playwright API. Notion, Cloudflare-protected sites, and any workflow needing session persistence make camoufox the default choice.

**Practical rule:** Try obscura first for static sites. Fall back to camoufox when you see blocks or need features obscura doesn't have.
