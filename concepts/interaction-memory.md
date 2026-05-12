---
title: Interaction Memory
created: 2026-05-03
updated: 2026-05-03
type: concept
tags: [enterprise-ai, memory, knowledge-management, company-brain]
sources: [raw/articles/company-brain-part-3-interaction-memory-ashwingop-2026-05-03.md]
related_entity: [[sentra]]
author: [[ashwin-gopinath]]
---
# Interaction Memory

The second layer of the [[company-brain]] framework. The memory of what happened *between people* before an artifact existed.

## Definition

Interaction memory preserves the organizational reasoning that factual memory usually drops:
- Why something happened
- How people expected the work to be done
- What constraint mattered
- Which assumption was fragile
- What was left unsaid

It is the chain of thought of the organization — the trace of how a group moved from partial information to judgment.

## Contrast with Factual Memory

| Factual Memory | Interaction Memory |
|----------------|-------------------|
| What happened | What was meant, debated, promised |
| Artifacts (tickets, CRM, docs) | Conversations before the artifact |
| Records the aftermath | Preserves how meaning was created |

Example: A CRM field says an account is at risk. The interaction memory explains the real objection from the customer call.

## The Ontology Problem

A transcript stores the sentence. A meeting summary stores the topic. But the *meaning* depends on the ontology:

> "We can ship this Friday if legal signs off and Acme is okay with the beta limitation."

Different lenses interpret this differently:
- **Product lens**: launch plan with a constraint
- **Legal lens**: approval dependency
- **Customer lens**: conditional commitment to Acme
- **Sales lens**: deal risk
- **Action lens**: contains follow-ups
- **Executive lens**: not actually a closed decision

## Dynamic Meaning

Interaction memory cannot be a static note archive. Change the ontology, and the same interaction means something different:
- A casual objection → later evidence of churn risk
- A technical concern → later explains why a launch slipped
- A one-line approval → later becomes precedent

## Requirements for a Useful System

1. **Before a call**: surface prior commitments, open issues, decision history, unresolved questions
2. **After a meeting**: identify decisions, assumptions, risks, follow-ups
3. **Weeks later**: notice patterns across interactions that no single person holds

## Proactive Capabilities

A Company Brain with interaction memory should notice:
- When the same objection appears in three customer calls
- When two teams use conflicting definitions of the same metric
- When a decision keeps getting reopened because the original tradeoff was never recorded
- When an owner is implied but never named
- When an escalation has quietly become a product signal

## Permissions and Boundaries

Not a detail — central to trust:
- Some interactions are personal
- Some are team context
- Some are company records
- Some can be summarized but not quoted
- Some should contribute to aggregate memory without raw exposure

Getting it wrong feels like surveillance. Getting it right feels like the company finally stopped losing the thread.

## Related Concepts

- [[company-brain]] — the framework this is a layer of
- [[factual-memory]] — the layer below
- [[action-memory]] — the layer above
- [[knowledge-graph-rag]] — context graph structure for connecting interactions
- [[agent-memory-architecture]] — related memory design principles
