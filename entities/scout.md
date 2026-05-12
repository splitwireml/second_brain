---
title: Scout
created: 2026-05-04
updated: 2026-05-04
type: entity
tags: [oss-ai, agent, ai-agent, model]
sources: [raw/articles/scout-ashpreetbedi-2049180168200106150.md]
related_entity: [[ashpreet-bedi]]
---

# Scout

Open-source context agent by [agno-agi](https://github.com/agno-agi/scout) that navigates live information sources to assemble context on demand. Built by [[ashpreet-bedi]] as a practical implementation of the company brain concept — connecting fragmented knowledge in Slack, Google Drive, Linear, and other tools.

## Problem: Company Brain Architecture

YC's Summer 2026 RFS named two related concepts:
- **Company Brain** — pull knowledge from fragmented sources (Slack, email, tickets), structure it, keep it current, turn it into something AI can act on
- **AI Operating System for Companies** — the connective layer that makes a company legible to AI by default; closed-loop systems that watch what happens after a decision and adjust

Scout builds on the "navigation over search" insight: the key is *navigation*, not structure-and-search. The index is always stale; navigating to the right context on demand is more reliable.

## Architecture: Context Providers

Scout introduces **Context Providers** — a thin abstraction layer between the main agent and tools. Each information source (Slack, Drive, CRM) exposes two natural-language interfaces:

- `query_<source>` — natural-language reads
- `update_<source>` — natural-language writes

The main agent never sees Slack's 12 native tools — it only sees `query_slack`. Behind each context provider is a sub-agent that owns all the quirks of that source (pagination, user lookups, thread conventions). This keeps the main agent's context clean and prevents context pollution from overlapping tool scopes.

**Contrast with Skills:** Skills move task knowledge into conditional prompts, but the underlying tools still land on the main agent with their intermediate results. Load 2 skills with search capabilities and the agent's context dies.

## Tool Surface

| Category | Tools |
|----------|-------|
| Web | `query_web` |
| Slack | `query_slack`, `update_slack` |
| Google Drive | `query_gdrive` |
| CRM | `query_crm`, `update_crm` |
| Knowledge wiki | `query_knowledge`, `update_knowledge` |
| Voice wiki | `query_voice` (read-only) |
| MCP servers | `query_mcp_<server>` |
| Workspace | `query_workspace` |
| Cross-cutting | `list_contexts` |

Scout builds its own wiki and CRM as it learns — shared notes get parsed into the company wiki, follow-ups get logged in the CRM.

## Key Design Decisions

1. **Navigation over search** — Default RAG (chunk, embed, retrieve top-k) fails because the index is always stale. Scout navigates to live context instead.
2. **Context Providers** — thin layer that isolates tool complexity from the main agent, preventing context pollution.
3. **Sub-agents own source quirks** — pagination, user lookups, thread conventions are handled by the context provider's sub-agent, not the main prompt.
4. **Learning machines** — the system improves over time as it discovers and records patterns.

## Links

- [Scout on GitHub](https://github.com/agno-agi/scout)
- [Agno Docs](https://docs.agno.com/)
- [Agno GitHub](https://github.com/agno-agi/agno)
