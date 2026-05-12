---
title: TheAhmadOsman
created: 2026-04-15
updated: 2026-04-27
type: entity
tags: [person, x-creator]
sources: [raw/articles/theahmadosman-agent-web-stack-2026-04-15.md, raw/articles/theahmadosman-inference-kernels-2026-04-26.md, raw/articles/theahmadosman-kernel-learning-path-2026-04-26.md, raw/articles/thread-TheAhmadOsman-2048608672348045540.md, raw/articles/homelab-private-cloud-ahmad-2026-05-01.md]
---

## Overview

X/Twitter creator focused on local LLM tooling and AI agent infrastructure. Posts practical stack guides for giving local models web access capabilities.

## Known Stacks

### Harbor + Open WebUI Stack (2026-04-03)

```
install Harbor → harbor pull unsloth/gemma-4-31B-it-GGUF:Q4_K_M → harbor up llamacpp searxng webui → open Open WebUI → load Gemma 4
```

Result: local model with a UI, web search (SearXNG), and a sandboxed full stack via Harbor (self-hosted AI platform).

### Agent Web Stack (2026-04-14)

Three-stage pipeline for agent web access:

```
SearXNG (candidate source discovery)
  ↓
Firecrawl (known-URL scrape and crawl)
  ↓
Camofox (browser fallback for JS/interaction)
```

Designed to be handed to an agent with instructions to self-setup.

## Related entities

- [[firecrawl]] — used for known-URL scraping
- [[scrapling]] — overlapping web scraping framework (adaptive, Cloudflare-aware)

## Sources

- `raw/articles/theahmadosman-agent-web-stack-2026-04-15.md`
