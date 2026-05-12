---
title: Paperclip Heartbeat Cost Optimization
created: 2026-04-12
updated: 2026-04-12
type: concept
tags: [agent, inference, optimization, orchestration]
sources: [raw/articles/aronprins-paperclip-heartbeats-2026-04-11.md]
author: [[aron-prins]]
---

# Paperclip Heartbeat Cost Optimization

## Overview

A cost optimization technique for [[paperclipai-paperclip]] deployments: disable agent heartbeat polling intervals, which generate thousands of wasteful token-spent wake-ups per week with no productive work.

Heartbeats cause agents to poll for work regardless of whether any exists. Each wake-up costs tokens. Five agents polling every 5 minutes generate ~2,400 useless runs per week — most returning "No tasks. Going back to sleep."

## The Problem

Paperclip agents ship with heartbeats OFF by default, but it's tempting to enable them. A ticking agent *looks* productive — green dots, regular heartbeat icons, buzzing dashboard. But each tick is a cost.

**Dashboard gaslight:** Pausing an agent stops it completely (won't respond to work, routines, or comments). Heartbeat OFF keeps it quiet but ready.

## The Three Agent Types

| Type | Description | Heartbeat |
|------|-------------|-----------|
| **Task agents** (90%+) | Wait for work to arrive (CEO, writer, researcher) | OFF |
| **Monitoring agents** (rare) | Poll external systems with no webhook | ON at hourly minimum |
| **Burst agents** (rare) | Respond to unpredictable events | Usually better as webhooks |

## Routines vs Heartbeats

**Heartbeat:** Fires regardless of work existence. Polls on interval.

**Routine:** Scheduled job with cron trigger. Creates a task that wakes the agent. No polling.

Use routines for:
- Morning standup summary (weekdays 9am)
- Weekly metrics rollup (Monday 8am)
- Monthly cleanup pass (1st of month)

## The Fix

1. Open the agent
2. Find "Run Policy" in Configuration tab
3. Toggle "Heartbeat on interval" OFF

Only enable heartbeat for agents polling systems with no webhook (RSS, email without push, polling-only APIs) — and set interval to hourly minimum.

## 60-Second Audit

Count agents with heartbeat intervals under 15 minutes. Any beyond 2 (neither polling external systems) is a leaky faucet.

## Related Concepts

- [[ai-cost-optimization]] — broader framework for cutting AI costs (RTK, Caveman, Bleap)
- [[paperclipai-paperclip]] — the platform this optimization applies to
- [[paperclip-orchestrator]] — Paperclip as AI orchestrator ("CEO agent")
- [[vibe-kanban-agent-spawning]] — alternative agent lifecycle management

## Source

- [[aron-prins]] — Paperclip user who documented ~$ hundreds/month savings across three companies
