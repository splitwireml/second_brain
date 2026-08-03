---
title: Outbound
created: 2026-05-31
updated: 2026-08-03
type: concept
tags: [b2b, cold-email, lead-gen, outbound, sales]
sources: [raw/articles/xarticle-building-a-3m-ai-sdr-team-2071370444285124950.md, raw/articles/xarticle-the-108010-rule-the-20-of-our-gtm-we-never-hand-to-2071586092223189382.md, raw/articles/xarticle-the-most-valuable-cold-outreach-masterclass-ever-c-2071980383520895262.md, raw/articles/xarticle-print-fck-you-money-selling-to-vc-funded-startups--2073585594857296349.md, raw/articles/xarticle-the-fastest-path-from-zero-to-10kmonth-online-righ-2079543867683025123.md, raw/articles/xarticle-the-complete-cold-email-playbook-for-2026-its-a-di-2083199326004838508.md, raw/articles/post-brannonhogue-youre-supposed-to-throw-away-75-of-your-cold-email-2083597307375735213.md, raw/articles/xarticle-how-to-target-enterprise-companies-on-linkedin-and-2083725262890357129.md]
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

## Qualification Before Outbound

Brannon Hogue's source adds a deliberately wasteful pre-send filter: begin with 5,000 emails, validate twice with no catch-alls, and keep roughly 2,900 valid addresses. Use “cheap ai search” to research prospects, then score them into tiers 1, 2, and 3 and remove tier 3, leaving a reported 1,200 tier-1/tier-2 leads.^[raw/articles/post-brannonhogue-youre-supposed-to-throw-away-75-of-your-cold-email-2083597307375735213.md]

The source's website-builder example qualifies accounts through a poor website, growing staff count, and active growth-minded hiring. It then pairs fit with an offer gate: give away a complete solution to a main business problem rather than a generic “free audit,” reject freeloaders and no-budget prospects, and turn the second problem revealed by the free work into the paid engagement.^[raw/articles/post-brannonhogue-youre-supposed-to-throw-away-75-of-your-cold-email-2083597307375735213.md]

The local evidence does not provide the validator, catch-all detection, research interface/API, Gemini version, scoring rubric, prompts, exact offer, campaign cadence, sending stack, or conversion data. The list counts and free-to-paid progression are source-described claims, not independent benchmarks.^[raw/articles/post-brannonhogue-youre-supposed-to-throw-away-75-of-your-cold-email-2083597307375735213.md]

## 2026-08-03 ColdIQ Seven-Step Refinement

Michel Lieben's source keeps the existing email-versus-LinkedIn split but makes it a seven-step operating sequence: enrich every row and segment by ICP; attach a real-profile LinkedIn touch to every email sequence; mine first-degree post engagement weekly; let AI handle scraping, enrichment, list building, ICP scoring, intent detection, and campaign analytics while humans keep the words; reverse-engineer proprietary signals from customers and sales-call transcripts; hand-write 35–50 messages and prove a pattern across 50 sends before scaling; use expiring pattern interrupts; and close the loop through meeting transcripts, sequencer events, CRM outcomes, and MCPs in [[claude-code]]. The source reports a 2.5x retention difference for multichannel clients over email-only clients; this is a source claim.^[raw/articles/xarticle-the-complete-cold-email-playbook-for-2026-its-a-di-2083199326004838508.md]

Its signal examples extend the existing intent-sourcing cluster: team spam folders merged into a target list via [[lemlist]], competitor-rep connection activity, sudden Meta ad spend, web-traffic spikes, and missing DMARC. The reusable discovery loop is last-20-customer calls → repeated sales-transcript sentence → public data point → targeting rule; the source says seven of ten prospects naming the same trigger is the threshold for acting on it. This is a method described by the source, not a validated universal threshold.^[raw/articles/xarticle-the-complete-cold-email-playbook-for-2026-its-a-di-2083199326004838508.md]

The loop's handoff is explicit: a meeting recorder holds buyer language, a sequencer records channel and step replies, a CRM records closed deals and reasons, and the next campaign changes persona, message, and targeting from those observations. A source-described example narrowed a broad sales persona to sales operations after seeing a three-times-higher response rate; a lost-deal reactivation used the original missing-feature objection once that feature shipped. At ColdIQ, GTM engineers reportedly review a Claude-connected campaign draft after about 30 minutes, with lists uploaded and touchpoints placed; the source gives no exact prompt, model, API schema, file format, or configuration.^[raw/articles/xarticle-the-complete-cold-email-playbook-for-2026-its-a-di-2083199326004838508.md]

