---
title: Skill-Based Agent Architecture
created: 2026-05-31
updated: 2026-06-11
type: concept
tags: [agent, workflow, agent-tool, architecture, skills]
sources: [raw/articles/xarticle-the-anatomy-of-a-claude-skill-how-a-40-line-markdo-2057763612341723572.md, raw/articles/xarticle-gradient-descent-for-skillmd-files-sounds-interest-2059113412278227328.md]
---

# Skill-Based Agent Architecture

An agent design pattern where the LLM calls named skills and tools instead of improvising each task from scratch. Skills package durable procedure: a small metadata surface for discovery, then progressively loaded detail only when the task actually needs it.

## Core Shape

Nav Toor's anatomy of a production-grade skill breaks the pattern into six parts:

1. **Frontmatter** — name, description, and trigger metadata that help the model decide whether to load the skill
2. **Trigger** — a narrow task signal that tells the agent when the skill applies
3. **Instructions** — the operating rules, output constraints, and non-negotiables
4. **References** — support files that add depth only when called
5. **Scripts** — optional executable helpers that let the skill do work, not just describe it
6. **Examples** — concrete input/output demonstrations that make behavior snap into place faster than prose alone

## Progressive Disclosure

The cost model depends on staged loading:

- **Level 0** — the model sees only name and description for the whole library
- **Level 1** — the matching skill's full `SKILL.md` loads when the trigger fires
- **Level 2** — heavyweight references or scripts load on demand

This lets an agent keep a wide skill library without paying the context cost for every file on every turn.

## SkillOpt Extension

Muratcan Koylan's SkillOpt summary adds a stronger claim: skills are not just reusable docs, they can be treated as **trainable context parameters**. The practical lessons carried into this wiki are:

- **Verifier quality is the gate** — self-editing loops only matter when a held-out evaluator rejects ties and weak edits
- **Bounded diffs beat rewrites** — 4–8 edits per step acts like a learning-rate cap for markdown skills
- **Compact skills win** — the best-performing skills stay short and high-signal rather than bloating into documentation dumps
- **Portability matters** — optimized procedural context can transfer across runtimes better than the runtime-specific harness that produced it

## Design Implications

- Narrow skills age better than broad “handle all social media” blobs.
- Example-driven skills outperform instruction-only skills.
- Reference files should hold knowledge used occasionally; always-needed rules belong in the main skill body.
- Skills should be patched like living infrastructure, not treated as static prompts.
- The hard problem in self-improving skill systems is still verification for open-ended tasks like writing, design, and strategy.

## Related

- [[agent-skills-framework]]
- [[claude-skills-service-business]]
- [[claude-code]]
- [[hermes-skills-workflow]]
