---
title: obscura
created: 2026-04-22
updated: 2026-04-25
type: entity
tags: [browser-automation, tools, ai-agents, web-scraping, rust]
sources:
  - raw/articles/nftcps-obscura-rust-browser-2046777680792850720.md
  - raw/articles/github-h4ckf0r0day-obscura-2026-04-25.md
url: https://github.com/h4ckf0r0day/obscura
related_entity: []
---

# obscura

Rust-based headless browser engine built for AI agent automation and web scraping. Drop-in replacement for Headless Chrome with Puppeteer/Playwright compatibility via Chrome DevTools Protocol (CDP). Single binary, no Chrome/Node.js dependencies.

## Setup

**Download binary:**
```bash
# Linux x86_64
curl -LO https://github.com/h4ckf0r0day/obscura/releases/latest/download/obscura-x86_64-linux.tar.gz
tar xzf obscura-x86_64-linux.tar.gz

# macOS Apple Silicon
curl -LO https://github.com/h4ckf0r0day/obscura/releases/latest/download/obscura-aarch64-macos.tar.gz
tar xzf obscura-aarch64-macos.tar.gz

# macOS Intel
curl -LO https://github.com/h4ckf0r0day/obscura/releases/latest/download/obscura-x86_64-macos.tar.gz
tar xzf obscura-x86_64-macos.tar.gz
```

**Build from source** (requires Rust 1.75+):
```bash
git clone https://github.com/h4ckf0r0day/obscura.git
cd obscura
cargo build --release

# With stealth mode (anti-detection + tracker blocking)
cargo build --release --features stealth
```

## Key Claims

| Metric | Obscura | Headless Chrome |
|--------|---------|-----------------|
| Memory | **30 MB** | 200+ MB |
| Binary size | **70 MB** | 300+ MB |
| Page load | **85 ms** | ~500 ms |
| Startup | **Instant** | ~2s |

## Features

- **CDP protocol** — Puppeteer and Playwright compatible without script changes
- **Stealth mode** — Per-session fingerprint randomization, 3,520 tracker domains blocked, anti-fingerprinting
- **CLI** — `fetch`, `serve` (CDP WebSocket server), `scrape` (parallel)
- **V8 JavaScript engine** — Real JS rendering

## Known Limitations

- **Notion** — ❌ blocked by bot detection. Renders HTML shell but Notion refuses to hydrate actual content; use [[camoufox]] instead

## Puppeteer Example

```javascript
const browser = await puppeteer.connect({
  browserWSEndpoint: 'ws://127.0.0.1:9222/devtools/browser',
});
const page = await browser.newPage();
await page.goto('https://news.ycombinator.com');
```

## Playwright Example

```javascript
const browser = await chromium.connectOverCDP({
  endpointURL: 'ws://127.0.0.1:9222',
});
```

## Architecture

- **Language:** Rust
- **JS engine:** V8
- **Protocol:** Chrome DevTools Protocol (CDP)
- **Stealth features:** GPU/screen/canvas/audio fingerprint randomization, `navigator.webdriver = undefined`, native function masking, tracker blocking across 3,520 domains

## CLI Reference

| Command | Description |
|---------|-------------|
| `obscura fetch <URL>` | Fetch and render a single page |
| `obscura serve --port 9222` | Start CDP WebSocket server |
| `obscura scrape <URL...>` | Parallel scrape with `--concurrency N` |

## Related

- [[pinchtab]] — HTTP-based browser control, Go binary
- [[camoufox]] — Anti-detection Firefox fork
- [[browser-harness]] — Chrome CDP harness
- [[firecrawl]] — AI web data API
- [[obscura-vs-camoufox]] — Full comparison (benchmarks, decision matrix)
- [[obscura-notion-query]] — Specific Notion test result
