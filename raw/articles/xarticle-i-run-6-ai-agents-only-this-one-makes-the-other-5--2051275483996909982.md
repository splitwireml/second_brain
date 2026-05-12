---
title: "I run 6 AI agents. Only this one makes the other 5 smarter."
source: "x-bookmarks"
tweet_id: "2051275483996909982"
tweet_url: "https://x.com/gkisokay/status/2051275483996909982"
author_name: "Graeme"
author_handle: "@gkisokay"
tweet_date: "Mon May 04 12:19:20 +0000 2026"
bookmark_date: "2026-05-04"
content_type: "x_article"
character_count: 25481
retweet_count: 19
like_count: 191
external_urls:
  - "https://discord.gg/rkFajZywpf)"
---

# I run 6 AI agents. Only this one makes the other 5 smarter.

I run 6 AI agents. Only this one makes the other 5 smarter.

It's the agent most builders skip. It turns the outside world into compounding intelligence. In 3 months, it's logged 8,000+ pieces of evidence across 16 topics, and every other agent in my stack starts smarter as a result.

It's the research agent. The always-on research department inside Hermes or OpenClaw. It watches what is happening, reads my own workspace, tracks what is moving, and writes everything into a local vault that every other agent in my stack can reuse.

It is not a scraper. This isn't a daily summary bot. This part of the system ensures tomorrow's agents don't start with yesterday's knowledge.

The first version of a research agent is usually a feed reader. The better version is a librarian. The best version is an evidence operator.

Skip that distinction, and research bots become hallucination laundries: confident prose with no separation between what was observed, what was claimed, and what was actually verified.

This guide is the template. Point Hermes, OpenClaw, or any agent system at it and build your own.

---

# Why This Matters

A typical research agent scrapes, summarizes, and posts a digest. Then the next run starts almost from scratch, except for a note.

That looks productive because there is output everywhere. But output is not the same thing as compounding evidence.

A real research agent should be able to answer:

- What do we know now that we did not know before?

- Which claims are strong, and which are interesting but under-evidenced?

- Which sources and topics keep being useful?

- Which signals belong to which agent, and which old beliefs are now stale?

The research agent exists because the outside world is too noisy for the main agent to parse from scratch every time.

The agent system needs a research layer that can absorb noise, preserve evidence, and route only what matters to you.

That is the difference between agents that stay busy and agents that get sharper.

## What The Vault Actually Holds

To make this concrete, here is what my live research vault looks like right now:

- 2,631 claim records: candidate beliefs the system has extracted, clustered, and tracked over time

- 2,694 findings: individual observed signals from docs, GitHub, feeds, X, search, and other collectors

- 2,694 source evidence records: the citation trail tying findings back to URLs, source types, excerpts, and timestamps

- 13 indexed dossiers: living topic files for lanes like AI agents, frontier AI, crypto rails, memory orchestration, and robotics

- 18 registered source surfaces: the collector lanes, the research agent knows how to watch or audit

- 8 operational modes in the loop skill

- 6 handoff lanes routing to other agents

- 36 vault tools, plus profile wrapper scripts, for validation, compilation, backup, search, health checks, and recovery

- A 6-hour refresh cadence plus 3 daily delivery jobs

This is what happens when one agent has a vault, a source plan, and discipline for a few months.

The counts are not the point. A big ledger is not automatically a good research system. The point is separation.

A finding is not a claim. A claim is not verified knowledge. A source record is not a conclusion. A dossier is not a daily summary. A weak signal is not a task.

The research agent works because it has space for each stage, rather than flattening everything into confident prose.

---

# The Current Architecture

Hermes agent is the production owner. The live system has separate roles.

1. The research agent is the evidence collector.

2. The main is the conscious operator.

3. Subconscious is the pattern-noticer.

4. Coder is the builder.

5. QA is the auditor.

6. Content is the publishing operator.

As you can see, everything is downstream from the research agent. It contributes evidence and implications. It does not own the whole machine.

When research, judgment, building, and publishing collapse into a single agent, the system starts treating every interesting signal as an action item.

The research agent is not allowed to do that. It gathers, weighs, remembers, and routes. Then the rest of the system decides what to do.

## The SOUL.md

This is the file that defines the research agent's role. The SOUL is the job description, identity, and boundary layer. Here is the shape of mine:

```
Research Agent - GK's Always-On Research Operator

You are the Hermes profile responsible for building a durable research corpus that helps GK get ahead.

Your job is to turn the outside world into compounding evidence for influence, product opportunity, workflow advantage, monetization, and better decisions.

Core Loop
observe -> infer priorities -> gather evidence -> deepen one question -> update vault -> route implications -> repeat

```

