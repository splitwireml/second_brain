---
title: Varick Agents
created: 2026-05-03
updated: 2026-05-03
type: entity
tags: [company, ai-company, enterprise, agent]
sources: [raw/articles/if-ai-is-so-great-why-isnt-it-working-varick-2026-04-30.md]
---

# Varick Agents

Enterprise AI deployment company founded by [[vas]] (@vasuman). Specializes in bringing AI into large enterprises to do real work without forcing massive migrations off systems of record.

## Position

Varick's core thesis: **the models are not the bottleneck**. Enterprise AI failures trace to process problems, not model capability. The company embeds operational fieldwork inside enterprises — auditing workflows, decomposing work into deterministic vs. judgment components, and building production agents on a single orchestration platform.

## Key Claims

- 18 months deploying AI agents inside enterprise teams (finance, sales, ops, engineering, marketing) at companies doing $500M to $5B+
- Varick is taking on new clients doing over $2B in revenue starting June 1, 2026
- Hiring as of the April 2026 X Article

## The "AI Isn't Working" Article

[[vas]]'s April 30 2026 X Article became a widely-discussed analysis of why enterprise AI adoption fails at 95%+ rates despite model improvements:

### Key Statistics Cited

- MIT NANDA GenAI Divide (August 2025): 5% of integrated AI pilots pull millions in value; 95% have nothing to show
- BCG: 4% have hit AI value at scale
- Deloitte: 6% achieve AI ROI within a year
- RAND: 80%+ of AI projects fail (twice the rate of normal IT projects)
- IBM: 75% of AI initiatives haven't delivered expected ROI
- McKinsey: 78% report regular AI use; 80%+ report zero EBIT impact

### Why AI Works for Engineers But Not Enterprise

Software engineering has four properties that make AI succeed:
- **Bounded**: functions take inputs and return outputs, scope is explicit
- **Checkable**: compilers and tests provide fast feedback (seconds)
- **Structured**: code lives in files, version control, deterministic build pipeline
- **Verifiable**: pull requests are discrete artifacts reviewable in 10 minutes

Enterprise functions (finance, sales, ops) are exception-heavy, undocumented, and span multiple non-interoperable systems. The conformance gap between documented SOP and actual workflow routinely runs 30-70%.

### The Four Enterprise AI Failure Modes

1. **Skip the audit** — build before understanding the actual workflow; conformance gap causes 30-70% exception rates
2. **Throw everything at LLMs** — 90% LLM calls instead of deterministic code; expensive, slow, hallucinates
3. **Agent sprawl** — individual employees build disconnected agents (50-100+ across a 200-person org), no shared spine, breaking in production
4. **Treat AI as a side-project** — budget like traditional software instead of continuously-evolving infrastructure

### What the 5% That Works Does

1. Audits 4+ weeks before building
2. Decomposes work until most is deterministic; LLM goes ONLY where judgment required
3. Builds a single orchestration layer (shared context, shared audit logs)
4. Stays model-agnostic (abstractions at task level)
5. Treats deployment as continuously evolving infrastructure with dedicated tuning team

## Related

- [[building-effective-agents]] — Anthropic paper on agentic AI; Varick cites its "find simplest solution" punchline
- [[agent-teams]] — multi-agent collaboration; Varick's orchestration layer relates to agent team architecture
- [[minimax-m27]] — open-weight model with agentic capabilities
