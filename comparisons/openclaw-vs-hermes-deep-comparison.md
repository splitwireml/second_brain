---
title: OpenClaw vs Hermes — Deep Comparison
created: 2026-04-19
updated: 2026-04-19
type: comparison
tags: [agent, comparison, hermes-agent]
sources: [raw/articles/openclaw-hermes-source-code-elvis-2045155784577687862.md]
participants:
  - [[openclaw]]
  - [[hermes-agent]]
---

# OpenClaw vs Hermes — Deep Comparison

9-hour source code analysis by [[elvis-x]] comparing OpenClaw and Hermes across skill architecture, governance, and product positioning.

## Dimensions

| Dimension | Hermes | OpenClaw |
|---|---|---|
| **Philosophy** | Maximalist, batteries-included | Primitive, governance-first |
| **Skill count** | 123 bundled + auto-authored | Baseline only, ClawHub-first |
| **Skill governance** | Agent auto-creates; no enforced dedupe | 5-tier precedence; rare core additions |
| **Self-improvement** | Yes — agent writes its own skills | No — requires explicit user action |
| **Skill explosion risk** | High — overlapping skills accumulate | Low — anti-bloat by policy |
| **Context overhead** | Higher surface area | Smaller, sharper responses |
| **Tool routing** | Good with explicit prompting | Better with TOOLS.md + Vercel AGENTS.md pattern |
| **Recovery** | Native checkpoints + rollback | Not analyzed |
| **Product positioning** | Own game — maximalist | Own game — primitives/legibility |

## Key Insight: Skill Explosion Problem

Hermes's self-authoring is powerful but creates accumulated redundancy — agent writes skills without deduping against existing ones. Three skills for "read image + local filesystem + model see it" with no awareness of each other.

OpenClaw's governance model prevents this but puts authoring burden on the user.

## When to Choose Which

- **Getting started quickly** → Hermes: opinionated defaults = productive day one
- **Production/team legibility** → OpenClaw: scope control + traceable skill sources
- **Building** → Depends — use one daily, steal patterns from the other

## Product Positioning Lesson

OpenClaw had category-definer mindshare. Competitors (nanoclaw, nullclaw, picoclaw, zeroclaw) tried to out-OpenClaw OpenClaw — none gained Hermes's traction.

Hermes made its own game: self-authoring, bundled-by-default, maximalist. Every release reinforces the same thesis. This is textbook product positioning — study not just the features but how they release them.

## Sources

- [Elvis — 9 hours studying OpenClaw and Hermes source code](https://x.com/elvissun/status/2045155784577687862)
