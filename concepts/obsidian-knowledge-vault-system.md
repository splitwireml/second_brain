---
title: Obsidian Knowledge Vault System
created: 2026-05-09
updated: 2026-06-11
type: concept
tags: [automation, claude, feedback-loop, knowledge-management, obsidian, pkm, productivity, second-brain]
sources: [raw/articles/xarticle-cyrilXBT-2052235121416188114.md, raw/articles/xarticle-how-to-use-obsidian-vellum-to-build-a-second-brain-2059461814333673705.md]
related_entity: [[cyrilXBT]]
author: [[cyrilXBT]]
---

# Obsidian Knowledge Vault System

A type-organized Obsidian vault for founders who want a thinking partner rather than a filing cabinet. The system combines fast capture, background automation, and an AI instruction layer so the vault can surface connections, maintain active projects, and produce regular synthesis without manual refiling.

## Core Thesis

Most knowledge systems fail because they are designed for input, not output. Information that goes in but never comes back out is not a knowledge system — it is a graveyard with good folders.

## Architecture

The later Cyril write-up expands the original pattern into five persistent layers:

1. **Inbox** — raw captures land fast with zero filing friction.
2. **Type-organized captures** — articles, ideas, patterns, questions, and numbers stay grouped by note type rather than by topic.
3. **Connections** — synthesis pages where the vault turns multiple notes into new insight.
4. **Projects** — active work folders that keep current execution separate from evergreen notes.
5. **VELLUM.md + workflow prompts** — the instruction layer that tells the AI who you are, what matters, and which routines to run.

## Capture and Automation Layer

- Obsidian remains the local markdown store.
- [[n8n]] handles automated routing and scheduled runs.
- Voice notes can be transcribed with [[whisper]] before landing in the inbox.
- Telegram and reading/highlight tools are treated as feed sources, not places where final structure should happen.

## Why Type-Based Organization Matters

Cyril's key claim is that organizing by type rather than topic makes cross-domain pattern finding easier. A market pattern, a psychology observation, and a crypto note can all land in the same "patterns" bucket, which gives the AI better odds of surfacing a connection that topical silos would hide.

## The Instruction File

The dedicated `VELLUM.md` file plays the same role that `CLAUDE.md` or system memory files do in agent workflows: it encodes identity, goals, current projects, and the style of help wanted. Without that layer, the model behaves like a generic chatbot. With it, the vault starts acting like a context-aware chief of staff.

## Operating Routines

The expanded system runs as recurring workflows rather than ad hoc searches:

- **Inbox processing** — sharpen raw captures and route them to the right type bucket
- **Daily brief** — surface recent connections, patterns, and one question worth thinking about
- **Weekly synthesis** — scan the vault for contradictions, recurring themes, and the highest-leverage next move
- **Project-specific research** — read the whole vault through the lens of one current build or decision

## Related Concepts

- [[second-brain]] — the broader PKM concept
- [[obsidian-vault-intelligence]] — the higher-level thesis that a vault should generate insights, not just store notes
- [[automated-knowledge-vault-system]] — adjacent pattern for agent-readable personal knowledge systems
- [[cyrilXBT]] — source author and recurring creator cluster