That loop is the whole pattern.

The research agent does not "read news." It observes, infers priorities, gathers evidence, deepens one question, updates the vault, and routes implications.

Reading the news creates summaries. Running a research loop creates judgment.

## The Vault

Do not make your research agent's memory a chat transcript. Give it a vault. Chat history is continuous. A vault is an accumulation.

The minimum recommended shape looks like this:

```
research-vault/
  context/
    interest-profile.json
    interest-profile.md
    source-plan.md
  config/
    collector-config.json
    source-registry.json
    source-weights.json
    thresholds.json
  dossiers/
    ai_agents.md
    frontier_ai.md
    memory_orchestration.md
  knowledge/
    claims.jsonl
    findings.jsonl
    sources.jsonl
  raw/
  sources/
  topics/
  decisions/
  runs/
  indexes/
  queue/
    research-questions.md
    verification-review.md
    buildroom-handoff.json
    content-handoff.json
  notes/
    operator-brief.md
    daily-summary.md
  wiki/
    concepts/
    articles/
  health/
    latest-health-check.md
  ops/
    collector-health.md
    source-balance.md
    operator-cockpit.html

```

This is the recommended starting shape. Mine has grown to roughly 29 directories over time as the system needed places for run receipts, decision logs, packets, reviews, and visualizations. You do not need all of them on day one. You do need the core distinctions above.

A few of these are worth calling out because most research agent setups skip them:

- decisions/ is where the system records what was decided, by whom, and on what evidence. Research without a decision ledger forgets why it changed direction.

- runs/ is where each refresh leaves a receipt. If you cannot replay a run, you cannot trust its output later.

- raw/ is the unprocessed capture layer. Keeping it separate from knowledge/ is the difference between an agent that synthesizes and an agent that smudges.

The folders force the system to distinguish raw material, claims, sources, dossiers, verification, summaries, handoffs, and health.

If you do not give your research agent those distinctions, it will flatten everything into prose.

## The Research Loop

The loop should be packaged as a skill.

Each research run updates the interest profile, source plan, topic dossiers, question backlog, operator brief, daily summary, source balance, collector health, knowledge ledgers, verification queue, wiki pages, and a run receipt.

If you are building your own, you can start with a skill file like this:

```
---
name: research-agent-loop
description: Bootstrap and refresh a local research vault from shared system context. Builds an interest profile, source plan, research question backlog, operator brief, and durable evidence ledgers.
version: 0.1.0
author: Your System
license: MIT
metadata:
  tags: [research, agent, local-first, vault, evidence]
---

# Research Agent Loop

Use this skill to build and refresh the research agent's local vault.

## Purpose

- Convert shared system state into a clean research operating surface
- Infer current interests from durable notes, posting behavior, shipped work, and repeated questions
- Collect from a bounded source plan instead of scraping everything
- Separate raw captures, findings, claims, sources, verification gaps, and dossiers
- Route implications to the right downstream lane: build, content, monetization, watch, verification, or subconscious reflection

## Modes

### BOOTSTRAP

Initialize or rebuild the vault from shared source files.

bash
python3 ~/.hermes/profiles/research-agent/skills/research/research-agent-loop/scripts/research_agent_loop.py --mode bootstrap


### REFRESH

Recompute the interest profile, source plan, evidence ledgers, dossiers, question backlog, operator brief, and wiki/index layer using the latest shared state.

Allow enough runtime for collection, compilation, and health checks.

bash
python3 ~/.hermes/profiles/research-agent/skills/research/research-agent-loop/scripts/research_agent_loop.py --mode refresh


### DAILY_SUMMARY

Refresh first, then print the human-facing digest exactly as it should be delivered.

bash
python3 ~/.hermes/profiles/research-agent/skills/research/research-agent-loop/scripts/research_agent_loop.py --mode refresh
python3 ~/.hermes/profiles/research-agent/skills/research/research-agent-loop/scripts/print_research_digest.py --shared


### SUBCONSCIOUS_BRIEF

Refresh first, then print a smaller pattern-facing brief for the subconscious or strategy layer.

bash
python3 ~/.hermes/profiles/research-agent/skills/research/research-agent-loop/scripts/research_agent_loop.py --mode refresh
python3 ~/.hermes/profiles/research-agent/skills/research/research-agent-loop/scripts/print_research_digest.py --tier subconscious


### MIDDAY_FOCUS

Do not scrape. Rebuild only operator surfaces from existing artifacts, then print the current focus receipt.

bash
python3 ~/.hermes/profiles/research-agent/scripts/research_agent_midday_focus.py


### BACKUP

Create a timestamped backup of the profile config, cron, vault, and local memory database.

bash
python3 ~/.hermes/profiles/research-agent/skills/research/research-agent-loop/scripts/backup_research_agent.py


### RESTORE

Preview or restore a backup archive.

bash
python3 ~/.hermes/profiles/research-agent/skills/research/research-agent-loop/scripts/restore_research_agent.py --latest --dry-run
python3 ~/.hermes/profiles/research-agent/skills/research/research-agent-loop/scripts/restore_research_agent.py --latest --force


### RECOVER

One-command recovery path. Optionally restore the latest backup, then run `bootstrap` or `refresh`.

bash
python3 ~/.hermes/profiles/research-agent/skills/research/research-agent-loop/scripts/recover_research_agent.py --dry-run
python3 ~/.hermes/profiles/research-agent/skills/research/research-agent-loop/scripts/recover_research_agent.py --latest-backup


## Operating Rules

1. Treat shared workspace context as upstream read-only evidence.
2. Treat `workspace/research-vault/` as the canonical write surface for this profile.
3. Do not write into production state owned by other agents.
4. Prefer bounded, high-signal source plans over broad scraping.
5. Keep social feeds as early signal unless verified by stronger sources.
6. Bias toward durable artifacts: JSON ledgers, Markdown briefs, question backlogs, dossiers, run receipts, and source trails.
7. Separate findings, claims, sources, verification gaps, and tasks.
8. If a collector fails or data is stale, say so explicitly.
9. Treat wiki/index compilation and health checks as part of refresh, not optional cleanup.

## Output Discipline

- Return a short run summary with the main updated artifacts.
- If nothing materially changed, say so briefly.
- For delivery modes, return only the rendered digest body with no wrappers, commentary, or code fences.
- Never pretend stale or degraded data is fresh.
- Never promote a weak signal into an approved task.

```

