---
title: "Browserbase Autobrowse — Browser Agent Memory"
created: 2026-05-09
updated: 2026-05-10
type: concept
tags: [browser-agents, memory, automation, skill-learning, ai-agents, open-source]
sources: [raw/articles/xarticle-browserbase-autobrowse-2052103973377867913.md]
---

# Browserbase Autobrowse — Browser Agent Memory

Browser agent memory framework where an agent learns any website once, then saves the lesson as a markdown file (SKILL.md) that every subsequent agent reads before starting — eliminating the "discovery tax" that browser agents have always paid.

## Key Claims

- **Amnesia problem**: Every browser agent before Autobrowse re-discovers every site from scratch, paying the full discovery cost on every run
- **Solution**: Agent iterates 3-5 rounds on a real task, converges on a working path, writes it as SKILL.md — the next agent loads it and skips straight to the answer
- **Cost reduction**: Craigslist scrape: $0.22/71s (generic loop) → $0.12/27s (graduated skill); form-fill: $1.40 → $0.24 by run 4
- **Discovery bonus**: Agent found undocumented federal grants portal JSON endpoint humans had missed — 28-page scrape collapsed into one fetch
- **100% open source, free**

## Relationship to Karpathy's Autoresearch

Same idea as Karpathy's autonomous ML loop, but applied to the open web instead of coding/research loops. The key difference: Karpathy's loop gets smarter inside one session; Autobrowse SAVES the lesson to a file the next agent reads before it starts. Iteration = graduation.

## How It Works (7-Step Loop)

1. **Objective** — give the agent a real task on a real site
2. **Run** — agent attempts the task end to end against a live browser
3. **Study** — agent reads its own trace: where did it stall, guess, waste tokens?
4. **Strategy** — outer loop maintains strategy.md scratchpad with observations
5. **Iterate** — refine based on notes, drop steps that didn't pull weight
6. **Converge** — short-circuit when consecutive runs stop yielding improvements
7. **Graduate** — write SKILL.md plus any helper files to the public skills repo

## Output

A small, readable markdown file — no transcript, no vector embeddings, no screenshot reel. Just markdown that any future agent can load and execute. The skill is the memory.

## Context

Authored by [[DeRonin_]] (@DeRonin_) in response to [[kylejeong]]'s Autobrowse announcement. [[autobrowse-browser-agent-memory]] concept covers the full technical writeup from Browserbase.

## Sources

- [x.com/i/status/2052697237856088114](https://x.com/i/status/2052697237856088114) — DeRonin_'s viral thread; 1,812 likes, 121 RTs (May 08, 2026)
- [x.com/i/status/2052103973377867913](https://x.com/i/status/2052103973377867913) — kylejeong's full Autobrowse announcement (May 06, 2026)

## Related Concepts

- [[autobrowse-browser-agent-memory]] — Browserbase's official technical writeup of the Autobrowse framework
- [[agent-orchestration-patterns]] — Multi-agent patterns including memory-aware architectures
- [[skillify]] — Garry Tan's skill-writing methodology (convert failures into tested skills)
- [[browser-use]] — AI browser automation company with self-healing CDP harness
- [[pinchtab]] — Standalone HTTP server for AI agent browser control