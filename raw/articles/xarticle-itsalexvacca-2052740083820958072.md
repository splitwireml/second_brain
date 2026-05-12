---
title: "How to Run an AI-Native Services-as-Software Agency (3 AI Workflows You Can Copy)"
author: "Alex Vacca"
username: "itsalexvacca"
created: "2026-05-08T13:19:08+0000"
source: "https://x.com/i/status/2052740083820958072"
exported_at: "2026-05-10T00:00:00+0000"
likes: 137
retweets: 10
---

How to Run an AI-Native Services-as-Software Agency (3 AI Workflows You Can Copy)

A few months ago, Y Combinator published their 2026 Request for Startups.

Gustaf Alströmer's category writeup describes the company we've been running for four years. Word for word: "AI-native companies that don't sell software, they sell the service. The total spend on services is many times larger than the spend on software. And a lot of these services are already outsourced, which makes them much easier to replace with an AI-native product."

I read it the way I read Sequoia's "Services: The New Software" thesis a few weeks earlier. With a small laugh. Then a longer one.

ColdIQ, started in 2022. $7M+ ARR, 70 active clients, a team of 30+ across 10 countries. Bootstrapped, no VC, no angel round. We sell the outbound work. The software stack that runs it stays internal, built by us on Claude Code, Clay, Instantly, Lovable, and a Twain integration that replaced one of the most expensive roles in the agency.

