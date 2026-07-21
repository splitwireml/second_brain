---
title: Agent Configuration
created: 2026-06-07
updated: 2026-07-16
type: concept
tags: [agent, claude, configuration]
sources: [raw/articles/xarticle-the-dark-arts-of-skill-engineering-2077114326985687525.md]
related_entity: [[hermes-agent]]
---

# Agent Configuration

How agent systems are configured — system prompts, skills, tools, parameters, permissions, hooks, and runtime-specific behavior. The local skill-engineering article argues that configuration is not merely prose: the most reliable behavior comes from composing the harness around the model.^[raw/articles/xarticle-the-dark-arts-of-skill-engineering-2077114326985687525.md]

## Control surfaces

- **Routing and disclosure** — use a compact top-level skill as a router and load only the relevant expert reference.
- **Executable guidance** — let scripts inspect the environment and print the next instruction when a critical branch is reached.
- **Passive enforcement** — use approved hooks to validate edits even when the user did not explicitly invoke a skill.
- **State and interaction** — persist snapshots across sessions and let browser events supply structured input for visual or interactive work.
- **Portability and gates** — compile one source into each harness/model syntax and make stop conditions explicit enough for weaker models to follow.

These controls connect [[agent-configuration]] to [[skill-based-agent-architecture]], [[model-agnostic-agent-harness]], and [[loop-engineering]]. The named Impeccable implementation is a source-described case study, not an independently tested configuration recipe.^[raw/articles/xarticle-the-dark-arts-of-skill-engineering-2077114326985687525.md]

## Related

- [[hermes-agent]]
- [[skill-based-agent-architecture]]
- [[model-agnostic-agent-harness]]
- [[impeccable]]
