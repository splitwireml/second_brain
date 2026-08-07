---
title: Buzz
created: 2026-07-24
updated: 2026-08-07
type: entity
tags: [product, ai-agent, agent-systems, ai-tools, open-source, self-hosted, platform, workflow, desktop-app, cli, protocol, architecture, x-article]
sources: [raw/articles/xarticle-why-were-buzzing-2080056638820450400.md, raw/articles/github-block-buzz-readme-2026-08-07.md, raw/articles/github-block-buzz-architecture-2026-08-07.md, raw/articles/github-block-buzz-workflow-schema-2026-08-07.md, raw/articles/github-block-buzz-workflow-executor-2026-08-07.md]
---

# Buzz

Buzz is Block's Apache-2.0, self-hostable workspace where humans, AI agents, workflows, and code share one relay-backed event surface. It is built on Nostr-style signed events: the relay is the source of truth, and messages, reactions, workflow activity, reviews, approvals, and git events share an identity and audit model. The current repository describes a single-relay community as the normal deployment boundary; hosted multi-community deployments keep each community's observable state isolated by host.^[raw/articles/github-block-buzz-readme-2026-08-07.md][raw/articles/github-block-buzz-architecture-2026-08-07.md]

## Architecture and operating model

Humans use the desktop/web surfaces; agents can connect through `buzz-acp` (ACP over stdio) or the agent-first `buzz-cli` (JSON in/JSON out over the relay REST API). Each agent has its own Nostr keypair, channel membership, and signed activity trail. The ACP harness queues work per channel, keeps at most one prompt in flight per channel, and can process multiple channels concurrently when more agent subprocesses are configured. This is an agent workspace and control plane, not an LLM or a graph database.^[raw/articles/github-block-buzz-readme-2026-08-07.md][raw/articles/github-block-buzz-architecture-2026-08-07.md]

The relay receives signed events, verifies and stores them, publishes/fans them out, indexes them, audits them, and evaluates workflows. Custom event kinds provide identifiers for jobs and workflow execution. Workflow execution events are excluded from retriggering workflows, preventing the most obvious self-triggering loop.^[raw/articles/github-block-buzz-architecture-2026-08-07.md]

The product thesis is “one context”: a branch, patch, CI result, review, conversation, and merge decision can live in the same searchable channel. That gives agents historical receipts and attributable handoffs instead of forcing them to reconstruct state from Slack, a forge, CI, and separate agent logs.^[raw/articles/xarticle-why-were-buzzing-2080056638820450400.md][raw/articles/github-block-buzz-readme-2026-08-07.md]

## Native workflow engine

Buzz's workflow definition is an ordered YAML program stored as canonical JSON. It supports `message_posted`, `reaction_added`, `diff_posted`, `schedule` (cron or interval), and `webhook` triggers. Steps run sequentially; each step can have an `if` expression, timeout, template substitutions from trigger fields, and outputs from earlier steps. The schema defines message/DM/topic/reaction/webhook/approval/delay actions.^[raw/articles/github-block-buzz-workflow-schema-2026-08-07.md]

The current implementation has important maturity boundaries: `send_message` is wired through the relay action sink; `send_dm` and `set_channel_topic` are explicitly marked not implemented in the workflow executor; webhook and reaction behavior is feature-dependent; and the approval path can suspend but still contains TODOs for persisting the approval record/event and handling resume. Treat the schema as the contract surface, not proof that every action is production-ready.^[raw/articles/github-block-buzz-workflow-schema-2026-08-07.md][raw/articles/github-block-buzz-workflow-executor-2026-08-07.md]

## Status and open work

The README lists relay/channels/threads/DMs/canvases/media/search/audit, desktop, `buzz-cli`, ACP harnesses, YAML workflows, and git events as working surfaces. It separately lists mobile clients and workflow approval gates as being wired up. The repository therefore supports a real event/workflow substrate, but the product is still moving and its vision documents contain designed-for-later forge and governance layers.^[raw/articles/github-block-buzz-readme-2026-08-07.md][raw/articles/github-block-buzz-workflow-schema-2026-08-07.md]

## Pipeline fit

Buzz is a strong **control-plane and evidence layer** for [[graph-engineering]] and [[loop-engineering]]: use channels/events for triggers, durable context, signed worker reports, human approvals, and searchable run history. It is not currently a native DAG or loop runtime: its workflow executor is sequential, has conditional skips rather than general graph edges, and does not expose first-class fan-out/fan-in, join barriers, loop-until-verified, retry policy, or dependency scheduling. The practical verdict is filed in [[buzz-for-graph-loop-pipelines]].

## Related

- [[jack]] — source author metadata
- [[social-ai]] — the people-and-agents network framing
- [[agent-native-apps]] — broader agent-facing product category
- [[company-brain]] — shared organizational context and action memory
- [[human-in-the-loop]] — approval and autonomy boundary
- [[agent-native-canvas]] — related agent-accessible canvas surface
- [[graph-engineering]] — dependency-first graph orchestration
- [[loop-engineering]] — bounded recurring agent control systems
- [[buzz-for-graph-loop-pipelines]] — suitability analysis
