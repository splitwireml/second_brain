---
title: ReelMeal
created: 2026-04-18
updated: 2026-04-18
type: concept
tags: [idea, mobile-apps]
sources: []
---

# ReelMeal

## What It Is

A kitchen utility app that transforms YouTube Shorts into structured, interactive cooking guides. Uses the YouTube IFrame API for full programmatic control (seek, pause, loop) combined with multimodal AI to extract ingredients, steps, and timestamps from Shorts video content.

## Problem

- **Pace mismatch**: 60-second cooking Shorts move too quickly for real-time cooking without constant pausing
- **Manual friction**: Touching screens with messy hands to pause/rewind
- **Data fragmentation**: Ingredients and quantities buried in captions or spoken aloud

## Target Customer

- Home cooks who follow recipe Shorts on YouTube
- People who cook while watching video tutorials on their phone/TV
- Frequency: regular home cooks who want to follow along, not just passively watch

## Monetization Hypothesis

- **Affiliate revenue**: Deep-links to grocery delivery (Blinkit, Zepto, Instashop) on ingredient lists — conversion on "add to cart" clicks
- **Saved recipe library**: Free tier with limit, premium for unlimited saves
- **Shopping cart integration**: Take a cut of affiliate links placed in the cart

## Why Now

- YouTube IFrame API provides full programmatic video control (seek, loop) — TikTok/Instagram don't expose this
- Multimodal LLMs (Gemini) can now extract structured JSON from video frames + audio in real-time
- Shorts format is dominant for recipe content but lacks structured data — gap between viral reach and usable format

## Core Features (MVP)

1. **URL Ingestion**: Paste YouTube Shorts URL → AI extracts ingredients, quantities, step-by-step instructions, and per-step timestamps
2. **Mise en Place Checklist**: Structured ingredient list with checkoff; deep-links to add missing items to grocery apps
3. **Step Cards with Video Sync**: Large-format cards, one step at a time; tapping a card uses `player.seekTo()` to jump video to that step's timestamp
4. **Loop Step**: Option to loop the specific video segment for the current step until user advances
5. **Voice Navigation**: "Next step" / "Repeat that" / "What's next?" via voice commands for hands-free cooking
6. **Recipe Library**: Save cleaned-up recipes for later

## Technical Constraints

- **YouTube-only**: Exclusive to Shorts for full IFrame API control — TikTok/Instagram are walled gardens that don't expose seek/loop APIs
- **AI Extraction**: Multimodal LLM processes video to generate structured JSON (ingredients, steps, timestamps)
- **Error risk**: AI timestamp accuracy — off by 10s breaks cook-along trust; error recovery unspecified

## What's Unclear

- **Viral mechanism**: No clear spread loop identified — who shares this and why? Recipe creators or home cooks?
- **Timestamp accuracy**: No defined error recovery when AI misreads a step; real-world accuracy rate unknown
- **Distribution**: YouTube Shorts viewers are scroll behavior — how does the app get discovered?
- **Affiliate conversion**: Grocery deep-links only convert if user is in buying mode; top-of-funnel leak likely high
- **Retention**: What % of users return to cook a saved recipe?

## Next Step

- Validate viral/spread hypothesis before advancing to build
- Test AI timestamp accuracy on a sample of recipe Shorts
