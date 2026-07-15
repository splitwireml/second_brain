---
source_url: https://x.com/nateherk/status/2051838770912129464
ingested: 2026-05-17
sha256: 0e769ea4255daf514e521a29168696cac05011fc72342443c2306072c0d0424f
---

# X Article: Master 97% of Codex in 1 Hour

**Author:** @nateherk (Nate Herk)
**Date:** 2026-05-06
**URL:** https://x.com/nateherk/status/2051838770912129464
**Tweet ID:** 2051838770912129464
**Likes:** 323 | **Retweets:** 35 | **Replies:** 8

## Raw Content

Master 97% of Codex in 1 Hour

Codex is an absolute beast. And most people are barely scratching the surface.

In one session I went from a blank project to a deployed YouTube comment intelligence system, complete with a reusable skill, a live dashboard, and a weekly automation that runs while I sleep.

Here's the entire flow, no skipped steps.

## TL;DR

→ Codex works inside a folder. Same as Claude Code. Different harness, different model.

→ Plan mode + agents.md + .env is the foundation. Get those right and the rest gets easier.

→ Skills turn one-off chats into reusable recipes. Global or project-level, your call.

→ GitHub + Vercel deploy any localhost dashboard to a live URL with one connect.

→ Weekly automations work, but the model picker defaults to GPT-5.2. Change it.

→ Browser use inside Codex is the cleanest QA loop I've used.

## The Codex Mental Model

If you've used ChatGPT on the web, the interface is going to feel familiar.

Projects on the left. Chats on the left. Talk to ChatGPT in the middle. The toggle at the bottom switches model (GPT-5.5, 5.4, etc.), speed, and intelligence (low, medium, high, extra high).

That's the surface. Underneath, it's a different beast.

Codex can do everything chat can do. Plus it reads your local files, builds Excel sheets, writes apps, controls your mouse and keyboard, and automates browsers. ChatGPT on the web can do none of that.

The closest comparison is Claude Code, which I still use every day. Same idea, different harness.

→ Claude Code uses Opus, Sonnet, Haiku

→ Codex uses ChatGPT models (5.5, 5.4, etc.)

→ Both work inside the same folder structure

→ Both speak markdown configuration files

I find Claude better for exploratory thinking and brainstorming. I find Codex more pragmatic, more execution-heavy, and stronger at staying on a long plan. Different strengths. Use both.

I did a full breakdown comparing and testing the two, check that out here: https://x.com/nateherk/status/2047436441664262323?s=20

The mindset shift: stop asking "which tool is the best?" Start asking "which tool is right for this specific job?"

## Setting Up Your First Project

A project in Codex is just a folder on your computer. That's the whole secret.

When you create a new project, Codex opens a file picker. Choose where the folder lives. Done. Now any file inside that folder, Codex can read, write, edit, organize, or move.

The first thing every project needs is an `agents.md` file.

If you're coming from Claude Code, this is the equivalent of `claude.md`. Same idea, different name. It's the onboarding doc Codex reads every time you open a new chat. It tells the agent who you are, what the project is, and what the goal looks like.

Don't write it yourself the first time. Just talk to Codex.

Tell it the project goal in plain English. Tell it to draft an agents.md. It creates the file in the project root with sections for context, project goal, product direction, and key constraints. You read it. You edit it. Done.

The next thing to know is plan mode.

Plan mode means Codex won't execute anything. It just brainstorms, asks questions, and produces a plan. I start every meaningful build in plan mode. Once the plan is solid, I submit and let it execute.

Skipping plan mode is the single biggest reason builds go sideways.

## Connecting to Anything

Codex has plugins for the obvious tools. Slack, Drive, GitHub, Vercel, Figma, Canva, Higgsfield, Hugging Face, Notion, Teams, SharePoint, and more.

But not everything has a plugin. YouTube, for example, doesn't.

When that happens, you don't go hunting. You ask Codex.

