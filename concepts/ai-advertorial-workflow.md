---
title: AI Advertorial Workflow
created: 2026-07-15
updated: 2026-07-15
type: concept
tags: [ai-content, ai-tools, marketing, paid-ads, ecommerce, conversion, funnel, copywriting, prompting, workflow, strategy, x-article]
sources: [raw/articles/xarticle-how-i-cook-killer-google-ads-advertorials-with-fab-2076724912937750754.md]
related_entity: [[claude]]
author: [[ecom-amin]]
---

# AI Advertorial Workflow

A search-driven advertorial system that uses an LLM to turn keyword intent, traffic awareness, product context, and a revision loop into editorial-style Google Ads landing-page copy. The central rule is to write for the reader's mental state before positioning the product, rather than asking AI for generic sales copy. ^[raw/articles/xarticle-how-i-cook-killer-google-ads-advertorials-with-fab-2076724912937750754.md]

## Awareness before copy

The workflow first maps the target keyword to the reader's awareness level:

- **Problem-aware:** a query such as “why do I wake up at 3am” signals a person trying to understand a problem, not shopping for a brand.
- **Solution-aware:** a query such as “best magnesium for sleep” signals awareness of a solution category but not a specific brand.
- **Most-aware:** a comparison query such as “brand X vs brand Y magnesium” supports a more direct product-comparison structure.

The advertorial should meet the reader at that stage. The source's conversion-rate and ROAS examples are claims from the author, not independently verified benchmarks.

## Six-block prompt architecture

Amin's prompt template combines:

1. **Traffic context** — exact keyword, awareness level, and first-visit status.
2. **Brand and product context** — product, mechanism, differentiator, price, and target demographic.
3. **Advertorial structure** — validate the struggle; explain the underlying cause; introduce a solution category; position the product as an implementation; add social proof; finish with a soft, risk-reversed CTA.
4. **Tone and voice** — editorial, mobile-friendly, conversational, and educational rather than commercial.
5. **Banned patterns** — no product-first opening, hype language, exclamation marks, generic transitions, or obvious ad phrasing.
6. **Output format** — short mobile paragraphs, regular subheadings, image placeholders, and a marker for the product-introduction section.

This turns a broad “write an advertorial” request into a constrained production environment. It complements the broader loop pattern in [[claude-fable-5-loop-design]].

## Revision and multiplication

The first draft is followed by three audits:

- **Hook audit:** rewrite the opening if it does not match the searcher's mental state.
- **Mechanism audit:** simplify the explanation until a non-specialist can understand why it differs from prior solutions.
- **CTA audit:** make the next step feel earned by the education rather than bolted on as a pitch.

For scale, the source proposes 3–5 distinct ideal-customer angles per product. Each angle gets its own keyword, emotional entry point, hook, and advertorial while reusing the underlying product mechanism. This is a text-first complement to [[ai-generated-ads]] and to the pain-point landing-page logic in [[ecommerce-funnel-training]].

## Boundary and open questions

The AI is treated as a production accelerator, not the strategist: the operator still chooses keywords, awareness levels, mechanisms, and test angles. The workflow also depends on truthful product evidence, compliant health claims, and real conversion data; editorial tone alone does not make a sales page trustworthy.

Open questions include whether the reported speed and ROAS gains generalize beyond the author's clients, how advertorial performance compares with direct PDP traffic across categories, and how much lift comes from awareness matching versus the model itself.

## Related

- [[ecom-amin]] — source author
- [[claude-fable-5-loop-design]] — bounded Fable 5 revision loops
- [[ai-generated-ads]] — adjacent AI advertising production
- [[conversion]] — outcome metric
- [[google]] — search and advertising context
- [[ecommerce-funnel-training]] — pain-point-specific landing-page funnel
