---
title: "Forget About Memory: I Built a Context OS for My Hermes Agent"
source: "x-bookmarks"
tweet_id: "2050793548430147982"
tweet_url: "https://x.com/tonysimons_/status/2050793548430147982"
author_name: "Tony Simons"
author_handle: "@tonysimons_"
tweet_date: "Sun May 03 04:24:18 +0000 2026"
bookmark_date: "2026-05-03"
content_type: "x_article"
character_count: 18155
retweet_count: 4
like_count: 37
external_urls:
  - "https://github.com/asimons81/hermes-vault"
---

# Forget About Memory: I Built a Context OS for My Hermes Agent

Forget About Memory: I Built a Context OS for My Hermes Agent

Most AI memory is a sticky note.

You paste a few facts into a system prompt. The model remembers that you prefer bullet points and that your cat is named Mittens. This is the state of the art for 95% of AI users, and it's embarrassing.

I didn't set out to build a memory stack. I set out to stop repeating myself. What I ended up with is something closer to a local context operating system, a layered infrastructure of identity, facts, procedures, session history, compression, and scheduled routines that my @NousResearch Hermes Agent reads, writes, and navigates like a file system of thought.

Earlier tonight, I asked Hermes to audit its own memory. Not a friendly summary. Not vibes. A real audit. I told it: no guesses, no assumptions, only local files, configs, databases, command output, code paths, and evidence.

The first answer was too vague, which is exactly what you get when your agent is being polite instead of thorough. I pushed harder. "Do not generalize. Show me the files. Show me the byte counts. Show me what is active, what is dormant, and what is broken."

The result was a 47-point structured breakdown of every memory surface in my setup. And sitting there reading it, I realized something uncomfortable: I had built something significantly more intense than I thought I had.

This isn't a brag post. This is the autopsy of a system I built accidentally, layer by layer, because the default "AI memory" story is a joke.

## The Setup: What Is Actually Running

Here's what's actually running under the hood.

The core Hermes install lives at ~/.hermes/hermes-agent, currently on version 2026.4.30, commit b19025ad1, Python 3.11.15. It's pinned to a feature branch called feature/pet-overlay-autostart because I ship things and then forget to merge them, which is a separate problem.

Inside that install, the memory architecture isn't one thing. It's at least eleven distinct layers, each with a specific job, and each with a specific failure mode when you use the wrong one for the wrong purpose.

## Layer 1: SOUL.md, The Identity File

At ~/.hermes/SOUL.md sits the operating instructions for Hermes itself. This isn't memory in the "Tony likes short posts" sense. This is the agent's personality document, role definition, delegation rules, quality standards, and tone guidelines.

It's around 15KB of markdown that says: be direct, be opinionated, be high-agency, delegate aggressively, verify claims before trusting them, push back when I am being vague, and don't write like a LinkedIn influencer.

Without this file, Hermes would still work, but it would sound like a generic corporate AI assistant. With it, the agent has a persistent operating identity that doesn't degrade over long sessions. This is memory at the identity layer, and it's the one file in the entire stack that I would never delete.

## Layer 2: MEMORY.md and USER.md, Always-On Context

These are the two files everyone thinks of when they say "AI memory." They live at ~/.hermes/memories/ and are injected into every single turn.

MEMORY.md is my notebook. Currently 2,819 characters, running at about 80% of its 3,500-character limit. It stores environment facts, tool quirks, project conventions, and durable lessons like "Hermes cron expressions are interpreted in America/Chicago, not UTC, always verify with hermes_time.now()." If it hits its cap, older entries get compacted or evicted.

USER.md is the user profile. 1,652 characters at 65% of its 2,500-character limit. It knows my pets (Carl the Jack Tzu, Ruby the Great Dane, Willow the cat), my X strategy (80/20 niche/shitpost), my preference for Google Docs as a review surface, and that I want tightly bounded execution with explicit approval before persistent Drive changes.

