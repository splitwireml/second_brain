---
title: Obsidian Personal OS
created: 2026-05-20
updated: 2026-05-20
type: concept
tags: [automation, knowledge-management, obsidian, productivity]
sources: [raw/articles/obsidian-personal-os-2056924424838815824.md]
---

## Definition

A three-layer architecture — Storage (Obsidian), Intelligence (Claude Code via MCP), Automation (N8N) — that transforms a notes vault into a self-maintaining personal operating system that survives bad days and compounds intelligently.

## Three-Layer Architecture

- **Storage** — Obsidian, plain text Markdown, 8 fixed folders
- **Intelligence** — Claude Code + Filesystem MCP reads vault, makes connections, generates outputs
- **Automation** — N8N on $5 server schedules workflows, fires triggers, calls Claude API

## Vault Structure (8 Folders)

- `00 CAPTURE/` — unprocessed input, absorbs everything
- `01 ACTIVE/` — projects, areas (health/finances/relationships/learning/career), daily notes
- `02 RESOURCES/` — research, references, templates, bookmarks
- `03 SYSTEM/` — CLAUDE.md, skills, workflows, logs
- `04 GENERATED/` — AI outputs (never manually edit)
- `05 QUEUE/` — pending tasks for Claude
- `06 CALENDAR/` — events, reviews
- `07 ARCHIVE/` — completed projects, never delete

## Five Core Workflows

1. **Morning Briefing** (6AM) — AI reads CLAUDE.md, generates daily priorities
2. **Capture Processor** (8PM) — AI files everything from CAPTURE folder
3. **Weekly Review** (Sunday 7PM) — summarize week, identify patterns, plan next week
4. **Queue Processor** (every 2 hours) — AI processes verb-topic named files from QUEUE
5. **Project Health Monitor** (Monday 7AM) — AI checks all active projects, flags stalled ones

## Anti-Breakdown Features

- **Capture Safety Net** — capture at speed of thought, process later automatically
- **Archive Never Delete** — nothing lost, storage infinite
- **CLAUDE.md Single Source of Truth** — one file to update, every workflow reflects automatically

## The Real Insight

A tool requires you to use it. An operating system runs. The system keeps operating whether you are operating it or not.

## Related

- [[knowledge-management]]
- productivity