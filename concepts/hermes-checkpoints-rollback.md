---
title: Hermes Checkpoints and Rollback
created: 2026-04-19
updated: 2026-04-19
type: concept
tags: [hermes-agent, agent, inference]
sources: [raw/articles/hermes-checkpoints-rollback-neo-ai-forecast-2045097742935195775.md]
author: [[neo-ai-forecast]]
---

# Hermes Checkpoints and Rollback

Native filesystem and conversation recovery system in Hermes Agent. Snapshot-before-mutation safety net with conversational state realignment.

## Definition

Hermes automatically creates a checkpoint (shadow git commit) before any destructive file operation, then exposes `/rollback` as the recovery interface. Key design: rollback also undoes the last conversation turn so agent context matches restored filesystem state.

## How It Works

**Triggers:** write_file, patch, destructive shell commands (rm, mv, sed -i, truncate, shred, output redirects `>`), Git reset/clean/checkout

**Shadow repo:** `~/.hermes/checkpoints/<working-directory>/` — separate from real project `.git`, avoids polluting project history

**At most one checkpoint per directory per turn** — prevents snapshot spam in long sessions

**Rollback also restores conversation state** — filesystem recovery and context alignment happen together

## Commands

```bash
/rollback              # list checkpoints
/rollback diff 1      # preview diff
/rollback 1           # restore checkpoint 1
/rollback 1 file.py   # restore single file
```

## Why Conversation State Matters

Without joint rollback: files revert but conversation history still reflects undone change → model reasons from non-existent state → compounds across turns.

## Config

```yaml
checkpoints:
  enabled: true
  max_snapshots: 50
```

## Related Concepts

- [[hermes-agent]] — the platform this feature is part of
- [[hermes-lcm]] — Hermes's lossless context management extension
- [[http-browser-automation-for-ai-agents]] — related Hermes safety patterns
- [[neo-ai-forecast]] — the source author who documented this feature
