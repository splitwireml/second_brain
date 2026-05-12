---
title: OpenRouter Agent Skill Creation
created: 2026-04-25
updated: 2026-04-25
type: concept
tags: [hermes-agent, skill, agent-tool]
sources: [raw/articles/openrouter-hermes-agent-openrouter-expert-2026-04-24.md]
related_entity: [[openrouter]]
author: [[openrouter]]
---

# OpenRouter Agent Skill Creation

A pattern where an agent builds its own domain-expert skill by reading the provider's LLM-optimized docs index. Demonstrated with [[hermes-agent]] + [[openrouter]], where Hermes reads the OpenRouter docs index (`openrouter.ai/docs/llms.txt`) and creates a reusable skill that routes future OpenRouter questions to the right docs.

## Pattern
1. Feed the agent a prompt instructing it to read the provider's docs index
2. Agent reads the structured docs index (built for LLM consumption)
3. Agent creates a compact resolver skill with decision frameworks, routing tables, gotchas, and verification steps
4. Skill is placed at `~/.hermes/profiles/<profile>/skills/<category>/openrouter-expert/SKILL.md`
5. Smoke test: ask a domain question and verify the agent loads the skill and checks docs

## Key Principle
The resulting skill keeps the agent from guessing about fast-changing details (model IDs, pricing, SDK behavior, docs URLs). Instead it provides decision frameworks and routes to current docs.

## Related
- [[hermes-skills-workflow]] — other Hermes skill patterns
- [[skillify]] — Garry Tan's methodology for converting agent failures into tested skills
- [[hermes-agent]] — the agent this pattern is demonstrated on
- [[openrouter]] — the platform this specific instance targets
