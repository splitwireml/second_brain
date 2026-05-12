---
title: TikTok Slideshow Automation
created: 2026-04-27
updated: 2026-04-27
type: concept
tags: [tiktok, content-automation, slideshow, ai-content]
sources: [raw/articles/alex-nguyen-tiktok-slideshow-automation-2047715075457507452.md]
related_entity:
---

# TikTok Slideshow Automation

A content pipeline for generating and posting 30-50 TikTok slideshows per day using AI generation + Pinterest curation hybrid approach.

## Key Components

1. **Format reverse-engineering** with Codex GPT-5.5 - analyze viral slideshow screenshots to extract reusable JSON schema
2. **Hybrid image strategy** - ChatGPT Images 2.0 for hook slide + Pinterest scraped images for content slides (85% cost reduction)
3. **Text compositor** - Sharp + @napi-rs/canvas for overlay compositing
4. **Post queue** - BullMQ + Redis for scheduling across 50+ TikTok accounts via Postiz

## Cost Economics

- Naive approach: $0.70-1.00 per slideshow × 30/day = $600-900/month
- Hybrid approach: $0.15 per slideshow × 30/day = $135/month

## Key Insight

The format (hook structure, pacing) is copyable. The visual language (fonts, colors) is adaptable. The content is original. Layer 1 is free IP to clone.

Related: Alex Nguyen, [[codex-gpt-5-5]], ChatGPT Images 2, Pinterest scraping strategy, BullMQ