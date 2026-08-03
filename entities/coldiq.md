---
title: ColdIQ
created: 2026-04-14
updated: 2026-08-03
type: entity
tags: [agency, b2b, marketing, outbound, seo]
sources: [raw/articles/michlieben-coldiq-4-layer-funnel-2026-04-14.md, raw/articles/xarticle-how-to-replace-your-sales-tools-with-claude-code-w-2057868136268128388.md, raw/articles/xarticle-the-complete-cold-email-playbook-for-2026-its-a-di-2083199326004838508.md]
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

## 2026-08-03 Cold Email Playbook

The new source adds a source-described ColdIQ operating pattern: attach a LinkedIn touch from a real profile to every email sequence, mine first-degree post engagement weekly, and use engagement topics as personalization signals. Its reported client comparison says multi-channel clients stay 2.5x longer than email-only clients; the figure is not independently audited.^[raw/articles/xarticle-the-complete-cold-email-playbook-for-2026-its-a-di-2083199326004838508.md]

The source's proprietary-signal examples are operational rather than vendor-catalog abstractions: merge the team's spam folders into a target list through [[lemlist]]; watch for target decision makers connecting with competitor reps; notice sudden Meta ad-budget or web-traffic spikes; and identify missing DMARC. ColdIQ's described signal-discovery method is to call the last 20 customers, read sales-call transcripts for repeated sentences, and target a public data point when seven of ten prospects name the same trigger. Michel says the spam pattern became one of ColdIQ's targeting rules after AI-post engagement and booked-call evidence pointed to different problems.^[raw/articles/xarticle-the-complete-cold-email-playbook-for-2026-its-a-di-2083199326004838508.md]

The source also describes GTM engineers prompting an entire campaign build, leaving for breakfast, and returning about 30 minutes later to review a finished draft with the list uploaded and every touchpoint placed. It reports that around 1,500 companies already run Lemlist through Claude each month. These are source-described workflow and adoption claims; the source does not specify the prompt, model version, API schema, uploaded-list format, or touchpoint configuration.^[raw/articles/xarticle-the-complete-cold-email-playbook-for-2026-its-a-di-2083199326004838508.md]

## Relationship to [[programmatic-seo]]

ColdIQ's SEO layer relies on programmatic page generation at scale — free mini-tools hosted on their own domain, each targeting a narrow ICP problem. Each tool ranks in organic search and feeds prospects directly into the lead capture layer. This maps directly to the programmatic SEO pattern documented in [[programmatic-seo]].

## Relationship to [[x-organic-b2b-sales]]

ColdIQ's LinkedIn strategy (150+ posts/month across 24 team members) is a coordinated content-as-reputation system. The coordinated multi-channel amplification (LinkedIn → cold email → retargeted ad hitting the same accounts) is the execution-layer implementation of the broad-hook-to-long-form conversion framework in [[x-organic-b2b-sales]].

## Relationship to [[offer-traffic-digital-asset-framework]]

ColdIQ's own growth is a live demonstration of the Offer × Traffic framework — strong offer, coordinated traffic, and owned workflow context compounding across repeated campaigns.
