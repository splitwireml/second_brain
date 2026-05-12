---
title: Research Agent Vault
created: 2026-05-05
updated: 2026-05-05
type: concept
tags: [ai-agent, research, memory, orchestration, workflow-automation]
sources: [raw/articles/xarticle-i-run-6-ai-agents-only-this-one-makes-the-other-5--2051275483996909982.md]
related_entity: [[hermes-agent]]
author: [[gkisokay]]
---

# Research Agent Vault

## Definition

A **research agent vault** is a structured, multi-layered local knowledge system that serves as the evidence base for an AI agent stack. Unlike chat history (continuous, ephemeral), a vault is an **accumulation** — durable, queryable, and designed for compounding intelligence over time.

The vault is the minimum recommended memory architecture for a research agent that needs to preserve uncertainty without losing momentum.

## Core Distinction

| Chat History | Research Vault |
|--------------|----------------|
| Continuous | Accumulated |
| Flat | Structured (raw → findings → claims → knowledge) |
| Ephemeral | Durable with receipts and health checks |
| Synthesis-prone | Separation-enforced |

## Vault Architecture

```
research-vault/
  context/          # Interest profile, source plan
  config/           # Collector configs, weights, thresholds
  dossiers/         # Living topic files
  knowledge/        # claims.jsonl, findings.jsonl, sources.jsonl
  raw/              # Unprocessed capture layer
  sources/          # Source records
  topics/           # Topic tracks
  decisions/        # Decision ledger (what was decided, on what evidence)
  runs/             # Run receipts (replay capability)
  indexes/          # Search indices
  queue/            # Verification review, handoff lanes
  notes/            # Operator briefs, daily summaries
  wiki/             # Compiled wiki pages
  health/           # Health checks
  ops/              # Operator surfaces, action ledgers
```

## Evidence Pipeline

```
collectors -> raw/*.json -> knowledge/*.jsonl -> dossiers/*.md -> wiki/concepts/*.md -> indexes + health
```

Raw evidence becomes findings. Findings become dossiers. Dossiers become wiki pages. Wiki pages become searchable memory. Health checks keep the structure from rotting.

## Evidence Stages

The vault enforces strict separation between:

1. **Raw input** — unprocessed capture
2. **Finding** — observed signal from a source
3. **Claim** — candidate belief extracted and clustered
4. **Verified knowledge** — claim confirmed by multiple sources
5. **Task** — verified knowledge that warrants action
6. **Approved work** — task that has been reviewed and greenlit

Without these separations, research bots become **hallucination laundries** — confident prose with no separation between observed, claimed, and verified.

## Key Components

### Interest Profile

Rebuilt from:
- Shared Hermes state
- Durable notes
- Thesis files
- Recent posting behavior
- Shipped builds
- Repeated questions
- Prior research outputs

Makes the research agent personal without making it sloppy. If the agent does not know what matters to you, it will optimize for whatever is loudest.

### Source Plan

The bounded set of sources the agent watches:
- Own posts and behavior
- Curated X lists
- GitHub repos (agent frameworks, memory tools)
- Hugging Face signals
- RSS feeds from high-signal AI sources
- Official docs and blogs
- Targeted domains (AI labs, crypto rails, developer tooling)

**Rule:** Prefer sources that change decisions. A wider collection is not always better.

### Decision Ledger

`decisions/` records:
- What was decided
- By whom
- On what evidence

Research without a decision ledger forgets why it changed direction.

### Run Receipts

`runs/` leaves a receipt for each refresh. If you cannot replay a run, you cannot trust its output later.

### Verification Queue

`queue/verification-review.md` and `queue/verification-leads.json` hold claims that are interesting but not yet safe to build on. Without a verification queue, uncertainty gets ignored or over-promoted.

### Handoff Lanes

```
queue/buildroom-handoff.json   # For the coder agent
queue/content-handoff.json     # For the content agent
queue/monetize-handoff.json    # For monetization
queue/subc-handoff.json        # For subconscious/strategy
queue/verify-handoff.json     # For verification
queue/watch-handoff.json       # For monitoring
```

If every signal is treated as the same kind of task, the system becomes reckless. If every signal has a lane, the system can route without pretending everything is urgent.

### Operator Surfaces

```
research-vault/ops/operator-cockpit.html      # For scanning
research-vault/ops/operator-action-ledger.md # For follow-through
research-vault/ops/operator-focus-discord.md # For what matters now
research-vault/ops/operator-action-dispatch.json # For routing
```

A research system should make the next decision easier.

## Quality Gates

### Source Balance

`ops/source-balance.md` and `ops/source-balance.json` track whether the run is over-dependent on:
- Low-trust surfaces (social media without verification)
- Stale collectors
- Degraded lanes

Research quality is about the balance of evidence.

### Health Checks

`health/latest-health-check.md` and `health/latest-health-check.json` check for:
- Broken links
- Missing front matter
- Gaps in source trail
- Orphan candidates
- Stale reviews
- Verification pressure
- Wiki compile drift

**If the vault is structurally unhealthy, do not trust new synthesis until the structure is fixed.**

## Research Loop Modes

Packaged as a skill with these operating modes:

- **BOOTSTRAP** — Initialize or rebuild vault from shared source files
- **REFRESH** — Full update of all vault layers and surfaces
- **DAILY_SUMMARY** — Refresh + human-facing digest delivery
- **SUBCONSCIOUS_BRIEF** — Refresh + pattern-facing brief for strategy layer
- **MIDDAY_FOCUS** — Rebuild operator surfaces only (no scraping)
- **BACKUP** — Timestamped backup of profile config, cron, vault, database
- **RESTORE** — Preview or restore from backup
- **RECOVER** — One-command recovery with optional restore

## Guardrails

The research agent is **not allowed** to:
- Make trading decisions
- Publish public posts
- Make purchases
- Commit to partnerships
- Touch secrets or auth surfaces
- Turn weak signals into approved tasks
- Pretend stale data is fresh

It can influence the machine, but it cannot seize the steering wheel.

## Relationship to Hermes Agent

The research agent vault pattern was demonstrated by [[gkisokay]] running on Hermes Agent with:
- Cron-based scheduled refresh jobs (every 360 minutes)
- Daily summary delivery
- Local terminal backend with persistent workspace
- Model tiering: MiniMax M2.7 for routine refresh, stronger models for synthesis and judgment

The vault is the **evidence layer** that makes Hermes Agent's multi-agent orchestration smarter over time.

## Related Concepts

- [[xarticle-2051275483996909982]] — The source X Article
- [[hermes-agent]] — The agent framework this runs on
- [[multi-agent-kanban-orchestration]] — Multi-agent workflow patterns
- [[agent-skills-framework]] — Skill-based agent configuration

## Source

- [X Article: I Run 6 AI Agents (2051275483996909982)](https://x.com/gkisokay/status/2051275483996909982) by [[gkisokay]] — Mon May 04 2026; 19 RT, 191 likes
