---
title: "Hermes OMI Obsidian Workflow"
created: 2026-04-29
updated: 2026-04-29
type: concept
tags: [ai-agent, memory, knowledge-management, workflow, hermes-agent]
sources: [raw/articles/xarticle-how-i-connected-hermes-to-obsidian-using-omi-for-p-2048710808386130068.md]
author: [[juliangoldie]]
---

# Hermes OMI Obsidian Workflow

Three-layer AI memory system: OMI captures daily context automatically, Obsidian stores it in a local vault, and Hermes uses that vault as persistent memory. Eliminates the need to rebuild context in every new chat.

## The Problem

Most AI agents forget everything between sessions. Even with strong models and good prompts, agents feel weak when they lack personal context — they don't know what you worked on earlier, which tasks matter, or what you already discussed. Users end up repeating the same background every morning.

## The Workflow

1. **OMI captures** — runs in the background, records microphone, screen, and daily activity; generates structured memories automatically
2. **Obsidian stores** — memories live in a local vault alongside tasks, ideas, projects, and workflows; clean, searchable, user-controlled
3. **Hermes reads** — agent is pointed at the vault file path; pulls relevant context when needed instead of starting from zero

## Why It Works

- **Shared memory base** — once context is in Obsidian, multiple agents (Hermes, OpenClaw, Claude Code) can potentially use it
- **Automatic growth** — memory base expands as you work; no daily discipline required
- **User control** — you can inspect, edit, and organize memory; set boundaries on what gets captured
- **Automation discovery** — with real workflow context, agents can spot repeated tasks and suggest automations

## Boundaries & Risks

- Review what OMI captures before exporting
- Keep sensitive information out of agent-accessible folders
- Start small — capture only useful context
- Give Hermes access to the right files, not your whole life

## Related

- [[omi-memory-capture]] — The capture layer
- [[hermes-agent]] — The agent layer
- [[obsidian-ai-second-brain]] — Obsidian as AI knowledge base
- [[open-webui-hermes-chat-frontend]] — Julian Goldie's Hermes setup guide
- [[ai-company-stack]] — Paperclip + Hermes orchestration stack
- [[byterover-cli]] — Links Obsidian vaults into coding-agent workflows
- [[juliangoldie]] — Author of this workflow documentation
