---
updated: 2026-04-16
title: "You're Overpaying for AI by $1,200. Here's the exact math and how to fix it."
author: Noisy (@noisyb0y1)
source: https://x.com/noisyb0y1/status/2042665267256250696
date: 2026-04-10
type: raw
---

**Author:** Noisy (@noisyb0y1)  
**Date:** Fri Apr 10 18:05:25 +0000 2026  
**URL:** https://x.com/noisyb0y1/status/2042665267256250696

---

You're Overpaying for AI by $1,200. Here's the exact math and how to fix It.

Most people pay $100-200/month on AI subscriptions and never think about it.

But inside that number there are two separate leaks - and most people don't even know the second one exists.

Leak 1 - you're burning tokens you don't need to burn. Leak 2 - you're getting nothing back on subscriptions you're already paying for.

Here's the math and how to fix both.

You're Overpaying for AI by $1,200. Here's the exact math and how to fix It.

Most people pay $100-200/month on AI subscriptions and never think about it.

But inside that number there are two separate leaks - and most people don't even know the second one exists.

Leak 1 - you're burning tokens you don't need to burn. Leak 2 - you're getting nothing back on subscriptions you're already paying for.

Here's the math and how to fix both.

The real number first

```plaintext
Count honestly:
Claude Pro          $20/month
ChatGPT Plus        $20/month
Gemini Advanced     $20/month
Cursor              $20/month
Perplexity          $20/month

Total:              $100/month -> $1,200/year
```

And that's before you hit limits and upgrade to Max. Claude Max alone is $100-200/month. That's an instant 10x on costs.

Most devs I know run 3-4 subscriptions at once. Minimum $80-120/month. $1,000-1,500/year just to have access to tools.

Then wonder why the bills keep growing.

## Part 1 - Stop burning tokens you don't need

Before fixing your subscriptions - fix what's happening inside them.

A typical 30-minute Claude Code session burns ~150,000 tokens and most of them aren't your actual work. It's noise - terminal output, passing tests, verbose logs, progress bars, ANSI codes. 

All of it goes straight into Claude's context window and costs you real money.

Two tools that fix this immediately.

RTK - Rust Token Killer (28,000+ stars)

> github.com/rtk-ai/rtk

RTK sits between your terminal and Claude and filters everything before it hits the context window.

```python
WITHOUT RTK:
git status -> raw output -> ~2,000 tokens -> Claude

WITH RTK:
git status -> RTK filters/groups/deduplicates -> ~200 tokens -> Claude
```

What RTK actually does to your output:

```plaintext
cargo test:    155 lines -> 3 lines    (98% reduction)
git status:    119 chars -> 28 chars   (76% reduction)
```

Real session numbers:

```plaintext
Typical 30-min session without RTK:    ~150,000 tokens
Typical 30-min session with RTK:       ~45,000 tokens
Reduction:                              70%
```

Install takes 30 seconds:

```python
curl -fsSL https://rtk-ai.app/install.sh | bash
rtk init -g
# restart Claude Code
```

The hook automatically rewrites bash commands - 100% coverage with no manual prefixing. Works with Claude Code, Cursor, Gemini CLI, Copilot, Windsurf and 5 more tools.

Replaces: paying for tokens that carry zero useful information.

Caveman skill - cuts Claude's responses by 65-87%

> github.com/JuliusBrussee/caveman

The other side of the token problem isn't what goes in - it's what comes out. Claude by default explains itself, summarizes, asks clarifying questions and adds filler before every response.

Real benchmarks from the API:

```plaintext
explain React re-render bug:          1,180 -> 159 tokens  (87% savings)
fix auth middleware:                    704 -> 121 tokens  (83% savings)
configure PostgreSQL connection pool: 2,347 -> 380 tokens  (84% savings)
implement React error boundary:       3,454 -> 456 tokens  (87% savings)

Average across 10 tasks:              75% savings
```

```python
/plugin marketplace add JuliusBrussee/caveman
/plugin install caveman
```

Three modes: lite removes filler, full removes articles and fragments, ultra cuts everything down to telegraph style.

Combined with RTK - input tokens minus 70%, output tokens minus 75%. A session that used to cost 150,000 tokens now costs ~30,000. Same work. Same results.

## Part 2 - Three more leaks you're probably ignoring

Edit instead of reply

Every follow-up message stacks on top of all previous ones and Claude re-reads the entire history each time.

```plaintext
5 messages:    7,500 tokens
10 messages:   27,500 tokens
20 messages:   105,000 tokens
30 messages:   232,000 tokens  ← message 30 costs 31x more than message 1
```

Hit Edit on your original message, fix it, regenerate. The bad exchange gets replaced, not accumulated.

Batch your questions

Three separate prompts = three full context loads. One prompt with three questions = one load.

```plaintext
INSTEAD OF:
"Summarize this article"      -> wait
"List the main points"        -> wait
"Suggest a title"             -> wait

WRITE:
"Summarize this article, list the main points and suggest a title."
```

Upload files to Projects once

```plaintext
100-page PDF = ~75,000 tokens
Uploaded 5 times = 375,000 tokens burned
In Projects = 75,000 once, the rest is free
```

Part 3 - Now fix the subscription itself

You've cut token consumption by 70-75%. Your sessions run longer, you hit limits less often.

But you're still paying full price for every subscription every month and getting nothing back.

The average dev pays $80-120/month on AI subscriptions. That's $960-1,440/year leaving your account.

Bleap closes this with one card.

20% cashback on every AI subscription - Claude, ChatGPT, Gemini - automatically. Real money back in your account immediately.

> bleapapp.go.link/9zubt

```python
Claude Pro $20/month      -> $4 back
ChatGPT Plus $20/month    -> $4 back
Gemini Advanced $20/month -> $4 back

Total cashback:           $12/month -> $144/year
```

If you're on Claude Max:

```plaintext
Claude Max $100/month     -> $20 back every month
                         -> $240/year from one subscription alone
```

Self-custodial finance app - free virtual and physical card, no fees on spending or transfers. Cashback works on Uber, Deliveroo, Netflix and grocery stores too, not just AI subscriptions.

Replaces: paying full price for subscriptions you're going to pay anyway and getting nothing back.

The full math

```plaintext
BEFORE - what most devs pay:
AI subscriptions:              $100/month
Token efficiency:              0% optimized
Cashback:                      $0

AFTER - with everything in this article:
AI subscriptions:              $100/month (same)
Token consumption:             -70% with RTK + caveman
Sessions before limit:         3x longer
Cashback from Bleap:           $20/month on $100 in subscriptions

Net monthly cost:              $80 instead of $100
Net annual savings:            $240 back + 3x more output per dollar spent
```

You're not spending less on AI. You're getting significantly more from every dollar you already spend.

What you get after reading this

```plaintext
RTK:           150,000 tokens -> 45,000 per session (70% reduction)
Caveman:       output tokens minus 75-87%
Edit > reply:  context costs minus 31x on long conversations
Projects:      repeated files cost 0 after first upload
Bleap:         20% back on every AI subscription automatically

Total:         same subscriptions, 3x more output, $240+/year back in your pocket
```

Replaces: $1,200/year on AI subscriptions with zero optimization and paying full price for tools you use every day while getting nothing back.

You build your own life - so choose the right path. 
/ If this was useful - follow /

more info in my tg channel: [https://t.me/noisyclub01](https://t.me/noisyclub01)