The key design decision here is that these files are small on purpose. They aren't the entire brain. They are the warm cache. The always-on layer has to fit in a few thousand characters because it rides along in every prompt, and prompt real estate is expensive. If you try to make this layer too big, you are doing it wrong.

## Layer 3: Holographic Memory (fact_store), Structured Facts

This is where things start getting interesting.

At ~/.hermes/memory_store.db sits a SQLite-backed structured memory system called "holographic memory." It stores individual facts, not paragraphs, not preferences, but discrete claims, with entity resolution, trust scoring, and compositional querying.

Right now it holds 139 facts across 107 entities. These are things like "Tony prefers Codex over Claude" and "project [hermes-vault](https://github.com/asimons81/hermes-vault) uses MCP protocol", small, queryable atoms rather than narrative text.

The holographic part refers to HRR-style (holographic reduced representation) compositional reasoning: you can query across entities to find facts that connect multiple things at once. In theory, this lets you ask "what do Tony and the hermes-vault project both relate to?" and get back meaningful overlaps.

In practice? It's currently degraded. The HRR reasoning path requires Numpy, and Numpy isn't installed in this environment. So the compositional query layer is running in a degraded relational-fallback mode. The trust scores, which are designed to surface reliable facts and bury stale ones, are all sitting at the default 0.5 because I have never trained them.

This is the honest version of "structured memory." The architecture is there. The data is there. The training and optimization aren't. It works, but it's running at maybe 40% of its design potential.

## Layer 4: Session Database and session_search, The Archive

This is the big one.

At ~/.hermes/state.db sits a session database tracking every conversation I have ever had with Hermes. The numbers are:

- 1,047 sessions

- 48,422 messages

- Sources: cron jobs, Telegram DMs, CLI sessions, TUI sessions

Behind that, the raw receipts live at ~/.hermes/transcripts/, 1,858 JSONL files totaling approximately 475 MB of raw conversation data. Every message, every tool call, every correction, every "please stop writing like a documentation page" moment is in there.

The session database doesn't stuff all of this into the prompt. That would be insane. Instead, it's searchable through session_search, I can ask Hermes "what did we do about the Kiln promo pipeline three weeks ago?" and it queries the archive, finds the relevant sessions, and returns a summary.

This is the distinction that most people miss. Storing 48,000 messages isn't the flex. The flex is knowing which parts are active, searchable, stale, or deliberately kept out of the prompt. Dumping everything into context is amateur hour. Searching the right thing at the right time is the actual superpower.

## Layer 5: LCM, Context Compression

Long Context Management. LCM isn't memory in the "Tony likes punchy posts" sense. It's survival gear.

At ~/.hermes/lcm.db, the LCM engine stores 6,622 messages across 16 summary nodes. When a session runs long, and mine run long, LCM compresses older turns into summaries, preserving the semantic content while reclaiming context window space. It lets the agent operate across extended sessions without degrading into repetition or amnesia.

The summaries are hierarchical. You can expand them to recover original detail when needed. The system also externalizes large payloads (big tool outputs, long file reads) to keep the main context lean.

This is compression, not memory. It's about surviving the current conversation, not remembering something for next week. Confusing LCM for long-term memory is like confusing your working memory for your notes app. Different systems, different jobs.

## Layer 6: Skills, Procedural Memory

Skills are where "what I know about Tony" becomes "how I execute Tony's workflows" for my Hermes Agent.

My setup has 250+ skills installed. Each one is a markdown file with YAML frontmatter, a self-contained operating procedure for a specific task. They cover everything from Google Workspace doc publishing to X/Twitter operations to ML training workflows to smart home light control.

When a task matches a skill, Hermes loads it and follows the instructions. This is procedural memory: not "Tony's favorite color" but "here is exactly how to create a Google Doc, populate it with formatted content, and route it to the correct Drive folder."

Skills are what turn Hermes from a chatty assistant into an operator. Without them, the agent can talk about tasks. With them, it can execute them. The difference is the difference between asking a coworker for advice and handing them your SOP binder.

