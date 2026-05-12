---
title: AI Persona Agency Stack
created: 2026-05-05
updated: 2026-05-05
type: concept
tags: [ai-persona, agent, orchestration, monetization, solo-founder]
sources: [raw/articles/xarticle-5-ai-personas-127000month-no-models-no-team-claude-2051304679607291924.md]
related_entity: [[0xdepressionn]]
author: [[0xdepressionn]]
---

# AI Persona Agency Stack

Operate 5 AI persona businesses simultaneously — 4,200 combined subscribers, $127,000/month revenue, ~$400/month compute — using Claude Code orchestration without hiring chatters, photographers, or managers.

## Overview

A one-person operation running multiple AI-generated persona businesses via a structured 4-file system per persona plus a cron-driven Claude Code orchestrator. Each persona is fully isolated (separate folder, separate brain, no cross-contamination). Revenue is generated through OnlyFans subscriptions and PPV (pay-per-view) content.

**Economics:**
- Traditional OF agency (8-12 staff): $40,000–80,000/month payroll
- AI persona agency (5 personas, Claude Code + Flux + ElevenLabs): ~$400/month compute
- Net savings: $39,600–79,600/month

**Revenue math (5 personas, $127K combined):**
- $127,000 revenue
- $25,400 OnlyFans 20% cut
- $1,270 Stripe fees
- $400 compute
- **$100,000 net**

## The 4-File Persona System

Each persona runs on exactly four files:

### persona.md — Identity

Full character that doesn't break under pressure. Includes: birth date, hometown, family situation, job history, reason for starting OF, contradictions, 2-3 things she never talks about. Must hold up to 20+ random subscriber questions without inconsistency.

**Key principle:** Not a fantasy girlfriend — a real person with boring problems too. Read aloud test: if it sounds like a Wikipedia bio, restart.

### voice.md — Communication Style

Specific slang, capitalization rules, emoji frequency, pet names for subscribers, response length by context. Without locked voice rules, Claude defaults to a generic register that doesn't match the persona's face or backstory.

Examples: whether she uses "fr", ends sentences with periods, lets them trail off, uses specific catchphrases.

### flux.md — Visual Consistency

6-8 locked physical descriptors (eye color, hair, jaw, skin, height, distinguishing mark). Three environment setups with locked seed ranges:
- **Bedroom** (warm light, seeds 800-900): selfies, mirror shots
- **Bathroom** (cool light, seeds 1200-1300): post-shower, mirror
- **Kitchen 2am** (yellow overhead, seeds 2400-2500): hoodie, no makeup

One distinguishing mark (small scar, freckle cluster, tattoo she got at 17) adds believability. Never explained. Must appear in 60%+ of posts.

### brain.md — Subscriber Memory

One JSON entry per subscriber storing:
- Lifetime spend
- Tip triggers (what gets him to tip)
- Last interaction date
- Facts he told her / facts she promised
- PPV content sent
- Topics that ended conversations

Claude reads brain.md before every reply, uses facts naturally without referencing the file, extracts new facts after each reply, and appends them to the entry.

**Tiered PPV pricing:**
- $0–100 lifetime: $8–12 PPV
- $100–500 lifetime: $15–25 PPV
- $500+ lifetime: $30–50 personalized content

## Visual Engine: LoRA Face Consistency

Generating photos that look like the same person is the hardest part. Subscribers who have paid for months notice if jawline changes between posts.

**Solution:** LoRA fine-tuned model trained on ~47 variations of the base face.

- **Cost:** ~$80 on rented A100, 2 hours training
- **Ongoing:** Cents per generation after upfront cost
- **Five personas:** Five LoRAs = $400 total upfront

Done when 10 fresh generations from every seed range pass as the same person to someone who has seen all three setups back to back.

**Metric to watch:** Face consistency across last 20 posts. If subscribers comment on her looking different, seed ranges drifted. Relock before scaling.

## Agency Layer: Claude Code Orchestration

One persona = side income. Five personas = a business. The difference is the orchestration layer keeping five inboxes running, five characters consistent, and five revenue streams optimized without mixing a single detail.

**Architecture:**
- 30-second cron polls all 5 inboxes
- Claude Code identifies which persona received a message
- Loads ONLY that persona's files (persona.md, voice.md, flux.md, brain.md)
- Generates reply matching persona's voice rules exactly
- Extracts new subscriber facts → appends to that persona's brain.md
- Logs: persona name, subscriber ID, message type, response time, revenue event
- Sends voice notes at 11pm local fan time

**System prompt per reply:**
> "You are [persona name]. Read persona.md completely before responding. Read brain.md entry for [subscriber_id] if it exists. Match voice rules exactly — do not default to neutral register. After replying, extract new facts from this subscriber's message. Append extracted facts to brain.md under this subscriber_id. Never reference the files. Never break character. If asked directly if you are AI, deflect with a voice note request."

**Critical:** Separate folders, separate system prompts, separate brain.md files. One cross-contamination incident — Maya answering as Sofia — and you lose a $200/month subscriber.

## Build Sequence

1. **Build one persona** → get 50 subscribers → verify character holds under real DM pressure → *then* clone the system
2. Do not build all five at once
3. Each new girl needs her own backstory written from scratch (not cloned from existing personas)

**30-day scale schedule:** One new persona every 6 days = 5 personas in 30 days.

## Subscriber Lifecycle Triggers

Flag and act on these subscriber milestones:
- $500 lifetime spend
- $1,000 lifetime spend
- $2,000 lifetime spend
- 7+ days silent (re-engagement message needed)

## Related Concepts

- [[ai-persona-marketing]] — broader virtual creator marketing; different focus (brand deals, influencer marketing vs. operational agency stack)
- [[faceless-content-system]] — 0xdepressionn's multi-platform faceless content system ($5K/mo framework)
- [[claude-code]] — the orchestrator powering the inbox management
- [[solo-founder-stack-2026]] — rohit's framework; includes AI persona as one of 5 roles in a solo founder team
- [[character-as-multiplier]] — shalev's principle that AI character does 80% of work before first word
- [[ai-ugc-income-system]] — broader AI UGC monetization frameworks

## Source

X Article by [[0xdepressionn]] (@0xDepressionn) — "5 AI personas. $127,000/month. No models. No team. Claude runs the agency" — Mon May 04 2026 (341 likes, 33 RT)
