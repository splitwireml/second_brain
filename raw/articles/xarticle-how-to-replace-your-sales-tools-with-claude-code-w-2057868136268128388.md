---
source_url: https://x.com/MichLieben/status/2057868136268128388
ingested: 2026-06-11
sha256: 66831eebbf87fe15c5f1aa38b08da595880520ffc522d1d908d45fe53521ad6d
---
---
title: "How to Replace Your Sales Tools With Claude Code (Without the Hype)"
source: "x-bookmarks"
tweet_id: "2057868136268128388"
tweet_url: "https://x.com/MichLieben/status/2057868136268128388"
author_name: "Michel Lieben"
author_handle: "@MichLieben"
tweet_date: "Fri May 22 16:56:11 +0000 2026"
bookmark_date: "2026-05-22"
content_type: "x_article"
character_count: 15019
retweet_count: 3
like_count: 42
external_urls:
  - "http://coldiq.com/)"
---

# How to Replace Your Sales Tools With Claude Code (Without the Hype)

How to Replace Your Sales Tools With Claude Code (Without the Hype)

Run outbound for a living and your tool stack quietly becomes a tax.

A scraper for LinkedIn engagement. A data provider for contacts. An enrichment tool for emails, plus a waterfall for the ones the first one misses. Clay sitting in the middle to glue it all together. A sequencer at the end to actually send. That is six logins, six invoices, and six separate places your targeting context lives, none of them aware the others exist.

Every campaign becomes the same ritual. 

Export from one tool, paste into the next, rebuild the formula you built last month, copy the output, paste it somewhere else. Call that a system if you want. It is really a relay race between SaaS products, and you are the baton.

Claude Code changes the shape of that problem instead of adding another lane to it. It runs in your terminal, it reads folders of context that you own, and you hand it the API keys for the platforms you already pay for. From there it stops being a tool and becomes the operator. It writes the integration code itself, tests that code against the live API, and saves the version that works so the next campaign skips the setup and goes straight to the result.

We run outbound for more than 400 B2B companies at ColdIQ. Over the last few months our GTM team has been moving its internal tooling into Claude Code, and the part that surprised us is how little of the old stack survives the move.

What follows is the three-agent setup our team runs now, with the steps to build each one. Ad campaigns, warm engagement, and full campaign buildouts. It also covers where the setup falls short, because most write-ups conveniently leave that part out.

---

# An agent is just a folder

The word "agent" makes this sound more exotic than it is.

In our setup, an agent is a folder. Open one of ours and you find a markdown file that works as the brain, the instructions the agent reads before it does anything. Next to it sit the API keys for the tools that workflow touches, templates of the output you want produced, a scoring criteria file, a set of copy frameworks, and a collection of skills.

Zoom out and the whole system is folders inside folders. We keep one for campaign tooling, one for the social engagement work, one for client delivery, and the architect sitting above them all. The architect holds the frameworks for building skills, organizing folders, and writing the code every other agent depends on. The terminal is only a window into these folders.

The skills are the part that matters. 

A skill is a saved script of code that already works. The first time you ask Claude Code to create a LinkedIn campaign through the API, it does not get it right on the first try. It writes a call, hits an error, reads the error, rewrites the call, and retries until the campaign actually appears in the ad manager. The moment it succeeds, you checkpoint it, and that working code is saved as a skill. The next run skips the trial and error and goes straight to the proven script.

> Before Claude Code, you hired a programmer to run that loop. Now the loop is the programmer. You just keep the parts that work.

The most expensive mistake we made early was skipping the architect. We built agents first, found the structure underneath them was wrong, and rebuilt every folder and skill from scratch. Build the architect first. The agents come easy after that.

---

## Agent 1: building ad campaigns from a spreadsheet

LinkedIn's campaign manager is a good place to lose an afternoon. Anyone running real ad spend across LinkedIn, Meta, and Google knows the interface fights back the second you try to move in volume. Updating bids, swapping account lists, launching variants. The UI was never built for an operator working fast.

So the first agent we built creates the campaign from a spreadsheet. 
One row per campaign, with a handful of columns: campaign group, campaign name, targeting type, ad copy, and a Drive folder reference for the creative. Targeting is either bottom-of-funnel against your own audiences or an ABM account list you built through outbound and filtered to specific job titles. You fill in the rows and run the agent. Claude Code reads the sheet, pulls the right creative from Google Drive by its reference, and hands back a plain summary of what it is about to build. You confirm, and the campaign is live in the ad manager seconds later, audiences and ads attached.

