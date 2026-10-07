---
title: API-Led GTM
created: 2026-05-06
updated: 2026-10-07
type: concept
tags: [workflow, api, automation, b2b, claude-code, gtm, outbound]
sources: [raw/articles/xarticle-the-complete-guide-to-api-led-gtm-2051029582070141119.md, raw/articles/xarticle-how-to-replace-your-sales-tools-with-claude-code-w-2057868136268128388.md, raw/articles/xarticle-heres-every-top-api-you-need-for-doing-gtm-from-th-2102017602289803275.md, raw/articles/xarticle-12-gtm-engineering-workflows-that-drive-revenue-fu-2107548563085689302.md]
related_entity: [[michel-lieben]]
author: [[michel-lieben]]
---

# API-Led GTM

## Overview

API-led GTM is a B2B go-to-market methodology where agents (primarily Claude Code) call APIs directly instead of operating through dashboard UIs. The thesis: the value in every SaaS GTM tool sits in the API behind the screen. Once an agent can read API docs, make the call, parse the response, and route the result, the dashboard becomes overhead.

Documented by [[michel-lieben]] and operationalized inside [[coldiq]].

## Core Thesis

The mental shift is moving from **tools** to **layers**. Each layer corresponds to a job in the GTM motion, and each job has interchangeable API providers. An agent calls any provider in a layer the same way — substitutions happen at the layer level without changing the workflow structure.

## The Six-Layer Stack

- **Signal layer** — what is worth working on at all
- **Data layer** — turning signals into contactable records
- **Action layer** — where the campaign fires
- **Automation layer** — what orchestrates the rest
- **System of record** — shared state every agent reads and writes
- **Conversion / revenue** — scheduling, billing, attribution, and analytics

## Folder-Native Extension (May 22)

The later ColdIQ write-up extends the original API thesis with a stronger operational claim: the agent should not just call APIs, it should own the surrounding context in local folders.

- Each agent is a folder with instructions, API keys, templates, scoring criteria, copy frameworks, and saved skills.
- The **architect** comes first; it defines folder structure and reusable patterns before downstream agents are built.
- Every API interaction that finally works gets checkpointed as a reusable skill, so future runs skip trial-and-error and go straight to execution.
- The real leverage is not “Claude Code replaced six SaaS tools” but “all targeting logic, copy frameworks, and campaign memory now live in one place the agent can reread every run.”

## Documented Workflows

### Ad Campaign Agent

Reads spreadsheet rows, validates campaign configuration, pulls creative from Drive references, and creates campaigns programmatically across LinkedIn, Meta, and Google Ads.

### Engagement-to-Pipeline Agent

Uses post-engagement signals as warm intent, enriches the people who interacted, qualifies them against ICP rules, and routes them into sequencers or SDR follow-up.

### End-to-End Campaign Buildout Agent

Scores companies in code, finds decision-makers, waterfalls enrichment, writes copy from existing frameworks, and pushes the full campaign into Instantly.

## 2026-09-22 Eight-Layer Terminal Stack

A local X Article by [[michel-lieben]] recasts the API-led approach as eight ordered jobs: **Data** (who exists and how to reach them), **Intent** (why buy now), **Outreach** (send), **Automation** (run without an operator), **Infrastructure** (inbox placement and durable truth), **Sales** (recorded conversion), **SEO/AEO** (inbound discovery), and **Affiliation** (partner-led selling). The stated invariant is deliberately narrow: Claude Code calls an API, writes the result to a table, and only then moves to the next step; no dashboard is opened in the loop and no key is pasted into a prompt. Tier 1 means dream-fit/manual-call accounts, tier 2 good fit, and tier 3 plausible fit; tier determines how much of the stack a lead receives. The article says layer 1 plus one sequencer is already usable and the rest should be added only when a concrete gap appears.^[raw/articles/xarticle-heres-every-top-api-you-need-for-doing-gtm-from-th-2102017602289803275.md]

### Local control files and onboarding

