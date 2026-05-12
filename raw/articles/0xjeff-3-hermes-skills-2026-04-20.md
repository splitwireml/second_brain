---
title: "3 Highly Useful Hermes Skills"
author: "@0xJeff"
username: "@0xJeff"
created: "2026-04-20"
source: "https://x.com/0xJeff/status/2046164193326628880"
type: "x_article"
tags: [hermes-agent, skills, productivity, ai-agents]
---

# 3 Highly Useful Hermes Skills

3 Highly Useful Hermes Skills

The coolest thing about Hermes is that it learns things about you — your preference, your way of doing things, your workflows. It synthesizes all of that and create skills out of them (usually proactively, without you having to do anything).

Its own memory config + external memory provider allow Hermes to remember things, retain context from past sessions, or search its knowledge base for things you need.

Self-learning + self-remembering make Hermes very useful, the agent gets better every time it interacts with you, take in knowledge, and form its own worldview.

But at the same time, you gotta be careful because the number of skills and cron jobs can expand fast. If you change your config/setups when you have 30 skills, it can be a mess to adjust the config & debug errors which are prone to occur.

I’ve made so many of these mistakes, wasted $150-200 tokens in the past 2 weeks debugging, testing skills out, and making sure my Hermes has the right setups.

Disclaimer: my key approach in using AI right now is to accelerate/augment learning + improve productivity. So... the use cases that I’m experimenting with are all done to let me consume information/insights faster which will give me more time to complete tasks that are much higher value

(e.g. Hermes feeds me X insights so i don’t have to spend 30 mins scrolling the feed and i can use that time to talk to founders instead)

Here are my fav use cases/skills + my learnings (what to do & what not to do)

## 1. Fetch & Analyze X insights

I run multiple cron jobs in the morning everyday following X accounts that offer lots of insights into macro, geopolitics, tech, and AI.

Bird CLI is a great free tool to use to do things on X. I let my Hermes install Bird CLI and use EditThisCookie (v3) Chrome Extensions to get Cookies and feed it to the agent. It’s a highly capable tool and that’s precisely how I made my first mistake with this.

Bird doesn’t just have a permission to read but also to tweet. My Hermes hallucinated a bunch of times when it tried to fetch content on X (it’d just say “test” or post random numbers on my timeline). Because of this, I tried asking it to create a safe wrapper around the tool to only allow read. That didn’t work lol. It could still post on my timeline. I deleted Bird CLI entirely and opted for official X API instead.

Despite having to pay $0.5 each day for X API credits, I can sleep much more soundly now cuz X API has clear permission settings.

This is how Hermes report to my every morning (Kobeissi is one of the best account to track real-time geopolitics & macro)

---

## 2. Breaks down X bookmarks

I bookmark 10-20 bookmarks everyday. Before AI, I’d probably just revisit 1-2 bookmarks if they’re really interesting. The rest just sits there, stale, I forgot about it and didn’t get to consume any of those insights.

Now, Hermes looks into my bookmarks, pick 15 and rank them with priority based on my preference/investments/interests. It then summarizes them and proposes next steps. Pretty handy.

The only blocker is X API v2 — it’s not able to read X articles (for some reasons). It’d just fetch t(.)co links. Because of this, for the X article portion of the cron job, I opted for Browser Harness that just came out yesterday.

[Embedded Tweet: https://x.com/i/status/2045566281991311483]

Browser Harness is able to take control of Chrome, debugs itself, click & do things just like a human would. Perfect solution to click into X articles and read them.

My daily X bookmark cron job now looks like this

- X API → fetch bookmarks list with tweet text + linked URLs

- Browser → navigate to each article URL → extract full text

- LLM → summarize each article

- Output → daily report & store insights in wiki

---

## 3. Reflect

One of the coolest thing you could do with Hermes is “Reflect” — the agent can synthesize past information, preferences, connects relationships, detect patterns, and provides you with actionable analysis.

In order to do this, Hermes needs an external memory provider. I use Hindsight because it consistently ranks #1 for recall accuracy, especially on long-horizon, multi-session, and large-scale memory tasks.

The result is Top 5 Daily insights that highlight the signals and why it matters for me

## Other useful tools/learnings

- last30dayskill great for getting last 30 days of activity on X, Tiktok, IG, Reddit (No API needed).

- Coingecko & Defillama = bread-and-butter at getting real-time market data

- Built-in delegate task often comes in handy to help perform long-running tasks better

- Opencode Go is the best subscription to start Hermes agent with because it costs $5 for the first month and the inference credits’ more than enough to set things up

- Don’t link Hindsight to Openrouter, I did this and connected it to Claude Sonnet 4.6. It burned through $50+ worth of tokens in a day. RIP

- If you’re thinking of using Bird CLI, make sure to enable only read function. Tells it to remove write function to avoid it hallucinating and posting things for you

- If you’re using Browser Harness, practice extreme cautions. Use isolated/fresh browser, don’t share sensitive credentials with it. Don’t let it browse thru the internet randomly

## What I plan to do next

Still in Phase 1 optimizing the outputs to the point + improving my current workflows.

The next workflow that I’m probably going to try out is pre-call context — gives context on a project/team before I hop on a call with them. Plugs into social media, my past transcripts & notes, and inform me of latest status 30 mins to an hour before the call.

Will look to see if I can get started on testing out a few prediction markets strat as well (likely low risk, consistently compounding strats that could hopefully better R/R for my DeFi lending positions)

## My takeaway

The longer I use Hermes, the more the important of tokens management became clear. I don’t know if it’s really worth it to plug into GPT5.4 or Opus 4.7 at all given the prices. Open models work well so far and their subscriptions have been great. There’s no block/ban on agent harnesses so I could freely try things.

Part of the challenge of using AI is making sure I don’t burn too much money for nothing. It’s balancing what I get (which is productivity boost + more learning) to what I pay for (which is inference cost + time/headaches fixing bugs).

Also, Claude is getting so expensive man. It’s fast, it’s useful, it’s great design but it burns so much tokens. I’ve been using Claude Code to ship websites for dashboards, for my travels, to find activities. It feels good for one-off tasks so I’ll probably keep the subs around but already downgraded to $20 package.

Anyway, super excited for the future of human x agents! See you in the next one.
