---
title: Agent Memory Systems
created: 2026-05-31
updated: 2026-07-27
type: concept
tags: [agent, llm, memory, knowledge-management]
sources: [raw/articles/xarticle-how-to-build-and-scale-a-one-person-business-with--2081017272924361162.md]
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
