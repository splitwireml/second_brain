---
title: Hermes Memory Architecture
created: 2026-05-04
updated: 2026-05-04
type: concept
tags: [ai-agent, memory, architecture, hermes-agent, nous-research]
sources: [raw/articles/xarticle-forget-about-memory-i-built-a-context-os-for-my-he-2050793548430147982.md]
---

# Hermes Memory Architecture

Tony Simons' 11-layer memory infrastructure for [[hermes-agent]], described as a "context operating system." Built accidentally layer by layer to stop repeating himself.

## The 11 Layers

1. **SOUL.md** — Identity file: personality, role definition, delegation rules, quality standards, tone guidelines (~15KB). The one file never to delete.

2. **MEMORY.md + USER.md** — Always-on warm cache. MEMORY.md: environment facts, tool quirks, project conventions (2,819/3,500 chars). USER.md: user profile, pets, X strategy, Google Docs preference (1,652/2,500 chars). Small on purpose — rides every prompt.

3. **Holographic Memory (fact_store)** — SQLite-backed structured memory with 139 facts across 107 entities. Entity resolution, trust scoring (all at 0.5 default — untrained), compositional HRR-style querying. Degraded: Numpy missing, runs in relational fallback mode at ~40% capacity.

4. **Session Database + session_search** — Archive of 1,047 sessions, 48,422 messages, 1,858 JSONL transcript files (~475 MB). Searchable, not dumped into prompt.

5. **LCM (Long Context Management)** — Context compression: 6,622 messages across 16 summary nodes. Hierarchical summaries, externalizes large payloads. Survival gear for current session, not long-term memory.

6. **Skills (250+)** — Procedural memory: markdown files with YAML frontmatter for specific tasks. "How to execute" vs "what I know."

7. **Project-Local Context Files** — AGENTS.md, .hermes.md, CLAUDE.md/.cursorrules, SOUL.md. Auto-picked up when entering project directories.

8. **Nexus (~11 MB)** — Second brain: wikis, raw notes, journals, plans, briefings. Library, not auto-injected. Accessed via workflows.

9. **Self-Improving Files** — ~/self-improving/ with hot/warm/cold tiers. Manual-write only. heartbeat-state.md exists but never used.

10. **Cron Jobs (8 active)** — Scheduled context routines: daily planning (6:45 AM CT), Git hygiene, content radar. Circulatory system, not memory.

11. **Hooks, Plugins, MCP** — Expansion surfaces for event-driven triggers, new tools, and external context sources (e.g., Notion via MCP server).

## Key Design Principles

- MEMORY.md = warm cache, not the whole brain
- Session search = retrieval, not recall
- Skills = procedures, not facts
- Nexus = reference surface, not auto-injected
- LCM = compression, not long-term memory
- Cron = routines, not storage
- More memory isn't automatically better

## Honest Caveats

- Holographic trust scoring untrained (all 0.5)
- HRR reasoning degraded (Numpy missing)
- heartbeat-state.md never used
- 475 MB transcript archive is receipts drawer, not indexed library
- Boundary between "what Hermes knows" vs "what it can find" is fuzzy

Architecture is solid. The optimization (training trust scores, installing Numpy, wiring heartbeat, pruning stale data) hasn't been done.

Related: [[context-os]], [[agent-memory-architecture]], [[hermes-agent]], [[tony-simons]], [[factual-memory]], [[interaction-memory]], [[action-memory]], [[skillify]]
