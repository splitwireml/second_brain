---
title: "How to Build Claude Subagents Better Than 99% of People"
source: "x-bookmarks"
tweet_id: "2064326627719311775"
tweet_url: "https://x.com/nateherk/status/2064326627719311775"
author_name: "Nate Herk"
author_handle: "@nateherk"
tweet_date: "Tue Jun 09 12:39:56 +0000 2026"
bookmark_date: "2026-06-09"
content_type: "x_article"
character_count: 9911
retweet_count: 24
like_count: 270
---

# How to Build Claude Subagents Better Than 99% of People

How to Build Claude Subagents Better Than 99% of People

One Smart Boss. A Team of Cheap Agents.

That's the mental model that makes Claude Code subagents click.

Your main chat is the boss. It talks to you, then quietly hands work to a team of agents that report back.

Most people either never touch subagents or use them backwards. Here's how to use them better than almost anyone.

## TL;DR

→ A subagent is just a markdown file with YAML front matter, the same thing as a skill, named differently

→ Each one runs in its own fresh context, so research and file-reading never pollute your main chat

→ Run a smart Opus "boss" that delegates to cheap Haiku "workers" and save real money

→ Make them read-only with tool restrictions so an agent literally cannot touch your data

→ Use one when you're about to dump a pile of stuff into your chat you'll never read again

→ Dynamic workflows spin up dozens at once, but they'll eat your session limit if you're careless

## What a Subagent Actually Is

I told Claude Code to spin up five subagents, each with a different persona, to review my book.

One was a complete beginner. Linda, 58, a retired elementary school teacher. One was a software engineer. One a COO at a 12,000-person company. One a publisher.

All five ran in parallel, in separate sessions, each with its own prompt. They came back with one combined review. I got about an 8, so I have some work to do.

The point is the structure. Your main session is the orchestrator. It's the one talking to you.

It can spin up as many subagents as you want, hand each one a job ("go read these files," "go research this," "go fix that bug"), and they only talk back to it. Different models, different personas, different skills, different subject matter expertise.

Then the main session takes their reports and relays it back to you.

## Why They're Worth It

The first reason is a clean context.

When you're chatting, building, or doing research in your main session, your context window fills up. You can watch it on the status line. Once it's polluted, quality drops.

Hand the heavy work to a subagent and it runs in a completely fresh chat. None of that noise hits your main window.

The second reason is money. Your main session might be on Opus, the most expensive model. But a subagent can do the same research on Haiku or Sonnet.

I had a researcher agent go look up a tool called Fireflies.ai. The main session stayed on Opus, the subagent did the web searching on a cheaper model, and only the summary came back.

The third reason is they're specialists. I've thought about AI this way since I started my channel. It's fun to have one mega-assistant that does everything, but the better play is each agent being really good at one thing.

Your main general agent is a jack of all trades because of skills. Subagents are the actual specialists.

→ One that's a security auditor

→ One that writes tests

→ One that writes docs

→ One that's an expert on database architecture and queries

You silo the work into an assembly line of agents that each do one thing extremely well.

And you can borrow that expertise. There's a GitHub repo called Awesome Claude Code Subagents with hundreds of pre-built agents: API designers, backend developers, GraphQL architects, TypeScript and SQL specialists.

Someone who knows CLI development better than you already packed their knowledge into a markdown file. You just drop it in.

One caveat. Because these are open source files, watch for prompt injections or anything malicious. You can even build a read-only verifier subagent whose only job is to scan a repo and confirm there's nothing nasty inside, with no ability to send data anywhere.

## It's Just a Markdown File

A custom subagent lives in your .claude/agents folder as a markdown file. It's the exact same tangible thing as a skill.md file, just called something else.

YAML front matter up top, instructions below

Take my clickup-searcher agent. Front matter has the name, the description, the model, and a color. Assign it a color and it shows up tinted when it runs, so you can see it working. I invoke it with plain natural language and it goes.

The front matter matters because of progressive disclosure. Claude Code reads only the name and description to decide if an agent fits your prompt. If it doesn't apply, Claude never loads the rest, so you don't waste tokens.

That's why the description is the most important line. It's the trigger.

Precise descriptions mean fewer misfires. A misfire is either an agent that should have fired and didn't, or one that fired when you didn't want it to.

You tune it by using it. When it doesn't fire and you think it should, you ask why, then update the description.

The docs list every lever you can pull in the front matter:

