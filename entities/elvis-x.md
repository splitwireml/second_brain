---
title: Elvis X
created: 2026-04-19
updated: 2026-04-19
type: entity
tags: [person]
sources: [raw/articles/openclaw-hermes-source-code-elvis-2045155784577687862.md]
---

# Elvis X

X creator (@elvissun) who published a detailed 9-post technical analysis comparing OpenClaw and Hermes Agent source code side-by-side.

## Source

> [i spent 9 hours studying the source code of openclaw and hermes side by side](https://x.com/elvissun/status/2045155784577687862)

## Key Findings

**Hermes strengths:**
- Self-authoring skills: agent creates its own skill files during tasks; watched it build an `extract-social-testimonial` skill unprompted
- 123 bundled SKILL.md files shipped on install covering GitHub PR workflows, Obsidian, Google Workspace, Linear, Notion, Typefully, Perplexity, Deep Research, Minecraft modpack server
- Tool Gateway subscription: 300+ models + first-party web scraping, browser automation, image gen, cloud terminal, text-to-speech
- Opinionated defaults as a product — "batteries-included" positioning

**OpenClaw strengths:**
- Anti-bloat skill governance: new skills go to ClawHub first, core additions require strong product/security reason
- Five-skill-source precedence: workspace > user global > managed > bundled > extra — always traceable
- Smaller surface area = cheaper runs, sharper responses, less drift on long tasks
- Tool activation correctness: combined TOOLS.md with Vercel AGENTS.md pattern for better tool routing from ~50 options

**Hermes weakness identified:**
- Self-authoring skills create a "skill explosion problem" — agent writes overlapping skills without deduping against existing ones (`read-local-image` vs `browser-read` vs `vision-skill`)

**Product positioning insight:**
- OpenClaw had mindshare and GitHub stars as category-definer
- Competitors tried to out-OpenClaw OpenClaw (nanoclaw, nullclaw, picoclaw, zeroclaw) — none gained Hermes's traction
- Hermes made its own game: self-authoring, bundled-by-default, maximalist on purpose

## Related

- [[hermes-agent]] — the subject of analysis
- [[openclaw-vs-hermes-deep-comparison]] — the comparison page for OpenClaw vs Hermes
- [[hermes-lcm]] — related Hermes extension layer
- [[hermes-checkpoints-rollback]] — the self-authoring skill pattern discussed