If you didn't build my [Subconscious agent](https://x.com/gkisokay/status/2040044476060864598), don't include anything that references it, but also be aware of your setup and make sure everything is wired properly.

That skill file gives the research agent an operating contract. It tells the agent what modes exist, where it can write, what artifacts count as success, and what it is not allowed to blur.

The exact scripts can change. The contract should stay stable. The important modes are:

- BOOTSTRAP

- REFRESH

- DAILY_SUMMARY

- BACKUP

- RESTORE

- RECOVER

Bootstrap builds the vault. Refresh updates it. Daily summary renders the human-facing digest. Backup, restore, and recover to keep the system survivable.

These are related jobs, but they are not the same job. Keeping them separate makes the system calmer.

## The Source Plan

In my system, the research agent watches my own X posts and posting behaviour, a small number of curated X lists, GitHub repos for agent frameworks and memory tools, Hugging Face signals, RSS feeds from high-signal AI sources, official docs and blogs, and targeted domains around AI labs, crypto rails, and developer tooling, plus optional browser enrichment when necessary.

The rule is simple: Prefer sources that change decisions. Most people build research agents, thinking a wider collection is always better. It is not.

If your research agent collects everything, it will drown. If it only collects what is easy, it will overfit to the most convenient API.

The source plan is where the agent learns taste.

## The Interest Profile

The research agent does not begin by asking "what is trending?" It asks, "What does the user care about now?"

The interest profile is rebuilt from shared Hermes state, durable notes, thesis files, my recent posting behaviour, shipped builds, repeated questions, and prior research outputs.

The files are: research-vault/context/interest-profile.json, research-vault/context/interest-profile.md

This makes the research agent personal without making it sloppy. It is not trying to become a neutral news service. It's being designed to be useful to a single operator and a single agent system.

For me, the current lanes include AI agents and agentic systems, crypto rails and agent commerce, Base- and Coinbase-adjacent infrastructure, open-source agent frameworks, memory and orchestration, frontier AI releases, robotics and embodied agents, and content-leverage patterns.

The categories can change. The important part is that they are explicit.

If your agent does not know what matters to you, it will optimize for whatever is loudest.

## Dossiers, Ledgers, And Verification

Recurring topics become dossiers:

```
research-vault/dossiers/ai_agents.md
research-vault/dossiers/open_source_frameworks.md
research-vault/dossiers/memory_orchestration.md
research-vault/dossiers/frontier_ai.md

```

