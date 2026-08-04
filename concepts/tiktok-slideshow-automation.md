---
title: TikTok Slideshow Automation
created: 2026-04-27
updated: 2026-08-04
type: concept
tags: [ai-content, content-automation, slideshow, tiktok]
sources: [raw/articles/alex-nguyen-tiktok-slideshow-automation-2047715075457507452.md, raw/articles/xarticle-no-bs-guide-to-ai-ugc-at-scale-2049286061105483868.md]
related_entity:
---

# TikTok Slideshow Automation

A content pipeline for generating and posting 30-50 TikTok slideshows per day using AI generation + Pinterest curation hybrid approach.

## Key Components

1. **Format reverse-engineering** with Codex GPT-5.5 - analyze viral slideshow screenshots to extract reusable JSON schema
2. **Hybrid image strategy** - ChatGPT Images 2.0 for hook slide + Pinterest scraped images for content slides (85% cost reduction)
3. **Text compositor** - Sharp + @napi-rs/canvas for overlay compositing
4. **Post queue** - BullMQ + Redis for scheduling across 50+ TikTok accounts via Postiz

## AI-persona cost branch

[[type-kshitij]]'s source uses a smaller persona-led variant: 1–2 Nano Banana persona images, 4–5 Pinterest images via [[apify]], and a local Sharp + Canvas compositor. It calculates `$0.04–$0.08` per slideshow, uses `$0.06` as the average, and estimates `$22/month` for 12 accounts posting one slideshow daily. The source recommends persona images in the first one or two slides so the asset feels like a moment from a recurring character's life rather than a generic scraped collage. These prices and scale claims are source-reported. ^[raw/articles/xarticle-no-bs-guide-to-ai-ugc-at-scale-2049286061105483868.md]

This is the slideshow path inside [[ai-ugc-persona-factory]]; the existing 30–50-post/day pipeline has a different throughput and cost model.

## Cost Economics

- Naive approach: $0.70-1.00 per slideshow × 30/day = $600-900/month
- Hybrid approach: $0.15 per slideshow × 30/day = $135/month

## Key Insight

The format (hook structure, pacing) is copyable. The visual language (fonts, colors) is adaptable. The content is original. Layer 1 is free IP to clone.

Related: Alex Nguyen, [[codex-gpt-5-5]], ChatGPT Images 2, Pinterest scraping strategy, BullMQ