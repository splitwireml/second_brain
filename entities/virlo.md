---
title: Virlo
created: 2026-09-22
updated: 2026-10-07
type: entity
tags: [product, platform, saas, content-marketing, content-automation, video, tiktok, instagram, youtube, mcp]
sources: [raw/articles/xarticle-jev-is-insane-for-marketing-2102054148925526206.md, raw/articles/xarticle-how-to-use-claude-for-content-marketing-so-well-it-2107130633029927004.md]
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

## Claude connector and recurring research (October 5, 2026 source)

Jaffa's later guide describes a **15M+** viral/outlier-video corpus across **TikTok, Instagram Reels, and YouTube Shorts**. Preserve that separately from the earlier source's 12.8-million claim; neither corpus size, platform coverage, availability, nor corpus growth was verified. The newer source's setup route is `claude.ai` → bottom-left profile icon → **Settings → Connectors** → **Add custom connector** → name **Virlo** → endpoint `https://dev.virlo.ai/api/mcp/mcp` → **Connect** → sign in with a Virlo account (or create one via the source's linked `https://dev.virlo.ai/?via=x`). Its Claude Code alternative is: ^[raw/articles/xarticle-how-to-use-claude-for-content-marketing-so-well-it-2107130633029927004.md]

```
claude mcp add --transport http virlo https://dev.virlo.ai/api/mcp/mcp
```

Then type `/mcp` and sign in. The article calls this a five-minute connection/collection setup and promotes hundreds of outliers about twenty minutes later, while the actual research prompt says return in **15–20 minutes** and accept **finalized**, not merely **completed**. These timing statements are source claims and interface distinctions, not measured service-level guarantees. ^[raw/articles/xarticle-how-to-use-claude-for-content-marketing-so-well-it-2107130633029927004.md]

The source requests Virlo's **agent playbook**, **intent cookbook**, and **keyword suggester**; one goal sentence, **7–12 multiword phrases**, ambiguous-word excludes, **hook and format analysis** and **Meta ads on**, and initially **no view or date filters**. Once finalized, read all videos and deduplicate, then gate `intent_match true`, `ai_provenance none`, `has_real_person true`, English/brand-safe/no reposts or compilations, and `is_sponsored false` except when studying ads (AI allowed only on request). Hook extraction is from the video's spoken hook field, else on-screen opener, never caption text. These are source-described signal names/values, not a validated API schema. ^[raw/articles/xarticle-how-to-use-claude-for-content-marketing-so-well-it-2107130633029927004.md]

A recurring copy runs **daily** with the same goal/phrases/excludes and analysis/Meta-ads settings; the author says it retains and sharpens phrases after each run and picks up breaking news. Monday uses the **last 7 days**, a brief **under 300 words**, **3** double-down items / **2** stops / **1** test with per-line video/link/views/followers, followed by **5 scripts**. Details and verbatim task contracts: [[content-research-agents]], [[content-research-agent-discovery-prompts]], [[content-research-agent-production-prompts]]. No connection or recurring agent was created here. The source gives no model/version, MCP tool names/schema, pagination, rank formula, thresholds, metric-missingness policy, scheduling/timezone configuration, or authentication protocol beyond account sign-in. ^[raw/articles/xarticle-how-to-use-claude-for-content-marketing-so-well-it-2107130633029927004.md]
