---
title: AI UGC Ad Scaling System
created: 2026-04-13
updated: 2026-04-26
type: concept
tags: [marketing, automation, genai, monetization, method]
sources: [raw/articles/stijn-feijen-claude-seedance-makeugc-system-2026-04-13.md]
related_entity: [[makeugc]]
author: [[stijn-feijen]]
---

# AI UGC Ad Scaling System

## Definition

A short-form advertising workflow that treats AI-generated UGC videos as a daily testing system rather than as handcrafted creative work. In [[stijn-feijen]]'s framing, the stack is simple: Claude generates angles and scripts, [[seedance-2-0]] generates videos, and [[makeugc]] distributes, tests, and scales the winning variants.

## Core operating thesis

The source's main idea is that the operator should optimize for volume + data, not perfection. The job is not to manually edit videos or manage creators; it is to run a repeatable testing machine for hooks, creatives, and offers.

## Workflow

1. Choose a product with a clear problem, visual appeal, and TikTok/Reels fit.
2. Use Claude prompts to generate 20 high-converting ad angles.
3. Turn the best angles into 15-second UGC-style scripts with clear CTAs.
4. Generate video assets via [[seedance-2-0]] inside [[makeugc]].
5. Publish across TikTok, Instagram Reels, and Meta.
6. Launch daily tests with multiple hooks and creative variants.
7. Review CTR, watch time, and conversions.
8. Kill losers, duplicate winners, and scale budget/distribution on what works.

## Why it matters

This pattern compresses the traditional ad loop:

- strategy and scripting are handled by prompted LLM output
- production is handled by generative video
- trafficking and iteration are handled by workflow software

That makes creative throughput the main lever. If the system can actually sustain daily hook iteration, it becomes a practical bridge between [[prompt-engineering-patterns]] and revenue-oriented execution models like [[ai-workflow-setup-service]].

## Claimed economics

The source claims:

- 10-30 videos for beginners
- 100+ videos/day at scale
- ~45 minutes/day of operator review time
- month-1 potential of €1K-€5K
- €5K-€50K/month through volume + iteration

These are source claims, not verified performance results.

## Open questions

- How much of the claimed lift comes from better hooks versus sheer creative volume?
- Does MakeUGC expose enough performance data to support systematic creative learning loops?
- Is [[seedance-2-0]] materially better than other AI video models for direct-response ads, or just the model bundled into this stack?
- Which product categories actually tolerate fully AI-generated UGC without hurting trust or conversion?

## Related pages

- [[makeugc]] — execution layer for publishing, testing, and scaling
- [[seedance-2-0]] — video-generation layer
- [[stijn-feijen]] — source author
- [[prompt-engineering-patterns]] — upstream prompting logic for hooks and scripts
- [[ai-workflow-setup-service]] — adjacent business model for selling automation systems to clients
- [[ai-cartoon-ugc-monetization]] — specific AI cartoon UGC monetization sub-strategy within this broader ad system

## References

- Raw source: `raw/articles/stijn-feijen-claude-seedance-makeugc-system-2026-04-13.md`
- Original tweet: https://x.com/spwfeijen/status/2043692176689795202
