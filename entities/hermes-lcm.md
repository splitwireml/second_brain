---
title: hermes-lcm
created: 2026-04-14
updated: 2026-04-14
type: entity
tags: [tools, agent, hermes-agent]
sources: [raw/articles/steve-schoettler-hermes-lcm-v020-2026-04-14.md]
---

# hermes-lcm

**Type:** Tools / Hermes Agent Extension
**Author:** [[stephen-schoettler]]
**Version:** v0.2.0

## Overview

hermes-lcm ("Lossless Context Management") is a Hermes Agent extension that persists every message in a conversation, enabling lossless context management across sessions. Announced as v0.2.0 on April 14, 2026 by Stephen Schoettler.

## Key Claims

- Every message persisted — lossless context (no message truncation or summarization between turns)
- Designed as a context management layer for [[hermes-agent]]

## Relationship to [[hermes-agent]]

hermes-lcm is a context extension for [[hermes-agent]], adding persistence to the agent's conversation memory. This is distinct from Hermes's built-in trajectory saving (`save_trajectories`) and session store (SQLite FTS5) — hermes-lcm appears to focus specifically on message-level losslessness.

## See Also

- [[hermes-agent]] — the host platform
- [[stephen-schoettler]] — the author/creator
