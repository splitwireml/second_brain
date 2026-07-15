---
title: Hermes Agent
created: 2026-04-27
updated: 2026-06-11
type: entity
tags: [agent, ai-agent, nous-research, open-source, research]
sources: [raw/articles/rohit-solo-founder-stack-2026-2047699770308014406.md, raw/articles/xarticle-the-10-hermes-agent-settings-most-users-never-find-2062720923942228205.md]
---

# Hermes Agent

Open-source AI agent by Nous Research (February 2026). Install: `curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash`

**Note:** Higgsfield Marketing Studio has its own internal "Hermes Agent" — different team, different tool. Same name, different product. The Nous Research version runs on your own machine.

Key capabilities:
- Built-in cron for scheduled research jobs
- Subagents in parallel for isolated workstreams
- Persistent memory across sessions
- Programmatic tool calling via execute_code (collapses 5-step pipelines into single inference call)
- 70+ built-in skills: web search, page extraction, browser automation, vision, image generation, text-to-speech

Operational configuration that shows up repeatedly in community writeups:
- Absolute-path memory storage and deeper retrieval make the agent genuinely cumulative across sessions
- Scheduler timezone, notifications, and failure recovery determine whether background automation is trustworthy
- Skill hot reload, chaining, and direct vault output routing are what turn Hermes from a chat tool into a 24/7 operating layer

Runs on $5 VPS.

Related: [[rohit]], [[solo-founder-stack-2026]], [[openclaw]], [[higgsfield-marketing-studio]], [[hermes-agent-practical-usecases]]

## Related

- [[oz-hermes-agent]]
- [[hermes-auto-think-auto-build]]
- [[hermes-agent-v0-13-tenacity-release]]
- [[hermes-agent-use-cases-2026]]
- [[hermes-agent-24-7-automation-patterns]]
