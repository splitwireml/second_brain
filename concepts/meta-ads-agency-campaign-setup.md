---
title: Meta Ads Agency Campaign Setup (George Clements)
created: 2026-05-12
updated: 2026-05-12
type: concept
tags: [meta-ads, facebook-ads, instagram-ads, campaign-setup, agency, paid-ads, b2b, lead-gen]
sources: [raw/articles/xarticle-how-i-set-up-a-new-meta-ads-campaign-for-my-agency-2053250110545334519.md]
related_entity: [[george-clem]]
author: [[george-clem]]
---

# Meta Ads Agency Campaign Setup (George Clements)

A step-by-step campaign setup process for running Meta (Facebook/Instagram) paid ads campaigns for agency lead generation, documented by [[george-clem]] (founder of [[george-clem|Paid House]]) in an X Article published May 9, 2026.

## Core Thesis

The default Meta Ads Manager settings are optimised for Meta's revenue, not advertiser results. Agency owners must override these defaults at every level — campaign, ad set, and ad — to build a disciplined cold-traffic acquisition system that produces booked meetings at a predictable cost.

## Key Metrics: The "Million a Month" Column Preset

| Metric | Why It Matters |
|---|---|
| **Amount Spent** | Denominator for all meaningful calculations |
| **Results** | Conversion events (e.g., booked meetings) |
| **Unique Outbound CTR** | Most important indicator of ad compelling-ness; benchmarks: video 1.5–2%+ good, 2%+ great; static 3–4%+ |
| **CPM** | Traffic cost; affected by ad quality score; can be lowered by making better ads |
| **Hook Rate** | 3-second video plays ÷ impressions; want >20% |
| **Frequency** | Avg. views per person; want <1.5 on cold traffic; >3 signals TAM exhaustion |
| **Cost per Result** | The decide metric: can you acquire a client profitably at this cost? |
| **ROAS** | Final judge — if positive, keep the ad running regardless of other metrics |

## Campaign Structure

### Campaign Level

- **Naming convention:** `ABO/CBO – Offer Name – Launch Date`
- **Budget structure:** ABO (Ad Set Budget Optimisation) preferred over CBO for creative testing control; CBO risks Meta starving untested ad sets
- **Objective:** Leads

### Ad Set Level

**Settings to override:**

1. **Conversion Location:** Set to "Website" (single), not multi-conversion path
2. **Pixel + Event:** Select your pixel and schedule event (e.g., booked call)
3. **Dynamic Creative:** OFF — single ads produce cleaner attribution and better delivery than algorithm-mixed variants
4. **Daily Budget:** $100/day minimum per ad set ($200/day preferred for faster learning)
5. **Audience Definition:** Broad targeting — let Meta's algorithm find the audience; do NOT add interests or detailed targeting

**Broad + Specific:**

- **Age range:** Manually set to 25–55 (or actual buyer age range from last 20 customers)
- **Gender:** Restrict based on actual buyer gender distribution from customer data
- **Detailed Targeting:** Leave completely empty — no interests, no behaviours
- **Placements:** Restrict to Facebook Feed, Facebook Reels, Instagram Feed, Instagram Reels, Instagram Stories, Facebook Stories. **Turn OFF Audience Network** (third-party sites/apps producing garbage traffic that ruins attribution)

**Ad Set Naming:** `Schedule – Batch N – Country – Age Range` (e.g., `Schedule – Batch 1 – US – 25-55`)

### Ad Level

**Naming:** Numbered by batch — 101, 102, 103... for batch 1; 201, 202... for batch 2

**Recommended volume:** 20 unique creatives per ad set post-Andromeda (minimum 8–12 for production constraints)

**Settings:**
- **Instant Form:** Select "None" — instant forms produce lower lead quality than landing page traffic
- **Destination URL:** The specific landing page funnel URL, not the agency homepage
- **Site Links:** OFF — single funnel destination, no distractions
- **Primary Text:** Most important copy element (people see this first, before the headline)
- **Headline:** Secondary — appears below CTA button
- **CTA:** "Learn More" consistently outperforms alternatives for B2B agency offers
- **AI Improvements:** OFF — Meta's AI enhancements are consistently bad

## Performance Benchmarks (Post-Launch, Days 5–7)

| Signal | Action |
|---|---|
| Cost per result within target, CTR + hook rate healthy | Scale: increase budget 20–30% max per step |
| Cost per result dramatically over target, CTR/hook rate well below benchmark | Kill: replace with next batch |
| Borderline | Hold: wait for more data |

**Hit rate:** ~10% of ads become winners. The other 9 are necessary failures that produced data.

## Real Account Results

- Campaign spend: £177,800
- Booked meetings: 737 (Meta reported; higher via Hyros attribution)
- Impressions: 1.5 million
- Top-performing ad: £42,000 lifetime spend, 2% unique outbound CTR, 350,000+ impressions
- **2025 total:** £300k ad spend → £800k cash collected, ~£2M projected LTV from acquired clients

## Related Concepts

- [[paid-ads-agency-funnel]] — broader agency funnel strategy by [[george-clem]]
- [[retargeting-ads-framework]] — the 3 Meta custom audience retargeting system by [[george-clem]]
- [[four-layer-b2b-funnel]] — ColdIQ's 4-layer B2B demand generation architecture