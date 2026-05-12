---
title: Garry Tan
created: 2026-04-23
updated: 2026-04-23
type: entity
tags: [person, y-combinator, x-creator, independent-developer]
sources: [raw/articles/garrytan-skillify-agent-reliability-2046876981711769720.md, raw/articles/xarticle-meta-meta-prompting-the-secret-to-making-ai-agents-2053127519872614419.md]
---

# Garry Tan (@garrytan)

President of Y Combinator, founder of GBrain and OpenClaw. X creator who wrote extensively about agent reliability engineering via the "skillify" methodology.

## Key Work

**Skillify Methodology** (April 2026): Garry Tan's framework for making AI agents permanently reliable by converting every failure into a tested skill. The 10-step skillify checklist: SKILL.md → deterministic code → unit tests → integration tests → LLM evals → resolver trigger → resolver eval → DRY audit → E2E smoke test → brain filing rules. The core insight: the model generates the constraint that prevents the model from being stupid — latent space builds the deterministic tool, then the deterministic tool constrains the latent space.

**Thin Harness / Fat Skills**: Agent architecture philosophy where the harness is minimal and skills carry the weight. Key distinction between latent (judgment-requiring) and deterministic (precision-requiring) work.

**Products**: GBrain (open-source knowledge engine for agents), GStack (speed-up tools for Claude Code), OpenClaw (agent framework).

## Key Links

- [GBrain](https://github.com/garrytan/gbrain) — knowledge engine
- [GStack](https://github.com/garrytan/gstack) — Claude Code speed-up
- [OpenClaw](https://openclaw.ai/) — agent framework

## Related

- [[openclaw]] — agent framework
- [[hermes-agent]] — compared to in article
- [[skillify]] — the methodology concept