In plan mode I told it the goal: pull recent comments from my YouTube channel. It came back with three options. API key, OAuth, or both. I chose API key. It came back with a step-by-step plan to set up Google Cloud, enable the YouTube Data API v3, and create a key.

A few minutes later I had a working API key in `.env.local`.

The dot in front of `env` matters. That's how Codex knows to exclude this file from public commits when you push to GitHub. Always paste keys there. Never into a random `secrets.txt`.

Once the key was in, I had Codex test the connection. It tried PowerShell first (failed on a TLS issue), then Node, then Python (both worked). I asked it to save that learning into project memory so it never tries the broken path again.

That's the loop you want. Try, fail, save the lesson, never fail the same way twice.

## Building a Real Deliverable

The point of any tool is the deliverable.

Mine was a YouTube comment intelligence Excel sheet. I asked Codex to pull 200 of my most recent comments across recent videos, analyze them, and put it all in a workbook with charts and creator-focused insights.

Plan mode again. Codex asked clarifying questions. How many comments? Which videos? How should it classify them?

I went with its recommendations.

A few minutes later I had a workbook with:

→ Content category mix (general feedback, questions, tool comparisons, etc.)

→ Tool mention rankings (Claude Code, Codex, API, etc.)

→ Question rate, content-requested rate, high-priority items

→ Frequent question patterns

→ Reply opportunities ranked by priority

→ Content idea suggestions pulled from the comments

→ A raw tab with all 200+ comments

The first version was OK. Not great. My prompt was vague.

That's the lesson. Vague prompts produce generic insights. The more specific you are about which patterns matter to you, the more useful the workbook becomes.

## Turning Workflows Into Skills

Here's where it got interesting.

That comment workbook took 20 minutes the first time. It would take 20 minutes every time, unless I turned it into a skill.

A skill is a reusable recipe.

Think of it like making chocolate chip pancakes. The first time, you pull up a recipe and follow it to a T. Measurements, temperature, timing. The next time, you grab the same recipe. The pancakes come out the same. If you tweak something and like it, you update the recipe. The skill gets sharper every time you use it.

Skills in Codex are markdown files. That's it.

After the workbook was built, I told Codex to turn the flow into a skill. It reverse-engineered everything I had just done into a fresh file inside the `.codex` folder.

Two storage levels:

→ Global: stored in the user-level `.codex` folder. Available in every project.

→ Project-level: stored inside the project itself. Only available there.

Switching between them is one sentence. "Move that skill to the project level." Done.

To call a skill, you have two options. Slash command (`/youtube-comment-insights`) or natural language ("pull recent comments and run the insights workflow"). Both work.

## From Localhost to Live URL

The Excel sheet was the backend. Now I needed a frontend.

I asked Codex to build a dashboard that visualizes the data, served on localhost, with charts, AI insights, a comment explorer, and a clean UI. I told it to use GPT Image 2 to mock up concepts before writing any code.

This is one of my favorite Codex patterns.

GPT Image 2 generates concept art, logos, and UI references that get saved as project assets. The dashboard build then references those assets. It produces a much sharper-looking output than letting the model freestyle the design.

Before Codex returned the dashboard, it ran a built-in browser verification loop. Two visual passes. It found three issues on its own, fixed them, and ran another pass before handing it back.

The dashboard worked. Localhost only.

Localhost lives on your machine. Nobody else can hit that URL.

To take it live I used two more tools. GitHub and Vercel.

1️⃣ Connect Codex to GitHub (one CLI auth step)

2️⃣ Tell Codex to create a private repo and push the dashboard codebase

3️⃣ Connect Vercel to the same GitHub account

4️⃣ Import the repo into Vercel

5️⃣ Click deploy

Thirty seconds later I had a live URL.

The killer detail: GitHub and Vercel talk to each other. Every push to the repo triggers an automatic Vercel deploy. So I never have to log in to Vercel again. I work in Codex. Codex pushes to GitHub. Vercel updates the live site.

Three tools. One workflow.

## Weekly Automations (and the gotcha)

Codex has an Automations tab. Scheduled chats that run on a cron.