I broke this down recently in a video I shared (https://x.com/itsalexvacca/status/2046571333857980843?s=20). This article is the operator-side version, with the math the video skipped and the workflows in detail. You can run this exact sequence of workflows to productize outbound services and run this like a software business underneath.

---

# What "AI-native services" actually means

The classical agency model worked because businesses pay experts a premium to make or save them money. They pay a meaningful multiple of any tool they could buy themselves. Marketing, content, sales, recruitment. Every category earns more than the SaaS underneath it, because clients want the outcome.

It capped at headcount. One human can fulfil only so many clients before the work degrades. Scale stopped wherever hiring speed and quality stopped, and margins flat-lined the moment they started covering management overhead.

The delivery layer started splitting 18 months ago.

> Strategy, accountability, judgement, client relationship: human. Pattern recognition, list building, copy production, deployment, reporting, admin: AI. The same delivery operator who used to run four accounts now runs thirteen.

P&L reads like SaaS.

Revenue per team member nearly triples. Cost per client stays flat. Gross margin starts looking like a software product instead of a body shop.

---

# The lever every agency operator should be tracking

There's one number we watch harder than ARR.

Our GTM engineer used to top out at four active clients. The cap was real. Run more than four campaigns at once and the quality slipped, the response times slipped, and the client noticed before we did.

Today the same role runs 13 active clients.

Same person. Same calibre of work. Same retention curve. Cost per client stayed flat because the human inputs didn't change. Revenue per team member nearly tripled because we deleted the parts of the job that didn't need a human in the loop.

That delta is the entire game.

YC's RFS describes the model from the customer side. AI does the work. Sequoia's thesis describes it from the budget side. The services dollar is bigger than the software dollar. The operator side, where per-employee throughput inside the agency decides whether the math works, is the one nobody writes up.

Three workflows draw the line between an agency with AI features and an AI-native services company.

---

# Workflow 1: The internal list builder

Every outbound agency burns disproportionate headcount on list building.

The classical workflow ran every week, per client, per campaign:

- Open Apollo, set the filters, click through pages of results, export the CSV.

- Repeat the routine inside LinkedIn Sales Navigator.

- Drop the list into Clay for enrichment.

- Fix the formatting issues by hand.

- Re-upload the cleaned list to the sequencer.

In some agencies that's a full-time hire. In others it's a team.

We rebuilt the workflow inside an internal tool we shipped on Lovable over nine months.

The operator dictates an ICP query in plain language with WhisperFlow. "VPs of sales, heads of growth, and chief revenue officers in New York City, at companies between 11 and 50 employees, who've raised seed or Series A, and have at least one GTM engineer on the team." The tool parses the query, sets the filters, runs the search, and pushes the resulting list into Clay for enrichment. Half a day in two UIs collapses to a fraction of the time.

The full-time list-builder role becomes a few minutes of dictation.

---

# Workflow 2: Sequence writing inside Clay

The second workflow that scaled badly was per-prospect copywriting.

Every campaign needs personalised copy. Every personalised email needs research. The classical workflow ran like this for every prospect on the list:

- Visit the prospect's LinkedIn profile and their company website.

- Find something relevant to them.

- Draft the email by hand and fit the personalised line in.

- Repeat the entire process for every prospect on the list.

Three emails per sequence. Hundreds of leads per campaign. Dozens of campaigns concurrent. In some agencies that's a full-time copywriter. In others, two.

We replaced the role with a Twain integration sitting inside Clay.

The campaign brief and the persona definition live as inputs. Every enriched lead in the Clay table flows in carrying its own context: the persona, the prospect's challenges, what they're working on, current company, company size, and their website. Twain reads the brief, reads the lead context, and writes a fully personalised three-step sequence per lead. The output sits in the same Clay table, ready for deployment.

The strategic frame stays human.

Campaign concept, offer logic, ICP, angle, trigger event, cadence rules: those decisions still get made by a senior operator who's run hundreds of campaigns and knows what works. The production layer underneath is what collapses. Once the strategist has designed the campaign, the writing of every personalised line runs on its own.

---

# Workflow 3: Campaign deployment via Claude Code

The third workflow is the one most agency owners look at and assume isn't worth automating.

Deploying a campaign in Instantly is pure admin. The classical workflow:

- Log in, create the campaign, upload the lead CSV.

- Map column headers to variables across every email in the sequence.

- Add the email accounts and set the sending schedule.

- Configure spin tax for every email in the sequence.

- Activate the campaign and confirm it's pushing.

An hour to two hours per campaign, per client. Pure admin. Zero strategic value. The layer most agencies still pay full-time humans for, because each task feels too small to bother automating and the tasks together feel too tedious to think about as a system.

We deleted the role. Claude Code does it.

The operator gives one instruction: "Here's the lead list. Upload it into Instantly, select my mailboxes, and tell me when the campaign is ready to be sent." Claude Code reads the instruction, calls the Instantly API, configures the campaign, maps the data, and reports back when the campaign is live.

The parts of the job that produce zero strategic insight and consume blocks of senior operator time are the easiest to automate and the highest-ROI to delete first. Most agencies postpone them, because automating admin feels less impressive than automating the strategy work. The order is reversed. Delete the admin first.

---

# Why the venture writeups can't tell you the operator side

Both YC's RFS and Sequoia's thesis are right about the macro. Services dollars are bigger than software dollars. Outsourced services categories are easy targets. AI-native delivery is the model that wins the next decade.

The model runs because per-employee throughput inside the delivery org compresses by a factor of three or four. At 70 active clients, the delivery layer that would have required around 18 GTM engineers in the old four-clients-per-engineer model now runs on 5 or 6 in the thirteen-clients-per-engineer one. Same revenue base, fraction of the headcount.

The math that used to flat-line at $1M ARR per founder keeps compounding past $7M because the layer that capped the old model is the layer AI eats first.

Vendor tools alone don't get you there. Our list builder is internal. Our copy production runs inside the data layer. Our deployment runs through Claude Code with custom skills. Three internal workflows, each removing a role's worth of headcount that an outside observer wouldn't notice was there.

YC's RFS lists four verticals where the model should hit hardest:

- Insurance brokerage

- Accounting, tax, and audit

- Compliance

- Healthcare administration

The model works in every one of them, and in 50 more YC didn't list.

Outbound is one of those 50. Recruitment, paid media, technical SEO, customer support, sales engineering, ABM. Every one has an outsourced services budget bigger than the software stack underneath, and a delivery layer that compresses cleanly when you build the right three or four workflows.

Sequoia named the category earlier this year. YC put it on the official list. The category is now the consensus bet for 2026, and the operator window is closing.

We packaged the playbook into a 12-week program at aiagency.io.

155 agencies have launched on the stack. The 11 AI agents we run inside ColdIQ ship to every member, and the same scoring criteria, copy frameworks, and Claude Code skills folder that handles our 70 active accounts gets handed over for the operator's first campaign in week one.

Built for operators, not spectators. If you're sitting at someone else's company with an idea you haven't acted on, or running a small agency stuck at a number you don't want to live at, book a call.

The category just opened. Three workflows separate the operators who run it from the ones who watch it.