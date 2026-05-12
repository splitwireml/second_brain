---
title: "The Complete Guide to API-Led GTM"
source: "x-bookmarks"
tweet_id: "2051029582070141119"
tweet_url: "https://x.com/MichLieben/status/2051029582070141119"
author_name: "Michel Lieben"
author_handle: "@MichLieben"
tweet_date: "Sun May 03 20:02:13 +0000 2026"
bookmark_date: "2026-05-03"
content_type: "x_article"
character_count: 12895
retweet_count: 2
like_count: 101
external_urls:
  - "http://trigify.io/)"
  - "http://cal.com/)"
  - "http://instantly.ai/)"
  - "https://coldiq.com/blog/the-6-apis-that-turn-claude-code-into-a-cold-email-engine)"
  - "https://coldiq.com/blog/how-to-run-a-linkedin-outbound-campaign-entirely-inside-claude-code)"
  - "http://claude.md/)"
  - "http://memory.md/))"
  - "https://coldiq.com/blog/the-content-engine-that-added-151k-mrr-in-87-days)"
  - "https://coldiq.com/blog/why-ai-agents-are-killing-seat-based-saas-pricing)"
  - "https://coldiq.com/blog/why-gtm-engineers-replace-5-hires-and-how-to-find-them)"
---

# The Complete Guide to API-Led GTM

The Complete Guide to API-Led GTM

Look at any SaaS in a typical B2B GTM stack and the value sits in the API behind the screen. Apollo is a contact database with a search bar bolted on. Underneath Clay's spreadsheet, a waterfall enrichment engine does the actual work. Smartlead's product is deliverability infrastructure; the sequence builder is the wrapper around it.

You're paying for the data and the infrastructure. The dashboards exist because the operators were human. Once an agent in Claude Code can read API documentation, make the call, parse the response, and route the result, the dashboard is overhead.

This guide is about running GTM from those APIs instead.

 It covers the stack we've tested across 70+ B2B clients at ColdIQ ($7M ARR), the workflows we ship every day on it, and the playbook for migrating your own.

---

# How the stack reorganizes around APIs

The mental shift is moving from thinking about tools to thinking about layers. Each layer corresponds to a job in the GTM motion, and each job has multiple API providers you can route through interchangeably. 

Here's the version we run.

- Signal layer. What's worth working at all. PredictLeads (hiring spikes, funding rounds, tech stack changes across 110 million companies). Common Room (community engagement on GitHub, Discord, G2, LinkedIn). [Trigify](http://trigify.io/) (social signal intelligence). RB2B and Vector (de-anonymized website visitors in Slack within ten seconds).

- Data layer. Turning signals into contactable records. Apollo for firmographic data at scale. AI Ark for company surfacing (70 million company database, lookalike search, hits in under two minutes). CompanyEnrich as alternative (30 million companies). Prospeo for verified emails (98% accuracy across 200 million contacts). FullEnrich for waterfall enrichment (cascades through 20+ providers, 80%+ find rates). Wiza for LinkedIn-to-contact conversion.

- Action layer. Where the campaign fires. Instantly for cold email at scale (warmup, deliverability, webhooks all programmatic). Lemlist for multichannel sequences. LinkedIn Ads and Meta APIs for paid media programmatic.

- Automation layer. What orchestrates the rest. Claude Code itself as the central runtime. n8n for long-running workflows that shouldn't stay open in a Claude Code session. Relevance AI for agent workflows that need more reasoning than a prompt chain.

- System of record. Attio is what we use, mostly because every object, list, and field has full API access. The CRM has become a shared state file every agent in the workflow reads from and writes to.

