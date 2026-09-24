---
title: Decision Work and Doing Work
created: 2026-09-24
updated: 2026-09-24
type: concept
tags: [workflow, agent, computer-use, codex, mcp, productivity]
sources: [raw/articles/xarticle-gpt-6-astra-has-completely-changed-the-way-i-run-m-2102753461796262232.md]
related_entity: [[codex]]
author: [[dickie-bush]]
---

# Decision Work and Doing Work

**Decision Work and Doing Work** is a source-described division of AI-assisted projects: people decide the outcome, requirements, trade-offs, and acceptance judgment; the agent carries out the bounded operational steps once those choices are supplied. It is a task-classification and control-boundary pattern, not a claim that a model can safely own the whole project. ^[raw/articles/xarticle-gpt-6-astra-has-completely-changed-the-way-i-run-m-2102753461796262232.md]

## Claimed harness shift

Dickie Bush reports using GPT-6 Astra only through the Codex/ChatGPT desktop harness for ten days while exhausting a $200/month plan. He attributes the shift to three claimed changes: better browser/computer operation, conversion of vague instruction into a clear plan, and longer sequential-task tracking. The article quotes OpenAI's claimed 1.9× faster Mind2Web completion versus GPT-5.6 Sol and lists forms, CRM updates, calendar organization, online research, email/document drafting, scientific plots, website generation and frontend QA, software installation/testing, and on-screen troubleshooting. Those model, benchmark, speed, safety, and reliability statements remain source-described; this capture supplies no model card, exact setup, benchmark protocol, access controls, or independent replication. ^[raw/articles/xarticle-gpt-6-astra-has-completely-changed-the-way-i-run-m-2102753461796262232.md]

The source calls the resulting operator role “Decider” rather than “Doer”: start with a rough objective, give relevant context, review a proposed build order, answer focused questions that change the outcome, then review output. Its claimed asynchronous-question behavior permits independent work to continue while waiting, sensible assumptions for non-consequential gaps, and a pause for consequential decisions. This is adjacent to [[human-in-the-loop]] and [[loop-engineering]], but does not replace explicit constraints, evidence, or final acceptance.

## Classification at the task level

The article rejects “can AI do this whole project?” in favor of decomposing a project into smaller decisions and executions. Its Typeform example classifies form questions, requiredness, and final appearance review as Decision Work. Loading questions, updating branding, testing routing/paths, copying the embed code, and pasting it into HTML are Doing Work. A newsletter similarly leaves topic, message, stories, banner, and reader action with the human while assigning uploading, scheduling, formatting, typo checks, graphic creation, and copy-paste distribution to the agent. The source says AI may assist decisions; it does not claim that it should choose them without the operator. ^[raw/articles/xarticle-gpt-6-astra-has-completely-changed-the-way-i-run-m-2102753461796262232.md]

## Five-step build loop

1. **First pass:** write what must be complete; it need not be perfect, only enough to reveal the next decision.
2. **Access:** after reviewing the rough build order, grant each required tool through an MCP plugin or an in-app-browser login.
3. **V1 review:** inspect the first implementation, then supply feedback and newly clarified decisions.
4. **Plain-English iteration:** repeat small outcome-level changes without manually editing each tool.
5. **Infrastructure test and recap:** exercise the whole path, then request a concise bullet summary of completed work and next steps.

The source's suggested start ritual is voice-mode brain dump → pull context from Slack, Fathom, Gmail, and Notion (or directly linked material) → ask for build order and clarifying questions. It says midstream “steering” directions can be supplied without losing the original goal, and it gives a recap request: concise progress bullets with links to new resources/built elements plus the next three steps. The underlying retrieval, permission, storage, asynchronous-job, recap-link, and steering-state interfaces are unspecified. ^[raw/articles/xarticle-gpt-6-astra-has-completely-changed-the-way-i-run-m-2102753461796262232.md]

## Vortex Mastermind case

The article's source-reported case is a fully connected Vortex Mastermind funnel completed in under an hour: landing page; application Typeform; lightweight Airtable CRM; email automations; Zapier links; Slack new-application notification; GitHub and Vercel hosting; custom vortexmastermind.com domain; and a Calendly booking step. Its eight-tool access matrix is **browser login** for Typeform, Namecheap, Calendly, and Zapier, and **MCP login** for Airtable, GitHub, Vercel, and Slack. Earlier workflow examples also name Webflow, Samcart, Skool, and Kit, plus manual antecedents such as email automations, Zapier workflows, CRM fields/views, and path testing. ^[raw/articles/xarticle-gpt-6-astra-has-completely-changed-the-way-i-run-m-2102753461796262232.md]

The initial specification was explain offer/audience/value/application; embed business questions in Typeform; pipe responses to Airtable; alert Slack; host through GitHub/Vercel; and connect the custom domain. The author reports a V1 in about 15 minutes versus his estimate of 3–4 hours manual setup. His stated correction set was shorten the landing page/offer section, attach a missing brand kit, supply an omitted exact offer stack, change an Airtable form to Typeform, and reduce an overlong survey. He then asked to shorten the hero and move a testimonial above the application form, reporting both HTML and live-site changes about 30 seconds later. These timings, successful connections, and first-try reliability are source claims, not audited results. ^[raw/articles/xarticle-gpt-6-astra-has-completely-changed-the-way-i-run-m-2102753461796262232.md]

The described final test navigated to the live landing page, completed every application question, booked Calendly, checked Airtable ingestion, and checked Slack notification. The article says all connected tools worked on the first try and records a test-email address in the immutable source; this synthesis deliberately does not reproduce personal contact data. It provides no integration configuration, field mapping, domain/DNS state, auth scopes, webhook payload, error path, rollback procedure, audit log, or test-fixture detail, so the case is evidence of the author's report rather than a reproducible deployment guide. ^[raw/articles/xarticle-gpt-6-astra-has-completely-changed-the-way-i-run-m-2102753461796262232.md]

## Operating boundary

The reusable claim is not unattended automation. The author says he could work in the background because only a few further decisions required context switching, likening the system to an intern who interrupts for yes/no choices. He still retained the first build order, access grant, V1 review, iterative decisions, final infrastructure test, and completion recap. The article closes with a free Deciding & Doing project-breakdown prompt and a Ship 30 for 30 cohort promotion; product availability, content, and outcomes are not independently verified. [[dickie-bush]] supplies the author context; [[codex]] records the source-specific harness claims.

## Related

- [[dickie-bush]]
- [[codex]]
- [[human-in-the-loop]]
- [[loop-engineering]]
