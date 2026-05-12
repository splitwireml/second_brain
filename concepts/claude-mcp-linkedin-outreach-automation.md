---
title: Claude MCP LinkedIn Outreach Automation
created: 2026-04-13
updated: 2026-04-13
type: concept
tags: [automation, agent, marketing, llm]
sources: [raw/articles/pierreeliottlal-claude-mcp-linkedin-2026-04-12.md]
related_entity: [[gojiberry-ai]]
author: [[pierreeliottlal]]
---

# Claude MCP LinkedIn Outreach Automation

Automated LinkedIn lead generation and outreach by connecting Claude to LinkedIn via a third-party MCP execution layer (Gojiberry.ai).

## Core Mechanic

Claude acts as the reasoning engine — it finds high-intent leads, analyzes their intent signals and online activity, and crafts personalized outreach messages. Gojiberry.ai serves as the MCP-powered execution layer that bridges Claude to LinkedIn's write APIs, enabling automated campaign launching without manual CSV exports or manual InMail.

The workflow loop:
1. **Find** — Claude surfaces leads matching ICP from across the web via Gojiberry's lead database
2. **Enrich** — Claude deep-dives into each lead's profile and recent activity
3. **Write** — Claude generates personalized messages based on real-time intent signals
4. **Launch** — Campaign is launched in one click within Gojiberry
5. **Analyze** — Claude reviews campaign performance and recommends optimizations

## Why This Pattern Works

Traditional outbound breaks the feedback loop: you export lists, craft messages blind, send, and wait. By the time you understand what worked, the opportunity is gone. Claude collapses this by operating on live data — it sees the same dashboards the marketer sees, and can reason across them in natural language.

The MCP bridge (Gojiberry) solves the API access problem: Claude cannot connect to LinkedIn directly, so Gojiberry acts as the authorized execution layer with LinkedIn OAuth already connected.

## Components

- **Claude Pro** ($20/mo) — reasoning, lead analysis, message generation
- **Gojiberry.ai** — MCP server + LinkedIn execution layer; stores OAuth, handles campaign operations
- **LinkedIn** — outreach platform; Gojiberry connected via official LinkedIn OAuth

## Metrics Claimed

- 2–5 meetings/day
- Replaces 2–5% reply-rate manual outreach

## Relationship to Other Concepts

- [[ai-cost-optimization]] — outreach at scale reduces cost per meeting booked
- [[ai-workflow-setup-service]] — this pattern is itself a sellable AI workflow service ($500 entry + $500–5K/month retainers)
- [[offer-traffic-digital-asset-framework]] — LinkedIn outreach generates traffic/leads; meetings booked are Offer × Traffic in action

## Source

> How I Book 2–5 Meetings/Day Using Claude MCP + LinkedIn — Pierre-Eliott Lallemant (@pierreeliottlal), 2026-04-12