## Layer 7: Project-Local Context Files

When Hermes enters a project directory, it picks up context files automatically:

- AGENTS.md, project-level agent behavior rules

- .hermes.md, Hermes-specific project configuration

- CLAUDE.md / .cursorrules, broader agent conventions

- SOUL.md, workspace-level identity overrides

These files inject project-specific memory without polluting the global memory files. When I am working in hermes-vault, Hermes knows about the MCP protocol, the open-source agent auth vision, and the preference for iterating on existing code over fresh starts. When I am in kiln, it knows about creative pipelines, Remotion rendering, and my preference for design-director passes over renderer feature passes.

Project context is the memory equivalent of walking into a workshop and having all your tools laid out exactly where you left them. No global memory required.

## Layer 8: Nexus, The Second Brain

Nexus lives at ~/nexus/ and clocks in at about 11 MB. It contains wikis, raw notes, journals, plans, briefings, and content pipeline material.

This is my local knowledge base. Not AI memory, human memory, structured and searchable. Hermes accesses it as a reference surface: when I ask about something that lives in Nexus, it reads the relevant files and incorporates that context.

Nexus isn't automatically injected into every prompt. That would be absurd, 11 MB of raw text would annihilate any context window. Instead, it's accessed by workflows. A skill loads the Nexus wiki. A cron job pulls from the briefing folder. A research task queries the raw notes.

Think of Nexus as the library, MEMORY.md as the notebook, session_search as the archive, and skills as the operating procedures. Different retrieval patterns for different purposes.

## Layer 9: Self-Improving Files, Manual After-Action Learning

The ~/self-improving/ directory stores lessons learned from corrections, failures, and successful patterns. It has a tiered structure:

- memory.md, hot tier, always loaded, capped at 100 lines

- projects/ and domains/, warm tier, loaded on context match

- archive/, cold tier, decayed patterns

The file heartbeat-state.md exists but has never been used. This is the part where I admit that not every surface in the memory architecture is fully wired. Some pieces are aspirational scaffolding, designed, created, and then left sitting because the manual writes never happened.

Self-improving files are write-only from the agent's perspective. It can append lessons, but I haven't wired automatic promotion/demotion or scheduled cleanup. The architecture supports it; the execution hasn't been prioritized.

## Layer 10: Cron Jobs, Scheduled Context Loops

Eight active cron jobs run on schedules. They aren't memory storage, they are routines that create and consume context.

A daily planning job fires at 6:45 AM CT and generates a structured brief. A Git hygiene job auto-commits dirty repos nightly. A content radar job turns news into content ideas. Each one reads from memory (preferences, project state, Nexus) and writes back (new context, new artifacts, new session entries).

Cron jobs are the circulatory system. They keep context flowing without me having to manually kick off every process. They aren't the brain, but without them, the brain sits in a jar.

## Layer 11: Hooks, Plugins, and MCP, Expansion Surfaces

The memory architecture isn't sealed. Hooks can trigger on events (session start, tool call, output generation). Plugins can inject new tools and new memory surfaces. MCP (Model Context Protocol) servers can expose external context sources, databases, APIs, knowledge bases, as queryable memory endpoints.

These surfaces are expansion ports. They mean the memory architecture can grow sideways without breaking the existing layers. If I want Hermes to remember things from a Notion workspace, I don't need to rewrite the memory system, I just point an MCP server at it.

## The Distinctions That Actually Matter

Here is the part where most "AI memory" content falls apart. People talk about "memory" like it's one feature with an on/off switch. It isn't. It's a stack of distinct systems, and using the wrong layer for the wrong job is worse than having no memory at all.

- MEMORY.md isn't the whole brain. It's the warm cache. Small, fast, always-on.

- Session search isn't the same thing as memory. It's a searchable archive of past conversations. Retrieval, not recall.

- Skills aren't facts; they are procedures. "Tony uses pytest" is a fact. "Run pytest with these exact flags in this exact order" is a skill.

