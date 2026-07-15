---
source_url: https://x.com/nateherk/status/2071588017878249890
ingested: 2026-07-01
sha256: b159f981f4169c6b0673addde8d5c175630aa28bbcdf288233e1d54255ed289f
---
---
title: "Stanford's Method Turns Claude Into a PHD Level Research Team"
source: "x-bookmarks"
tweet_id: "2071588017878249890"
tweet_url: "https://x.com/nateherk/status/2071588017878249890"
author_name: "Nate Herk"
author_handle: "@nateherk"
tweet_date: "Mon Jun 29 13:34:06 +0000 2026"
bookmark_date: "2026-06-29"
content_type: "x_article"
character_count: 5635
retweet_count: 24
like_count: 174
---

# Stanford's Method Turns Claude Into a PHD Level Research Team

Stanford's Method Turns Claude Into a PHD Level Research Team

Stanford has a research method called STORM that peer-reviewed testing shows produces articles 25% more organized than the next best method.

I put those principles into my own Claude skill and I'm giving it away for free.

You point it at a topic. You get back a verified HTML briefing built by five different agents, each looking at the problem from a different angle.

## TL;DR

→ STORM runs your topic through five expert lenses instead of one prompt, so the blind spots one angle misses get caught by another

→ The five lenses: practitioner, academic, skeptic, economist, historian

→ Six more agents then verify every fact and mark each source confirmed, corrected, or demoted

→ You get one self-contained HTML report, with findings ranked by reliability

→ I tested it against Claude Code's built-in Deep Research, and a separate model picked STORM on all six quality measures

## Why One Prompt Isn't Enough

Send one prompt to Claude and you get one angle of research.

That leaves a pile of blind spots in the plan.

STORM fixes that with five perspectives, and each angle finds a hole the others miss.

→ The practitioner cares about what actually works

→ The academic wants the evidence

→ The skeptic pokes holes

→ The economist follows the money

→ The historian looks at what came before

Each agent role-plays its own background and area of expertise. When they all dig into the same topic, you get coverage no single prompt would catch.

## STORM vs Claude's Built-In Deep Research

Claude Code has a native Deep Research feature that launched with dynamic workflows.

You give it a topic, it spins up a dynamic workflow, and it kicks off hundreds of agents in the background. In my run it fired off 103 agents.

It didn't even hand me a report at first. I had to ask where it was, and it gave me a markdown file that was decent but thin. Two sources up top, a few unconfirmed ones at the bottom, and some open questions.

Then I dropped the exact same prompt into STORM.

It ran the five lenses, converged them, mapped where they disagreed, then ran six more agents to verify every fact. Out came a clean HTML report.

Here's what stood out.

I put both reports into Codex, a completely different model, and asked which was better. It picked the STORM briefing on all six measures: evidence quality, source diversity, thesis strength, actionability, risk control, and fit for video and content.

STORM ran faster and came in 100% cheaper. About 12 agents total versus over 100 for Deep Research. And Deep Research got hit by API rate limits, which is the risk when you spin up that many agents at once. With STORM it's always your five personas.

## Inside the Report

Every report comes back on the same template, so it looks consistent every time.

→ A 60-second summary up top

→ Key findings, each ranked by reliability

→ A reliability score per finding, like 9 out of 10, with which lenses supported it and which challenged it

→ Sources at the bottom marked confirmed, corrected, or demoted from the V2 verification pass

It even calls out the assumption the whole briefing rests on, plus the missing lens. In one run, all five lenses looked at the topic from the owner's chair, adoption, productivity, ROI. None sat in the seat of the customer or the frontline employee. So I told it to spin up that sixth lens and run a V3.

Deep Research gives you a brain dump of stats. STORM you can tailor. You can tell the skill what your business is and what your goals are, and it shapes the takeaways around what you'd actually do differently.

## How It Works and How to Get It

Under the hood it's four prompts chained together.

1️⃣ Spin up the five angles on your topic

2️⃣ Build the contradiction map, where the perspectives disagree and which evidence is strong or weak

3️⃣ Synthesize everything into one report

4️⃣ Adversarial peer review that verifies every citation against its primary source

I ran that chain manually, it worked, then I packaged the whole thing into a skill so I can hand it a topic and it does all four steps and returns the same HTML template every time.

A skill is just a master prompt. You say "run STORM research on X," it reads the whole thing and runs it. Hands-off once it's installed.

To install: drop the markdown file and the HTML template into your .claude folder. It works in Codex or other agents too, you just put the skill in that agent's folder instead.

When it runs, phase 0 scopes the topic and asks a question or two if you were vague. Then the five lenses run in parallel. You can click into any subagent and watch its prompt and its live web browsing.

One distinction worth knowing. These are subagents, not an agent team. Subagents all work for one main session and can't talk to each other. Agent teams can talk to each other and even debate to a consensus, but they cost more. Mine ran on Opus 4.8, though you can run them on Haiku or Sonnet if you want it cheaper.

## The Real Takeaway

Grab the skill and test it on a topic you already know well, so you can see where it's right and where it needs another lens. Maybe you add a beginner lens, or a content creator lens.

But the skill matters less than the idea behind it. The more perspectives you have researching and contradicting each other, the more holistic your research gets.

If you don't have the subject matter expertise, borrow it. Find the gaps in your own knowledge and build a council of agents that each kill a different blind spot.

I walk through the whole thing step by step in the full video. Link in the first reply.
