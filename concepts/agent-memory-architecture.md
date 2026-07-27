---
title: Agent Memory Architecture
created: 2026-04-29
updated: 2026-07-27
type: concept
tags: [agent, memory, architecture, knowledge-management]
sources: [raw/articles/xarticle-why-karpathys-second-brain-breaks-at-agent-scale-h-2049082538686382397.md, raw/articles/xarticle-your-ais-memory-is-quietly-making-it-dumber-i-cut--2070966613994795489.md, raw/articles/xarticle-a-beginners-guide-to-metacognition-2079624266707054825.md, raw/articles/xarticle-how-to-build-and-scale-a-one-person-business-with--2081017272924361162.md]
related_entity: [[mercury-agent]]

---

# Agent Memory Architecture

The design principles for memory systems that serve autonomous agents running continuously, as distinct from human-facing knowledge bases.

## Relationship to Other Agent Memory Systems

This page focuses on the **principles** of agent-scale memory. For concrete implementations:

- [[context-os]] — [[tony-simons]]'s 11-layer implementation on [[hermes-agent]], including SOUL.md identity, holographic fact_store, LCM compression
- [[personal-ai-infrastructure]] — [[noisy]]'s PAI Life OS (12k+ stars, 45 skills, 171 workflows) built on [[claude-code]]
- [[personal-ai-agent-architecture]] — [[seelffff]]'s simpler two-layer setup combining desktop AI + memory + tools
- [[soul-md-agent-framework]] — the SOUL.md identity file that serves as the top layer in Tony Simons' Context OS

## Human vs Agent Memory Requirements

| Dimension | Human Second Brain | Agent Memory |
|-----------|-------------------|--------------|
| Primary goal | Readability, reflection, learning | Fast retrieval, persistent state, low token cost |
| Update frequency | Occasional (manual) | Continuous (after every task/tool call/decision) |
| Retrieval mode | Browse pages, infer | Query facts directly |
| Conflict handling | Manual correction | Automated rules (newer wins, confidence scoring) |
| Decay | Manual archiving | Automatic weakening/expiration |

## Why Markdown Wikis Break at Agent Scale

1. **Fact extraction overhead** — loading a 500-line page to find one preference is wasteful
2. **Token budget inflation** — irrelevant content in context increases cost and latency
3. **Stale information parity** — old notes ranking equally with fresh data causes reasoning errors
4. **No prioritization metadata** — storage is easy; knowing what matters now is hard
5. **Write pattern mismatch** — human note-taking is sporadic; agent memory is high-frequency

## Hybrid Architecture

The practical direction is **both** formats, separated by purpose:

- **Markdown for humans** — reports, summaries, journals, identity files, browsing
- **Structured memory for agents** — facts, entities, relationships, preferences, task state, indexes, timestamps, confidence scores

This gives humans readability and agents efficiency without forcing one format to serve both masters.

## Core Properties

- **Selective injection** — relevance-filtered context, not memory dumps
- **Structured retrieval** — queryable state, not page-scanning inference
- **Scoring metadata** — confidence, freshness, importance, reinforcement
- **Conflict resolution** — deterministic rules for contradictory facts
- **Decay** — time-based weakening and archival
- **Budgeted always-on context** — keep the permanently injected layer aggressively small, because instruction files that load every session compete directly with task context.^[raw/articles/xarticle-your-ais-memory-is-quietly-making-it-dumber-i-cut--2070966613994795489.md]

## Human memory as memoization

Will Chen's article applies the same scarcity model to the human half of a human–AI system: working memory, energy, and context switches are finite, while AI can generate candidate branches faster than a person can verify them. Writing a thought down is treated as memoization because retrieval is cheaper than reconstructing the reasoning; branch caps and external notes therefore protect human attention in much the same way selective injection protects an agent's context budget. The analogy is source framing, not a claim that human memory and agent memory are interchangeable.^[raw/articles/xarticle-a-beginners-guide-to-metacognition-2079624266707054825.md]

## Push vs Pull Memory

Matt Van Horn's June 2026 article makes a useful operational distinction that sharpens the earlier theory.^[raw/articles/xarticle-your-ais-memory-is-quietly-making-it-dumber-i-cut--2070966613994795489.md]

- **Push memory** is loaded automatically at session start: `CLAUDE.md`, auto-memory, or any always-on instruction layer. Its failure mode is not just cost but silent degradation: oversized files get truncated, stale rules keep steering decisions, and skill-specific lessons poison unrelated sessions.^[raw/articles/xarticle-your-ais-memory-is-quietly-making-it-dumber-i-cut--2070966613994795489.md]
- **Pull memory** sits outside the prompt and gets queried only when needed: search, structured stores, or external knowledge layers like gbrain, supermemory, Mem0, Letta, Zep, and Cognee. This preserves recall without bloating every run.^[raw/articles/xarticle-your-ais-memory-is-quietly-making-it-dumber-i-cut--2070966613994795489.md]

The practical rule is scarcity at the push layer and retrieval at the pull layer: keep the always-loaded surface short enough to actually steer, and move durable but scoped lessons into skills, repos, or queryable stores instead of journaling them into global memory.^[raw/articles/xarticle-your-ais-memory-is-quietly-making-it-dumber-i-cut--2070966613994795489.md]

## Operational Hygiene

- **Skill-specific lessons should ship as skill updates**, not private memory notes, so the fix becomes versioned behavior instead of stale tribal knowledge.^[raw/articles/xarticle-your-ais-memory-is-quietly-making-it-dumber-i-cut--2070966613994795489.md]
- **Finished work should be archived, not kept hot**, because shipped PRs and completed tasks are provenance, not steering context.^[raw/articles/xarticle-your-ais-memory-is-quietly-making-it-dumber-i-cut--2070966613994795489.md]
- **Project-level instruction files should avoid duplication**: using `CLAUDE.md` as a thin importer for `AGENTS.md` keeps cross-agent conventions synchronized and reduces instruction drift.^[raw/articles/xarticle-your-ais-memory-is-quietly-making-it-dumber-i-cut--2070966613994795489.md]

## Machina's bounded-memory rule set

Machina's source offers a deliberately low-tech memory ladder for a working agent: level 1 files loaded at startup, level 2 a meaning-retrieval store such as mem0 when the material outgrows context, and level 3 a graph of entities and facts with time windows when “what changed when” is the real question. The recommendation is to stop at the lowest level that solves the problem; most one-person businesses remain at level 1. ^[raw/articles/xarticle-how-to-build-and-scale-a-one-person-business-with--2081017272924361162.md]

The source's controls are a few-hundred-line cap for always-loaded memory, on-demand loading for the rest, review dates for entries, and old facts marked as replaced when a new version is written. It reports one production store logging 10,000 entries in a month with about 200 worth keeping, illustrating why forgetting and review are part of memory design. Identity files remain separate from job memory so saved facts cannot rewrite agent identity; a specialist instead gets a bounded memory, a knowledge-base slice, and a schedule/gate. ^[raw/articles/xarticle-how-to-build-and-scale-a-one-person-business-with--2081017272924361162.md]

## Related

- [[karpathy-llm-wiki]] — human-facing pattern that inspired this analysis
- [[knowledge-graph-rag]] — graph-based structured memory approach
- [[hermes-omi-obsidian-workflow]] — human-centric three-layer memory stack
- [[karpathy-claude-md]] — always-on instruction budgeting and behavior contracts for `CLAUDE.md`
- [[ai-memory-systems]] — broader ecosystem of persistent memory tooling
- [[mercury-agent]] — open-source implementation of these principles
- [[metacognition-human-ai-systems]]
- [[will-chen]]
