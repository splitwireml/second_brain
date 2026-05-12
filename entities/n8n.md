---
title: n8n
created: 2026-05-10
updated: 2026-05-10
type: entity
tags: [automation, workflow-automation, platform, self-hosted]
sources: []
---

# n8n

Open-source workflow automation platform (fair-code license). Chains nodes representing tools, APIs, and logic into automated pipelines. Used as the automation layer in [[obsidian-knowledge-vault-system]] for scheduled data ingestion into Obsidian vaults.

## Relationship to AI Agent Workflows

n8n acts as the orchestrator/scheduler layer, triggering workflows that feed data into AI systems. In the obsidian-knowledge-vault pattern, n8n handles the "automated capture" part of the pipeline — polling sources and writing to Obsidian on a schedule.

## See Also

- [[obsidian-knowledge-vault-system]] — where n8n is used as the automation layer
- [[workflow-automation]] — the broader concept
- [[obsidian]] — the destination vault system
