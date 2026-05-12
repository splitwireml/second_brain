---
title: Four-Layer B2B Funnel
created: 2026-04-14
updated: 2026-04-14
type: concept
tags: [marketing, b2b, agency, outbound, seo, content-marketing]
sources: [raw/articles/michlieben-coldiq-4-layer-funnel-2026-04-14.md]
related_entity: [[coldiq]]
author: [[coldiq]]
---

# Four-Layer B2B Funnel

A B2B demand-generation architecture with four distinct layers, each feeding the next. Most B2B companies between $1M and $10M ARR only implement two of the four layers — generating leads and closing them — leaving a void where pipeline dies. The framework was documented by [[coldiq]] (Michiel Lieben) who grew ColdIQ to $7M ARR without external capital using this architecture.

## The Problem: The 2-Layer Trap

The standard B2B funnel (as implemented by most sub-$5M companies):

1. **Layer 1 only:** Generate awareness — cold email, LinkedIn posts, ads
2. **Layer 4 only:** Close — sales call, proposal, contract

The gap between awareness and the sales call is unaddressed. The prospect clicks a LinkedIn post on Tuesday and appears on the calendar three weeks later with no intermediate engagement, nurture, or scoring. They arrive cold and skeptical, already comparing the vendor with three competitors found the same week.

The core claim: if the only conversion mechanism is "book a call," every prospect who isn't ready for a call right now is lost — and most aren't ready right now. The 2-layer funnel is described as "a coin flip," not a system.

## The Four Layers

### Layer 1: Lead Generation

Attract prospects into the funnel through multiple coordinated channels, not a single pipe. Each channel feeds a different part of the funnel. The key insight is **channel coordination** — the same prospect is hit from multiple angles simultaneously, with each touchpoint reinforcing the others.

ColdIQ's Layer 1 (2025):
- 330,000 unique website visitors
- Five channels: automated outbound, LinkedIn publications, LinkedIn Ads, Google Ads, SEO
- 150+ LinkedIn posts/month across 24 team members
- Post-meeting amplification via Thought Leader Ads at ~$40 CPM to the same accounts targeted by outbound

**Mini-tools as SEO layer:** Instead of traditional content marketing, ColdIQ builds free mini-tools (deliverability checker, subject line analyzer, cold email grader) on their own domain. Each solves a narrow problem for the ICP, ranks in organic search, and feeds prospects into Layer 2's capture mechanisms. This layer accounts for ~30% of total website traffic.

### Layer 2: Lead Capture (First Missing Layer)

The mechanism that catches prospects who aren't ready for a sales call when they first encounter the company. Without this layer, every awareness touchpoint that doesn't immediately convert is wasted.

Three capture mechanisms:

1. **Lead magnets / mini-tools** — email exchange for useful tools. Built with Claude Code + Lovable, hosted on Vercel. Converts browsing into captured leads.

2. **De-anonymization technology** — reverse-identifies anonymous website visitors (Vector, Midbound) and LinkedIn engagers who never visited the site (Trigify, Jungler). All signals flow into a Clay table where leads are auto-scored, segmented, and tiered:
   - Tier 1: best fit / highest intent → manual personalized outreach
   - Tier 2: good fit / moderate intent → multichannel sequence (email + LinkedIn)
   - Tier 3: lower intent → automated email only

3. **Video sales letters (VSL)** — Wistia-hosted VSLs on Webflow that pre-sell the offer before the prospect ever speaks to a human. Qualification happens automatically via Default's routing (one input field → calendar if qualified, longer form if not) without a friction-heavy 12-field form.

### Layer 3: Lead Management (Second Missing Layer)

What happens after a lead is captured but before they're ready to convert. Content as a lead management tool — not a lead generation tool. The distinction: content builds trust that makes outbound campaigns convert better, rather than directly generating inbound leads.

Four components:
1. **Warm outreach campaigns** — targeted sequences to leads who already engaged with content or visited specific pages, scored via Clay + OpenAI/Claude. Messaging maps to demonstrated interest, not generic pitches.
2. **Newsletter nurture** — ~10,000 active subscribers via beehiiv, 40%+ open rates. Welcome sequence delivers the requested resource within 1 minute, followed by tool-stack education and steal-able workflows. Keeps ColdIQ in the prospect's mental orbit without selling.
3. **Content-as-re-engagement (dark post strategy)** — identifying leads who went dark and sending them a piece of content relevant to what they originally researched. Not "just checking in." ~20% of re-engagements attributed to this strategy.
4. **Review generation** — capturing testimonials at moments of maximum satisfaction during active engagements, used for social proof and re-engaging lapsed prospects.

### Layer 4: Close

The sales call, proposal, and negotiation. The claim is that the close itself doesn't change — what changes is who arrives at the close. Prospects pre-sold through Layers 1-3 arrive warm: they've encountered the brand 4+ times, understand the methodology, and in many cases already understand the offer.

## Key Numbers (ColdIQ, 2025)

| Metric | Value |
|--------|-------|
| Unique website visitors | 330,000 |
| Meetings booked | 1,500+ |
| New ARR added | $4M |
| Total ARR | $7M |
| Newsletter subscribers | ~10,000 |
| Newsletter open rate | 40%+ |
| Mini-tools/programmatic SEO traffic share | 30% |
| LinkedIn posts/month | 150+ (across 24 people) |
| AirOps pipeline ROI | 15x ($7.8M pipeline from $233K spend) |

## Relationship to [[programmatic-seo]]

ColdIQ's Layer 1 mini-tools strategy (free tools → organic traffic → lead capture) is a direct implementation of [[programmatic-seo]] at the funnel layer 1 position. Each tool solves a narrow keyword-relevant problem, ranks programmatically, and feeds captured leads directly into Layer 2.

## Relationship to [[x-organic-b2b-sales]]

ColdIQ's coordinated multi-channel amplification (LinkedIn post Monday → cold email Wednesday → retargeted ad Friday, all hitting the same accounts) is the execution-level implementation of the broad-hook-to-long-form [[x-organic-b2b-sales]] playbook. The 150+ posts/month across 24 team members mirrors the "broad hooks for reach" component; the layered nurture (Layers 2-3) mirrors the long-form reasoning and proof content that drives high-ticket inbound.

## Relationship to [[offer-traffic-digital-asset-framework]]

The four-layer funnel is an Offer × Traffic multiplication system. Strong offer (full-funnel B2B marketing service with demonstrated $7M ARR results) multiplied by coordinated five-channel traffic (not one channel, but five feeding different parts of the funnel simultaneously). The funnel architecture is the practical embodiment of the [[offer-traffic-digital-asset-framework]] principle that traffic is digital real estate that compounds when orchestrated correctly.

## Related Concepts

- [[llm-seo]] — Layer 3 reframes content as lead management rather than lead generation; Layer 1's mini-tools/programmatic SEO overlaps with LLM SEO patterns (AI-generated pages at scale)
- [[claude-cowork-seo-system]] — another content/SEO system documented in the wiki; ColdIQ's approach is more tool-centric and programmatic
