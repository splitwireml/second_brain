---
title: Mercury Agent
created: 2026-04-29
updated: 2026-04-29
type: entity
tags: [agent, open-source, memory, knowledge-management, hermes-agent]
sources: [raw/articles/xarticle-why-karpathys-second-brain-breaks-at-agent-scale-h-2049082538686382397.md]
---

# Mercury Agent

Open-source MIT-licensed agent memory system by [mercury.cosmicstack.org](https://mercury.cosmicstack.org). Built by Zaid (@Ctrl_Alt_Zaid) to address the gap between human-facing knowledge systems (Karpathy's LLM Wiki pattern) and machine-facing operational memory for autonomous agents.

## Core Thesis

Karpathy's markdown wiki pattern excels for human knowledge work (readability, browsing, reflection, manual correction) but breaks at agent scale because:

- **Agents need facts, not pages** — loading a full document to extract one sentence is structurally wasteful across thousands of calls
- **Tokens become a real budget** — every irrelevant token increases cost, latency, and distraction risk
- **Memory drift is real** — outdated notes ranking equally with fresh information creates reliability problems
- **Ranking matters more than storage** — prioritization (newest, strongest, most relevant) is harder than simple storage
- **Continuous writes change everything** — agents update memory after every task, conversation, tool call, and decision

## Architecture: Hybrid Memory

Mercury separates human-facing and machine-facing memory:

| Layer | Format | Use |
|-------|--------|-----|
| Human | Markdown / persona files | Notes, reports, summaries, journals, identity files |
| Agent | Structured memory | Facts, entities, relationships, preferences, task state, indexes, timestamps, scoring |

Principle: **Markdown as interface. Structured memory as substrate.**

## Required Agent Memory Properties

1. **Selective injection** — only relevant memory enters context; everything else stays in storage
2. **Structured retrieval** — agents query for latest preference, task state, related decisions, prior context — not just read notes
3. **Scoring** — memories carry metadata: confidence, freshness, importance, reinforcement
4. **Conflict resolution** — rules for contradictory facts (newer wins, higher-confidence wins, or ask user)
5. **Decay** — some memory weakens, expires, or archives; remembering everything equally = remembering poorly

## Relationship to Karpathy's Wiki

Not a criticism — the wiki pattern is strong for what it was built for (human knowledge compounding). Mercury extends the conversation to machine-scale memory infrastructure.

## Related

- [[karpathy-llm-wiki]] — the pattern Mercury builds upon
- [[knowledge-graph-rag]] — graph-based retrieval as one structured-memory approach
- [[hermes-omi-obsidian-workflow]] — three-layer human-centric memory stack (OMI → Obsidian → Hermes)
- [[agent-web-stack]] — agent infrastructure including memory and context layers
