---
title: Nate Herk
created: 2026-04-30
updated: 2026-07-01
type: entity
tags: [person, ai-design, brand, content-creator]
sources: [raw/articles/claude-design-brand-workflow-nateherk-2026-04-30.md, raw/articles/xarticle-nateherk-codex-master-guide-2051838770912129464.md, raw/articles/xarticle-stanfords-method-turns-claude-into-a-phd-level-res-2071588017878249890.md]
related_concept: [[ai-design-workflow]]
related_entity: [[claude-design]]
---

# Nate Herk

X creator (@nateherk). Documents pragmatic AI workflows spanning brand design, agent coding, and full-stack automation. Known for end-to-end build threads with no skipped steps.

## Key Work

- [[ai-design-workflow]] — End-to-end brand-building pipeline: brainstorm in Claude chat → execute in Design → ship via [[claude-code]] + Vercel
- [[codex-master-guide]] — Complete Codex tutorial: plan mode → skills → GitHub/Vercel deploy → weekly automations → browser QA
- [[storm-multi-perspective-research]] — Research skill adapting Stanford's STORM method into five lenses plus adversarial source verification
- [[higgsfield-claude-creative-agency]] — [[nate-herk]]'s full creative agency stack: Higgsfield + Claude + systematic knowledge injection

## Related Claude Code Power Users

- [[kaize]] — Claude Code configuration, skills, plugins
- [[deronin]] — [[vibe-coding-cost-optimization]] and token economics
- [[tony-simons]] — Context OS, SOUL.md framework, [[hermes-agent]] operator

## Core Findings (Claude Design)

- **Design system first** — Lock colors, typography, spacing, and components before any project work; exports to [[claude-code]] as a zip
- **Brainstorm in chat** — Use regular Claude for planning (separate limit from Design); saves ~8% of weekly Design quota
- **Edit in canvas** — Three editing surfaces (edit tool, draw tool, tweaks panel) cost zero session tokens vs prompting
- **Opus 4.7 for planning, Sonnet 4.6 for tweaks** — Quality holds on Sonnet 4.6 when specs are tight
- **Export to Code when quota hits** — Zip the project, drop into [[claude-code]], continue until Design resets

## Codex Workflow Philosophy

- **Plan mode first** — Skipping plan mode is the single biggest reason builds go sideways
- **Skills as reusable recipes** — Markdown files in `.codex/` folder, global or project-level
- **GitHub + Vercel as one pipeline** — Push triggers auto-deploy; never log into Vercel again
- **Browser QA baked into skills** — Agent tests its own output before returning to user
- **Tool-rightness over tool-bias** — "Stop asking which tool is best; ask which is right for this job"
- **Perspective councils beat one-shot research** — For deep briefings, fixed multi-lens workflows plus a verifier pass can outperform a single research prompt

## Brand Built: Tally

Full brand identity created entirely in [[claude-design]] with no prior assets — just a logo PNG, a markdown brand concept doc, and button feel notes. Outputs included investor pitch deck, landing page, mobile app prototype, brand guidelines doc, and animated launch video via HyperFrames.

## Related Concepts

- [[ai-design-workflow]] — The three-surface pipeline: chat (plan) → Design (execute) → Code (ship)
- [[claude-code-subagents]] — Boss-worker framing for isolated Claude Code workers with cheaper delegated execution
- [[codex-master-guide]] — Deep tutorial on OpenAI Codex: setup, skills, automations, browser QA
- [[claude-code-workflows]] — Parallel CLI-agent patterns in the Claude ecosystem
- [[storm-multi-perspective-research]] — Research workflow using fixed expert lenses, contradiction mapping, and adversarial fact verification
- [[landing-page-ai-workflow]] — Another AI landing page workflow; overlaps on vibe-coding principles and design-to-code handoff

## Related
- [[xarticle-2050941624578920535]] — xarticle by @nateherk, related entity
