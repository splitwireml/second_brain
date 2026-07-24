---
title: Agent-Native Apps
created: 2026-07-16
updated: 2026-07-24
type: concept
tags: [ai-agent, agent-systems, skills, tools, mcp, opportunity, framework, business-models, platform]
sources: [raw/articles/xarticle-how-id-make-10-million-with-ai-agents-2076733920834371585.md, raw/articles/xarticle-introducing-tldraw-offline-2077784657869902121.md, raw/articles/xarticle-why-were-buzzing-2080056638820450400.md]
related_entity: [[greg-isenberg]]
author: [[greg-isenberg]]
---

# Agent-Native Apps

Agent-native apps are products designed for an agent operating surface rather than a human tapping through a conventional GUI. In [[greg-isenberg]]'s source-described framing, the model runs programs, the context window supplies memory, tools touch the world, markdown files act as configuration, and skills act as applications.^[raw/articles/xarticle-how-id-make-10-million-with-ai-agents-2076733920834371585.md]

## Product surface

The proposed app is often a plain-English skill or tool definition that an agent can load and execute. Candidate surfaces include:

- voice agents that answer missed business calls and book work;
- payments, memory, and identity infrastructure for agents;
- industry skill libraries such as bookkeeping procedures for a dental practice;
- systems that turn undocumented business knowledge into agent-readable operating context;
- message-native products that work through iMessage rather than requiring a new app install.

The source's claim that thousands of MCP servers exist against tens of millions of US businesses is directional and source-reported, not an independently verified market census.^[raw/articles/xarticle-how-id-make-10-million-with-ai-agents-2076733920834371585.md]

[[tldraw-offline]] supplies a concrete file-native example of the category: the source describes a local canvas with no account or server that agents can access, edit, and extend with scripts. This is the narrower spatial pattern captured by [[agent-native-canvas]].^[raw/articles/xarticle-introducing-tldraw-offline-2077784657869902121.md]

## Shared-workspace example

[[buzz]] supplies a networked example of the category. Its source-described workspace puts people, agents, conversations, and code behind a shared cryptographic identity system; signed events, searchable history, channels, patches, reviews, workflows, and approvals are intended to preserve context across the work surface. Unlike a single-user skill or file-native tool, this is the mixed human/agent collaboration variant named [[social-ai]]. Product capabilities and roadmap details remain source-reported.^[raw/articles/xarticle-why-were-buzzing-2080056638820450400.md]

## Design implications

Agent-native apps should expose clear triggers, context requirements, tools, autonomy boundaries, approval points, escalation rules, and success criteria. That seven-question specification connects this market thesis to [[agent-saas-playbook]]: the product is not merely a prompt, but a bounded workflow with an observable finish line and a trust wrapper.

The packaging layer is [[agent-skills-framework]] and related skill systems: reusable markdown instructions can carry domain procedures across model and execution contexts. The implementation still needs the controls described by [[agentic-software-five-layer-framework]], including data, security, interface, and infrastructure boundaries.

## Evidence status

- **Source-described:** markdown skills, MCP connectivity, voice, messaging, infrastructure, and business-legibility are presented as open opportunity areas.
- **Interpretive synthesis:** the durable distinction is between software that waits for a person to click and software that an agent can invoke when a trigger, context, and permission boundary are satisfied.
- **Open questions:** discoverability, identity, payment authorization, security, and the economics of distributing skills remain unresolved in this single source.

## Related

- [[greg-isenberg]] — source author
- [[buzz]] — networked human/agent workspace example
- [[social-ai]] — shared human/agent network framing
- [[agent-saas-playbook]] — bounded agent products sold as completed work
- [[agent-skills-framework]] — skill packaging and reusable markdown instructions
- [[agentic-software-five-layer-framework]] — production systems architecture and controls
- [[ai-business-models-2026]] — business-model context
