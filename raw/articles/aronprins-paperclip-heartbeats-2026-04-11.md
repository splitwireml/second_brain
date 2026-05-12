---
updated: 2026-04-17
title: Paperclip Heartbeats Are Draining Your Budget. Here's the Fix.
source: https://x.com/aronprins/status/2042965786277347530
type: post
---

# Paperclip Heartbeats Are Draining Your Budget. Here's the Fix.

**Source:** https://x.com/aronprins/status/2042965786277347530
**Author:** [[aron-prins]]
**Date:** 2026-04-11
**Platform:** X/Twitter

---

Paperclip Heartbeats Are Draining Your Budget. Here's the Fix.

You don't need more agents. You need fewer alarm clocks.

Hello Paperclippers! 👋

I have a confession to make: I was burning through tokens faster than I should have been. My agents were running constantly, my dashboard was noisy, and after the initial success, my API bills didn't match what I was actually getting done.

While discussing a PR I submitted earlier and mentioned WHY I needed that so bad, @dotta spotted the flaw in my setup immediately:

He was right. I'd never touched this setting other then dialling it up or down.

And it was quietly costing me hundreds of dollars a month across my three companies.

Here's the question I now ask every time I look at my dashboard:

"Why is this agent running right now?"

Not "what is it doing." Just — why?

Most of the time: "It isn't. It's just waking up every 5 minutes to check if there's anything to do. There isn't."

That's a heartbeat. And if you've never touched this setting, your agents might have one switched on right now. Burning money while they sleep.

## The One Setting Draining Your Wallet 💸

Paperclip ships with heartbeats OFF by default but it is tempting to turn them on.

It feels right. Proactive. Your agent is "alive" and checking in regularly.

It isn't. It's just ringing an alarm clock with nothing on the other side.

Five agents, ticking every 5 minutes, generate roughly 2,400 useless wake-ups per week. Most of those runs say the same thing: "No tasks. Going back to sleep."

Each one costs tokens. You don't notice. Then your bill arrives.

## The Dashboard Gaslight

Here's the sneaky part.

A ticking agent looks productive. Green dots. Regular heartbeat icons. Dashboard looks buzzing.

Then you open one of those runs and find a 3-line transcript that cost $0.03.

So you think: "Maybe I should pause this agent."

You do. The dashboard goes quiet. Great.

Except — you just paused it completely. It won't wake up when you assign work. Won't run routines. Won't respond to comments. You have to manually unpause it.

This went on longer than I'm proud of.

## Pause vs. Heartbeat Off — The Actual Difference

Heartbeat off = quiet and ready. The agent sits there until work arrives.

Paused = completely dead. Hard stop. Not a volume dial.

## The Fix Takes 10 Seconds Per Agent

For each agent:

1. Open the agent
2. Find Run Policy In the Configuration tab
3. Toggle Heartbeat on interval OFF

Done.

The only time you need a heartbeat ON: an agent polling something with no webhook (RSS, an email inbox without push, an API that only exposes polling). Even then — every few hours is fine.

Most people - including myself it turns out - do not need a heartbeat on any agent.

## Routines Are the Right Tool for Scheduled Work 💡

"But I need my agent to do something every morning."

That's not a heartbeat. That's a routine.

A routine is a scheduled job. You define it once, attach a trigger (a cron expression in your local timezone, or a webhook), assign it to an agent, and Paperclip handles the rest.

When the trigger fires → Paperclip creates a task → assigns it → the agent wakes up. Clean. No polling.

Examples of things that should be routines:

- Morning standup summary (every weekday at 9am)
- Weekly metrics rollup (every Monday at 8am)
- Monthly cleanup pass (1st of every month)

The difference: a heartbeat fires regardless of whether there's work. A routine fires because it's time to do work.

## The Three Types of Agents

I now categorize every agent I create:

Type 1 — Task agents (most of them)
Wait for work to arrive. Heartbeat OFF. Examples: CEO agent, content writer, researcher.

Type 2 — Monitoring agents (rare)
Watch an external system with no webhook. Heartbeat ON, but interval set to hourly minimum.

Type 3 — Burst agents (rare)
Respond to unpredictable events. Usually still better as webhooks or comments, not heartbeats.

90%+ of Paperclip setups are 100% Type 1. Zero heartbeats needed.

## What a Healthy Setup Looks Like

After fixing this across my three companies:

- Most agents: heartbeat OFF, sitting quiet until work arrives
- A few routines: scheduled recurring work, each targeting one agent
- One or two monitoring agents: heartbeat ON but on a long interval, only if polling external systems
- Pause: reserved for actual problems, not volume control

The dashboard stops being noise. It becomes what it should be: a quiet status board that speaks up when something real is happening.

## The 60-Second Audit

Open your dashboard right now and count:

How many agents have heartbeat intervals under 15 minutes?

If it's more than 2 — and neither is polling an external system — each one is a leaky faucet. Turn them off.

The work still gets done. Your agents still run when needed. Your token bill drops.

You just stopped paying for alarm clocks that ring with nothing to do.

P.S. I'm currently rolling this out across all of my Paperclip companies - I'll report back with real numbers on what this actually saves in practice. This is the way forward.

If you've been running Paperclip with default settings, try this and see what drops. @dotta's advice saved me — might save you too.