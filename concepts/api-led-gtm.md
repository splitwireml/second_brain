---
title: API-Led GTM
created: 2026-05-06
updated: 2026-06-11
type: concept
tags: [workflow, api, automation, b2b, claude-code, gtm, outbound]
sources: [raw/articles/xarticle-the-complete-guide-to-api-led-gtm-2051029582070141119.md, raw/articles/xarticle-how-to-replace-your-sales-tools-with-claude-code-w-2057868136268128388.md]
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

## Where the Hype Breaks Down

- Strategy is still human work; the agent runs the motion but does not pick the market for you.
- Some stack components survive, especially enrichment and routing systems like Clay.
- Creative output still needs review.
- The first few weeks are slower because every skill starts as failed calls before it becomes reusable memory.

## Related Concepts

- [[four-layer-b2b-funnel]] — broader demand-generation architecture
- [[services-as-software]] — business model that benefits from this operating style
- [[claude-code]] — primary runtime
- [[x-organic-b2b-sales]] — adjacent content-plus-outbound coordination pattern
