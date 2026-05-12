---
title: Automated Knowledge Vault System
created: 2026-05-09
updated: 2026-05-09
type: concept
tags: [knowledge-management, agent, automation, obsidian, second-brain]
sources: [raw/articles/xarticle-ziwenxu_-2053241837453029439.md]
related_entity: [[ziwen]]
---

# Automated Knowledge Vault System

A self-supercharging personal knowledge management system built on a 5-layer flat architecture (AGENTS.md, inbox/, notes/, ideas/, projects/) that Codex navigates like a mental map. Uses Obsidian as the local "Brain" and a custom Codex Skill to bridge notes to the LLM. The system compounds over time — the agent doesn't just store information, it uses it to sharpen its own tools.

## Architecture: The 5-Layer Neural Structure

The vault is organized for machine navigation, not human filing:

- **AGENTS.md** — Master file Codex reads first. The "Global Variable" of your life: who you are, 2026 goals, non-negotiable rules (e.g., "Never give me boilerplate", "Always check /notes before suggesting"). Every structural change gets documented here.

- **inbox/** — Staging area. Every article, technical doc, or voice note lands here first. No manual filing, no tagging, no friction. Raw RAM of the system.

- **notes/** — Personal Wikipedia. Processed information lives here as interlinked facts: API schemas, framework deep-dives, research papers. Source of Truth.

- **ideas/** — Original thinking and "vibe." Storing unique logic here prevents Codex from giving generic AI answers. Forces the agent to solve problems the way *you* would.

- **projects/** — Where work happens. Because projects sit next to notes, Codex can grab an insight from a paper read 3 months ago and apply it to code shipping now.

This structure is the Day One baseline. Obsidian serves as the local Brain; the custom [Codex Skill](https://github.com/duolahypercho/codex-knowledge-llm) bridges the vault to the LLM.

## Rule of Constant Refinement

Don't be afraid to break the structure. The moment you hit a new domain or complex concept that doesn't fit, tell your agent to carve out a new space:

- **Create New Contexts** — If deep diving into a new framework or niche like "Local LLM Fine-tuning," spin up a dedicated folder immediately.
- **Force the Update** — Every time you change the structure, go back to AGENTS.md and tell agents: "The map has changed. Here is the new logic for how we store and retrieve this specific data."

## Building a 24/7 Intelligence Assistant

The #1 reason knowledge systems fail is **Capture Friction**. The Passive Ingest system eliminates it — the pipes do the work, not you.

Instead of manual bookmarking, Browser-use or Computer Use in Codex scrapes digital highlights once per day. This ensures no new habit is required while still extracting all knowledge.

### X (Twitter) Extraction Prompt

> "use @computer Navigate to my X Bookmarks. Extract the content of every thread saved in the last 24 hours. Strip out the ads and engagement bait. Convert the core insights into a clean Markdown file titled YYYY-MM-DD-X-Insights.md and save it to my /inbox."

### YouTube Knowledge Prompt

> "Access my YouTube 'Watch Later' list. For every video added today, pull the full transcript. Use your internal logic to summarize the technical 'How-To' or 'Big Idea' from each. Save these as individual Markdown files in my /inbox so I can search them locally."

### Daily Evolution Prompt

> "Audit all new files in the /inbox and /notes from the last 24 hours. Cross-reference them with our roadmap in AGENTS.md.
> MEMORY ENHANCEMENT: Identify new technical patterns or logic I need to internalize for our current projects.
> STRATEGIC SHIFT: Does this new information suggest a better way to execute our current tasks? If so, flag the contradiction.
> IMMEDIATE ACTION: Based on these upgrades, what is the single most high-leverage task for today? Update your internal memory and save the strategy to DAILY-BRIEF.md."

### Weekly Self-Management Prompt

> "Analyze all Daily Briefs and new intelligence from the past 7 days.
> EMERGING THESIS: What high-level skill or concept have we mastered this week?
> ARCHITECTURAL EVOLUTION: Reorganize our folders and concepts to reflect our current level of understanding. Create new specialized directories if our focus has shifted.
> FIRM WARE UPGRADE: Rewrite the 'Core Logic' section of AGENTS.md. Integrate everything we've learned this week so you start Monday morning as a more capable, more senior version of yourself."

The system grows on its own. You aren't filing transcripts and bookmarks — you are feeding an organism.

## The Freshman Rule: Accuracy Over Ego

As the vault grows, agents get "cocky" — they take shortcuts. The Freshman Rule enforces accuracy:

- **Cite the Source** — The agent isn't allowed to make a technical decision unless it can link back to a specific file in /notes. If the info isn't in the vault, the agent has to admit it's guessing.
- **"Plan-First" Checkpoint** — Never let an agent start typing code. Force it to write a 3-sentence "Battle Plan" based on current AGENTS.md before it touches the keyboard.
- **Kill the Assumptions** — If a task contradicts a note saved 3 months ago, the agent needs to stop and ask for the tie-breaker.

## Related Concepts

- [[obsidian-knowledge-vault-system]] — [[cyrilXBT]]'s similar five-folder Obsidian vault with N8N pipeline + Claude intelligence layer
- [[jarvis-obsidian-second-brain]] — DamiDefi's compounding second brain in Obsidian with CLAUDE.md-driven type-organized captures
- [[hermes-omi-obsidian-workflow]] — [[juliangoldie]]'s three-layer memory system: OMI → Obsidian → Hermes
- [[research-agent-vault]] — [[gkisokay]]'s structured evidence-based research agent memory system

## Sources

- [x.com/i/status/2053241837453029439](https://x.com/ziwenxu_/status/2053241837453029439) — full X Article (7,009 chars, 705 likes, 80 RTs, May 9 2026)
- [github.com/duolahypercho/codex-knowledge-llm](https://github.com/duolahypercho/codex-knowledge-llm) — Codex Skill implementation