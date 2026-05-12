---
title: PinchTab
created: 2026-04-16
updated: 2026-04-16
type: entity
tags: [browser-automation, ai-agents, tools, open-source, golang]
sources: [raw/articles/heynavtoor-pinchtab-browser-automation-2026-03-03.md, raw/articles/pinchtab-github-repo-2026-04-16.md]
related_entity: [[heynavtoor]]
---

# PinchTab

**Website:** https://pinchtab.com | **Docs:** https://pinchtab.com/docs

Standalone HTTP server for AI agent browser control. ~15MB self-contained Go binary. Launches and manages Chrome instances, exposes an accessibility-first DOM tree with stable element refs, and exposes click/type/scroll/navigate via plain HTTP calls. No framework lock-in — any agent, any language, even curl.

## Key Facts

- **Binary size:** ~15MB (tweet said 12MB)
- **License:** MIT
- **Language:** Go
- **Stars:** 8,739 | **Forks:** 637
- **Created:** 2026-02-15
- **Releases:** 15 (actively maintained)
- **Default port:** 9867

## Core Features

- HTTP API for all operations (click, type, scroll, navigate, extract)
- ~800 tokens/page via `/text` endpoint vs ~10,000 for screenshots (13x cheaper)
- Smart diff mode — returns only what changed since last snapshot
- Built-in stealth mode bypassing bot detection on major sites
- Persistent sessions — log in once, stays logged across restarts
- Multi-instance orchestration with real-time dashboard
- Headed or headless — human does 2FA, agent takes over
- ARM64/Raspberry Pi support
- Docker container isolation option

## Security

- Binds to `127.0.0.1` by default
- IDPI (Intelligent Detection Prevention) with local-only allowlist by default
- Sensitive endpoint families disabled by default
- `attach` disabled by default
- **Known risks (per @mrscottiem):** unauthenticated HTTP port, flat-file credential storage, prompt injection attack surface when agent reads invisible webpage text

## Process Model

1. **Daemon/Server** — control plane, manages profiles and instances
2. **Bridge** — lightweight runtime for single browser instance
3. **Attach** — register externally managed Chrome instances

## Compared to Alternatives

| Tool | Lock-in | Protocol |
|------|---------|----------|
| PinchTab | None (standalone HTTP) | HTTP |
| OpenClaw browser | OpenClaw only | Internal |
| Playwright MCP | Framework-locked | SDK |
| Browser Use | Own stack coupled | SDK |
| Vercel Agent Browser | Vercel ecosystem | Integrated |
| WebMCP (Chrome) | Protocol-level | Protocol |

## Author

[[heynavtoor]] — Nav Toor, X creator who posted the viral announcement.

## Related Concepts

- [[agent-web-stack]] — similar three-stage browser access pattern (PinchTab is an alternative to Firecrawl/Camofox in that stack)
- [[scrapling]] — adaptive web scraping framework; PinchTab targets agent browser control vs scraping
- [[camoufox]] — browser automation with anti-detection; PinchTab competes in the same stealth browser space
- [[hermes-agent]] — could use PinchTab as browser backend via HTTP calls
