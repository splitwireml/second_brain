---
title: Hermes Agent
created: 2026-05-19
updated: 2026-06-12
type: concept
tags: [agent, memory, workflow, orchestration, hermes-agent, nous-research, open-source, skills]
sources: [raw/articles/xarticle-how-to-become-a-hermes-agent-operator-2055335043904492011.md, raw/articles/xarticle-hermes-agent-as-a-personal-ai-operating-system-2063645563241844823.md, raw/articles/thread-JulianGoldieSEO-2058397577234817381.md, raw/articles/xarticle-8-loops-inside-hermes-agent-and-why-they-compound-2064377155476193362.md]
confidence: high
---

## Overview

**Hermes Agent** is an autonomous agent framework built by [[nous-research]] that turns a model into a persistent operator. It has its own memory that survives between sessions, writes its own skills as it works, and ships with 123 built-in skills. Ranks #1 on OpenRouter for global token usage with 150,000+ GitHub stars.

## Architecture

Every Hermes agent has three core components:

### Brain
Memory lives at `~/.hermes/memories/` with two files:
- **MEMORY.md** - stable facts about business, customers, products
- **USER.md** - stable facts about the operator (timezone, working hours, preferences)

Sessions stored in SQLite with full-text search across sessions.

### Personality (SOUL.md)
Defines the agent's voice and behavior. Spin up multiple agents with different souls, same brain underneath. Examples: outbound rep with closer's energy, researcher who likes long sentences, brief assistant.

### Skillset
- 123 skills out of the box (GitHub PRs, Obsidian, Google Workspace, Linear, Notion, Typefully, Perplexity, deep research, browser control, web scraping, vision, voice, scheduling)
- Closed learning loop: agent writes new skills as it learns your work
- Skills accumulate on top of the 123 bundled skills

## Deployment Targets

- Local (laptop)
- Docker container (isolated, portable)
- SSH VPS (runs when laptop closed)
- Daytona, Singularity, Modal (serverless)

## Messaging Surfaces

20+ surfaces: Telegram, Discord, Slack, email, voice mode, CLI

## Browse-hub browser skills

A May 2026 thread by [[juliangoldie]] highlights a practical extension of Hermes's skill model into browser navigation: the agent can connect to Browserbase's Browse hub, search a catalogue of 100+ website/task-specific browser skills, preview them, and install them inside Hermes.^[raw/articles/thread-JulianGoldieSEO-2058397577234817381.md]

The important claim is not just "more browser automation." It is that fragile website knowledge moves into editable plain-text playbooks. Instead of hoping the model magically generalizes through a layout break, the operator updates the skill and every future run inherits the fix. Goldie's framing emphasizes the operational payoffs: less random clicking, fewer timeouts, better form-filling, and more reliable site navigation. This slots naturally beside [[browserbase-autobrowse-agent-memory]] and the broader [[browser-agents]] cluster.

## Control Room Architecture

Reference setup from Shann³'s guide:

```
/root/vps-agents/         → control room (docs, rules, runbooks, no secrets)
/srv/<agent-name>/data/   → live runtime (secrets, memory, skills, sessions)
```

### Four Levels of Setup

**Level 1**: One agent on your laptop
**Level 2**: Direct specialist agents (SEO, dev, cmo, ops) - no orchestrator
**Level 3**: Orchestrator + specialists - one front door routes across specialists
**Level 4**: Automated agent team with cron workflows

## Key Concept: Closed Learning Loop

The agent watches itself work, writes new skills as it learns the shape of your work, refines memory periodically, and recalls past context across sessions. You don't re-teach it next week.

> Rule: Don't write your own skills on day one. Run real work, let the agent watch, and let the harness write the skills. You build a custom skill library faster by working than by writing prompts.

## Comparison

| Aspect | Hermes Agent | OpenClaw |
|--------|---------------|----------|
| Philosophy | Rails - opinionated defaults, batteries included | Linux - primitives, guarantees, explicit control |
| Productivity | High - productive day one | Low - requires more setup |
| Control | Agent does more thinking for you | Agent does exactly what you told it |

## Related

- [[shann-holmberg]] - AI marketer who wrote the setup guide
- [[nous-research]] - builder
- [[hermes-agent-control-room]] - Shann's control room template
- [[hermes-orchestrator]] - orchestration concept
- [[agent-orchestration-patterns]] - broader patterns

## Personal AI operating system framing

A June 2026 source by [[yanxbt]] sharpens the core metaphor: Hermes is not just a chat agent with tools, but an operating layer that combines persistent memory, isolated profiles, reusable skills, Kanban tasking, and a multi-surface gateway into one long-running system. The article makes the architectural claim explicit: the value comes from composing persistence, workload isolation, and orchestration rather than from one frontier model call in isolation.

This framing overlaps strongly with [[hermes-agent-24-7-automation-patterns]], but adds a systems-level lens that explains why the pieces cohere.

## Eight-loop architecture

YanXbt's June 2026 loop analysis makes the internal architecture more explicit than the earlier operating-system metaphor. The key claim is that Hermes compounds because it runs eight nested loops at different timescales: the core turn loop, `/goal`, self-improvement via skills, curator maintenance, persistent memory, Kanban dispatch, context compression, and sub-agent delegation.^[raw/articles/xarticle-8-loops-inside-hermes-agent-and-why-they-compound-2064377155476193362.md]

The practical insight is that these are not independent features. Skill creation speeds up future `/goal` runs; the curator keeps that skill library searchable; memory makes each new core turn less cold; Kanban and delegation expand parallel capacity; compression keeps long-running work affordable enough to sustain. The source is useful because it explains why Hermes behaves more like a runtime than a chat wrapper: the compounding comes from the interaction surface between loops, not from any single feature in isolation.^[raw/articles/xarticle-8-loops-inside-hermes-agent-and-why-they-compound-2064377155476193362.md]
