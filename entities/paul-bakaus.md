---
title: Paul Bakaus
created: 2026-07-16
updated: 2026-07-16
type: entity
tags: [person, x-creator, developer, ai-tools, skill-authoring, workflow, design]
sources: [raw/articles/xarticle-the-dark-arts-of-skill-engineering-2077114326985687525.md]
---

# Paul Bakaus

Paul Bakaus (@pbakaus) is the author and builder behind the local source's discussion of [[impeccable]], a design-oriented skill/harness extension. In the article, he distills lessons from taking Impeccable from a personal experiment to a broadly used toolkit; the adoption description is source-reported and not independently verified here.^[raw/articles/xarticle-the-dark-arts-of-skill-engineering-2077114326985687525.md]

## Contribution to skill engineering

Bakaus's nine-part framework treats a skill as an extension of the agent harness rather than a saved prompt. The durable controls are adversarial review, forced divergence, internal routing, persistent state, scripts that emit just-in-time instructions, passive hooks, browser interaction, per-harness builds, and gates designed for the weakest supported model.^[raw/articles/xarticle-the-dark-arts-of-skill-engineering-2077114326985687525.md]

The article's practical emphasis is to move important behavior from prose into machinery: independent checks, explicit state, executable scripts, event hooks, and runtime-specific compilation. This connects [[skill-based-agent-architecture]] to [[model-agnostic-agent-harness]] and [[loop-engineering]].

## Related

- [[impeccable]] — the central case study
- [[skill-based-agent-architecture]] — durable skill structure and progressive disclosure
- [[model-agnostic-agent-harness]] — context, loops, tools, checks, and memory around the model
- [[loop-engineering]] — bounded execution and verification loops
- [[claude-code]] — one of the named target harnesses
