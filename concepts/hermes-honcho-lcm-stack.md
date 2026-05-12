---
title: Hermes Honcho LCM Stack
created: 2026-04-23
updated: 2026-04-23
type: concept
tags: [hermes-agent, agent, memory, observability, architecture]
sources: [raw/articles/bayendor-hermes-honcho-lcm-stack-2046755138501800427.md]
related_entity: [[bayendor]]
author: [[bayendor]]
---

# Hermes Honcho LCM Stack

Production agent architecture combining Hermes Agent (execution), Honcho self-hosted (persistent memory), and Hermes-LCM (measurement/control). The three-layer design targets continuity, observability, and repeatability across sessions.

## Architecture

```
User Input
    ↓
Hermes Agent (execution layer)
    ↓
Gateway API / CLI fallback
    ↓
Honcho Memory Layer (persistent, dual-peer)
    ↓
LCM Measurement / Control Layer
    ↓
Session state, logs, usage, results
```

## Three Layers

1. **Hermes Agent**: execution — Gateway API chat, SSE streaming, tool-call cards, session resume, stop controls, multi-agent profiles
2. **Honcho**: persistent memory — prompt-time context injection, cross-session continuity, durable writeback; dual-peer model (user + AI knowledge representation); configuration: `recallMode: hybrid`, `writeFrequency: async`, `sessionStrategy: per-directory`
3. **Hermes-LCM**: measurement and control — makes the stack verifiable, comparable, improvable

## Key Claims

- Dual-peer memory models both sides of the relationship (user preferences + agent's own knowledge)
- Self-hosted Honcho configuration at `localhost:8000` for full data control
- 28 permissions, 12 groups, 21 CSRF-protected endpoints
- The difference between "vibe-based automation" and "data-based execution"

## Related

- [[hermes-agent]] — execution layer
- [[hermes-lcm]] — measurement layer
- [[honcho]] — memory provider for Hermes
- [[hermes-auxiliary-model-configuration]] — another Hermes optimization pattern
