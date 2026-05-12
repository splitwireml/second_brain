---
title: Hermes Ultimate Analyst
created: 2026-05-05
updated: 2026-05-05
type: concept
tags: [hermes-agent, productivity, ai-agent, workflow-automation]
sources: [raw/articles/xarticle-hermes-as-the-ultimate-analyst-ive-found-the-gist--2051214993719427258.md]
related_entity: [[hermes-agent]]
author: [[0xJeff]]
---

# Hermes Ultimate Analyst

Using Hermes Agent as a personal investment analyst with persistent memory, daily briefings, and portfolio tracking.

## Overview

0xJeff's setup for using Hermes as an investment analyst. The core moat is data/context — Hermes remembers investment theses, preferences, risk appetite, and current positions across crypto, equities, and prediction markets.

## Key Components

### Daily Briefings

- **Tech Briefing**: Tracks @SemiAnalysis_ and other accounts
- **Macro Briefing**: Tracks @KobeissiLetter and news sources
- **X Bookmark Briefing**: Queries bookmarks from last 24hr with priority scoring
- **Top 5 Daily Synthesis**: Reflects on all briefings and surfaces top insights
- **Polybond Morning Brief**: Surfaces potential insiders, sharp signals, and trends from Polymarket dashboard

### Investment Tracking

Hermes updates daily on key stock prices and shares stress test analysis. Key differentiator: Hermes has context on:
- 3 key investment theses
- Personal preferences
- Risk appetite
- Current positions (crypto, equities, prediction markets)
- Rationale for investments

This allows tailored research that normal LLMs cannot provide.

### Memory Architecture

Daily loop:
1. Cron jobs run
2. Hindsight ingests insights
3. Pull patterns & synthesize across any time period
4. Recalls past sessions and draws conclusions

### Setup Stack

- **$20/month**: Claude Pro for dashboard maintenance
- **~$60/month**: DeepSeek API for Hermes (~$2/day during discount period)
- **OpenCode CLI**: Recommended harness for first-time Hermes setup ($5 first month)

### Platform Choice

- Discord: Good for text but no visuals or artifacts
- OpenWebUI: Unlocks full ChatGPT/Claude-like experience with HTML previews and visual explainers

## Why It Works

The moat is in the data/context, not the model. Hermes compounds knowledge over time while maintaining investment theses, preferences, and positions.

## Related Concepts

- [[hermes-skills-workflow]] — Original three skill patterns (insights fetching, bookmark breakdown, reflection)
- [[hermes-memory-architecture]] — Tony Simons' 11-layer memory stack
- [[context-os]] — Layered AI agent memory approach
- [[hermes-agent]] — The platform being used
