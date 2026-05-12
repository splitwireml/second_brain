---
title: Content OS
created: 2026-05-08
updated: 2026-05-10
type: concept
tags: [content-system, ai-writing, content-os, bookmarkable-content, content-marketing, ai-agent-workflow, productivity, hermes-agent, postiz]
sources: [raw/articles/xarticle-shannholmberg-2052780393326092407.md]
platform: x
platform_handle: "@shannholmberg"
---

# Content OS

AI-driven content operating system for producing bookmarkable content at scale. Drove 5M impressions in 2 weeks and 100K bookmarks in 2 months from a near-silent account.

## Core Thesis

Content is only as good as the person and the system behind it. Low effort in → low quality out. The system is an accelerator, not autopilot — always hand-finish drafts.

## Key Principles

**Bookmarkable content** is the optimization target. A bookmark = a promise to future self ("I will need this again"). Higher bar than a like, and it behaves better in algorithms. Posts that earn bookmarks keep showing up in feeds long after the post date.

**Content objects** — every piece of content is an object that carries its own state from idea to published. Each piece gets a `run folder`.

**Two knowledge layers:**
- Signal layer (external): X bookmarks, articles, transcripts, DMs, competitor posts
- Knowledge graph (internal): personal OS, notes, journals, voice memos, owned content archive

**Four routes** for content objects:
1. ORIGINAL — from internal knowledge or second brain
2. REPURPOSE — extend owned content into new formats
3. REWRITE — external source through your POV and voice
4. RESEARCH + IDEATE — explore topic, generate angles

**Content lifecycle states:** captured → idea_review → brief_ready → drafting → verification → shann_draft_review → approved → scheduler_ready → scheduled → published → feedback_24h → feedback_72h → learned

## Components

**Strategy layer:** positioning, audience, pillars, source watchlist. Edited by hand only.

**Voice layer:** voice profile + master avoid-slop document. 54 patterns across three severity tiers. Loaded by every writer agent before drafting.

**Stores:** inbox, workboard, ideas/, hooks/, proof/, feedback/

**Modules:** writer skill (SKILL.md, references, templates), production code

**Workflows:** idea-to-published, verifier checklist, scheduler handoff, feedback loop

## Bookmarkability Rubric

Score 0-2 on each row (out of 12, bar is 8):
1. Saves the reader a future task
2. Includes proof (numbers, screenshot, named example)
3. Gives a reusable takeaway (template, checklist, frame)
4. Has a specific audience and job-to-be-done
5. Can be applied without me being in the room
6. Has a strong screenshot or visual

Below 8 → fix the row, re-score, ship. Not trash.

## Writer Context Packet

Tight brief that gives the writer enough to draft sharply without flooding the model with entire knowledge base. Lives in run folder as brief.md. Template fields: thesis, reader, proof, angle, constraints, voice anchors, risks, open loops.

## Two-Model Split

- **Writer model** (Opus 4.7): taste, rhythm, compression, voice, actual draft
- **Orchestrator model** (GPT-5.5): routing, context packaging, verifier, handoff to publish layer

## Publish Layer

Postiz (gitroomhq/postiz-app) — open source, self-hostable, multi-channel scheduling (X, LinkedIn, Instagram, Threads, TikTok, YouTube, Bluesky, Reddit).

## Feedback Loop

Weekly metrics: views, bookmarks, bookmark rate, replies, DM follow-ups. Bookmark rate is the primary signal. Winners become inputs; losers update voice rules, banned patterns, or idea filter.

## Tools Referenced

- [Hermes Agent](https://hermes-agent.nousresearch.com) — recommended orchestrator for this workflow
- [Postiz](https://postiz.com) — publish layer
- [Claude Code](https://claude.ai/code) — VPS option for self-hosted

## Related Concepts

- [[seo-blog-indexing-blueprint]] — Shann's earlier SEO blueprint
- [[hermes-agent]] — recommended orchestrator
- [[multi-agent-kanban-orchestration]] — similar multi-agent routing patterns
- [[agent-orchestration-patterns]] — broader context

## Sources

- [X Article 2052780393326092407](https://x.com/i/status/2052780393326092407) — full system breakdown (380 likes, 32 RTs, May 8 2026)
- [bookmarkable.io](https://bookmarkable.io) — full blueprint (in progress)