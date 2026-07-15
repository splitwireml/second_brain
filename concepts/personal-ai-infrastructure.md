---
title: Personal AI Infrastructure (PAI)
created: 2026-05-11
updated: 2026-05-11
type: concept
tags: [tools, workflow, ai, architecture, open-source]
sources: [raw/articles/personal-ai-os-2053772855691690278.md]
related_entity: [[noisy]]
author: [[noisy]]
---

# Personal AI Infrastructure (PAI)

Personal AI Infrastructure (PAI) is a Life Operating System built on top of Claude Code. Not a chatbot wrapper. Not a prompt library. An operating system that provides persistent memory, skills, and workflows for AI-assisted work.

## Overview

Built by [[noisy]] (with significant community contributions), PAI represents a fundamental shift in how individuals relate to AI tools. Where most people start every AI session from zero, PAI accumulates context over time, creating a system that already knows who you are, what you're working on, and what decisions you've already made.

## Relationship to Other Agent Memory Systems

PAI and [[tony-simons]]'s [[context-os]] represent two independent implementations of the layered-agent-memory concept:

- **PAI** — built on [[claude-code]], community-maintained, 12k+ GitHub stars, Algorithm v6.3.0, 45 skills, 171 workflows
- **Context OS** — built on [[hermes-agent]], [[tony-simons]]'s personal implementation, 11-layer stack including SOUL.md identity file, holographic fact_store, LCM compression, 250+ skills

See also:
- [[agent-memory-architecture]] — the generic principles that both PAI and Context OS implement
- [[personal-ai-agent-architecture]] — [[seelffff]]'s simpler two-layer approach to the same problem

```
GitHub stars:        12,100+
Skills:              45
Workflows:           171
Hooks:               37
Algorithm version:   6.3.0
Active contributors: 1,700+ forks
```

## Three-Layer Architecture

1. **PAI as OS** — handles memory, skills, and workflows
2. **Pulse** — local dashboard at localhost:31337 showing everything in real time
3. **DA (Digital Assistant)** — personal AI with name, voice, and persistent memory

## Four Memory Types

The core insight of PAI is eliminating the "start from zero" problem:

- **Work memory** → active projects, current decisions, open tasks
- **Knowledge memory** → domain expertise, research, frameworks
- **People memory** → contacts, companies, relationship context
- **Learning memory** → patterns, mistakes, what works for you specifically

## Algorithm v6.3.0

Every complex task runs through a seven-step cycle:

```
OBSERVE → THINK → PLAN → BUILD → EXECUTE → VERIFY → LEARN
```

This is not a prompt — it's an operating doctrine that routes requests to the appropriate processing level (MINIMAL, NATIVE, or ALGORITHM).

## ContainmentGuard Privacy System

Unlike most AI systems that handle privacy through guidelines, PAI enforces privacy through code. ContainmentGuard physically blocks sensitive data from being written outside designated containment zones.

## Key Principles

- **Plain text beats databases** — every memory, decision, and context file lives in Markdown
- **Tool definitions belong in code, not in context** — follows the Code Mode pattern
- **The real AI moat is accumulated context** — not the model itself

## Productivity Numbers

Based on documented PAI user cases:
- Daily briefing automation: 30-90 min saved per day
- Context reload elimination: 15-40 min saved per session
- Meeting recovery: 20-60 min saved per meeting

## Repository

[github.com/danielmiessler/Personal_AI_Infrastructure](https://github.com/danielmiessler/Personal_AI_Infrastructure) — 12,100+ stars, open source.

## Related Concepts

- [[ai-memory-systems]] — memory architecture patterns for AI agents
- [[claude-code-workflows]] — Claude Code as the execution layer
- [[vibe-coding]] — broader vibe coding context
- [[claude-code]] — the CLI tool PAI runs on top of
