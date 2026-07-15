---
title: ColdIQ
created: 2026-04-14
updated: 2026-06-11
type: entity
tags: [agency, b2b, marketing, outbound, seo]
sources: [raw/articles/michlieben-coldiq-4-layer-funnel-2026-04-14.md, raw/articles/xarticle-how-to-replace-your-sales-tools-with-claude-code-w-2057868136268128388.md]
---

# ColdIQ

B2B marketing agency run by [[michel-lieben]]. ColdIQ crossed $7M ARR without raising external capital and specializes in coordinated multi-channel outbound, inbound, and ABM campaigns for B2B SaaS companies.

## Key Claims

- $7M+ ARR (self-funded, no venture capital)
- 330,000 unique website visitors in 2025
- 1,500+ meetings booked in 2025
- $4M in new ARR added in 2025
- 15x pipeline ROI on the AirOps case study ($7.8M pipeline from $233K ad spend)

## Service Offering

Full-funnel B2B marketing agency. Layer 1 (lead generation) through Layer 4 (close). Clients include AirOps, for whom ColdIQ broke a pipeline plateau of ~$536K/month, generating $7.8M in qualified pipeline and $1.5M in closed-won revenue.

## Claude Code Operating Model

The May 22 article describes ColdIQ's internal GTM stack as a set of agent folders rather than a bundle of disconnected sales tools:

- **Architect folder** — holds the frameworks for building skills, organizing folders, and standardizing code used by the other agents
- **Ad campaign agent** — turns spreadsheet rows into live campaigns across LinkedIn, Meta, and Google Ads
- **Engagement agent** — scrapes post engagers, enriches them, scores them, and routes them into sequencers or SDR queues
- **Campaign buildout agent** — tiers target accounts, finds contacts, waterfalls enrichment, writes copy, and pushes the full campaign into Instantly

The key implementation detail is that each successful API interaction becomes a reusable skill, which makes the GTM system more deterministic over time.

## Relationship to [[programmatic-seo]]

ColdIQ's SEO layer relies on programmatic page generation at scale — free mini-tools hosted on their own domain, each targeting a narrow ICP problem. Each tool ranks in organic search and feeds prospects directly into the lead capture layer. This maps directly to the programmatic SEO pattern documented in [[programmatic-seo]].

## Relationship to [[x-organic-b2b-sales]]

ColdIQ's LinkedIn strategy (150+ posts/month across 24 team members) is a coordinated content-as-reputation system. The coordinated multi-channel amplification (LinkedIn → cold email → retargeted ad hitting the same accounts) is the execution-layer implementation of the broad-hook-to-long-form conversion framework in [[x-organic-b2b-sales]].

## Relationship to [[offer-traffic-digital-asset-framework]]

ColdIQ's own growth is a live demonstration of the Offer × Traffic framework — strong offer, coordinated traffic, and owned workflow context compounding across repeated campaigns.
