---
title: Agent Memory Architecture
created: 2026-04-29
updated: 2026-04-29
type: concept
tags: [agent, memory, knowledge-management, architecture]
sources: [raw/articles/xarticle-why-karpathys-second-brain-breaks-at-agent-scale-h-2049082538686382397.md]
related_entity: [[mercury-agent]]

---

# Agent Memory Architecture

The design principles for memory systems that serve autonomous agents running continuously, as distinct from human-facing knowledge bases.

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

## Related

- [[karpathy-llm-wiki]] — human-facing pattern that inspired this analysis
- [[knowledge-graph-rag]] — graph-based structured memory approach
- [[hermes-omi-obsidian-workflow]] — human-centric three-layer memory stack
- [[mercury-agent]] — open-source implementation of these principles