## Zero-budget warm outreach and proof

A local X Article by [[whotfiszackk]] recommends a warm-first outbound motion for a new productized AI service: list 30 known business contacts, explain the narrow problem and outcome, and ask whether they know someone who might be a fit. The referral ask lowers pressure while still surfacing direct demand from people who recognize the problem. ^[raw/articles/xarticle-the-fastest-path-from-zero-to-10kmonth-online-righ-2079543867683025123.md]

The article then moves from proof to colder outreach: deliver the first engagement exceptionally, document the result as a case study, and use that evidence in new prospecting. It is a useful early-stage complement to the page's intent-sourced and deliverability-aware outbound systems, not an argument for blasting an unproven offer. ^[raw/articles/xarticle-the-fastest-path-from-zero-to-10kmonth-online-righ-2079543867683025123.md]

This warm-to-cold sequence links outbound to [[agency-client-acquisition]], [[distribution]], and [[services-as-software]]: the message is only one layer of a system that includes a narrow offer, proof, follow-up, and a human-owned quality boundary. ^[raw/articles/xarticle-the-fastest-path-from-zero-to-10kmonth-online-righ-2079543867683025123.md]

## Relationship to [[four-layer-b2b-funnel]]

This architecture fits inside the funnel's Layer 1 and Layer 3 mechanics. Email-wide testing produces the market signal, LinkedIn turns that signal into warmer conversations, and the CRM plus automation stack supplies the lead-management continuity that prevents duplicate touches and dead follow-up.

## 2026-08-02 Enterprise LinkedIn Account Motion

Din's enterprise playbook treats an account as an organizational structure to map before outreach, extending the existing signal-sourced and multichannel outbound model. Start at the division or business unit that owns the problem, identify the function leader inside that unit, trace the reporting line above and below, and note current triggers such as a reorganization, new hire, acquisition, or earnings comment. The source says this map determines both the contacts and their order. [[linkedin-growth]] [[lead-gen]] ^[raw/articles/xarticle-how-to-target-enterprise-companies-on-linkedin-and-2083725262890357129.md]

The contact set is deliberately multi-threaded: function owner (director or VP), executive above them with budget authority, and a lower-level champion who feels the pain daily. Reach several people because enterprise decisions involve committees and the actual decision owner may surface only through replies; qualify hard because company size creates many false-fit contacts. ^[raw/articles/xarticle-how-to-target-enterprise-companies-on-linkedin-and-2083725262890357129.md]

The enterprise message should cover scale, risk, and integration; mention a current company or division detail; lead with the relevant problem instead of a service category; use language native to that buyer; and keep the ask small. An opinion request is the source's contrast case against a 30-minute call request, with the former presented as more replyable for senior people. The cycle then requires several stakeholder conversations, parallel nurture, patience with internal processes, valuable touches, and material a champion can use to sell upward. ^[raw/articles/xarticle-how-to-target-enterprise-companies-on-linkedin-and-2083725262890357129.md]

The source frames one enterprise client as potentially worth more than fifty small ones and recommends treating each account as a project rather than replacing focused work with careless volume. Its footer claims Din runs cold outbound systems using LinkedIn and email for B2B businesses making $10k/month or more, has worked with 140+ companies across 30 industries, and sees ROI for most clients within 60–90 days; these are source-described commercial claims. ^[raw/articles/xarticle-how-to-target-enterprise-companies-on-linkedin-and-2083725262890357129.md]

Evidence boundary: beyond LinkedIn, InMail, and work email, the local article supplies no named tool, model/version, automation framework, command, configuration value, parameter schema, prompt, API/interface, file format/path, or independent measurement of its reachability, ROI, company-count, industry-count, or timing claims. Those omissions remain explicit. ^[raw/articles/xarticle-how-to-target-enterprise-companies-on-linkedin-and-2083725262890357129.md]

## Related Concepts

- [[lead-gen]] — outbound as lead generation
- [[cold-email]] — outbound channel
- [[linkedin-growth]] — LinkedIn as the lower-volume, higher-trust layer of the outbound mix
- [[lemlist]] — source-described sequencer and deliverability layer
- [[dra]] — source operator documenting funding-triggered LinkedIn outreach into recently funded startups
- [[brannon-hogue]] — source operator documenting qualification-first list reduction and free-offer gating
- [[four-layer-b2b-funnel]] — broader B2B demand-gen system that gives outbound a capture and nurture context
- [[levikmunneke]] — source operator documenting AI-assisted SDR execution
- [[b2b]] — B2B outbound context
- sales — sales process
