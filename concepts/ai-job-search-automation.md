---
title: AI Job Search Automation
created: 2026-04-13
updated: 2026-04-13
type: concept
tags: [agent, monetization, project]
sources: [raw/articles/santifer-career-ops-2026-04-13.md]
related_entity: [[career-ops]]
---

# AI Job Search Automation

Using AI agents to automate the job search process — evaluating offers, tailoring CVs, scraping portals, and tracking applications. The agent acts as a personal recruiter that works continuously without fatigue.

## Core Pattern

1. **Portal Scanning**: Agent crawls job boards (Greenhouse, Ashby, Lever, Wellfound) for matching roles
2. **Offer Evaluation**: Structured scoring across multiple dimensions (CV match, comp, level fit, culture)
3. **CV Personalization**: Generates ATS-optimized CV tailored per job description
4. **Tracking**: Maintains pipeline state across all applications
5. **Human-in-the-Loop**: AI recommends; human makes final decision

## Key Implementations

### Career-Ops ([[career-ops]])

Built by Santiago (@santifer) on Claude Code. 740+ evaluations, 100+ CVs, 1 job landed. 45+ portals pre-configured, batch processing, Go TUI dashboard. The canonical reference implementation.

## Tradeoffs

- **Quantity vs. Quality**: Automated systems can blast hundreds of applications — but experts strongly advise against scores below 4.0/5. Time is the bottleneck, not opportunity.
- **Personalization vs. Scale**: Tailoring each CV takes time. Batch systems risk generic output if not carefully prompted.
- **Authenticity**: Does an AI-tailored CV still sound like the candidate? Quality systems maintain voice.
- **Ethics**: Mass auto-application can overwhelm ATS systems and waste recruiter time. Ethical tools filter aggressively rather than spray.

## Related Concepts

- [[autoresearch]] — same autonomous loop pattern applied to marketing copy testing
- [[ai-freelancer-200-hour-guide]] — monetizing AI skills via freelancing (different angle on same problem: earning income with AI)
- [[paperclip-orchestrator]] — agent orchestration with human approval gates