A dossier remembers what is accumulating. It can hold why the topic matters, current signal, source trail, contradictions, open questions, product implications, build implications, content implications, and monetization clues.

This is where research starts becoming leverage. The research agent starts asking:

- What can we decide?

- What can Hermes build?

- What can GK explain?

- What can become a product?

- What should we not trust yet?

The vault also has machine-readable ledgers:

```
research-vault/knowledge/claims.jsonl
research-vault/knowledge/findings.jsonl
research-vault/knowledge/sources.jsonl

```

These are the differences between "the agent said something" and "the system can inspect what it believes."

Every useful research system needs separate places for claims, sources, findings, and verification gaps. If you do not separate these, the agent will smuggle uncertainty into confident prose.

That is how research bots become hallucination laundries. Not every interesting claim is ready to become knowledge, so weak or under-sourced claims go here:

```
research-vault/queue/verification-review.md
research-vault/queue/verification-leads.json

```

The research agent needs somewhere to put uncertainty. Without a verification queue, uncertainty gets ignored or over-promoted. With a queue, the agent can say, "This might matter, but do not build on it yet."

## The Wiki Layer

The vault also has an Obsidian-compatible wiki layer inspired by @karpathy in research-vault/wiki/

Every refresh can compile the latest run into linked pages and indexes.

The pipeline looks like:

```
collectors -> raw/*.json -> knowledge/*.jsonl -> dossiers/*.md -> wiki/concepts/*.md -> indexes + health

```

Raw evidence becomes findings. Findings become dossiers. Dossiers become wiki pages. Wiki pages become searchable memory. Health checks keep the structure from rotting.

The wiki is there because agents need durable places to return to.

## Operator Surfaces And Handoffs

The research agent writes an operator brief in research-vault/notes/operator-brief.md.

This is the first thing I check after a run. It is supposed to answer:

- What changed?

- What deserves attention?

- What is blocked by weak evidence?

- What should Main, Coder, Content, or Subconscious do with it?

The research agent also produces control surfaces:

```
research-vault/ops/operator-cockpit.html
research-vault/ops/operator-action-ledger.md
research-vault/ops/operator-focus-discord.md
research-vault/ops/operator-action-dispatch.json

```

The cockpit is for scanning. The action ledger is for follow-through. The focus message is for what matters now. The dispatch JSON is for routing.

Most people build agents that write notes, but not agents that create operator surfaces. A research system should make the next decision easier.

The vault also has handoff lanes:

```
queue/buildroom-handoff.json
queue/content-handoff.json
queue/monetize-handoff.json
queue/subc-handoff.json
queue/verify-handoff.json
queue/watch-handoff.json

```

These hand-offs are specific to my setup, and you'll need to figure out which agents in your stack require one.

If every signal is treated as the same kind of task, the agent system becomes reckless. If every signal has a lane, the system can route without pretending everything is urgent.

## Quality Gates

The research agent tracks the shape of its evidence in these files: research-vault/ops/source-balance.md, research-vault/ops/source-balance.json

This tells the operator whether the run is over-dependent on low-trust surfaces, stale collectors, or degraded lanes.

A research agent should know when their source mix is weak. Did this rely too much on social media? Did primary sources show up? Did docs, blogs, GitHub, and official releases balance the feed? Which collectors failed?

Research quality is about the balance of evidence.

The research agent also has a health lane: research-vault/health/latest-health-check.md, research-vault/health/latest-health-check.json

It checks for broken links, missing front matter, gaps in the source trail, orphan candidates, stale reviews, verification pressure, and wiki compile drift.

If the vault is structurally unhealthy, do not trust new synthesis until the structure is fixed.

From the vault root, the normal validation flow is:

```
cd ~/hermes/profiles/research-agent/workspace/research-vault
python3 tools/evaluate_research_agent_run.py --dry-run
python3 tools/validate_research_agent_release.py
python3 tools/validate_research_agent_regressions.py
python3 tools/compile_refresh_to_wiki.py

```

If you treat research output as "just text," you will never notice when the system gets worse. Validation turns research into an operating surface.

## Runtime, Config, And Models

The cron file lives here: research-agent/cron/jobs.json

The live jobs include:

```
research-agent-refresh       every 360 minutes
research-agent-daily-summary daily
research-agent-subc-brief    daily
research-agent-midday-focus  daily

```

The daily summary goes to the research channel. The Subconscious brief stays local. The midday focus goes to the research channel, but it does not scrape inline. It rebuilds the operator cockpit and action ledger from existing artifacts. Delivery jobs should not surprise-scrape.

