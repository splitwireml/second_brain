---
title: agent-skills-framework
created: 2026-05-09
updated: 2026-07-16
type: concept
tags: [agent, ai-agent, delegation, prompting, skill]
sources: [raw/articles/xarticle-httpstco1flvfypeuv-2053056506157781419.md, raw/articles/xarticle-the-dark-arts-of-skill-engineering-2077114326985687525.md]
related_entity: [[ridark]]
---

# agent-skills-framework

ridark's framework for structuring AI agent skills. Core principles: keep skills concise (~50 tokens), use `references/` directory for depth, set degrees of freedom, test across Haiku/Sonnet/Opus, and delegate creation to AI. It contrasts with [[skillify]]'s failure-conversion approach by focusing on concise skill authorship rather than failure-driven skill creation.

The local substantive article adds a complementary systems view: effective skills are not just reusable instructions but extensions of the agent harness. Their leverage comes from moving important behavior into routing, adversarial checks, durable state, executable scripts, hooks, browser input, and runtime-specific builds.^[raw/articles/xarticle-the-dark-arts-of-skill-engineering-2077114326985687525.md]

## Dark-arts additions

- **Route and disclose progressively** — keep the top-level skill as a router and load one relevant expert reference instead of flooding context with every capability.
- **Prefer machinery over wishes** — use blind reviewers, deterministic checks, scripts that print just-in-time instructions, and hooks that validate edits without being explicitly invoked.
- **Design for deployment reality** — persist state across sessions, compile for each harness/model combination, and make critical gates explicit enough for the weakest supported model to follow.

These additions extend the earlier concise-skill framework toward [[skill-based-agent-architecture]] and [[model-agnostic-agent-harness]] without creating a separate article-specific concept.^[raw/articles/xarticle-the-dark-arts-of-skill-engineering-2077114326985687525.md]

## Sources

- [X Article](https://x.com/ridark_eth/status/2053056506157781419) — May 9, 2026; export failed (bird read --json); full content unavailable
- [The Dark Arts of Skill Engineering](https://x.com/pbakaus/status/2077114326985687525) — July 16, 2026; local full export; source-reported case study

## Related

- [[ridark]] — related entity from frontmatter; explicit cross-link
- [[paul-bakaus]] — author of the substantive skill-engineering article
- [[impeccable]] — central case study
- [[skill-based-agent-architecture]] — structured skill design
- [[model-agnostic-agent-harness]] — harness-level control surfaces
