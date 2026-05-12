---
title: Agent Web Stack
created: 2026-04-15
updated: 2026-04-15
type: concept
tags: [agent, framework, automation]
sources: [raw/articles/theahmadosman-agent-web-stack-2026-04-15.md]
author: [[theahmadosman]]
---

## Definition

A three-stage web access pipeline for AI agents, designed to give local LLMs full web browsing capability through a Search → Extract → Interact workflow.

## The Three Layers

| Stage | Tool | Role |
|-------|------|------|
| 1. Search | [[searxng]] | Candidate source discovery — finds relevant URLs |
| 2. Extract | [[firecrawl]] | Known-URL scrape and crawl — extracts content from discovered URLs |
| 3. Interact | [[camoufox]] | Browser fallback for JavaScript/interaction — handles JS-rendered pages |

## Architecture Rationale

Each layer handles what the previous layer cannot:

- **SearXNG** handles candidate discovery (finding URLs worth scraping)
- **Firecrawl** handles structured content extraction from known URLs (markdown, metadata, links)
- **Camofox** handles JavaScript-rendered pages and interactive elements that require a real browser

This division-of-labor approach avoids overloading a single tool — SearXNG isn't trying to scrape, Firecrawl isn't trying to do JS rendering, and Camofox only kicks in when the first two fail.

## Design Pattern

The stack is designed to be **handed to an agent with instructions to self-setup** — the agent receives the tool trio and sets them up locally rather than relying on external APIs. This makes it suitable for:

- Air-gapped or privacy-sensitive environments
- Cost reduction (no per-call API fees for search or scraping)
- Full control over data handling

## Related Concepts
- [[scrapling]] — the adaptive web scraping framework that overlaps most directly with the extract layer (Firecrawl) in this stack
- [[three-tier-local-model-routing]] — related architecture pattern for local LLM stacks with specialized tool layers
- [[programmatic-seo]] — a concrete use case for agent web stacks (discovering keywords, scraping competitor content, extracting structured data at scale)

## Sources

- `raw/articles/theahmadosman-agent-web-stack-2026-04-15.md`
