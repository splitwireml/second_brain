---
title: Action Memory
created: 2026-05-03
updated: 2026-05-04
type: concept
tags: [enterprise-ai, memory, knowledge-management, company-brain]
sources: [raw/articles/company-brain-part-4-action-memory-ashwingop-2026-05-04.md, raw/articles/company-brain-part-3-interaction-memory-ashwingop-2026-05-03.md]
related_entity: [[sentra]]
author: [[ashwin-gopinath]]
---
# Action Memory

The third layer of the [[company-brain]] framework. Coordinates what happens next once the company remembers what happened (factual) and understands what interactions meant (interaction).

## Core Thesis

The most important thing a Company Brain can do at the action layer is **not act**. Doing nothing is a first-class action. A useful system acts because context says it should, and stays still when it should not. If a Company Brain cannot do nothing on purpose, it cannot be trusted to do anything on purpose.

Action memory is partly agentic — it must participate by noticing condition changes, deciding whether something should happen, choosing the right path, respecting guardrails, and either acting or asking a human to act. This makes it closer to the nervous system of the company than to a knowledge base.

## Four Memory Parts

### 1. Procedural Memory
How a process is supposed to work. Covers known paths for: onboarding enterprise customers, issuing refunds, approving pricing, escalating incidents, handling security reviews. The work that companies pretend is more standardized than it is.

### 2. Trigger Memory
When something should happen. Conditions that should wake a workflow up:
- A customer mentions churn risk twice
- A support ticket sits unresolved for 48 hours
- A deal crosses a discount threshold
- A renewal is 30 days away
- A roadmap commitment becomes late
- A metric crosses a line
- A promise is made in a meeting
- An agent takes an action that needs human review

### 3. Execution Memory
What actually happened in a specific case:
- Who approved the exception
- Which step took too long
- What workaround was used
- Which agent sent the email
- Who corrected it
- What handoff failed
- Which system became the source of confusion

### 4. Outcome Memory
What happened after the action:
- Customer renewed / didn't renew
- Workaround created technical debt
- Escalation reduced / increased risk
- Agent action needed human correction
- Same issue came back two weeks later

The result matters because the company should not treat every completed workflow as successful.

## Key Distinction: Official vs Actual Workflow

Most workflow diagrams are "polite fiction" — they show the official process, not the real one.

Example support flow:
- **Official**: create ticket → assign owner → resolve issue → update customer
- **Actual**: customer texts founder → founder asks product → product remembers related bug → engineering fixes directly → support updates ticket later

The gap grows as companies scale. Routing logic becomes tribal knowledge:
- This customer needs legal
- That customer should go through the CEO
- This exception is safe under 10% but needs finance above that
- This integration always breaks when procurement gets involved

## The Three Layers Together

| Layer | Function | Agent Capability |
|-------|----------|-----------------|
| [[factual-memory]] | Record of what exists | Find account, ticket, policy, contract, document |
| [[interaction-memory]] | Organizational reasoning | Understand why work matters, what was promised, what was debated |
| **Action memory** | Operational continuity | Know when something changed, what workflow should start, who needs to care, what guardrails apply, whether to act or escalate |

An agent with action memory can: draft the follow-up, create the ticket, request approval, notify the owner, update the CRM, escalate the risk, or deliberately do nothing. That is the difference between an agent that has tools and an agent that can operate inside a company without creating more cleanup work than it saves.

## Guardrails

Action memory functions as guardrails. A refund, customer email, pricing exception, and production change should not all be treated the same way just because an agent can technically perform them:
- Some actions are safe to execute
- Some require approval
- Some affect money or production
- Some look similar to precedent but differ in one detail that changes the risk

The system must remember the difference between "this is routine" and "this only looks routine."

## Timing

Much important work does not start because someone asks a question. It starts because a condition changed:
- A risk appears
- A promise is made
- A deadline is approaching
- A customer repeats an objection
- A blocker appears in a meeting
- A metric moves
- An agent takes an action that needs review

Action memory is the difference between remembering a process and noticing that the process has become relevant.

## Role Perspectives

- **IC**: needs the next step and context to do it well
- **Manager**: needs to see where handoffs are failing and where commitments are stuck behind a single reviewer
- **CEO**: "Where is the company repeatedly failing to turn decisions into action?" — a map of where the company loses momentum, where the same operating failure shows up under different names, and where strategy is silently translating into nothing

## The Loop Closes When Actions Become Memory

If an agent drafts an email, creates a ticket, updates Salesforce, escalates a risk, requests approval, or notifies an owner — the system should remember what happened:
- A successful action → becomes precedent
- A failed one → becomes risk memory
- A human correction → becomes a signal
- A workflow change → becomes part of how the company operates next time

This is how the Company Brain stops being a better knowledge base and starts becoming an **operating system** for the company.

## Related Concepts

- [[company-brain]] — the overall framework
- [[factual-memory]] — Layer 1
- [[interaction-memory]] — Layer 2