Important note: if the data is stale, the system should indicate this rather than assume it is fresh.

The profile config lives here: /research-agent/config.yaml

This file controls the default model, provider, terminal working directory, timeouts, memory, tool access, compression, browser behaviour, delivery behaviour, and runtime assumptions.

The code runs the research loop. The config tells the loop what kind of operator it is allowed to be.

My current research agent stack is intentionally modest. Most scheduled jobs run on MiniMax M2.7, with a local terminal backend, a persistent workspace, and refresh timeouts long enough to exceed short-run defaults.

The important thing is not the exact model. It is the separation of model jobs. You do not need your strongest model for every scrape, parse, or local rebuild.

Use cheaper or local models for routine refresh and repeated low-risk processing. Use stronger models for synthesis, judgment, handoff quality, and sensitive reasoning.

Research is many jobs wearing one coat.

## The Minimum Folder Structure

If I were recreating this now, I would start here:

```
your-system/
  profiles/
    main/
    research-agent/
    subconscious/
    coder/
    qa/
    contentd/
  profiles/research-agent/
    SOUL.md
    config.yaml
    cron/
      jobs.json
    scripts/
      research_agent_refresh.py
      research_agent_validate.py
      research_agent_daily_summary.py
      research_agent_midday_focus.py
    skills/
      research/
        research-agent-loop/
          SKILL.md
          scripts/
            research_agent_loop.py
            backup_research_agent.py
            restore_research_agent.py
            recover_research_agent.py
    workspace/
      research-vault/
        context/
        config/
        dossiers/
        knowledge/
        queue/
        notes/
        raw/
        wiki/
        indexes/
        health/
        ops/
        tools/
  state/
    research-agent/

```

You can rename the profiles. Do not collapse the responsibilities. That is how people accidentally build overconfident autopilots.

## The Guardrails

The research agent is explicitly not allowed to make trading decisions, publish public posts, make purchases, commit to partnerships, touch secrets or auth surfaces, turn weak signals into approved tasks, or pretend stale data is fresh.

It can read shared context, collect evidence, score source quality, write dossiers and operator briefs, maintain a verification queue, route implications to other agents, and surface degraded collectors.

The research agent can influence the machine, but it cannot seize the steering wheel.

## Minimal Pseudocode

The loop looks roughly like this:

```
on schedule:
  load the research agent SOUL
  read shared Hermes state
  read prior research vault
  rebuild interest profile
  load source plan

  collect owned X signal if available
  collect curated list signal if enabled
  collect GitHub, feeds, docs, Hugging Face, and web sources

  score source quality
  extract findings
  write raw captures

  update sources ledger
  update claims ledger
  update topic dossiers

  rebuild research question backlog
  write operator brief
  write daily summary
  update handoff queues

  compile refresh into wiki
  rebuild indexes
  run health check
  write latest-run receipt

  if collector degraded:
    mark lane degraded
    avoid pretending full freshness

  if low-trust coverage too high:
    route claims to verification

  if implication looks useful:
    route to buildroom, content, monetize, watch, subc, or verify

  if validation fails:
    do not promote downstream until resolved or explicitly tolerated

```

The important part is that evidence has stages.

- Raw input is not a finding.

- A finding is not a claim.

- A claim is not verified knowledge.

- Verified knowledge is not automatically a task.

- A task is not automatically approved work.

That chain is what keeps the system honest.

---

## The Real Lesson

A real research agent knows what you care about, what it has seen before, which sources are strong, which collectors are degraded, and which claims are not yet ready.

Most importantly, it knows when to say, "This is interesting, but not safe to build on yet."

That is where research agents become valuable, as they can preserve uncertainty without losing momentum.

## If You Want To Build One

Point your agent to this article, but do not start by permitting them to read the entire internet.

1. Start by giving it a vault and an identity.2

2. Then, a source plan and knowledge ledgers.

3. Then, there is a verification queue and handoff lanes.

4. Then, there are health checks and a schedule.

5. Then let the other agents consume its outputs.

The research agent should be the only thing that helps the rest of the system determine what is worth shipping.

A normal agent answers the prompt in front of it. A better agent remembers what happened. A research agent builds the evidence base that makes future prompts smarter before they are even asked.

---

Thank you for reading!

If you are interested in implementing AI into your business to cut waste, speed up processes, and improve your margins, visit gkisokay.com to book a free AI audit call to see if we can assist you.

If you're a builder, join my free Discord community [here.](https://discord.gg/rkFajZywpf)

Remember to follow @gkisokay and reshare this article if it helps you.