→ tools it can use

→ disallowed tools, so you can make it explicitly read-only

→ which MCP servers it's allowed to touch

→ skills it can invoke

Yes, subagents can invoke skills, and skills can invoke subagents. They work together, not against each other.

One more split to know: project-level vs global. Project agents live in the repo's .claude folder and ship with the repo. Global agents live at the user level, work across every project on your machine, and don't get shared when you push to GitHub. Since it's just a markdown file, moving one between the two is trivial.

## Building One Live

The /agents command does it for you. Pick personal, global, or project, then "generate with Claude" or configure manually.

I built a plan roaster. The prompt: criticize my work, play devil's advocate, find every hole, roast it. Trigger it when I say "roast my plan" or "review my plan."

Then it walks you through the rest:

1️⃣ Tools. I picked read-only. You can go deeper into MCP servers and individual tools like bash if you want.

2️⃣ Model. I picked Haiku, or you can inherit from the parent.

3️⃣ Color. Pink.

4️⃣ Memory. Project, none, user, or local. I default to project. Pick none if you want it to wake up completely blind.

When Claude generates the agent, the description comes out huge. Trim it. Progressive disclosure means a bloated description just wastes tokens.

Here's where it got real. I fed it a terrible plan: an ice cream stand on Oak Street Beach in Chicago, no refrigerator, selling tiny scoops for $20.

It didn't fire. My roast skill grabbed the job first, because that skill also spins up five subagents.

So I debugged it out loud. I asked Claude why the plan roaster didn't fire. Turned out I never closed the quotes in my front matter, which broke the YAML. Mechanical, not judgment.

Good tip: always close your quotes. Open one and forget it and you'll break the whole thing.

Once I was explicit ("use the plan roaster subagent, not the roast skill"), it kicked off. The prompt that went over: "roast this business plan hard." It tore into the missing refrigerator and the absurd $20 price.

The plan roaster burned 22.8K tokens doing it. None of those tokens polluted my main session. All I got back was the verdict.

That's the entire payoff in one number.

By the way, copy-pasting out of the terminal is horrible. Have it write to a text file, or use the desktop app.

## When to Use One, and When to Skip It

The core question: is this about to dump a pile of stuff into my chat I'll never read again?

If yes, delegate it. If no, keep it inline.

Reach for a subagent when:

→ You're about to read a lot of files

→ You'll spit out a wall of output

→ It's a job you keep repeating, so build a custom one

→ The work is independent and parallel, like reviewing 15 book chapters at once

→ You want an unbiased reviewer with no memory and no context to bias it

Skip it when:

→ It's a quick edit

→ The steps depend on each other, 1 then 2 then 3

→ The agents need to talk to each other, which is an agent team, not subagents

→ The agent needs the full conversation context or needs to ask you a question

Worth knowing: subagents are one-to-one with the main session, not one-to-many. Five running at once can't talk to each other. If they need to coordinate and share a task list, that's an agent team, which costs more.

And remember the permission mindset. If an AI can read or touch data, assume it will, even if you never prompt it to. Explicit tool and MCP restrictions are a real layer. "Please don't do that" in a prompt is not. There's a big difference.

You can also cap runaway agents with max turns, say 10, if one starts looping through research. I rarely need it, but the lever's there.

The money math is the cleanest example. A 300-page report where you just want three facts doesn't need Opus, probably not even Sonnet. Send it to a Haiku subagent, get the summary back. Smart boss, cheap workers, faster and cheaper.

## Dynamic Workflows, The Careful One

This one spins up a workflow that delegates to a ton of subagents in parallel. Same idea, main chat orchestrates, but now it's three to forty agents at once.

I've seen it launch 41 at the same time. In testing I once triggered 210 at once. It worked, but it ate through my session limit like crazy.

The trigger word changed too. It used to be "workflow," now it's "ultracode," so Claude won't accidentally kick off a giant fan-out when you're clearly talking about something else.

Powerful, but expensive. Be deliberate about when you fire one.

## Wrap

Subagents aren't magic. They're markdown files, clean context, the right model for the job, and a boss that knows what to hand off.

Don't force them. One quick thing doesn't need one. Too many and your results get worse.

But when you've got a pile you'll never reread, an independent parallel job, or a report you want a fresh set of eyes on, spin one off. Works the same in the terminal, the desktop app, VS Code, or the web.

I walk through every piece of this step by step in the full video. Link in the first reply.
