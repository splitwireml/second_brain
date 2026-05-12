---
title: Skill Graph Content Engine
created: 2026-04-10
updated: 2026-04-10
type: concept
tags: [marketing, brand, method, llm]
sources: [raw/articles/deronin-skill-graph-content-engine-2026-04-10.md]
---

# Skill Graph Content Engine

An AI-powered content production system using a folder of interconnected markdown files with wikilinks that function as persistent memory for an AI agent. One idea enters; ten platform-native pieces of content come out — each rethinking the topic, not just reformatting it.

## Core Concept

A **skill graph** is a folder of markdown files where each file is a "knowledge node." Nodes are cross-linked via wikilinks. When an AI agent receives a topic, it reads the entry point (index.md), follows the links, and builds a complete contextual understanding of brand voice, audience, platform rules, and repurposing logic before producing content.

The key insight: **connections between files create intelligence no single prompt can match.** One flat .md file is a tool; a graph of interconnected files is a team.

## Structure

17 files across 4 directories:

- **index.md** — Command center. Entry point that briefs the AI on identity, node map, and execution order.
- **platforms/** (8 files) — One playbook per platform (X, LinkedIn, Instagram, TikTok, YouTube, Threads, Facebook, newsletter). Each defines format, tone, frequency, and content rules.
- **voice/** (2 files) — brand-voice.md (core personality DNA) and platform-tone.md (how that voice adapts per platform).
- **engine/** (4 files) — hooks.md (opener formulas), repurpose.md (production chain), scheduling.md, content-types.md.
- **audience/** (2 files) — builders.md and casual.md (audience personas).

## The Repurposing Chain

Production order:

1. **X** (write first — forces core idea extraction)
2. **LinkedIn** (add narrative, professional framing)
3. **Instagram** (visual carousel)
4. **TikTok** (45-90sec raw script)
5. **YouTube** (8-12min structured tutorial)
6. **Newsletter** (deepest, most personal)
7. **Threads** (conversational)
8. **Facebook** (community discussion)

## Key Mechanic: Rethink, Don't Reformat

The same topic expressed differently per platform — not copy-paste with character limit adjustments. Each platform version has a different angle, hook, voice, structure, and format. A follower on all 10 platforms should never feel like they're reading the same post.

## Tools

- **Claude Projects** (recommended): Upload all .md files for persistent context across conversations
- **Cursor/Claude Code**: Agent reads files directly from local filesystem and can update them (graph evolves over time)
- **Any LLM**: Paste index.md + relevant nodes as context

## What It Replaces

- $5K-12K/month content agency retainer
- Manual per-platform rewriting
- Content team overhead

Runs 10 social media accounts for multiple clients with zero manual writing.

## Related Concepts

- [[prompt-engineering-patterns]] — Prompt templates that complement skill graph execution
- [[vibe-kanban-agent-spawning]] — Agent spawning patterns relevant to automating multi-agent content workflows
- [[byterover-vs-docmancer-vs-skill-graph-content-engine]] — comparison of markdown-native agent context systems with different jobs
- [[hermes-agent]] — Hermes Skills use the same YAML-frontmatter Markdown file pattern as the skill graph; the wikilink-based persistent memory concept is shared between both systems