The source specifies three per-client-folder inputs. `.mcp.json` holds MCP server commands or URLs and environment references; its ColdIQ example uses `command: "npx"`, `args: ["-y", "@coldiq/mcp@latest"]`, and `env: { "COLDIQ_API_KEY": "${COLDIQ_API_KEY}" }`, after which the first interactive session asks for server approval. `.env` holds script-call keys—explicitly `COLDIQ_API_KEY`, `APOLLO_API_KEY`, `PROSPEO_API_KEY`, `FULLENRICH_API_KEY`, `LEADMAGIC_API_KEY`, `FINDYMAIL_API_KEY`, `EXA_API_KEY`, `THEIRSTACK_API_KEY`, `PREDICTLEADS_API_KEY`, `SUMBLE_API_KEY`, `INSTANTLY_API_KEY`, `LEMLIST_API_KEY`, `SUPABASE_URL`, and `SUPABASE_SERVICE_KEY`—and must be added to `.gitignore`; `.mcp.json` may remain in the repo because it contains only an environment reference. Load keys before a session with `set -a; source .env; set +a` and then run `claude` inside the client folder, or the first MCP call can fail authentication.^[raw/articles/xarticle-heres-every-top-api-you-need-for-doing-gtm-from-th-2102017602289803275.md]

`CLAUDE.md` is the source's persistent rules interface: keys stay in `.env` and are never printed or prompted; every API result reaches the leads table before the next step; uncertain rows go to `review.csv`, not a live sequence; and the email waterfall is Findymail → LeadMagic → Prospeo → Apollo → Limadata, stopping on the first verified hit while keeping catch-alls out of live sequences. Its onboarding prompt is: fetch a named tool's API documentation, authenticate from `.env`, make one single-record test call, print the raw response, and enumerate the available actions. The source explicitly says later prompts should use fields observed in that raw response.^[raw/articles/xarticle-heres-every-top-api-you-need-for-doing-gtm-from-th-2102017602289803275.md]

### Catalog and data waterfall

The article's 28 APIs are: **Data:** Apollo, Prospeo, AI Ark, Explorium, Limadata, FullEnrich, LeadMagic, Findymail, GetLeads, Exa; **Intent:** TheirStack, Sumble, RB2B, PredictLeads, Adyntel; **Outreach:** Instantly, lemlist, Expandi; **Automation:** Zapier, Airtop, Vibe Prospecting; **Infrastructure:** Hypertide, Supabase; **Sales:** folk, Claap; **SEO/AEO:** AirOps, Ahrefs; **Affiliation:** PartnerStack. It describes Exa plain-English search as producing pages/domains for later enrichment; Apollo as a broad first pass with reported 240M+ contacts/30M+ accounts and stated one-credit email/eight-credit mobile pricing; Prospeo as database/finder with one-credit verified business email, 10-credit mobile, and a reported $49/2,000-credit Starter plan; AI Ark as a ten-best-clients-to-next-100 lookalike input; Explorium as a 100+-source data API and Vibe Prospecting substrate; and Limadata as a fresh-data API with 50+ endpoints and a stated ~$0.02 Starter credit.^[raw/articles/xarticle-heres-every-top-api-you-need-for-doing-gtm-from-th-2102017602289803275.md]

For finding and verification, it names FullEnrich's claimed 20+-vendor/80%+ cascade, one-credit email, 10-credit mobile, and $55/1,000-credit pricing; LeadMagic as finder plus verifier with a 0.25-credit validation versus one-credit find; Findymail as first in the default order with one-credit email, 10-credit phone, and a stated credit refund after >5% bounce; and GetLeads as a stated $497/month unlimited plan with a 500,000-rows/day fair-use cap. A found address is `verified` (keep and stop), `catch-all` (retain but exclude from live sequences), or `not found` (ask the next finder); misses are said to be free. The five-finder pseudocode reads a `.env` key per HTTP call, calls `validate(email)` through LeadMagic, returns immediately on verified, retains only the first catch-all, and otherwise returns `(None, "not found", None)`. The ColdIQ MCP alternative is a `find_emails` call using seven default finders—Findymail, LeadMagic, Prospeo, Apollo, Limadata, Icypeas, Wiza—and the article's 40%-versus-80% find-rate illustration is a source claim.^[raw/articles/xarticle-heres-every-top-api-you-need-for-doing-gtm-from-th-2102017602289803275.md]

