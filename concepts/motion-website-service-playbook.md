---
title: Motion-Website Service Playbook
created: 2026-07-23
updated: 2026-07-23
type: concept
tags: [ai-agent, workflow-automation, web-development, website-design, services-as-software, marketing, mcp]
sources: [raw/articles/xarticle-35k-motion-website-playbook-higgsfield-claude-code-2067204840342630789.md]
related_entity: [[zeuuss-01]]
confidence: medium
contested: true
---

# Motion-Website Service Playbook

A source-described productized service for producing high-end animated marketing websites with an agentic workflow rather than a traditional multi-role studio pipeline.

The core offer is not “a website made cheaply.” It is **a branded, motion-rich website delivered quickly enough to make custom animation accessible to businesses that would not buy a conventional studio engagement**.

## Source-described stack

- **Higgsfield MCP** — generative motion assets and access to multiple models through one connector.
- **Claude / Claude Code** — agent interface for orchestration, frame extraction, HTML/CSS generation, and assembly.
- **Motion Website Generator skill** — reusable recipe for chaining the workflow.
- **Scroll-animation layer** — the source names GSAP ScrollTrigger, Lenis smooth-scroll, frame extraction, asset optimization, layout, and copy as the systems normally coordinated manually.
- **Output** — a working scroll-driven website with cinematic effects such as film grain, particles, vignette, glass cards, color tints, and controlled scroll pacing.

The source calls the execution environment “Fable 5” in one section while the title and setup describe Claude Code / Claude. This ingest preserves that wording but does not resolve the product naming or capability boundary.

## End-to-end workflow

1. Connect Higgsfield MCP to Claude Desktop/web or Claude Code.
2. Load the motion-website generation skill.
3. Provide a brand kit and business details.
4. Generate motion clips through the Higgsfield connector.
5. Extract frames from the generated clips.
6. Generate the HTML/CSS and scroll-driven interaction layer.
7. Assemble the site and apply the visual effects.
8. Deploy a live demo that can be used in sales conversations.

## Productization model

The source recommends:

- Build three niche demos first: SaaS, e-commerce, and local service.
- Lead with a live portfolio rather than a proposal deck.
- Sell the motion/video angle: the site functions as a product video distributed across the whole page.
- Reskin one codebase for multiple clients.
- Target Shopify and Amazon sellers, Kickstarter campaigns, and local SMBs with basic static websites.

The reusable asset is the production pipeline, not any single client site.

```text
brand kit + business details
→ motion assets
→ frame extraction
→ generated HTML/CSS
→ scroll-driven site
→ niche-specific reskin
→ live demo
→ service sale
```

## Economics: evidence boundary

The source claims:

- Boutique animated websites sell for approximately $6,000–$35,000+.
- Standard agency websites range from approximately $2,500–$10,000+.
- The source cites an average project around $5,280.
- Marginal delivery cost is described as a Claude subscription plus a few dollars of Higgsfield credits.
- A Higgsfield monetization article is said to frame the stack at up to $38,400/month.

These figures are **source-reported claims**, not independently verified pricing or profit benchmarks. Actual economics depend on model credits, revisions, hosting, QA, design quality, client acquisition, legal rights, and the amount of human work required after generation.

The durable economic hypothesis is narrower:

> If a repeatable pipeline reduces production time while preserving a client-visible outcome, the operator can compete below studio pricing without selling hours one-for-one.

## What must still be validated

- Whether the referenced Motion Website Generator skill is publicly available and current.
- Which Higgsfield MCP tools and models are actually exposed at the time of use.
- Whether Claude Code performs the complete frame-extraction and assembly flow without manual intervention.
- Real per-site token and credit costs.
- Cross-browser performance, accessibility, responsive behavior, and deployment reliability.
- Whether clients value the motion site enough to pay for it over a conventional landing page.
- Rights and licensing for generated assets and reference materials.
- The conversion impact of motion websites versus well-built static sites.

## Related concepts

- [[ai-3d-scroll-websites]] — earlier wiki concept covering AI-generated 3D scroll-effect marketing sites.
- [[higgsfield-claude-creative-agency]] — broader Higgsfield + Claude creative-production stack.
- [[higgsfield]] — Higgsfield platform page.
- [[claude-code]] — agentic coding and assembly layer.
- [[zeuuss-01]] — source author.
