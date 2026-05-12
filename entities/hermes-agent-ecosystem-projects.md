---
title: Hermes Agent Ecosystem Projects
created: 2026-04-21
updated: 2026-04-21
type: entity
tags: [hermes-agent, agent, open-source, ecosystem]
sources: [raw/articles/nfctcps-hermes-agent-ecosystem-5-projects-2026-04-20.md]
related_entity: [[hermes-agent]]
---

# Hermes Agent Ecosystem Projects

Community-built projects extending Hermes Agent's core loop with specialized capabilities. All five projects share Hermes's底层循环 (core loop) as DNA, with the community layering on safety, deployment, automatic skill generation, and long-term memory.

## The Five Projects

### 1. hermes-agent-camel
Fork of Hermes Agent with integrated [CaMeL](https://github.com/piot-ga/camel) trust boundaries. Enables safe autonomous task execution in production environments without "翻车" (failure/going off the rails). Built by nativ3ai.

### 2. hermes-alpha
Cloud deployment templates + managed infrastructure for one-command Hermes deployment to cloud providers. Aims to eliminate deployment friction.

### 3. hermes-skill-factory
Meta-skill plugin — after an agent completes a task, it automatically generates a new reusable skill. Described as "Hermes 自己给自己造武器" (Hermes makes weapons for itself).

### 4. maestro
Long-running reinforcement framework with structured memory and plan-approve-execute workflow. Gives Hermes endurance for long tasks, not just short sprints.

### 5. icarus-plugin
Self-memory + automatic training of successor agents plugin. Agents work while simultaneously training their replacements — "退休计划" (retirement plan) built-in.

## Key Claims
- All five projects launched within 6 weeks of each other
- All built on Hermes Agent's core loop as shared DNA
- hermes-agent-camel specifically targets the trust boundary problem that blocks production deployment

## Related
- [[hermes-agent]] — the upstream project
- [[hermes-lcm]] — another Hermes extension (lossless context management)
- [[hermes-checkpoints-rollback]] — another reliability pattern for Hermes
