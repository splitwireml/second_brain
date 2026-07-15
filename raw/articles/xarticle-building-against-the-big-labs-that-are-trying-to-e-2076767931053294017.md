---
source_url: https://x.com/BrainsAndTennis/status/2076767931053294017
ingested: 2026-07-15
sha256: b9f46f135378e7ea1917e6a809824d0324449908264d7c47e22391c7c59dd036
tweet_id: "2076767931053294017"
tweet_url: https://x.com/BrainsAndTennis/status/2076767931053294017
source_file: "/Users/mali/Development/x-bookmarks/data/run-2026-07-14/2026-07-13/xarticle-building-against-the-big-labs-that-are-trying-to-e-2076767931053294017.md"
run: run-2026-07-14
---
---
title: "Building against the big labs that are trying to eat you"
source: "x-bookmarks"
tweet_id: "2076767931053294017"
tweet_url: "https://x.com/BrainsAndTennis/status/2076767931053294017"
author_name: "Peter Wang"
author_handle: "@BrainsAndTennis"
tweet_date: "Mon Jul 13 20:37:13 +0000 2026"
bookmark_date: "2026-07-13"
content_type: "x_article"
character_count: 6518
retweet_count: 28
like_count: 211
external_urls:
  - "https://www.databricks.com/blog/benchmarking-coding-agents-databricks-multi-million-line-codebase)"
---

# Building against the big labs that are trying to eat you

Building against the big labs that are trying to eat you

The ongoing doomer sentiment on big model companies eating your product / startup is getting a little exhausting. Startups and builders still have natural structural advantages, and these can be used to carve out a niche and win.

So I'm sharing lessons I learned building the Shortcut agent when Claude for Excel is our competitor.

## Your harness is better because your life depends on it

For the labs, the main quests are training the smartest model, recursive self-improvement, and having enough enterprise revenue to do the first two. Everything else is secondary.

For me, agentic performance on spreadsheet tasks is the whole of Shortcut existence. So I'm going to beat competitors by obsessing over the harness. Prompts, tools, and context are ruthlessly refined until they are beautifully minimalistic and general. For our internal evals, which reflects the broad swaths of finance work done by our users (to be publicly released), we are 40% cheaper and 17% more accurate than Claude for Excel even when we standardize on the same base model (Opus 4.8).

We make roughly half the tool calls (37 vs 61 per task) because we have more efficient tools and are somehow more code-execution-pilled than Claude for Excel.

We take about the same number of turns they do - 36 vs 34 - but each of our turns uses a much lighter context: 3.7M input tokens per task against their 7.1M. After we break the per-task cost down by token class, our output token cost matches theirs, but they pay far more to re-read a heavier context on every turn.

A leaner context is cheaper to run and smarter to reason over, so we win on both cost and accuracy.

## Your harness is better by definition

Why? Because your domain is smaller than theirs. Claude Code and Codex ships 30+ tools each because they have to. Their tail is larger than your entire customer base, so they must support features for each of these use cases. But their capitulation to breadth floods their agent's context with additional instructions, tools, and skills, whereas you can trim all this fat to focus on 2-3 killer use cases. As an example, Pi's stripped-down harness beats Claude Code and Codex on [coding tasks](https://www.databricks.com/blog/benchmarking-coding-agents-databricks-multi-million-line-codebase), and it's not because the folks at Anthropic and OpenAI don't know what they're doing. CC and Codex serve many millions of customers and Pi is only serving devs and evals.

The goals of big labs are also often far more multidimensional than yours. Customers do not want a workflow that spawns 10 subagents, takes 20 minutes, and costs $30 for a quick PR review. This is also largely why Pi and other agent harnesses have their own niche in this coding harness ecosystem.

You, unencumbered, should not and cannot lose a marathon against a guy wearing a weighted vest.

## You must sling models

By virtue of existing outside of any one lab's ecosystem, you are allowed to use any model you wish. This is your biggest structural advantage, as big as the sodden clay of Agincourt for the English. Do not cede it at any cost. Some recent anecdotes from Shortcut:

- Shortcut's default has been Opus-family models for over a year. But when we benchmarked GPT 5.6 Sol, we found it was 2x cheaper and 2x faster than Opus 4.8 while [being just as accurate](https://x.com/BrainsAndTennis/status/2075385183436697755). So we replaced Opus for Sol as the default model 24 hours after release.

- For reading images, PDFs, and scanned tables, we benchmarked the field of multimodal models through a combination of public and internal evals. Gemini Flash won by a clear margin on accuracy, not even considering cost. So Shortcut's image and PDF perception capabilities, which powers financial data extraction, runs on Gemini. Claude for Excel still has to read your image and PDF files with Claude models even when they are worse at it and costs a great deal more.

- We recently benchmarked GLM 5.2 using our internal evals and found it was 2x slower, 2x cheaper, and scored 2-4% lower than SOTA models (79% for GLM 5.2 vs 81-83% for Opus48/Sol). This is an extremely attractive option for those that are cost-sensitive and do not need SOTA accuracy on the hardest Excel tasks. So no brainer, we serve GLM 5.2 routed through the same harness, same tools, same skills.

-  Train your own model. We trained our own model, [Pivot](https://x.com/shuying_luo/status/2072362603729568006), off of Qwen3.5-27B, for finance and spreadsheet work, and it is in production. While it still has ways to go in accuracy and performance (~Sonnet 4.5 level), it is smaller, faster, and dirt cheap to serve. Even if it never gets to Fable level intelligence, the ability to offload tasks to worker subagents for spreadsheet tasks will optimize your cost-accuracy frontier. And in the long-term, building model training and serving expertise will allow you to own your own fate, especially for enterprise customers that require ZDR and customized deployments.

Use the full landscape of closed and open-source models to widen the gap between you and any big lab forced to operate within their walled garden.

## You care more

@nicochristie and I fly to New York to sit with customers and learn the workflows that actually matter to them. Not GTM, not FDEs, founders. Then our team holds their hands until each specific workflow works, one at a time. Then we turn those workflows into benchmarks and evals written in the spirit of the real tasks, and we hillclimb against them obsessively. Then we turn the research insights back into the product, so the accuracy we won for one customer gets delivered to all of them.

A lab likely cannot run this loop for your vertical, because your vertical is not their main quest. We can, because it's the whole business. This loop, of real workflows in, benchmarks and features out, is the magic sauce.

## Expectations

Distribution is still the single biggest force in this market, but it doesn't win everything. It wins the enormous middle of the market that is genuinely fine with "good enough".

But in every single domain, there is a real and valuable slice of users who demand the best, and will pick the product that is actually right more often even if it comes from a smaller company they had to go find. Being right more often is a thing you can win by providing model choice, a focused harness, and caring more. It's hard, it's exhausting, and it's also enough.