How to build it:

1. Drop your LinkedIn, Meta, and Google Ads API keys into the agent folder. Meta and Google also expose MCP servers, which connect faster than wiring the raw API yourself.

2. In plan mode, have Claude Code work out the API calls. It will run live tests, hit errors, read them, and retry until a campaign genuinely creates in the ad manager.

3. Checkpoint each working call as its own skill: create a campaign, attach an audience, upload a creative. Each call only has to be solved once.

4. Build the campaign spreadsheet and point the agent at it. From there, a new campaign is just a new row.

For a recent webinar we needed two campaigns live at once, one bottom-of-funnel and one against an ABM list. That was two rows and a single run, both live with their audiences and creative attached in under a minute.

Campaign creation is only the start of it. The same agent handles the bulk edits the native UI makes painful. When bids need to drop across every live campaign at once, that is one instruction instead of an afternoon of clicking. 

Point it at a base design and it will draft ad copy and run creative iterations through a generative image model, though our copywriters and designers still sign off before anything ships.

---

## Agent 2: turning post engagement into pipeline

Every like, comment, and share on your LinkedIn content is a person quietly raising their hand. They saw a post about a topic you sell into, and they engaged. That is an intent signal sitting in plain sight, and most teams let it evaporate, because catching it used to mean paying for scraping tools and moving the output into a CRM by hand.

The second agent removes that work. You hand it a LinkedIn post URL, it scrapes everyone who engaged, and the qualified ones land in your sequencer.

How to build it:

1. Give the agent a skill that takes a post URL and scrapes everyone who engaged through a scraping API.

2. Pipe that list into a Clay table where the enrichment runs. For each person: identify who they are, check them against your CRM, run them past partner lists and blocklists, and score them against your ICP.

3. Add a routing step. Qualified leads get pushed to Instantly, and the rest drop into a Slack channel for an SDR to work by hand.

4. Once it runs clean, have Claude Code wrap it in a simple UI and put it on a weekly schedule.

That one agent replaced more than $300 a month of scraping subscriptions.

The scraping tools we used to rent, against the plan that now does the same job.

Step four is the one most people skip, and it matters more than it sounds.

Most of a GTM team will never want to live in a command line, and the UI is what gets the workflow actually used. Ours runs every week, not just against our own posts but against competitor profiles and topic keywords like "ABM" or "go to market," so fresh engagers flow into outbound without anyone opening the terminal.

There is a second move hiding here. Take that same engaged audience, upload it to LinkedIn as a matched audience, and run your organic posts to them as ads. You are advertising to people already interacting with your topic. Warm gets warmer.

---

## Why warm beats cold

The reason this agent earns its place is in the numbers. 

A cold list of 1,000 contacts, blasted the usual way, returns about 20 replies, 5 calls, and 1 deal. The same 1,000 contacts pulled from real engagement returns 30 to 50 qualified leads, 10 or more calls, and around 3 deals. Same volume, different inputs.

Calls and deals from the same 1,000 emails. Signal-based targeting triples the deals closed.

> The post engagers this agent collects already showed you something. Their behavior pointed at the problem you solve before you ever reached out, which is why a warm motion you can run every week beats a cold one you run once a quarter.

---

## Agent 3: a full campaign, built end to end

The third agent replaces the most tools at once, and it runs on plain language. No filters, no formulas.

To set it up, the folder needs the API keys for a data provider, an email enricher, and your sequencer, plus two reference files. One is a scoring criteria file that defines a tier 1 account by industry, headcount, funding, revenue signals, and tech stack. The other is a copy framework file holding the email structures you already know convert. Those two files are where your judgment lives, and the agent leans on them on every run.

After that it is a conversation. You drop a CSV of companies into the folder and work through it one instruction at a time:

1. "Tier this company list using my scoring criteria." The agent reads the list and the scoring file, writes Python to score every row, and splits it into tier 1, tier 2, and tier 3. You get a short summary of the top accounts and the ones it disqualified, so you can sanity-check the logic before spending a credit.

2. "Find the sales leaders at tier 1 and tier 2 companies." It calls Apollo, pulls 153 matching contacts, and saves them to a CSV.

