---
title: "How Hermes Agent Can Save You 85% (Or More) in BG Task Token Cost"
source_type: transcription
url: https://youtu.be/NoF-YajElIM
uploader: Onchain AI Garage
date: 2026-04-21
duration: "18:04"
audio: raw/assets/2026-04-21-HowHermesAgent.mp3
transcription: raw/transcripts/2026-04-21-HowHermesAgent.md
created: 2026-04-21
updated: 2026-04-21
type: raw
tags: [hermes-agent, cost-optimization, inference]
---

# How Hermes Agent Can Save You 85% (Or More) in BG Task Token Cost

*Source: [Onchain AI Garage](https://youtu.be/NoF-YajElIM) — 2026-04-21, 18:04*

## Summary

Deep-dive on Hermes Agent's 8 auxiliary background models — hidden tasks that run silently on every request. Shows that the default `auto` config routes these through Gemini Flash 3 via OpenRouter, generating consistent background costs. Live demo proves 85% savings on compression alone (13¢ Opus → 1.9¢ Kimi K2). Covers all 8 tasks, per-task model recommendations, local model configuration, and the config file location.

## Key Claims

- 8 auxiliary tasks run silently on every Hermes request
- Default `auto` routes through OpenRouter → New Portal → Codex → Gemini Flash 3
- Compression fires 10–20x/day for heavy users
- At 15 compressions/day: Opus = $60/mo, Kimi K2 = $9/mo, Local = $0/mo
- Config location: `~/.hermes/config.yaml`, `auxiliary:` section

## Timestamps

- 0:00–6:00 — Introduction: what auxiliary models are, why they matter
- 6:00–10:45 — The 8 tasks explained (compression, web extract, vision, flush memories, session search, skills hub, MCP dispatch, approval)
- 10:45–14:10 — Config file location and per-task model configuration
- 14:10–18:04 — Live demo: 50K token compression with Opus (13¢) vs Kimi K2 (1.9¢)

## Entities

- [[hermes-agent]] — The agent being optimized
- [[onchain-ai-garage]] — Channel/uploader

## Concepts

- [[hermes-auxiliary-model-configuration]] — The main concept page for this topic
