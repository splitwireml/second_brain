---
title: Agent Memory Systems
created: 2026-05-31
updated: 2026-10-07
type: concept
tags: [agent, llm, memory, knowledge-management]
sources: [raw/articles/xarticle-how-to-build-and-scale-a-one-person-business-with--2081017272924361162.md, raw/articles/xarticle-autonomous-agent-architecture-unifying-context-eng-2088234998654472340.md]
related_entity: [[hermes-agent]]
---

# Agent Memory Systems

How agents maintain context, learn from interactions, and store knowledge across sessions. Core challenge: episodic, semantic, and procedural memory for agents.

## Machina's three-level stopping rule

Machina's source distinguishes three levels: markdown files for startup-loaded facts, procedures, and preferences; a semantic memory product such as mem0 when the material outgrows context; and a graph of entities and facts with time windows when change history is the real question. It recommends a few-hundred-line cap for working memory, on-demand loading for the rest, review dates, and marking superseded facts as replaced. A source-reported production store kept about 200 useful entries out of 10,000 logged in one month, so forgetting is an explicit design requirement. ^[raw/articles/xarticle-how-to-build-and-scale-a-one-person-business-with--2081017272924361162.md]

The source separates an agent's durable identity file from its bounded job memory, and pairs both with a knowledge-base slice plus a schedule/gate. This is a source-specific operating rule rather than a claim that one memory implementation fits every agent. ^[raw/articles/xarticle-how-to-build-and-scale-a-one-person-business-with--2081017272924361162.md]

## Related

- [[agent]] — agents that use memory
- [[hermes-agent]] — agent with memory architecture
- [[knowledge-management]] — KM for agents
- [[mem0ai]] — memory infrastructure

## Marfin: atomic-note memory engineering and lifecycle

[[marfinxx]] defines Memory Engineering as extraction, structuring, updating and forgetting entirely outside the active inference window; Context Engineering instead governs the working scratchpad. Blindly embedding raw chats is said to cause retrieval drift when semantically similar but outdated conversations pollute future queries. The source cites A-MEM, Zep and Memory-R1 as examples of incoming-event processing into self-contained atomic notes; it supplies no code or API binding for those systems. The four operational tiers and raw-trace-to-persistent-substrate handoff are preserved in [[agent-memory-architecture]], not collapsed into the existing three-level Machina taxonomy. ^[raw/articles/xarticle-autonomous-agent-architecture-unifying-context-eng-2088234998654472340.md]

### CRUD decision interface and infrastructure update example

The explicit decisions are ADD for a completely novel atomic record; UPDATE to merge new detail into an existing record without duplication; DELETE to invalidate or remove historical records explicitly contradicted by new facts; and NOOP to discard transient noise, conversational pleasantries and temporary variables. The UPDATE example is an incoming migration from Redis to Dragonfly on port 6379, targeting mem_infra_cache_081 with subject infrastructure.caching, fact text, tags infra/caching/dragonfly and a reasoning field: ^[raw/articles/xarticle-autonomous-agent-architecture-unifying-context-eng-2088234998654472340.md]

```
Incoming User Message:
"We migrated our cache from Redis to Dragonfly on port 6379."

Memory Extraction Decision:
{
  "action": "UPDATE",
  "target_memory_id": "mem_infra_cache_081",
  "memory_note": {
    "subject": "infrastructure.caching",
    "fact": "Primary cache runs Dragonfly on port 6379 (migrated from Redis)",
    "tags": ["infra", "caching", "dragonfly"]
  },
  "reasoning": "Modifies existing caching specification without creating duplicate memory"
}
```

### Controlled forgetting and retention inputs

The article describes embedding saturation and context clutter from retaining everything. Exponential decay inspired by the Ebbinghaus forgetting curve assigns each memory a dynamic retention score from (1) Semantic Relevance: cosine similarity to the current task, (2) Access Frequency: how often it is recalled and verified, and (3) Temporal Recency: elapsed time since last access. Unreferenced items decay; below an eviction threshold they are archived or deleted so the active memory index stays selective. It provides no decay equation, coefficients, threshold value, reinforcement algorithm, archive format or restore policy. Contradiction invalidation through DELETE and low-retention eviction are different decisions; neither supplies a universal “newer wins” policy. ^[raw/articles/xarticle-autonomous-agent-architecture-unifying-context-eng-2088234998654472340.md]

### Post-session durable-fact extraction: structured JSON contract

Implementation step 3 triggers a lightweight extraction call at the end of each session, using structured JSON output to distill durable facts into an atomic storage table (SQLite or Qdrant). The complete ADD example uses target_memory_id: null, subject codebase.convention, fact_contents, keywords, tags, importance_score: 0.9 and reasoning_trace; the fact is the example convention that all database queries use async SQLAlchemy sessions with explicit commit blocks. SQLAlchemy is example memory content, not an inferred runtime dependency of the architecture. ^[raw/articles/xarticle-autonomous-agent-architecture-unifying-context-eng-2088234998654472340.md]

```json
{
  "action": "ADD",
  "target_memory_id": null,
  "memory_note": {
    "subject": "codebase.convention",
    "fact_contents": "All database queries must use async SQLAlchemy sessions with explicit commit blocks",
    "keywords": ["database", "sqlalchemy", "async"],
    "tags": ["architecture", "backend"],
    "importance_score": 0.9
  },
  "reasoning_trace": "Extracted architectural convention established during refactoring session"
}
```

The two example interfaces deliberately retain their different fields: UPDATE uses memory_note.fact, tags and reasoning; ADD uses memory_note.fact_contents, keywords, tags, importance_score and reasoning_trace. The source does not define a unified schema, extraction system prompt, model choice, tool call, SQL DDL, Qdrant configuration, policy filename, CLI command, concurrency handling or validation protocol; none is filled in here. The runtime account extracts and links facts asynchronously while idle, updates graph entity relations and decay scores, prunes obsolete records and resolves contradictions. Subsequent hybrid retrieval selects a top-K compressed slice; it does not hand the full episodic transcript or permanent procedural repository to the context window. [[production-ai-systems-foundations]] preserves the cache layout, explicit full-file-on-request boundary, SQLite FTS5 retrieval channel and MMR λ = 0.7. ^[raw/articles/xarticle-autonomous-agent-architecture-unifying-context-eng-2088234998654472340.md]
