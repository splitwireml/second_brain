---
title: Meta-Meta-Prompting
created: 2026-05-09
updated: 2026-05-09
type: concept
tags: [ai-agent, skill, knowledge-management, second-brain, context-engineering, prompting, agentic-ai]
sources: [raw/articles/xarticle-meta-meta-prompting-the-secret-to-making-ai-agents-2053127519872614419.md]
related_entity: [[garrytan]]
author: [[garrytan]]
---

# Meta-Meta-Prompting

Meta-metadata prompting is Garry Tan's term for the methodology of building persistent, compounding AI agent systems where the agent maintains a structured "brain" of accumulated knowledge, and every interaction both learns from and contributes to that brain. The core thesis: the future belongs to individuals who build compounding AI systems, not those who use corporate-owned centralized AI tools.

## Core Thesis

The article argues that treating AI as a "chat window" wastes its potential. Instead, the right approach is treating AI as an **operating system** — a persistent, context-rich runtime that compounds over time. This is achieved through:

1. **Thin Harness / Fat Skills**: The agent framework (harness) should be minimal — just routing logic. The actual intelligence lives in **skills**: self-contained markdown files with detailed instructions for specific tasks, each encoding operational knowledge that would take a human assistant months to learn.

2. **Skillify Loop**: When a workflow is repeated, the `skillify` command extracts the pattern into a tested skill with triggers and edge cases. Every fix compounds across all future uses.

3. **Personal Brain**: A structured knowledge base (~100,000 pages) where every person, meeting, book, article, and idea gets a page. The brain is continuously updated by AI that was at the meeting, read the email, or ingested the PDF.

4. **Entity Propagation**: After every meeting, the system walks through every person and company mentioned and updates their brain pages with what was discussed.

## Key Architecture

| Component | Role |
|---|---|
| Harness | Thin router (~few thousand lines). Routes messages to skills. OpenClaw or Hermes Agent. |
| Skills | Fat, self-contained markdown files. 100+ skills covering specific tasks (book-mirror, meeting-prep, enrich, media-ingest, etc.) |
| Brain | Fat data: 100K pages of structured knowledge. Every person, company, meeting, book, article linked and searchable. |
| Models | Interchangeable. Opus 4.7 1M for precision, GPT-5.5 for recall, DeepSeek V4-Pro for creative work, Groq+Llama for speed. |

## Key Tools

- **GBrain**: Open-source knowledge infrastructure. Best retrieval system benchmarked (97.6% recall on LongMemEval). Ships 39 installable skills.
- **GStack**: Coding skill framework (87K+ stars) used to build GBrain.
- **OpenClaw / Hermes Agent**: The harnesses that route messages to skills.

## How It Works

The system doesn't exist as a monolith — it was assembled from skills. Skills compose: `book-mirror` calls `brain-ops` for storage, `enrich` for context, `cross-modal-eval` for quality, and `pdf-generation` for output. When one skill improves, every workflow that uses it gets better automatically.

**Skillify** is a meta-skill that creates new skills. When a workflow is repeated: "skillify this" → examines what happened → extracts repeatable pattern → writes tested skill file with triggers and edge cases → registers it in the resolver.

## The Compound Effect

Every meeting adds to the brain. Every book enriches the context for the next book. Every skill built makes the next workflow faster. Every person page updated makes the next meeting prep sharper. The system compounds: 100 cronjobs running 24/7, meeting ingestion automated, email triage every 10 minutes, knowledge graph self-enriching.

## Related

- [[garrytan]] — author, Y Combinator president
- [[skillify]] — the skill creation methodology
- [[openclaw]] — thin harness framework
- [[hermes-agent]] — alternative harness mentioned
- [[second-brain]] — related concept
- [[context-os]] — layered memory infrastructure approach
- [[agent-memory-architecture]] — design principles for machine-scale agent memory