The article's concrete data prompt reads `leads.csv`; confirms each company domain with Exa; runs the default-order waterfall and LeadMagic validation; sends verified emails to a live list; puts catch-alls in a separate column; marks misses; and writes `clean-list.csv` with `company, domain, person, title, email, email_status, found_by`. It says 14 of the 28 APIs sit behind ColdIQ's one key/credit balance across 43 providers and 700+ marketplace endpoints; its example POST target uses provider/resource routing (`/v1/apollo/people/search`), bearer authorization, JSON content type, `person_titles: ["Head of Sales"]`, and `q_organization_domains: ["example.com"]`. The reported free tier is 300 credits and includes the MCP server; all access, endpoint, credit, and provider figures remain source-described.^[raw/articles/xarticle-heres-every-top-api-you-need-for-doing-gtm-from-th-2102017602289803275.md]

### Intent, sending, and shared record

The source assigns TheirStack technology/hiring lookup to `Head of Sales` or SDR postings in the last 30 days plus a running tool; Sumble to account initiatives, owners, and quarterly movement before tier-1 email (reported free tier: 500 credits/month); RB2B to US pricing-page visitor identity arriving by webhook; PredictLeads to job/news/technographics/financing across a reported 120M+ companies and a last-90-days query (first 100 calls/month stated free); and Adyntel to LinkedIn, Google, Meta, and TikTok competitor-ad timing, charging only for data-returning calls. The article's one reported scoring example treats a job move in the past 90 days as a recent signal, but says other windows should follow event dates and review cadence. A chained prompt uses TheirStack for a country/role/last-30-days/HubSpot filter, Prospeo for heads of sales, the waterfall and LeadMagic, `signal = "hiring"` plus posting date in the leads table, and a mandatory review of the first 20 rows before a sequence load.^[raw/articles/xarticle-heres-every-top-api-you-need-for-doing-gtm-from-th-2102017602289803275.md]

For sending, Instantly is described as the volume channel: v2 API creates a campaign, uploads leads/merge fields, and reads replies; lemlist is the email/LinkedIn/calls/WhatsApp/SMS multichannel route for tiers 1–2; Expandi is tier-1-only LinkedIn due to profile daily limits. Hypertide is described as Google/Microsoft/Entra cold-email infrastructure at about $3.30 per Google inbox/month, with vendor guidance of 30–50 sends/inbox/day; the article also claims 500K+ monthly ColdIQ sends across four platforms. Supabase is the designated Postgres system of record whose per-table REST API and stated 500 MB free tier hold all layer results. The proposed `leads` table fields are `id bigint generated always as identity primary key`; `company`, `domain`, `person`, `title`, `email`, `found_by`, `signal`, `channel`, `sequence_id` as text; `email_status text check (email_status in ('verified', 'catch-all', 'not found'))`; `signal_date date`; `tier smallint`; `status text default 'new'`; and `updated_at timestamptz default now()`. `found_by`, `signal`/`signal_date`, `tier`, and `sequence_id` are the source's four key attribution/control fields.^[raw/articles/xarticle-heres-every-top-api-you-need-for-doing-gtm-from-th-2102017602289803275.md]

The campaign prompt selects verified tier-1 hiring rows, creates an Instantly campaign named `[client]-hiring-[month]`, maps `company`, `person`, and `signal` as merge fields, uploads without activation, then writes each campaign id to `sequence_id`. The article attributes a "value first in email 1" rule to analysis of 1,000,000+ Instantly emails, but does not provide its data/method. Its performance claims—500–1,000 hyper-targeted prospects at 20–30% reply versus 100,000-contact blasts at 2–3%, threefold campaign speed, and capacity moving from three to ten clients—are source-reported, not independent benchmarks.^[raw/articles/xarticle-heres-every-top-api-you-need-for-doing-gtm-from-th-2102017602289803275.md]

### Automation, sales, and scheduled compounding

The automation layer uses Zapier as event/action glue (reported 30,000+ actions in 9,000+ apps); the author says ColdIQ previously ran 13 n8n workflows written by Claude Code, while Zapier's MCP is included with plans and costs two tasks per call, so scripts should carry volume. Airtop covers logins/forms without an API through a cloud browser (source-reported 1,000 free monthly credits plus a one-time 10,000-credit bonus). Vibe Prospecting accepts plain-English list requests atop Explorium's reported 146M+ entities; both are to be proven on one job before entering the loop. A positive Instantly reply is classified from the last 24 hours, recorded as positive/neutral/negative in `leads`, and then creates a folk contact owned by the operator while posting company, signal, and reply text to Slack. folk is described as CRM-with-table-primary and Premium-plan API access; Claap as a no-bot call/meeting/email capture tool, owned by lemlist since October 2025, whose transcript search surfaces competitor mentions. Every Zapier/Claap result must write to Supabase before the next step.^[raw/articles/xarticle-heres-every-top-api-you-need-for-doing-gtm-from-th-2102017602289803275.md]

