---
title: Autobrowse — Browser Agent Memory Framework
created: 2026-05-09
updated: 2026-05-10
type: concept
source: x.com/i/status/2052103973377867913
tags: [browser-agents, memory, automation, skill-learning, ai-agents]
sources: [raw/articles/xarticle-2052103973377867913.md]
---

# Autobrowse — Browser Agent Memory Framework

Autobrowse is a workflow for teaching browser agents to remember what they've learned, converting transient task executions into durable reusable skills.

## Core Problem: Browser Agent Amnesia

Browser agents re-discover every site from scratch on every run, paying the full "discovery tax" forever. The first run is exciting, the hundredth is depressing — cost graph is a straight line going up with no durable artifact to show for it.

**Key insight**: The real bottleneck for browser agents in production is memory, in a form humans and agents can both read and trust. Reasoning has stopped being the constraint.

## How Autobrowse Works

1. **Objective** — Hand the agent a real task on a real site
2. **Run** — Agent attempts the task end-to-end against a live browser
3. **Study** — Agent reads its own trace, identifying where it stalled/guessed/wasted tokens
4. **Strategy** — Maintain a `strategy.md` scratchpad where the agent dumps observations between iterations
5. **Iterate** — Refine strategy; drop steps that didn't pull weight; lean on deterministic helpers
6. **Converge** — Short-circuit when consecutive iterations stop yielding improvements
7. **Graduate** — Write out `SKILL.md` plus helper files into the public skills repo

Capped at ~3-5 iterations with aggressive short-circuiting. Goal is reliable-enough path, not theoretical global optimum.

## The Output: Skills as Memory Artifacts

Every Autobrowse run produces a durable markdown file (SKILL.md) that any future agent can load and execute. No transcript, no vector embeddings, no screenshot reel — just readable markdown.

Skills encode:
- The shortest reliable path found
- Site-specific gotchas (undocumented APIs, geo-redirects, etc.)
- Deterministic helpers (CLI calls, fetches, selectors, helper scripts)
- Evidence of convergence (iterations, cost/turn improvements, validation results)

## Key Results

| Task | Generic Loop | Autobrowse Skill |
|------|-------------|------------------|
| Craigslist search | ~$0.22, 71s | ~$0.12, 27s |
| Form fill | $1.40/run | $0.24/run (4 iterations) |

## When to Use / Not Use

**Shines on**: Hidden APIs, heavy JS rendering, multi-step login flows, non-trivial UIs, token-saving opportunities.

**Wrong tool for**: Deterministic parsing of static HTML (e.g., a 167-row state catalog). Use `browse fetch` + BeautifulSoup instead — sub-second, zero inference cost.

Rule: Probe with `fetch` first. Escalate to Autobrowse only when response is empty/dynamic/gated.

## Why It Changes Workflows

A skill is legible, durable, debuggable, human-auditable, and ownable. Engineers can read/edit/commit; non-engineers can understand what the agent is doing without touching code.

We go from "just trust the agent's output" to "read the agent's playbook."

The compounding effect: each new site yields one more durable skill. The library grows. The agent gets cheaper and faster on repetitive workflows because it stops paying the discovery tax.

## Future Directions

- **Smarter stopping**: Let agent reason about convergence explicitly, comparing trace structure across runs
- **Better priors**: Reach for `fetch`/`search` before spawning full browser session
- **Recursive Autobrowse**: Use Autobrowse to improve its own harness (prompts, convergence heuristics, skill templates)

## Related Concepts

- [[browser-agents]]
- [[skill-based-agent-architecture]]
- [[agent-memory-systems]]

## Source

- Author: [[kylejeong]]
- X Article: https://x.com/i/status/2052103973377867913 (May 6, 2026)
- Full article: [[xarticle-kylejeong-2052103973377867913]]