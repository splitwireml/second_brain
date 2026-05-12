---
title: "obscura vs camoufox: Notion JS rendering"
created: 2026-04-25
updated: 2026-04-25
type: query
tags: [browser-automation, web-scraping, performance]
sources: []
question: "Can obscura render Notion pages that require JavaScript?"
answer_status: answered
related_pages:
  - [[obscura]]
  - [[camoufox]]
---

## Question

Can obscura render Notion pages that require JavaScript, or does it fail like a standard headless browser?

## Answer

**obscura fails on Notion.** It fetches the page, runs JavaScript, but Notion's bot detection identifies it as a headless browser and refuses to hydrate the actual content. The `<div id="notion-app">` remains empty even with `--stealth` and 15s wait.

### Test details

- **URL:** `https://cactus-diploma-d38.notion.site/How-to-Create-Ads-with-AI-Animated-Objects-Videos-31756c8bc0b080a4b02fe2c2c2517a6b?pvs=149`
- **obscura result:** "JavaScript must be enabled" noscript fallback — Notion detected headless mode despite `--stealth` flag. Page loads in ~3.5s but content is a JS-block notice.
- **camoufox result:** Full rendered content — 1,620 lines including the full article text ("How to Create Ads with AI Animated Objects Videos...") in 11s.

### Why obscura fails on Notion

Notion runs aggressive bot detection that specifically targets headless browser signatures. The `--stealth` flag in obscura provides fingerprint randomization and tracker blocking, but Notion's detection goes deeper — it checks for headless-specific JS globals and Chrome DevTools protocol exposure.

### Practical implication

For any Notion-based content (documentation, wikis, course materials), **camoufox is required**. obscura cannot substitute.

## Verdict

obscura: ❌ fails on Notion  
camoufox: ✅ renders fully