For inbound, AirOps supplies AI-search mention and fix guidance; Ahrefs supplies keywords plus Brand Radar for AI-answer mentions, with API/MCP access said to begin at Lite; PartnerStack supplies affiliate/referral/co-sell recruitment, payment, and queryable referral rows. The source's weekly cron is `0 7 * * 1  cd ~/gtm && claude -p "$(cat prompts/weekly-monitor.md)" >> logs/weekly.md`: Monday 07:00, it reads `prompts/weekly-monitor.md`, writes `logs/weekly.md`, pulls Ahrefs tracked-keyword changes, AirOps mentions for the company and competitor, Adyntel competitor ads, and three Sumble-moving accounts, then saves the one-page report to `reports/[date].md`. It also says Google Analytics MCP powered agency SEO analysis and claims high-competition first-place rankings within weeks; no reproducible configuration, GA query, model/version, ranking evidence, or independent vendor validation is supplied.^[raw/articles/xarticle-heres-every-top-api-you-need-for-doing-gtm-from-th-2102017602289803275.md]

### Evidence boundary

This is a source-specific operational catalog, not product documentation or a verified benchmark. It supplies named APIs, paths, commands, environment variable names, JSON/SQL shapes, file paths, prompts, statuses, tiers, row/table handoffs, timing windows, and stated prices/credits/capacities. It does not supply executable credentials, API documentation snapshots, response schemas beyond the shown examples, actual `.mcp.json` files, a full `CLAUDE.md`, model/version selection, deliverability configuration, campaign copy, error handling, or reproducible measurements for its adoption, capacity, credit, find-rate, ranking, send-volume, or reply-rate claims.^[raw/articles/xarticle-heres-every-top-api-you-need-for-doing-gtm-from-th-2102017602289803275.md]

## Where the Hype Breaks Down

- Strategy is still human work; the agent runs the motion but does not pick the market for you.
- Some stack components survive, especially enrichment and routing systems like Clay.
- Creative output still needs review.
- The first few weeks are slower because every skill starts as failed calls before it becomes reusable memory.

## 2026-10-06 Acquisition Workflows — Separate Source Boundary

[[adamrahmangtm]] supplies a complementary acquisition taxonomy in [[gtm-engineer]]: 12 trigger-driven workflows with buying-committee enrichment, double email verification, fit/timing scoring, and tiered sales handoffs. It names Claude Code/Gong objection extraction, Sumble/RB2B/PredictLeads change signals, HubSpot/OutboundSync CRM routing, MasterInbox interested-tag triggers, GetLeads/FullEnrich/BetterContact dials, Slack alerts, Apify/Serper review research, Jev/OpenRouter scoring, Firecrawl reading, DiscoLike lookalikes, HeyReach LinkedIn openers, and Salesfinity parallel calling. ^[raw/articles/xarticle-12-gtm-engineering-workflows-that-drive-revenue-fu-2107548563085689302.md]

This is **not** an API implementation specification: its four-vendor waterfall is unnamed; its scoring prompt is mentioned but not reproduced; no model version, endpoint/schema, keys/configuration, local file paths, code, commands, retries, or orchestrator are supplied. Do not import this page's separate ColdIQ/Supabase/Instantly or `.env`/`.mcp.json` architecture into Rahman's stack. Keep his revgrowth.ai `/playbooks/*` paths with `utm_source=x`, `utm_medium=social`, and `utm_campaign=gtm-workflows-article` as unfetched source references. Commercial pipeline/conversation claims remain source-described and unverified. ^[raw/articles/xarticle-12-gtm-engineering-workflows-that-drive-revenue-fu-2107548563085689302.md]

## Related Concepts

- [[four-layer-b2b-funnel]] — broader demand-generation architecture
- [[services-as-software]] — business model that benefits from this operating style
- [[claude-code]] — primary runtime
- [[x-organic-b2b-sales]] — adjacent content-plus-outbound coordination pattern
