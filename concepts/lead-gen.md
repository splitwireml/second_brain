---
title: Lead Generation
created: 2026-05-31
updated: 2026-10-07
type: concept
tags: [b2b, business, cold-email, lead-gen, outbound, sales]
sources: [raw/articles/post-brannonhogue-youre-supposed-to-throw-away-75-of-your-cold-email-2083597307375735213.md, raw/articles/xarticle-12-gtm-engineering-workflows-that-drive-revenue-fu-2107548563085689302.md]
related_entity: [[monetization]]
---

# Lead Generation

The practice of identifying and attracting potential customers (leads) who have expressed interest or fit ideal customer criteria. The foundation of B2B and services revenue.

## Key Channels

- **Outbound**: cold email, LinkedIn, cold calling, direct outreach
- **Inbound**: SEO, content marketing, viral loops
- **Paid**: Google Ads, LinkedIn Ads, display

## Qualification-First List Reduction

Brannon Hogue's local source treats lead generation as a quality filter before outreach: start with 5,000 emails, validate them twice without catch-alls, and reduce the list to roughly 2,900 valid addresses. Research prospects with “cheap ai search,” score them into tiers 1, 2, and 3, remove tier 3, and keep a reported 1,200 tier-1/tier-2 leads.^[raw/articles/post-brannonhogue-youre-supposed-to-throw-away-75-of-your-cold-email-2083597307375735213.md]

For a website-builder offer, the source's example signals are a poor website, growing staff count, and active growth-minded hiring. It recommends a free offer that solves a main business problem—not a generic “free audit”—while screening out freeloaders and prospects without budget; the solved first problem may expose a second, paid problem.^[raw/articles/post-brannonhogue-youre-supposed-to-throw-away-75-of-your-cold-email-2083597307375735213.md]

The source names Gemini or another research AI but gives no validator, catch-all detector, interface/API, model version, scoring rubric, prompt, exact offer, cadence, or conversion measurement. The counts and free-to-paid path are source-described rather than independently verified.^[raw/articles/post-brannonhogue-youre-supposed-to-throw-away-75-of-your-cold-email-2083597307375735213.md]

## 2026-10-06 Qualification and Revenue-Signal Gates

[[adamrahmangtm]] distinguishes owned-data leads (CRM Re-engagement, Champion Moves, Reply to Warm Call, Form Fill to Call), public-intent signals (Website De-anonymization, LinkedIn Inbound, Competitor Followers, Content Engagement, Competitor Reviews), and net-new market creation (Lookalike Audiences, Cold Email, Cold Calling). [[gtm-engineer]] carries the full trigger/tool/qualification/handoff taxonomy rather than replacing those twelve workflows with a generic lead list. ^[raw/articles/xarticle-12-gtm-engineering-workflows-that-drive-revenue-fu-2107548563085689302.md]

The spend/ownership gates differ by trigger: unchanged closed-lost blockers stay parked without credits; champion job moves need a second confirmation; forms and identified website visitors already belonging to customers or open deals route to their owner; LinkedIn non-fits receive no message; competitor followers exclude competitor employees; competitor-review campaigns exclude customers, open deals, and active sequences. Reviews are pulled through Apify from G2/Capterra/Trustpilot and Serper from Reddit; Claude Code clusters complaints, only seller-solvable complaints survive, and Sumble competitor-tool accounts are matched to a single relevant complaint. Review themes do not establish that a reviewer is the mapped account. ^[raw/articles/xarticle-12-gtm-engineering-workflows-that-drive-revenue-fu-2107548563085689302.md]

Lookalike Audiences derives the ICP from best HubSpot accounts/Gong calls, builds three DiscoLike website-seeded lookalike lists, qualifies before enrichment with Firecrawl site reading and Jev/OpenRouter scoring, then enriches, verifies twice, writes messaging, and routes by tier. Website De-anonymization uses RB2B's source-claimed roughly 1-in-10 to 1-in-5 US visitor identification, CRM ownership checks, pricing/repeat visits and Sumble hiring/tool changes; tier one reaches a rep in minutes via Slack, others get evergreen email. The coverage and performance are unverified source claims. ^[raw/articles/xarticle-12-gtm-engineering-workflows-that-drive-revenue-fu-2107548563085689302.md]

Form Fill to Call retains originating-page context for demo/contact/pricing forms, enriches person/company with a direct dial, routes fits now and customers/open deals to owners, and gives non-fits a useful response. Slack carries identity/request context, the rep calls within five minutes, and no answer triggers five days of short follow-ups from their own inbox. The article's Harvard Business Review nearly-7x comparison concerns within-an-hour responses versus an hour longer, not direct evidence of the five-minute SLA. Missing scoring prompts, score thresholds, validators, integrations, and linked playbook bodies remain unknown. ^[raw/articles/xarticle-12-gtm-engineering-workflows-that-drive-revenue-fu-2107548563085689302.md]

## Related Concepts

- [[b2b]] — lead gen in B2B context
- [[cold-email]] — cold email outreach
- [[monetization]] — converting leads to revenue
- [[agency]] — services that depend on lead gen

## Related
- [[google-maps-client-acquisition]] — lead-gen umbrella for client acquisition tactics
- [[outbound]] — lead generation through proactive B2B outreach
- [[brannon-hogue]] — source author of the qualification-first list workflow
