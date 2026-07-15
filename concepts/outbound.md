---
title: Outbound
created: 2026-05-31
updated: 2026-07-06
type: concept
tags: [b2b, cold-email, lead-gen, outbound, sales]
sources: [raw/articles/xarticle-building-a-3m-ai-sdr-team-2071370444285124950.md, raw/articles/xarticle-the-108010-rule-the-20-of-our-gtm-we-never-hand-to-2071586092223189382.md, raw/articles/xarticle-the-most-valuable-cold-outreach-masterclass-ever-c-2071980383520895262.md, raw/articles/xarticle-print-fck-you-money-selling-to-vc-funded-startups--2073585594857296349.md]
---

# Outbound

Proactive sales and outreach — cold email, LinkedIn, cold calling. The foundation of B2B [[lead-gen]] before inbound or organic channels mature.

## Channel Roles

Levi Munneke's June 2026 build guide adds a useful split that many outbound teams blur: [[cold-email]] and LinkedIn should not be treated as interchangeable send pipes. Email is the discovery layer because it can run wide, generate fast feedback, and reveal which industries, pains, and titles actually respond. LinkedIn is the warmer conversion layer because it carries more relationship context but much lower throughput. In that framing, email finds signal and LinkedIn closes it.^[raw/articles/xarticle-building-a-3m-ai-sdr-team-2071370444285124950.md]

## Operational Architecture

The same source describes outbound as a coordinated system rather than a single sequence:

- real rep identities and aged accounts matter more than clever copy because deliverability and platform trust are the limiting constraints
- each rep runs both a LinkedIn motion and a supporting email stack under the same name
- a shared CRM preserves ownership so replies from either channel stay attached to one operator and one conversation history
- AI handles research, reply drafting, and follow-through tasks humans usually drop at scale

This makes outbound less like one blast and more like a multichannel operating model that depends on identity continuity, routing discipline, and memory.

## Automation Layer

The source also sharpens where AI is most useful. The high-value automation is not merely generating copy; it is covering the follow-through gap after interest appears. Prospect enrichment before send, fast personalized draft replies, and [[n8n]] workflows for reminders and re-engagement make a cheap rep bench behave more like a disciplined SDR team.^[raw/articles/xarticle-building-a-3m-ai-sdr-team-2071370444285124950.md]

## Judgment Boundary

Alex Vacca's June 2026 10·80·10 rule adds a control-layer distinction to outbound. The first 10% stays human: decide who to target, what a strong-fit account looks like, and which angle to lead with. AI owns the middle 80%: research, enrichment, draft messages, and repetitive follow-through. The final 10% returns to the operator for quality control: cut hallucinated lines, reject off-tone copy, and decide whether the batch is good enough to send under the brand's name.^[raw/articles/xarticle-the-108010-rule-the-20-of-our-gtm-we-never-hand-to-2071586092223189382.md]

Vacca's warning is operational, not philosophical: if the middle runs without fences, a fully autonomous system can optimize straight into deliverability damage or bad-fit outreach. In this framing, the human job is to hold the targeting brief, the guardrails, and the final approval gate while the machine absorbs the labor.

## Deliverability as the hard constraint

Dimitar Angelov's June 2026 masterclass extends the outbound page from channel design into infrastructure discipline. The argument is blunt: [[cold-email]] performance starts with DNS and domain hygiene, not copy tweaks. Do not send from the main domain; use multiple dedicated sending domains per campaign, 2-3 inboxes per domain, 30 days of warmup, and strict daily send caps around 40-50 emails per inbox. In this framing, deliverability is the rate limiter that determines whether any targeting or copy experiment gets a fair read.^[raw/articles/xarticle-the-most-valuable-cold-outreach-masterclass-ever-c-2071980383520895262.md]

The same source adds a simple diagnostic ladder for underperforming outbound:

- low opens + high bounces -> deliverability problem
- healthy opens + weak replies -> copy or offer problem
- positive replies + weak booking rate -> reply-handling problem

That failure-mode split is useful because it prevents teams from treating every miss as a copy problem when the actual issue may be inbox placement, list quality, or slow operator follow-up.

## Signal-sourced targeting and reply handling

Angelov also sharpens how outbound lists should be built. Broad purchased lists are the low-intent, high-volume baseline, but the stronger motion comes from intent-sourced leads: people posting buying signals on LinkedIn, companies hiring for the exact role you replace, forum posts describing the relevant pain, or funding announcements that imply an immediate growth mandate. This makes outbound less about blasting a static ICP and more about routing attention toward accounts that have already emitted evidence of demand.^[raw/articles/xarticle-the-most-valuable-cold-outreach-masterclass-ever-c-2071980383520895262.md]

[[dra]] adds a narrower version of that funding-trigger rule for LinkedIn-led B2B selling. Recently funded startups are attractive because the raise simultaneously creates budget, investor pressure to grow, and a public event that makes the first message feel specific rather than generic. The strongest lead window is immediately after the round closes, especially when the raise is paired with active hiring or another signal that the company has already begun spending.^[raw/articles/xarticle-print-fck-you-money-selling-to-vc-funded-startups--2073585594857296349.md]

On execution, the article reinforces a minimalist copy model: specific first line, small front-end offer, one concrete proof point, and a soft ask. Follow-ups must add new information rather than merely bump the thread, and the highest-leverage operational target is response time on positive replies: during business hours, aim to answer in under 60 seconds before interest decays.

## Relationship to [[four-layer-b2b-funnel]]

This architecture fits inside the funnel's Layer 1 and Layer 3 mechanics. Email-wide testing produces the market signal, LinkedIn turns that signal into warmer conversations, and the CRM plus automation stack supplies the lead-management continuity that prevents duplicate touches and dead follow-up.

## Related Concepts

- [[lead-gen]] — outbound as lead generation
- [[cold-email]] — outbound channel
- [[linkedin-growth]] — LinkedIn as the lower-volume, higher-trust layer of the outbound mix
- [[dra]] — source operator documenting funding-triggered LinkedIn outreach into recently funded startups
- [[four-layer-b2b-funnel]] — broader B2B demand-gen system that gives outbound a capture and nurture context
- [[levikmunneke]] — source operator documenting AI-assisted SDR execution
- [[b2b]] — B2B outbound context
- sales — sales process
