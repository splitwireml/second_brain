---
title: "OMI (Memory Capture Tool)"
created: 2026-04-29
updated: 2026-04-29
type: entity
tags: [ai-agent, memory, knowledge-management, tool]
sources: [raw/articles/xarticle-how-i-connected-hermes-to-obsidian-using-omi-for-p-2048710808386130068.md]
---

# OMI (Memory Capture Tool)

AI memory capture layer that automatically records daily context (microphone, screen, activity) and exports it into structured memory stores like Obsidian. Part of the Hermes OMI Obsidian workflow.

## Overview

OMI is the automatic capture component in a three-layer AI memory stack. It runs in the background, listens via microphone access, observes screen context, and generates memories from daily activity. These memories are then exported into an Obsidian vault where they can be used by AI agents like Hermes as persistent context.

## Key Capabilities

- **Microphone access** — captures spoken context from calls and conversations
- **Screen context** — understands what the user is working on
- **Automatic memory generation** — creates structured memories without manual note-taking
- **Bulk export** — can produce hundreds of memories after short periods of use

## How It Fits the Stack

| Layer | Role | Tool |
|-------|------|------|
| Capture | Automatic context recording | **OMI** |
| Storage | Local vault organization | [[obsidian-ai-second-brain]] |
| Usage | Agent memory retrieval | [[hermes-agent]] |

## Related

- [[hermes-omi-obsidian-workflow]] — Full three-layer memory system
- [[hermes-agent]] — The agent that consumes OMI-exported memories
- [[obsidian-ai-second-brain]] — Obsidian as AI context source
- [[juliangoldie]] — Documented this workflow
