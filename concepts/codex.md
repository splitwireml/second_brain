---
title: Codex
created: 2026-05-31
updated: 2026-07-11
type: entity
tags: [llm, model, code-generation, coding, openai]
sources: [raw/articles/xarticle-how-i-build-apps-with-codex-without-opening-xcode-2040132557983936772.md]
related_entity: [[openai]]
---

# Codex

OpenAI's code-specialized model family — fine-tuned from GPT for programming tasks. Powers GitHub Copilot and the [[openai-codex-plugin-cc]] for Claude Code.

In Paul Solt's source, Codex is used as the operating agent for iPhone and Mac app development. The key enabler is not model access alone but an [[agent-friendly-xcode-projects]] substrate: low-noise build output, repeatable `make` actions, focused tests, runtime logs, and project rules.

## Related

- [[openai]] — parent company
- [[openai-codex-plugin-cc]] — Codex plugin for Claude Code
- [[agent-friendly-xcode-projects]] — Apple app-development substrate for Codex
- [[paul-solt]] — source author documenting the workflow
- code-generation — code gen more broadly
- coding — programming context
