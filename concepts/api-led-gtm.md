---
title: API-Led GTM
created: 2026-05-06
updated: 2026-05-06
type: concept
tags: [gtm, outbound, api, automation, b2b, claude-code, workflow]
sources: [raw/articles/xarticle-the-complete-guide-to-api-led-gtm-2051029582070141119.md]
related_entity: [[michel-lieben]]
author: [[michel-lieben]]
---

# API-Led GTM

## Overview

API-led GTM is a B2B go-to-market methodology where agents (primarily Claude Code) call APIs directly instead of operating through dashboard UIs. The thesis: the value in every SaaS GTM tool sits in the API behind the screen. Once an agent can read API docs, make the call, parse the response, and route the result, the dashboard becomes overhead.

Documented by [[michel-lieben]] (ColdIQ) across 70+ B2B client implementations.

## Core Thesis

The mental shift is moving from **tools** to **layers**. Each layer corresponds to a job in the GTM motion, and each job has interchangeable API providers. An agent calls any provider in a layer the same way — substitutions happen at the layer level without changing the workflow structure.

Example: Apollo is a contact database with a search bar bolted on. Clay's value is the waterfall enrichment engine underneath. Smartlead's product is deliverability infrastructure. The dashboards exist because operators were human — not because dashboards are the right interface for agents.

## The Six-Layer Stack

```
Signal layer      → What's worth working on at all
Data layer        → Turning signals into contactable records
Action layer      → Where the campaign fires
Automation layer  → What orchestrates the rest
System of record  → Shared state every agent reads/writes
Conversion/Rev    → Scheduling, billing, attribution
```

### Signal Layer

Sources of intent data — what accounts are actively hiring, recently funded, or showing buying signals.

- **PredictLeads** — hiring spikes, funding rounds, tech stack changes (110M companies)
- **Common Room** — community engagement signals (GitHub, Discord, G2, LinkedIn)
- **Trigify** — social signal intelligence
- **RB2B + Vector** — de-anonymized website visitors in Slack within 10 seconds

### Data Layer

Enriching signals into contactable B2B records.

- **Apollo** — firmographic data at scale
- **AI Ark** — 70M company database, lookalike search, <2 min response
- **CompanyEnrich** — 30M companies (alternative to AI Ark)
- **Prospeo** — verified emails (98% accuracy, 200M contacts)
- **FullEnrich** — waterfall enrichment cascading through 20+ providers (80%+ find rates)
- **Wiza** — LinkedIn-to-contact conversion

### Action Layer

Campaign execution.

- **Instantly** — cold email at scale (warmup, deliverability, webhooks all programmatic)
- **Lemlist** — multichannel sequences
- **LinkedIn Ads + Meta APIs** — paid media programmatic execution

### Automation Layer

Orchestrating workflows.

- **Claude Code** — central runtime
- **n8n** — long-running workflows that shouldn't stay open in a Claude Code session
- **Relevance AI** — agent workflows needing more reasoning than a prompt chain

### System of Record

CRM as shared state file.

- **Attio** — every object, list, and field has full API access; the CRM is a shared state every agent reads from and writes to

### Conversion + Revenue

Closing the loop.

- **Cal.com** — scheduling (agent embeds link in the right email at the right moment)
- **Hyperline** — billing webhooks
- **Dreamdata** — B2B revenue attribution (every touchpoint feeds back to the signal layer)

## Documented Workflows

### 300-Account Outbound Campaign in <20 Minutes

Natural language prompts into Claude Code → live Instantly campaign in draft mode:

1. **AI Ark** pulls 300 SaaS companies (200–500 employees) from 70M DB in <2 min
2. **PredictLeads** layers buying signals (hiring, tech changes, product launches) → 186 qualified
3. **BlitzAPI** finds decision-makers (Dirs, VPs, C-suite) via ICP waterfall
4. **Limadata** fills email gaps (second email provider)
5. **FullEnrich** cascades 20+ providers for mobile numbers → 95% match rate
6. **Instantly** creates campaign, configures sending (plain text, no HTML, proper wait times), parks in draft for review

After launch: Claude pulls analytics from Instantly → identifies best-performing personas → builds lookalikes → feeds into next campaign. Outbound auto-improves like a retargeting pixel.

### Paid Ads from the Terminal

>$300K/mo ad spend through Claude Code (Ivan, ColdIQ head of growth)

1. ICP matrix construction
2. Source + enrich via Prospeo
3. Brand specs extracted and stored in a skill the agent reads at session start
4. **fal's API** generates creative variations across 600+ AI models
5. **LinkedIn Ads + Meta APIs** handle audience uploads, campaign builds, bid configuration

Skills detect creative fatigue automatically. Output doubled after skills folder matured.

### LinkedIn Outreach from One Terminal

Architecture (with Othmane Khadri, Earleads):

- Four layers: Input → CLAUDE.md → Skills → memory.md
- 7-gate qualification pipeline underneath
- Tools: **Unipile** (LinkedIn outreach, 20–25 connection requests/day/inbox), **Apify** (social scraping), **Firecrawl** (company-page parsing)

Full breakdown in [ColdIQ blog: How to Run a LinkedIn Outbound Campaign Entirely Inside Claude Code](https://coldiq.com/blog/how-to-run-a-linkedin-outbound-campaign-entirely-inside-claude-code).

## 5-Step Migration Playbook

1. **Set up the runtime** — Claude Code + CLAUDE.md (<200 lines: ICP definition, scoring rules, tool preferences, voice guidelines) + empty .claude/skills/ + .env with API keys
2. **Pick the first workflow** — target list scoring via Apollo; one skill: "score a CSV of leads against my ICP and return the top 50%"; run on real Apollo export
3. **Run it deterministically twice** — same scoring rule on a second export must produce the same tiering; if not, policy is in the prompt not the markdown; move it to markdown until deterministic
4. **Add the next layer** — connect Instantly; build cold email workflow on the scored list; chain two skills; add PredictLeads or FullEnrich next; each layer = one markdown file + one API key
5. **Fork the config** — copy the entire project folder for the next client; rewrite only scoring criteria and copy frameworks; everything else carries over

## Business Impact

1. **Cost shape inverts** — seat line collapses; API spend grows; net roughly flat, throughput up several multiples
2. **Pricing models reprice** — Clay went from free orchestration to per-action; agents spending $4,200/month in API credits without being told to stop; seat pricing unmaps from value created
3. **Hiring profile shifts** — GTM engineer replaces 3-person SDR pod by building the revenue factory; key skill is writing a CLAUDE.md that scopes the agent's job

## When NOT to Use This

- Sales cycles measured in days
- Buyers not in digital channels (no signals to wire up)
- Compliance environments blocking agent actions on customer data
- Solo founders sending <50 cold emails/week (setup overhead exceeds leverage)

## Related Concepts

- [[four-layer-b2b-funnel]] — ColdIQ's broader demand-gen architecture; API-led GTM is the execution-layer complement
- [[coldiq]] — The agency and author
- [[claude-code]] — The primary runtime
- [[gtm-engineer]] — The role that emerges from this architecture
- [[programmatic-seo]] — ColdIQ's inbound layer; API-led GTM handles outbound

## Related Entities

- [[michel-lieben]] — Author
- [[coldiq]] — Agency running this stack
- [[alex-vacca]] — Co-documentor of ColdIQ services-as-software model

## Source

- [X Article: The Complete Guide to API-Led GTM (2051029582070141119)](https://x.com/MichLieben/status/2051029582070141119) — Sun May 03 2026; 2 RT, 101 likes; 12,895 chars
