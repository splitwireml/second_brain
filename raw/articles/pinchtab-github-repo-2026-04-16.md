---
title: Pinchtab Github Repo 2026 04 16
updated: 2026-04-16
source: https://github.com/pinchtab/pinchtab
date: 2026-04-16
type: github-repo
tags: [github, browser-automation, golang, ai-agents, cdp, headless-chrome, stealth, web-scraping]
---

# pinchtab/pinchtab — GitHub Repository

**Full name:** pinchtab/pinchtab
**URL:** https://github.com/pinchtab/pinchtab
**Stars:** 8,739 | **Forks:** 637
**Language:** Go
**License:** MIT
**Created:** 2026-02-15
**Pushed:** 2026-04-15
**Default branch:** main
**Open issues:** 9
**Topics:** browser-automation, cdp, golang, headless-chrome, orchestrator, stealth, web-scraping

## Description

High-performance browser automation bridge and multi-instance orchestrator with advanced stealth injection and real-time dashboard.

## README Summary

### What is PinchTab?

PinchTab is a standalone HTTP server that gives AI agents direct control over Chrome. ~15MB binary, no external dependencies.

### Installation

```bash
curl -fsSL https://pinchtab.com/install.sh | bash
# or
pinchtab daemon install

# Homebrew
brew install pinchtab/tap/pinchtab

# npm
npm install -g pinchtab
```

### Key Features

- **CLI or Curl** — Control via command-line or HTTP API
- **Token-efficient** — 800 tokens/page with text extraction (5-13x cheaper than screenshots)
- **Headless or Headed** — Run without a window or with visible Chrome
- **Multi-instance** — Run multiple parallel Chrome processes with isolated profiles
- **Self-contained** — ~15MB binary, no external dependencies
- **Accessibility-first** — Stable element refs instead of fragile coordinates
- **ARM64-optimized** — First-class Raspberry Pi support with automatic Chromium detection

### Security

- Server binds to `127.0.0.1` by default
- Dashboard session cookies are `Secure` only when served over HTTPS
- Sensitive endpoint families disabled by default
- `attach` disabled by default
- IDPI (Intelligent Detection Prevention) enabled with **local-only website allowlist** by default
- Remote/container/distributed setups are advanced operator-managed deployments

### Process Model

1. **Server** — main product entry point and control plane
2. **Bridge** — runtime that manages a single browser instance
3. **Attach** — advanced mode for registering externally managed Chrome instances

### Use Cases

- Headless navigation (agent task automation)
- Headed navigation with named Chrome profiles (authenticated sessions)
- Local container isolation (Docker sandboxing)
- Distributed automation (QA, testing, distributed browsing)

### Comparisons Made in README

- OpenClaw: only works inside OpenClaw
- Playwright MCP: framework-locked
- Browser Use: coupled to its own stack
- Vercel Agent Browser: tightly integrated into Vercel ecosystem
- WebMCP (Chrome): protocol-level vs standalone HTTP server

### License Discrepancy

README shows Apache 2.0 badge in README but GitHub API reports MIT license — verified MIT via LICENSE file.