- Nexus isn't automatically injected. It's a reference surface, accessed by workflows, not dumped into every prompt.

- LCM isn't long-term memory. It's context compression, survival gear for the current session, not continuity across sessions.

- Cron jobs aren't memory storage. They are scheduled routines that read context, execute workflows, and write results.

- More memory isn't automatically better. Bad memory, stale facts, wrong preferences, outdated procedures, makes an agent worse, not better.

Remembering everything is a terrible design. The actual superpower is knowing what to remember, where to put it, when to load it, and when to let it decay.

## What This Actually Gets Me

So I have 11 layers of memory infrastructure. So what? Here is what it means in practice.

I repeat myself less. Hermes knows my environment, my projects, my workflows, my preferences, and my recurring patterns. I don't have to explain that "cron expressions are in Chicago time" every time I schedule something, because it's in MEMORY.md. I don't have to remind it that I prefer MiniMax over OpenRouter for delegation work, because it's in USER.md and fact_store.

It can search old sessions instead of stuffing everything into the prompt. When I ask "what was that bug we hit with the ComfyUI pipeline last month?" it queries session_search, finds the relevant transcripts, and returns a summary. No prompt bloat required.

It can load procedures through skills. When I say "publish this as a Google Doc in the articles folder," it doesn't guess. It loads the Google Workspace skill and follows the documented pipeline: create, format, route, verify, return link.

It can use project rules when inside a repo. When I am working in hermes-vault, it knows about the MCP architecture. When I am in Kiln, it knows about the creative pipeline. Context switches are automatic.

It can run scheduled routines. The daily planning job fires without me thinking about it. The Git hygiene job catches things I forget. The content radar surfaces ideas I would have missed.

It can build continuity across work without becoming one giant prompt blob. Each layer handles its slice of the problem, and Hermes navigates between them based on the task. This isn't a single memory system. This is a memory operating system.

## The Honest Caveats

I am not going to sit here and tell you this setup is perfect. It isn't.

The truth is:

- Holographic trust scoring is untrained. Every fact sits at 0.5. The system has no signal about which facts are reliable and which are noise.

- HRR compositional reasoning is degraded because Numpy is missing. The most interesting query capability, reasoning across multiple entities simultaneously, is running in a relational fallback mode that's functional but not what the architecture was designed for.

- Some self-improving files are manual-write only. The heartbeat system has scaffolding but no signal. heartbeat-state.md exists and has never been used.

- More memory isn't automatically better, and I have memory surfaces with stale data. The raw transcripts archive at 475 MB is a receipts drawer, not an indexed library. Most of it will never be queried.

- The boundary between "what Hermes knows" and "what Hermes can find" is fuzzy. Sometimes the right answer is in a fact_store entry. Sometimes it's buried in a three-week-old session transcript. Sometimes it's in Nexus but the retrieval path wasn't triggered.

This is the difference between architecture and optimization. The architecture is solid. The optimization, training trust scores, installing Numpy, wiring the heartbeat, pruning stale data, is the boring work I haven't done yet.

## Why Any of This Matters

The AI industry is currently obsessed with "memory" as a product feature. Every AI startup has a slide that says "persistent memory" like it's a solved problem. It isn't.

Memory isn't a feature. Memory is infrastructure.

If you treat it as a feature, a checkbox, a single toggle, a "we remember your conversations" banner, you get a sticky note. You paste some facts into a prompt and call it a day. That works until you have more than 20 things to remember, at which point your context window is eating itself and your agent is dumber than when you started.

If you treat memory as infrastructure, a layered stack of identity, facts, procedures, archives, compression, scheduling, and expansion surfaces, you get something that grows with you. Each layer handles its slice. The agent navigates between them. Context flows through the system instead of pooling in one giant prompt.

The difference is the difference between "I know what you like" and "I know how you work."

One is a sticky note. The other is a context operating system.

This article was co-written by my Hermes Agent. I just call him Hermes. Or Herm-Dog. Or Herman Munster. Or... You get the picture.