3. "Get the work emails of the contacts that don't have one." It runs a waterfall through enrichers like Prospeo and LeadMagic, and lands 149 contacts with work emails.

4. "Write copy for a campaign about a webinar on running LinkedIn ads." It opens the copy framework file and writes the full sequence, mapped to the data on each lead.

5. "Create a campaign in Instantly with the leads and copy above." It reads Instantly's API docs, builds the campaign, and loads all 149 leads with their personalization tokens.

The Python step in instruction one is the one to understand. 

The scoring runs on raw numbers in code, not on an AI prompt asked to "rate this company." Code does not hallucinate at row 4,000. It scores 10,000 companies exactly the way it scores 10, which is what makes this safe to run on a list of any size.

You refresh Instantly and the campaign is sitting there, sequences written, leads mapped, signatures in place. What used to be half a day of moving data between four tools is now five sentences typed into a terminal.

---

# The real unlock is context

The cost drop is real, but the bigger win is context.

Before this, our copy frameworks lived in Google Docs, our targeting logic lived in Clay tables, and our API documentation was scattered across browser tabs. None of it talked to anything else, so every campaign started with someone reassembling that knowledge by hand. Now it sits in one folder the agent reads on every run, and it accumulates instead of scattering.

It also closes the loop. 

Let a campaign run for a week, then ask the agent to pull the analytics from Instantly: which copy replied, which job titles responded, which subject lines died. Save that back into the copy framework file, and the next campaign starts from evidence instead of a blank page.

> The workflows that win are the ones you own outright, sitting in one folder, getting smarter every time you run a campaign.

Signal-based targeting is how we hold a 28% win rate and an average contract value north of €150K. Those numbers come from a system that compounds, not a clever subject line.

---

The agency these three agents now run. Claude Code is how we keep a machine this size cheap to operate.

---

# Where the hype breaks down

Most of what gets posted about Claude Code and outbound is a highlight reel. Here is what gets cut from it.

It runs the work. The strategy is still on you. 

Claude Code will build the list, score it, write the sequence, and launch the campaign. It will not tell you which market to go after, what your offer should be, or why a segment is worth targeting. We have tried handing it the strategy and the output was weak. It is the operational arm, and the judgment that moves results is still yours.

It does not replace everything either. We still run Clay for parts of the enrichment and routing logic. The honest version is that Claude Code replaced our scraping tools outright and absorbed a lot of manual work, but the stack did not go to zero. It went from sprawling to small.

Anything creative still gets a human. The ad agent will iterate on a design you already have and draft copy from frameworks that already convert, but our copywriters and designers sign off on the final version. Give the agent thin context and it shows. In one campaign it left a date placeholder sitting in the copy because we never told it when the webinar was.

The first few weeks are also slower, not faster. Every skill starts as a string of failed API calls before it works, and that groundwork takes real time. The compounding is real. It just starts after the setup, not during it.

---

# How to start from zero

If you are building this yourself, the order matters more than the speed.

Start with the architect folder, not the agents.

Get your folder structure and skill-building frameworks right before you wire up a single workflow. We did it backwards once and paid for it with a full rebuild.

When you do not know how an API works, run Claude Code in plan mode and let it walk you through the setup and the tests. Build every skill the same way: let it fail, let it retry, and checkpoint the call the moment it works so it never gets rewritten. Then take one agent all the way to done before you start the next, so each one is earning its keep while you build.

A good first project is a YouTube summarizer agent.

Point it at tutorials, collect the summaries, and feed them into your architect folder as raw material. Channels like Nate Herk, Greg Eisenberg, and Riley Brown are worth the watch time. None are GTM-specific, but they teach the mechanics well. We also packaged the exact folder framework our team uses into a free resource, and the ColdIQ blog breaks down the APIs that turn Claude Code into a working cold email engine. The free directory of 1,300+ AI sales tools on [coldiq.com](http://coldiq.com/) maps out everything you can wire in.

A $20 Claude plan is enough to run all of this. You do not need the expensive tier to start.

---

# Owning your workflows is the moat

The stack was never the moat.

The six logins, the Clay credits, the scraping subscriptions, none of that was ever the edge. It was overhead we mistook for capability. The real advantage is owning your workflows as code, in one place, where every campaign you run makes the next one sharper than the last.

We are early. Most outbound teams have not opened the terminal yet. The next two years belong to whoever stops renting their workflows and starts owning them as code.