I set one up to run every Sunday at 5pm. The prompt: pull fresh comments, update the Excel sheet, refresh the dashboard data, push to GitHub, let Vercel auto-deploy.

That's a real "while I sleep" workflow.

But here's the thing.

The first run took 40 minutes when it should have taken 7. Two reasons.

→ I had the Excel file open on my desktop. Codex couldn't overwrite it.

→ The automation defaulted to GPT-5.2, which is way slower than 5.5.

The model picker inside the automation panel does NOT inherit from your active chat. You have to set it explicitly per automation. I switched mine to 5.5 high. Re-ran. Done in 7 minutes.

If you build an automation and it feels slow, check that model setting first.

The other thing to know about local automations: they only run when your machine is on. Close Codex or shut down your laptop, the cron pauses. For 24/7 you need a cloud setup. Claude Code recently shipped cloud routines for exactly this. Codex doesn't have a native equivalent yet, so for now keep your machine on or move the workflow to a VPS.

## Browser Use as a QA Loop

Codex has built-in browser use that's smoother than anything I've used elsewhere.

I told it to open the dashboard in the in-app browser, click around, try to break it, and report back. It did.

Six issues found:

→ External YouTube links not opening in a new tab

→ Empty explorer state too bare

→ Search too literal, no fuzzy matching

→ Active tab state mostly visual, not accessible

→ Two minor UI inconsistencies

Watching the cursor move around the dashboard live in the in-app browser is wild. It catches things I missed. It surfaces UX problems I never would have caught from the code alone.

The pattern that unlocks this: bake the QA pass into your skill or your project memory. Every time you ship a new dashboard or feature, the agent runs a browser pass before it returns to you. You stop being the QA tester. The agent does it.

Browser use isn't just for QA either. Use it for:

→ Logging into tools that don't have an API

→ Pulling reports from dashboards that don't expose data

→ Automating clicks through any UI you can describe in natural language

## Quality-of-Life Details Worth Knowing

A handful of things that make Codex feel less like a tool and more like a workspace.

→ The pet. A tiny animated character in the bottom corner. Pick from Codex, Dewey, Sadie, BSOD, Stacky, or Fireball. While Codex works, the pet shows progress. Hover for the current task. Switch tabs and a notification dot appears when something needs attention.

→ Side chat. Open a side chat off your main conversation. Same project context, different thread. Ask a quick question without polluting the main session. Close it when you're done.

→ Personality. Friendly or Pragmatic. I run Pragmatic by default. Concise, task-focused, direct. No filler.

→ The slash menu. `/personality`, `/pets`, `/skills`, `/browseruse`, `/pdf`, `/skillcreator`, and more. Type a slash and browse what's available.

→ The `@` mention. Tag a specific file or plugin in your prompt. Way cleaner than pasting a path.

→ The session bar. Bottom of the chat shows context window usage. Settings shows session limits remaining (5-hour and weekly). Codex auto-compacts the context just like Claude Code, so you rarely have to manage it manually.

→ Full access mode. Settings → General → Full access. Skips approval prompts. Faster, riskier. Start on default. Switch to full once you trust the project.

## Wrap

Codex is not magic.

The first time you build something, it'll hit issues. The first automation will run slow. The first skill won't be perfect. That's normal.

Treat every failure as golden knowledge. When something breaks, ask Codex to save the lesson into project memory. Next time, it knows. The system gets smarter every time you use it.

You're teaching a kid to ride a bike. You don't take your hand off the handlebars on day one.

In one hour I went from blank project to a working AI workflow that pulls fresh data from YouTube, analyzes 200+ comments, visualizes them on a live dashboard, refreshes itself every Sunday, and QAs itself with browser use before shipping.

All from inside a folder on my computer.

That folder is portable. Open it in Codex, Claude Code, OpenClaude, Cursor, or anything else that speaks markdown. The harness changes. The work doesn't.

Master that pattern and you've mastered 97% of what these tools are for.

I walk through the entire build step by step in the full video. Link in the first reply.
