---
title: Company Brain
created: 2026-05-03
updated: 2026-05-04
type: concept
tags: [enterprise-ai, memory, knowledge-management, ai-agent]
sources: [raw/articles/xarticle-ashwingop-2052777467732283817.md, raw/articles/company-brain-part-4-action-memory-ashwingop-2026-05-04.md, raw/articles/company-brain-part-3-interaction-memory-ashwingop-2026-05-03.md]
related_entity: [[sentra]]
author: [[ashwin-gopinath]]
---
# Company Brain

A three-layer enterprise AI memory architecture for preserving and reasoning about organizational knowledge. Proposed by [[ashwin-gopinath]] at [[sentra]].

## Three Layers

### Layer 1: Factual Memory
What happened. Where the source is. Who owns it. When it changed. How things connect.

Preserves artifacts: tickets, CRM updates, roadmap notes, launch documents. The aftermath of decisions.

### Layer 2: Interaction Memory
What happened *between people* before the artifact existed. The chain of thought of the organization.

Preserves: why something happened, how people expected work to be done, what constraint mattered, which assumption was fragile, what was left unsaid. The organizational reasoning that rarely makes it into artifacts.

### Layer 3: Action Memory
The third layer. Remembers how the company moves. Coordinates what happens next once the company remembers what happened and understands what interactions meant.

Differs from Layers 1 and 2: it is partly agentic. Must notice condition changes, decide whether something should happen, choose the right path, respect guardrails, and either act or ask a human to act.

**Four-part structure**: procedural memory (how work is supposed to happen) + trigger memory (when to wake up) + execution memory (what actually happened) + outcome memory (what resulted).

### Layer 4 (Part 7): Semantic And Ontology
Company Brain as infrastructure layer (Part 7). Key arguments:

- **The App Mistake**: Vibe coding creates seductive demos but infrastructure is judged by durability after months of writes, permission changes, stale docs, and concurrent agents. An app can be useful while being messy. Infrastructure has to survive being depended on.

- **Markdown Brains Are Prototypes**: Personal markdown brains scale poorly organizationally. Companies have multiple writers, inherited permissions, regulated data, stale sources, conflicting teams. Files can hold information but don't decide who can see it, which ontology applies, or what happens when two agents update related state simultaneously.

- **The AWS Lesson**: Cloud made primitives reliable enough companies could build higher. Company Brain has the same shape: shared infrastructure with company-specific ontology, policy, permission model, and judgment.

- **Tool Access Is Not Company Brain**: MCP is query-time context (agent discovers company from scratch on each task). Company Brain should be maintained state that updates as work happens, with sources and permissions attached.

- **The Hard Part Is State**: Writing requires concurrency control, provenance, permission propagation, ontology binding, action traces, evals, deletion policy, and conflict handling. These are why the system can be trusted.

## Key Argument

Companies do not make most decisions inside databases — they make them in conversation. The database records the aftermath. A Company Brain must preserve both the artifacts *and* the human meaning created in interaction.

Without interaction memory, agents operate downstream of incomplete context: they retrieve the ticket, draft the email, update the CRM — but don't know the human reason the work matters.

Without action memory, the company keeps paying the coordination tax: the same exception gets rediscovered, the same escalation gets rerun, the same decision gets reopened.

## The Operating System Vision

> "This is how the Company Brain stops being a better knowledge base and starts becoming an operating system for the company. It remembers what happened, understands why it mattered, knows when a condition has changed, coordinates what should happen next, and learns from the result."

## Related Concepts

- [[factual-memory]] — Layer 1
- [[interaction-memory]] — Layer 2
- [[action-memory]] — Layer 3
- Semantic and Ontology — Layer 4 (Part 7): why shared infra beats internal builds; MCP vs maintained state; the hard problem of concurrent writes
- [[knowledge-graph-rag]] — related graph-based knowledge representation
- [[agent-memory-architecture]] — related design principles for machine-scale agent memory
- [[mcp]] — related Model Context Protocol for tool access (contrasted with Company Brain as maintained state)
