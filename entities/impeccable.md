---
title: Impeccable
created: 2026-07-16
updated: 2026-07-16
type: entity
tags: [product, open-source, skill, skill-authoring, ai-tools, ui-design, design, claude-code, codex, workflow]
sources: [raw/articles/xarticle-the-dark-arts-of-skill-engineering-2077114326985687525.md]
---

# Impeccable

Impeccable is the design-focused skill and harness extension used as the central case study in [[paul-bakaus]]'s local article. The source describes it as extending coding harnesses with design-language guidance, automatic AI-slop checks, a command palette, visual iteration, and runtime-specific behavior; those capability and adoption claims are source-reported and were not independently tested here.^[raw/articles/xarticle-the-dark-arts-of-skill-engineering-2077114326985687525.md]

## Engineering patterns

The article describes Impeccable as a system rather than a long prompt:

- `/critique` combines deterministic detectors with a blind design-review sub-agent, then synthesizes the separate outputs.
- `/polish` reads per-target snapshots written by critique, giving the skill durable cross-session memory.
- Scripts such as `context.mjs` inspect the environment and print the next required instruction just in time.
- PostToolUse hooks scan edits and inject findings even when the skill was not explicitly invoked.
- `/impeccable live` connects a local browser page to the agent through a blocking poll, so visual selections become edit inputs.
- A source build compiles syntax, commands, and model-specific rules for multiple harnesses rather than assuming one runtime.
- Explicit stop gates and Haiku-baseline testing aim to keep weaker models from skipping critical steps.

These patterns make Impeccable a concrete instance of [[skill-based-agent-architecture]], [[model-agnostic-agent-harness]], and [[loop-engineering]], not merely a design prompt collection.^[raw/articles/xarticle-the-dark-arts-of-skill-engineering-2077114326985687525.md]

## Related

- [[paul-bakaus]] — article author and builder
- [[skill-based-agent-architecture]] — skills as structured, progressively loaded procedures
- [[model-agnostic-agent-harness]] — portable harness control surfaces
- [[loop-engineering]] — repeated execution, checking, and bounded stopping
- [[ui-design]] — the design domain Impeccable targets
- [[claude-code]] — one named compatible harness
- [[codex]] — one named compatible harness
