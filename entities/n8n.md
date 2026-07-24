---
title: n8n
created: 2026-05-10
updated: 2026-07-24
type: entity
tags: [platform, automation, self-hosted, workflow-automation]
sources: [raw/articles/xarticle-youre-using-claude-wrong-if-you-dont-have-these-6--2080083376976044193.md]
---

# n8n

Open-source workflow automation platform (fair-code license). Chains nodes representing tools, APIs, and logic into automated pipelines. Used as the automation layer in [[obsidian-knowledge-vault-system]] for scheduled data ingestion into Obsidian vaults.

## Relationship to AI Agent Workflows

n8n acts as the orchestrator/scheduler layer, triggering workflows that feed data into AI systems. In the obsidian-knowledge-vault pattern, n8n handles the "automated capture" part of the pipeline — polling sources and writing to Obsidian on a schedule.

## Claude MCP Use Case (2026-07-24)

AI with Remy's article describes an n8n MCP that lets Claude plan, build, and run workflows directly. Examples include a scheduled weather email and a webhook-triggered lead-magnet delivery flow; the source emphasizes approving the plan before spending roughly 10% of the time on the build. These are source-described workflows, not independently verified n8n or MCP behavior. ^[raw/articles/xarticle-youre-using-claude-wrong-if-you-dont-have-these-6--2080083376976044193.md]

Related: [[model-context-protocol]], [[aiwithremy]].

## See Also

- [[obsidian-knowledge-vault-system]] — where n8n is used as the automation layer
- workflow-automation — the broader concept
- obsidian — the destination vault system