- Conversion + Revenue layers. [Cal.com](http://cal.com/) for scheduling (link embedded by the agent in the right email at the right moment). Hyperline for billing webhooks. Dreamdata for B2B revenue attribution (every touchpoint feeds back to the signal layer for the next campaign).

Use this map to pick one API per layer. 
Whichever you pick, the agent calls it the same way, and substitutions happen at the layer level (CompanyEnrich for AI Ark, Lemlist for Instantly) without changing the workflow structure.

---

# The kind of workflows people are building with this

Three of ours, documented in detail across our X content. Each takes a prompt as input and returns a live deliverable for human review.

## A 300-account outbound campaign in under 20 minutes

We asked Claude Code to build an outbound campaign targeting SaaS companies between 200 and 500 employees. Kenny on our team typed a few natural language prompts into the terminal.

- AI Ark pulled from a 70 million company database and surfaced 300 SaaS companies in the right headcount band in under two minutes. CompanyEnrich's 30 million company database would have worked the same way as a substitute.

- PredictLeads layered buying signals on top: hiring spikes, tech stack changes, product launches, press releases. 186 of the 300 companies were actively hiring for sales and marketing roles. The other 114 got dropped before any further work was done.

- BlitzAPI found decision-makers at the surviving companies through their ICP waterfall. Directors, VPs, C-suite. Filtered by persona, seniority, and department. Multiple contacts per account.

- Limadata filled the email gaps BlitzAPI missed. Two providers in the email layer matters because each has different strengths at scale.

- FullEnrich cascaded through 20+ providers to find mobile phone numbers and hit a 95% match rate on the contacts found.

- [Instantly.ai](http://instantly.ai/) created the campaign, pushed the leads, configured sending settings (plain text, no HTML, proper wait times, deliverability optimized), and parked it in draft mode for review.

The entire process ran on natural language. No code written. No tabs switched. No CSV exports.

After the campaign launches, Claude pulls campaign analytics from Instantly, identifies which personas responded, builds lookalikes of the best-performing leads, and feeds them into the next campaign. 

Outbound auto-improves like a retargeting pixel.

The composition is interchangeable: CompanyEnrich for AI Ark, Prospeo for Limadata, Lemlist for Instantly. The workflow runs end-to-end either way. The point is the stack reorganized itself around APIs and the agent picked which surface to call based on the job.

Full breakdown of this exact campaign with every API call is in [The 6 APIs That Turn Claude Code Into a Cold Email Engine](https://coldiq.com/blog/the-6-apis-that-turn-claude-code-into-a-cold-email-engine). Kenny's on-camera walkthrough video and tweet that gives away the underlying skills folder (376 likes, 451 replies) is [here](https://twitter.com/MichLieben/status/2044079352120520959):

[Embedded Tweet: https://x.com/i/status/2044079352120520959]

---

# Paid ads from the terminal

Same architecture, different APIs. Our head of growth Ivan runs more than $300K/mo in ad spend through Claude Code across LinkedIn Ads and Meta.

The workflow starts with ICP matrix construction, then sources target companies and contacts and enriches their emails via Prospeo. Brand specs get extracted from existing creative and stored in a skill the agent reads at session start. fal's API generates creative variations across 600+ AI models through a single endpoint. LinkedIn Ads and Meta APIshandle the audience uploads, campaign builds, and bid configuration programmatically.

The skills doing the work execute bulk edits across platforms, upload custom audience lists, and detect creative fatigue automatically. Once the skills folder matured, output doubled without sacrificing quality.

Ivan walks through the entire build on camera, here:

[Embedded Tweet: https://x.com/i/status/2045162376690073886]

---

# LinkedIn outreach from one terminal

We documented this architecture (developed alongside Othmane Khadri at Earleads in a 54-minute masterclass) in [How to Run a LinkedIn Outbound Campaign Entirely Inside Claude Code](https://coldiq.com/blog/how-to-run-a-linkedin-outbound-campaign-entirely-inside-claude-code).

The setup runs an entire LinkedIn outbound motion from one Claude Code terminal: list build, qualification, personalized message drafting, and outreach all from a single prompt.

The architecture is four layers (Input, [CLAUDE.md](http://claude.md/), Skills, [memory.md](http://memory.md/)) with a 7-gate qualification pipeline running underneath.

Tools wired in:

- Unipile for LinkedIn outreach (multi-account, with safe ceilings of 20 to 25 connection requests per day per inbox).

- Apify for any social scraping not natively covered.

- Firecrawl for company-page parsing, plus the standard ICP-scoring and copy-generation skills from the rest of the stack.

The 7-gate structure (qualification checkpoints between list build and outbound message) is the part most teams underbuild. The full breakdown is in the article.

---

## The 5-step migration playbook

If you wanted to move your stack to API-led GTM tomorrow, this is the order I'd run.

- Step 1. Set up the runtime. 
Install Claude Code (or Conductor on top of it). Create a project folder with CLAUDE.md, an empty .claude/skills/ directory, and a .env file ready for API keys. Spend an afternoon on CLAUDE.md: ICP definition, scoring rules, tool preferences, voice guidelines for cold email copy. Keep it under 200 lines. The agent reads this on every run.

- Step 2. Pick the first workflow. 
Start with target list scoring. Connect Claude Code to Apollo. Write one skill: "score a CSV of leads against my ICP and return the top 50%." Run it on a real Apollo export. The output is your first deliverable. Start here because the workflow is small enough to ship in one session and concrete enough that the value is immediately legible.

- Step 3. Run it deterministically twice. 
Run the same skill on a second Apollo export. The same scoring rule has to produce the same tiering on the same accounts. If it doesn't, your policy is sitting in the prompt instead of in the markdown, which means the workflow won't survive being handed to a teammate. Move the policy into the markdown until the second run matches the first.

- Step 4. Add the next layer. 
Connect Instantly. Build the cold email campaign workflow on the scored list from step two. Now you've chained two skills together with the output of the first feeding the second. Add PredictLeads or FullEnrich next so signals layer onto your scoring before copy gets generated. Each new layer is one markdown file plus one API key.

- Step 5. Fork the config. 
After your first campaign ships, the saved scripts in .claude/skills/ are the start of your institutional memory. Copy the entire project folder for the next client or campaign. Rewrite only the two voice-specific files: scoring criteria and copy frameworks. Everything else carries over. Onboarding the next workflow becomes a writing exercise.

The whole stack of skills we use across our 70+ clients is open-sourced. 
The giveaway tweet with the GitHub repo is [here](https://twitter.com/MichLieben/status/2044079352120520959):

[Embedded Tweet: https://x.com/i/status/2044079352120520959]

The 27-skill content engine architecture (a separate stack, content production specifically) is in [The Content Engine That Added $151K MRR in 87 Days](https://coldiq.com/blog/the-content-engine-that-added-151k-mrr-in-87-days).

---

# What changes in your business when you run this way

1. The cost shape inverts. 
The bill you used to pay for SaaS seats scaled linearly with headcount. Today the operators driving outbound for our 70+ clients sit on a fraction of those seats. The seat line collapsed. The API spend grew. Net spend roughly flat, throughput up several multiples.

2. The pricing models inside the stack reprice themselves. 
Clay is the example furthest along: workflow orchestration on Clay used to be free, then agents started building hundreds of thousand-row tables for free while humans were paying per seat for the privilege of running one workflow at a time, and Clay had to start charging per action. One of our agents spent $4,200 in API credits in a single month and no one told it to stop. When that's the workload pattern, seat pricing stops mapping to value created. I wrote the broader thesis on this in [Why AI Agents Are Killing Seat-Based SaaS Pricing](https://coldiq.com/blog/why-ai-agents-are-killing-seat-based-saas-pricing).

3. The hiring profile shifts. 
The skill that matters in this architecture is writing a CLAUDE.md that scopes the agent's job and trusting the agent to run the stack. I made the case for the new role explicitly in [Why Companies Are Replacing SDR Teams With GTM Engineers](https://coldiq.com/blog/why-gtm-engineers-replace-5-hires-and-how-to-find-them). One GTM engineer on our team replaces a 3-person SDR pod by building the revenue factory the SDRs would otherwise operate inside.

Campaign latency drops. Workflows that used to take days of human coordination ship from one prompt in minutes. Speed compounds because every campaign is a config file you can fork and reuse for the next one.

---

# When to skip this

The architecture won't earn its rent in a few situations.

Sales cycles measured in days. By the time you've migrated, the competitor has already closed. Transactional SMB motions don't benefit from the leverage this stack provides.

Buyers who don't live in digital channels. No signals to wire up means no targeting advantage on top of an empty signal layer.

Compliance environments that won't approve agent actions on customer data. The migration is still possible but the latency advantage shrinks dramatically.

Solo founders sending under fifty cold emails a week. The setup overhead exceeds the leverage at that volume.

For everyone else, pick one workflow this week. Rewrite it as a CLAUDE.md and a few API keys. That's the hour that changes which tools get to stay in your stack.
