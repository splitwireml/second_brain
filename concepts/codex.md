---
title: Codex
created: 2026-05-31
updated: 2026-07-28
type: entity
tags: [llm, model, code-generation, coding, openai]
sources: [raw/articles/xarticle-how-i-build-apps-with-codex-without-opening-xcode-2040132557983936772.md, raw/articles/xarticle-practical-multi-agent-orchestration-in-codex-2080707291603407077.md, raw/articles/xarticle-gpt-6-astra-has-completely-changed-the-way-i-run-m-2102753461796262232.md]
related_entity: [[openai]]
---

# Codex

OpenAI's code-specialized model family — fine-tuned from GPT for programming tasks. Powers GitHub Copilot and the [[openai-codex-plugin-cc]] for Claude Code.

In Paul Solt's source, Codex is used as the operating agent for iPhone and Mac app development. The key enabler is not model access alone but an [[agent-friendly-xcode-projects]] substrate: low-noise build output, repeatable `make` actions, focused tests, runtime logs, and project rules.

## Multi-Agent V2 orchestration

Eric Provencher's July 24, 2026 local X Article describes Codex's source-reported **Multi-Agent V2** tools as a coordination layer for GPT-5.6 Sol and Terra. The article presents **Ultra** as a coordination default for high-stakes work where ambiguity or scattered context justify extra depth. For other tasks, a short prompt or skill can encourage collaboration while Sol remains in the user's conversation. These capability and model-behavior claims are preserved as source-described rather than independently verified.^[raw/articles/xarticle-practical-multi-agent-orchestration-in-codex-2080707291603407077.md]

The article keeps one model family and routes work by reasoning effort: **GPT-5.6 Sol Light** as a read-only Scout for locating files, tracing code paths, and finding tests; **GPT-5.6 Sol Medium** as a Worker for scoped implementation and checks; and **GPT-5.6 Sol High** as a Smart worker for difficult implementation, ambiguity, or coordination. It says Sol Light retains enough judgment to find useful context without spending as much reasoning on discovery.^[raw/articles/xarticle-practical-multi-agent-orchestration-in-codex-2080707291603407077.md]

The coordinator assigns substantive work, avoids duplicate investigations, and tracks agent activity. Scouts can investigate in parallel, workers can share implementation when responsibilities are clear, and agents can message one another through a common messaging system with separate inboxes. Concurrency is configurable per thread and defaults to **four agents including the coordinator**. The source does not specify the messaging protocol, inbox storage, scheduler, or API surface.^[raw/articles/xarticle-practical-multi-agent-orchestration-in-codex-2080707291603407077.md]

Forked conversation history carries the broader goal and earlier decisions; `fork_turns: "none"` starts a fresh, focused assignment. Fresh-context agents can still contact teammates but do not inherit task-specific tool or safety boundaries. The source's leaf-worker boundary is: `Complete this assignment directly. Do not spawn other agents; your parent's delegation instructions apply only to your parent.` Its coordinator skill uses `reasoning_effort: "low"` for focused read-only scouts, `"medium"` for routine implementation, and `"high"` for harder problems; it requires clear ownership, non-overlapping assignments, no delegation by leaf workers, result synthesis, and keeping approvals with the user.^[raw/articles/xarticle-practical-multi-agent-orchestration-in-codex-2080707291603407077.md]

## Astra computer-use workflow (2026-09-24)

A Dickie Bush local X Article presents **GPT-6 Astra in Codex/ChatGPT desktop** as a source-described computer-use harness rather than a CLI-only coding flow. The article quotes a claimed 1.9× Mind2Web task-completion speedup against GPT-5.6 Sol and claims browser/form, CRM, calendar, research/email/document, scientific-data/plot, website/frontend-QA, software-install/test, and on-screen-troubleshooting coverage; it reports no reproducible configuration, benchmark protocol, permission model, auth scope, connector contract, or independent verification. ^[raw/articles/xarticle-gpt-6-astra-has-completely-changed-the-way-i-run-m-2102753461796262232.md]

The source's concrete access matrix is browser login for Typeform, Namecheap, Calendly, and Zapier, versus MCP login for Airtable, GitHub, Vercel, and Slack. It describes a rough desired outcome and build-order review, then autonomous execution interrupted only for consequential decisions, iterative plain-English changes, full cross-tool testing, and a final bullet summary. This is a source-specific instance of [[decision-work-and-doing-work]], [[human-in-the-loop]], and [[loop-engineering]]; it does not establish that the named integrations, completion timings, or first-try results generalize. ^[raw/articles/xarticle-gpt-6-astra-has-completely-changed-the-way-i-run-m-2102753461796262232.md]


## Related

- [[openai]] — parent company
- [[openai-codex-plugin-cc]] — Codex plugin for Claude Code
- [[agent-friendly-xcode-projects]] — Apple app-development substrate for Codex
- [[paul-solt]] — source author documenting the workflow
- [[pvncher]] — source author documenting Codex Multi-Agent V2 orchestration
- code-generation — code gen more broadly
- coding — programming context
