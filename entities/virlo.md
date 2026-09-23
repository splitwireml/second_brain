---
title: Virlo
created: 2026-09-22
updated: 2026-09-22
type: entity
tags: [product, platform, saas, content-marketing, content-automation, video, tiktok, instagram, youtube, mcp]
sources: [raw/articles/xarticle-jev-is-insane-for-marketing-2102054148925526206.md]
---

# Virlo

**Virlo** is a source-described content-research platform that creates niche-specific agents to collect and analyze short-form videos, then exposes filtered results through a dashboard or an MCP/API path. This page records one local promotional/operator article; availability, scale, performance, pricing, and product behavior are not independently verified.^[raw/articles/xarticle-jev-is-insane-for-marketing-2102054148925526206.md]

## Source-described interface and handoffs

The article gives two operator surfaces: a dashboard for browsing agent research and videos, or a Claude Code-style agent connected through the Virlo MCP server at `https://dev.virlo.ai/api/mcp/mcp`. It says a Virlo API key begins `virlo_tkn_`, a separate TypeSafe Jev API key is required for the judgment layer, and the configured agent ID is handed from setup into the per-video Jev pass. The source suggests passing its full Markdown article to Claude for strongest MCP/API results; this is source advice, not a tested integration recipe.^[raw/articles/xarticle-jev-is-insane-for-marketing-2102054148925526206.md]

## Research and clearance pipeline

Virlo is described as drawing from a database of more than 12.8 million viral TikTok, Instagram Reels, and YouTube Shorts videos. Before a video reaches a niche research run, a Jev-backed **Clearance** stage asks whether it actually matches the niche and whether its hashtags are misleading, using caption, hashtags, and transcript rather than hashtags alone. The article says the next stage benchmarks 80 performance signals and presents hook, format/topic, visual, production, speech, and product/sales intelligence. It explicitly assigns visual/production tagging and the 80-signal panel to Virlo, while Jev decides whether a video should enter the comparable sample.^[raw/articles/xarticle-jev-is-insane-for-marketing-2102054148925526206.md]

## Evidence boundary

The source claims 100,000 users, a 12.8-million-video corpus, 384-plus Bloom Nutrition results in under 20 seconds, and broad multi-client/solo use. It supplies no public schema, authentication flow, API version, rate limit, dataset provenance, signal definitions, scoring formula, model/version for visual or audio analysis, retention policy, or reproducible product evaluation.^[raw/articles/xarticle-jev-is-insane-for-marketing-2102054148925526206.md]

## Related

- [[content-research-agents]]
- [[jev]]
- [[dsqjaffa]]
- [[ai-video-virality-formats]]
