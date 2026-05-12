---
title: Skillify
created: 2026-04-23
updated: 2026-04-23
type: concept
tags: [agent, skill, reliability, testing, llm]
sources: [raw/articles/garrytan-skillify-agent-reliability-2046876981711769720.md]
related_entity: [[garrytan]]
author: [[garrytan]]
---

# Skillify

Garry Tan's methodology for making AI agents permanently reliable by converting every failure into a tested skill. A skill is a markdown procedure (SKILL.md) that teaches the model how to approach a task — not what to do (the user supplies the what), but the process. Once "skillified," a failure becomes structurally impossible to repeat.

## Core Loop

> The model uses judgment (latent space) to write the deterministic script. The skill (markdown, in latent space) tells the agent to use that script. The deterministic script constrains the model. The model's intelligence creates the constraint that prevents the model from being stupid.

## The 10-Step Checklist

1. **SKILL.md** — the contract (name, triggers, hard rules)
2. **Deterministic code** — `scripts/*.mjs` (no LLM for what code can do)
3. **Unit tests** — vitest on deterministic functions
4. **Integration tests** — live endpoints, real data
5. **LLM evals** — quality + correctness via model-as-judge
6. **Resolver trigger** — entry in AGENTS.md routing table
7. **Resolver eval** — verify the trigger actually routes correctly
8. **Check-resolvable + DRY audit** — find unreachable/duplicate skills
9. **E2E smoke test** — full pipeline verification
10. **Brain filing rules** — where things go in the knowledge base

## Key Examples

- **calendar-recall**: Agent was doing calendar lookups in latent space (slow, wrong). Skill forces "always search local knowledge base first for historical events." Agent wrote the deterministic `calendar-recall.mjs` script. Now runs in <100ms, zero LLM calls.
- **context-now**: Agent was doing UTC→PT timezone math in head (wrong). Skill forces "always run `context-now.mjs` before any time-sensitive claim." Structurally impossible to get timezone math wrong again.

## The Thin Harness / Fat Skills Philosophy

Key distinction:
- **Latent work**: requires judgment, reasoning, interpretation → LLM
- **Deterministic work**: requires precision, consistency → scripts

The failure mode is doing deterministic work in latent space (slow, error-prone). The fix is a skill that routes to a script.

## GBrain

GBrain is the open-source implementation of the skillify pattern. gbrain doctor auto-repairs DRY violations and checks all 10 steps. SkillPacks are portable bundles of skills + tests + resolver triggers that can be installed into any OpenClaw/Hermes Agent setup.

## Why Existing Frameworks Fall Short

LangChain raised $160M but only gives testing tools, not an opinionated workflow. No framework says "in order: write the skill, now write the deterministic code, now write the unit tests, now write the LLM evals." That loop doesn't exist in LangChain, LlamaIndex, etc. You get primitives; skillify provides the practice.

## Related

- [[openclaw]] — framework where skillify is implemented
- [[hermes-agent]] — compared in article (Hermes handles creation, GBrain handles verification)
- [[hermes-tool-plugin-architecture]] — Hermes's skill architecture
- [[agent-teams]] — related multi-agent patterns
