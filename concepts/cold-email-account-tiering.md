---
title: Cold Email Account Tiering
created: 2026-10-07
updated: 2026-10-07
type: concept
tags: [cold-email, b2b, lead-gen, workflow, claude-code, mcp]
sources: [raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]
related_entity: [[michel-lieben]]
---

# Cold Email Account Tiering

CRM-derived ICP/TAM qualification and effort tiering: folk closed-won data and warm accounts become scored company research, tier-specific human/framework outreach, and closed-won feedback. The complete source prompts and scoring rubric are retained. Its top-500 research input versus “next 500” tier-2 wording is preserved without inventing additional researched rows. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

Michel Lieben’s October 6, 2026 course is preserved below as source material, not independently verified tool documentation, legal advice, pricing, platform policy or measured results. First-person statements belong to the author. Commands, prompts and templates are archival examples only: none were executed and no campaign was created. Only the source’s stated privacy, private-key, opt-out and approval constraints are retained. Linked destinations were not retrieved. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

## Source-preserved operational detail

# Step 2: Map your TAM and split it into 3 tiers (days 2 to 5)

> Tier the effort. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

Your TAM (total addressable market) is every company that matches your ICP (ideal customer profile): the kind of company, and the person in it, that buys from you. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

## Set up Claude Code

Every prompt here runs in Claude Code, Anthropic's AI agent for your terminal: it takes a request in plain English and does the work. It comes with every paid Claude plan (Pro is $20 a month). Paste this into the Terminal app and press Enter: ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

```plaintext
curl -fsSL https://claude.ai/install.sh | bash
```
^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

Then make a folder for this playbook, and always start Claude Code from it (log in on the first run): ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

```plaintext
mkdir cold-email && cd cold-email && claude
```
^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

Keep every file this playbook names in that folder. Claude Code writes any of them for you: paste the text and ask it to save the file. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

---

# Pull the four inputs from your CRM

It starts in folk, our CRM, with four inputs: ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

1. Closed won: every company that has paid you, sorted by deal size. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

2. Fit criteria: what your best customers share, like industry, headcount, country, tools and the signer's title. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

3. Buying signals: what happened at those companies in the months before they bought, like hiring, funding or a new leader on the buying team. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

4. Warm accounts: companies that already know you, like past demos, newsletter readers, post engagers and the new companies of past users. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

Import customers and past demos into folk as a CSV file, tag newsletter readers and post engagers, and list your 5 dream customers in dream.md, one per line, with the reason each fits. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

folk's MCP server (a connector that lets Claude Code use folk directly) comes with every paid plan. Deal values live in its Deals object, from Premium ($48 per member a month, billed annually). Type /exit, paste this into the Terminal, then run claude again and type /mcp to sign in: ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

```plaintext
claude mcp add -t http -s user folk https://mcp.folk.app/mcp
```
^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

```plaintext
Read every closed-won deal in folk, and read dream.md.
List what the top 20 by deal value have in common
(industry, headcount band, country, tools, signer's title)
and write it as a one-page ICP in icp.md.
Export every company that already knows us (past demos,
newsletter readers, post engagers, new companies of past users)
to warm.csv.
```
^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

---

# Map the TAM

Turn icp.md into Apollo filters (industry, headcount, location, technologies) and export every match as tam.csv. Apollo's free plan selects 25 records at a time and Basic ($49 per seat a month, billed annually) selects 1,000, so run the full export on Basic. GetLeads and Explorium do the same job. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

---

# Score, research and tier

Save this as score.md: ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

```plaintext
FIT (0 to 3)
+1 industry matches your best customers
+1 headcount is inside your band
+1 uses a tool your product works with

SIGNAL (0 to 3)
+1 hiring for a role your product helps
+1 raised money in the last 12 months
+1 new leader on the buying team

WARM (0 to 2)
+1 engaged with your posts, emails or newsletter
+1 a past user of your product works there

TOTAL = FIT + SIGNAL + WARM (0 to 8)
```
^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

FIT only needs the Apollo export, so it's scored first, and the research runs on the 500 best fits. Your emails open on this hyper-enriched data: tech stack, funding, job posts, case studies and the LinkedIn headline, which comes with the people in step 3. PredictLeads covers the first four at $0.04 a call after 100 free a month, so 500 companies across 4 datasets is about 2,000 calls, roughly $80. Connect it the same way: ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

```plaintext
claude mcp add -t http -s user predictleads https://mcp.predictleads.com/
```
^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

```plaintext
Score every company in tam.csv on FIT, using score.md.
For the 500 with the highest FIT score, add from PredictLeads
their technologies, last funding round and its date,
open job posts and new leaders hired in the last 90 days,
plus the customers named on their case studies page.
Save it as tam_research.csv.
```
^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

Then tier the list: ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

```plaintext
Score every company in tam_research.csv on SIGNAL and WARM,
using score.md and warm.csv.
Add 3 columns: total, tier, and the one fact
your email should open on.
Tier 1: the highest totals, as many as I can write
to by hand this month (start with 20).
Tier 2: the next 500 companies by total, two people each.
Tier 3: everyone else, queued for the months after.
Save it as tiers.csv.
```
^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

## Work each tier its own way

- Tier 1: 1:1 lead selection → handwritten messages → manual outreach. You pick each person, write each message and send it yourself, by email and LinkedIn. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

- Tier 2: identify the product user and the decision maker → personalized messaging → multichannel outreach. The daily user and the signer each get a framework email with a custom first line, plus Expandi LinkedIn touches. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

- Tier 3: find the decision maker → messaging frameworks → email outreach. One decision maker per company, one framework from step 4. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

All three end the same way: meeting booked → sales process → closed won. Each new closed-won deal goes back into folk for next month's scoring. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

---

## Related

- [[cold-email]]
- [[four-layer-b2b-funnel]]
- [[cold-email-campaign-plays]]
- [[api-led-gtm]]
