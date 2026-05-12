---
title: ByteRover CLI
created: 2026-04-13
updated: 2026-04-13
type: entity
tags: [tools, ai-tools, agent]
sources: [raw/articles/kevinnguyendn-obsidian-byterover-2026-04-13.md]
---

# ByteRover CLI

ByteRover CLI (`brv`) is a markdown-native memory and retrieval layer for coding agents. In the 2026-04-13 source thread, it is presented as a way to treat an [[obsidian-vault-as-agent-context-source]] as a read-only knowledge source, so agent workflows can search personal notes and project code together.

## Confirmed from source and GitHub

- Repo: `campfirein/byterover-cli`
- Release referenced in the source: `v3.2.0` (published 2026-04-11)
- Core command in the workflow: `brv source add <path>`
- Positioning: portable memory layer for autonomous coding agents
- Storage model: local markdown files plus a `.brv/` directory and context tree

## Why it matters

ByteRover turns a curated markdown knowledge base into agent-accessible context without requiring a plugin inside Obsidian itself. That makes it adjacent to [[local-rag-for-coding-agents]], but the focus here is personal note reuse rather than documentation ingestion. It also overlaps with [[skill-graph-content-engine]] in the sense that both rely on interconnected markdown files as durable agent context.

## Workflow described in the source

1. Initialize ByteRover inside the vault.
2. Curate selected vault folders into the ByteRover context tree.
3. Link the vault into a development project as a read-only source.
4. Search/query across code and vault knowledge from the project directory.

## Boundaries

Confirmed: the post explicitly claims read-only safety for linked vault sources.

Likely: this is most useful when the vault already contains implementation decisions, architecture notes, and reusable patterns that an agent would otherwise not see.

## Related

- [[obsidian-vault-as-agent-context-source]] — the workflow pattern enabled by ByteRover’s source feature
- [[local-rag-for-coding-agents]] — nearby retrieval pattern for agent grounding
- [[skill-graph-content-engine]] — another markdown-graph pattern for persistent AI context
- [[byterover-vs-docmancer-vs-skill-graph-content-engine]] — comparison of markdown-based agent memory, retrieval, and workflow systems
