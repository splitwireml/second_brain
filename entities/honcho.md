---
title: Honcho
created: 2026-04-23
updated: 2026-04-23
type: entity
tags: [person, tool, hermes-agent]
sources: [https://github.com/friendlycactus/honcho]
related_entity: []
---

# Honcho

Self-hosted memory layer for AI agents. Provides persistent context injection across sessions with dual-peer modeling (user preferences + agent knowledge representation). Used in the [[hermes-honcho-lcm-stack]] as the memory provider.

## Key Features

- Prompt-time context injection for cross-session continuity
- Dual-peer model: user side + AI knowledge representation side
- Self-hosted at `localhost:8000` for full data control
- Configuration: `recallMode: hybrid`, `writeFrequency: async`, `sessionStrategy: per-directory`
- 28 permissions, 12 groups, 21 CSRF-protected endpoints

## In Hermes Stack

Used as the memory layer in [[hermes-honcho-lcm-stack]], sitting between Hermes Agent execution and Hermes-LCM measurement/control.
