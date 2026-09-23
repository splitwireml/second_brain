---
title: Content Research Agents
created: 2026-09-22
updated: 2026-09-22
type: concept
tags: [agent, ai-agent, workflow, content-marketing, content-automation, video, tiktok, instagram, youtube, mcp]
sources: [raw/articles/xarticle-jev-is-insane-for-marketing-2102054148925526206.md]
related_entity: [[virlo]]
author: [[dsqjaffa]]
---

# Content Research Agents

A **content research agent** is a workflow that continuously gathers candidate short-form videos for a declared niche, filters them before they contaminate comparative analysis, attaches reusable hook/format/angle evidence, then routes ranked examples into a script or brief. The concrete system below is a source-described Virlo + [[jev]] deployment, not a product-neutral reference architecture.^[raw/articles/xarticle-jev-is-insane-for-marketing-2102054148925526206.md]

## Setup contract and handoff

The article's operator intake asks for niche, brand name, competitor names, and platforms—TikTok, Instagram, and YouTube Shorts—then drafts a keyword mix for human confirmation and saves an agent ID. It supports a dashboard path or an MCP/API path through `https://dev.virlo.ai/api/mcp/mcp`; the source says the Virlo credential prefix is `virlo_tkn_` and a TypeSafe Jev key connects the decision layer. The subsequent prompt substitutes `[AGENT ID]` and asks that every surfaced video be judged directly rather than summarized. It describes Virlo's candidate corpus as more than 12.8 million viral short-form videos across TikTok, Instagram Reels, and YouTube Shorts; that corpus claim is source-described, not independently verified.^[raw/articles/xarticle-jev-is-insane-for-marketing-2102054148925526206.md]

## Clearance before benchmarking

The source's key gate is **Clearance**: reject niche-mismatched videos and hashtag-stuffed videos before ranking. It evaluates caption, hashtags, and transcript, not hashtags alone; a qualifying video is then eligible for a content-research agent. The source calls both decisions structured yes/no calls with confidence and reports roughly 7,000 input tokens for a batch of 25 videos. The token volume/cost claim, exact Noul threshold, batching implementation, and false-positive/false-negative policy are not supplied.^[raw/articles/xarticle-jev-is-insane-for-marketing-2102054148925526206.md]

## Typed decision outputs versus analysis

For each admitted video, the article requests four distinct outputs: **Noul** for worth-scripting probability from 0 to 1, **Choice** for hook type/format/angle, **Score** for performance against that creator's own baseline, and confidence attached to each call. It says only Noul-passing results reach the operator. Virlo, not Jev, is said to benchmark 80 performance signals and tag visual, production, CTA type/frequency, and brand-safety information; Jev's role is upstream sample qualification. The speech category is described as using transcript and soundwaves alongside caption/hashtag context, but the source does not specify its audio model, interface, or data contract.^[raw/articles/xarticle-jev-is-insane-for-marketing-2102054148925526206.md]

## From ranked evidence to scripts

The script handoff uses already-tagged top results: group openings as a question, bold claim, or before-and-after; retain the attached hook/format/angle rather than guessing; choose the brand-fitting outlier; and produce a beat-by-beat script using the real opening, pacing, and structure. The source's constraint is to adapt the winning structure rather than copy it verbatim. This is a research-to-script branch of [[ai-video-virality-formats]], not evidence that any listed format will generalize.^[raw/articles/xarticle-jev-is-insane-for-marketing-2102054148925526206.md]

## Calibration status and prompt sensitivity

The article says Jev is in a live **Calibration** comparison with an existing judge rather than a finished migration. It reports 44 human-labeled videos across six research intents, with Jev correct on 33 and the existing judge on 30; it also reports a nearly-300-video disagreement population with only a handful manually graded, where Jev was right three of the first four. A prompt that treated format, tone, and audience description as hard requirements reportedly scored 16/44; one line identifying topic as the actual requirement and other brief fields as preferences reportedly moved the same test set to 33/44. These are source claims with small/partial samples, not a reproducible benchmark or a universal prompt rule.^[raw/articles/xarticle-jev-is-insane-for-marketing-2102054148925526206.md]

## Evidence boundary

The article claims Jev is up to 200× faster and 400× cheaper for classification, that response time barely changes from one to fifteen questions, and that a source example returned 384-plus videos for Bloom Nutrition in under 20 seconds. It does not provide model/version pinning, prompt text beyond the workflow instructions, request/response payloads, confidence calibration method, labeling protocol, data sampling, baseline-judge identity, threshold values, evaluation rubric, or independent replication. Keep claims, tool roles, and data handoffs distinct from other video/agent stacks.^[raw/articles/xarticle-jev-is-insane-for-marketing-2102054148925526206.md]

## Related

- [[virlo]]
- [[jev]]
- [[ai-video-virality-formats]]
- [[dsqjaffa]]
