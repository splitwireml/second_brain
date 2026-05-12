---
title: AI Lead Gen Agent
created: 2026-05-07
updated: 2026-05-07
type: concept
tags: [ai-agent, automation, lead-gen, hermes-agent, memory, workflow, outbound, b2b]
sources: [raw/articles/michel-lieben-ai-lead-gen-agent-hermes-2051707320699396454.md]
related_entity: [[michel-lieben]]
---

# AI Lead Gen Agent

Self-improving AI lead generation agent architecture built on [[hermes-agent]], demonstrated by Michel Lieben (@MichLieben) via Max Mitcham's (Trigify) live deployment. The system writes content, runs prospecting, books meetings, and updates its own skills based on performance data.

## Core Architecture

### Wikipedia-Graph Memory

Agent memory structured as markdown files in Obsidian, linked like a Wikipedia graph — each concept is a file, each link is an edge. The agent walks the graph before answering anything, picking up related context across multiple anchor points.

[[hermes-agent]] adds an active layer on top: auto-creates new skill files for recurring tasks, auto-creates new memory files for things kept referencing, and updates both based on actual usage patterns. After two weeks, the graph reflects how the operator runs their business.

### Content Engine

Three-input, one-output content system:

- **Signal layer**: Monitor X, LinkedIn, YouTube, Substack for trends gaining steam and format-level patterns (hooks, length, structure, thumbnails, opening lines)
- **Understanding layer**: Pull from longer-form content (Substack articles, podcast transcripts, YouTube videos) to build depth
- **Internal context layer**: Connected to Fireflies (sales calls), Granola (internal team calls), Slack, email, and Stripe — drafts pull from actual conversations, customer base, and product behavior

Output assembles all three layers into a draft Substack post, LinkedIn post built on a trend plus internal data, and YouTube script structured around patterns seen across 50+ videos in the category.

### Self-Learning Loop

The compounding core. A harness runs a cron over performance data (reply rates, content engagement, meeting bookings), generates hypotheses based on patterns, runs experiments, logs results, and updates beliefs before asking for human approval via Slack.

Two design rules:
1. Patterns, not points — a single viral post doesn't trigger a belief update; the same pattern must repeat enough times to clear a threshold
2. Beliefs are version-controlled — when a new experiment contradicts an old belief, the belief updates

After two months, the agent has dozens of validated beliefs about the audience, formats, market, and customer base that inform every new piece of content and outbound campaign.

### AI SDR (Sales Development Representative)

Same architecture running a sales motion. Two signal sources:

- **External signals**: Substack, X, Hacker News, LinkedIn for engagement on relevant topics, competitor mentions, funding rounds, role changes, company changes, hiring spikes
- **Internal signals**: Onboarding drop-off, spend thresholds, upsell candidates, churn risks, hiring signals from existing customer base

Once a lead clears qualification, the workflow runs: API query → enrichment (Lead Magic, Surfe) → compose (brain pulls from past calls, product context, accumulated copywriting patterns) → route/send → feed results back (each outcome updates beliefs about which signals, copy, and sequences produce pipeline).

## Key Tools in Stack

- **Harness**: Hermes Agent (~90% of work), OpenClaw (~10% for heavy tool-calling)
- **Models**: Codex 5.4 ($200/month plan) for heavy reasoning/coding, Claude Code for front-end/lighter tasks
- **Memory**: Obsidian (Wikipedia-graph brain), free
- **Signal data**: Trigify for social and intent monitoring
- **Email enrichment**: Lead Magic and Surfe (run two in parallel)
- **Outreach**: Instantly for cold email at scale
- **CRM**: Any CRM with full API access (Attio at ColdIQ)
- **Call recordings**: Fireflies (sales calls), Granola (internal team calls)
- **Interface**: Warp terminal, Slack, Discord

## Related Concepts

- [[hermes-memory-architecture]] — Tony Simons' 11-layer memory stack for Hermes
- [[context-os]] — Layered memory infrastructure for AI agents
- [[hermes-agent]] — The orchestrator platform
- [[api-led-gtm]] — Michel Lieben's related GTM methodology
- [[four-layer-b2b-funnel]] — ColdIQ's B2B demand-gen architecture
- [[content-automation]] — Automated content creation workflows
