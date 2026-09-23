---
source_url: "https://x.com/MichLieben/status/2102017602289803275"
ingested: "2026-09-22"
sha256: "dec7e7b6746fe82f435a56f484b807f12ee0d5fa7b5a8a89a460d66535900b31"
tweet_id: "2102017602289803275"
local_source: "/Users/mali/Development/x-bookmarks/data/run-2026-09-22/2026-09-21/xarticle-heres-every-top-api-you-need-for-doing-gtm-from-th-2102017602289803275.md"
run: "run-2026-09-22"
---
---
title: "Here's Every Top API You Need for Doing GTM From the Terminal"
source: "x-bookmarks"
tweet_id: "2102017602289803275"
tweet_url: "https://x.com/MichLieben/status/2102017602289803275"
author_name: "Michel Lieben"
author_handle: "@MichLieben"
tweet_date: "Mon Sep 21 12:50:24 +0000 2026"
bookmark_date: "2026-09-21"
content_type: "x_article"
character_count: 22158
retweet_count: 1
like_count: 36
external_urls:
  - "https://api.coldiq.com/v1/apollo/people/search"
  - "http://coldiq.com/)"
---

# Here's Every Top API You Need for Doing GTM From the Terminal

Here's Every Top API You Need for Doing GTM From the Terminal

3 clients per GTM engineer became 10 at the agency I built on the way to $7M ARR.

Claude Code is what made that possible. Below are the 28 APIs I would wire into it today, sorted into the eight layers a GTM system is made of. Each one comes with the call it earns, plus the three files that keep your keys out of your prompts and the schedule that keeps it running without you.

Everything is yours to copy, and you can follow it without ever having read an API doc, because the agent reads them for you.

Almost every tool in a GTM stack is a login screen wrapped around an API that does the actual work. Apollo is a contact database with a search bar bolted on. A sequencer is a deliverability engine with a form in front of it. It took me 300+ hours of testing coding agents for lead gen, with plenty broken and rebuilt from scratch along the way, to see that plainly. From the terminal you skip the screen and talk to the part that works.

---

# The map: eight layers, one terminal

Every campaign we ever ran had to settle the same eight questions, in roughly this order. The 28 APIs below are sorted by the job they do, because that is how the agent will use them.

1. Data (10 APIs): who exists, and how do I reach them?

2. Intent (5): who has a reason to buy this month?

3. Outreach (3): how does the message go out?

4. Automation (3): which steps run without me in the loop?

5. Infrastructure (2): do the emails land, and where does the truth live?

6. Sales (2): how does a reply become a recorded call?

7. SEO / AEO (2): how do buyers find us before we find them?

8. Affiliation (1): who else sells this for us?

The 28 by layer, so you can screenshot this once:

```javascript
Data            Apollo · Prospeo · AI Ark · Explorium · Limadata · FullEnrich · LeadMagic · Findymail · GetLeads · Exa
Intent          TheirStack · Sumble · RB2B · PredictLeads · Adyntel
Outreach        Instantly · lemlist · Expandi
Automation      Zapier · Airtop · Vibe Prospecting
Infrastructure  Hypertide · Supabase
Sales           folk · Claap
SEO / AEO       AirOps · Ahrefs
Affiliation     PartnerStack
```

One operating rule sits under all eight. The agent calls the API, writes the result to a table, and moves to the next step. Nobody opens a dashboard along the way, and no key ever gets pasted into a prompt. Hold on to that rule and the rest of this playbook is, honestly, wiring.

One word comes up in every layer after this: tier. Tier 1 is the dream-fit account you would call by hand, tier 2 a good fit, tier 3 a plausible one, and the tier decides how much of the stack a lead gets.

Layer 1 plus one sequencer is already a working system. The rest get added the week you feel the gap each one fills.

---

# Step 1. Wire the terminal, once

Claude Code reads three things before it touches an API: the servers listed in .mcp.json, the keys your shell loaded from .env, and the rules in CLAUDE.md. Set them up once per client folder and every prompt after that stays short.

## The server file.

Tools that ship an MCP server go here. One entry per server, the command or URL from the tool's docs, and the key pulled from the environment. The first interactive session in the folder asks you to approve the servers listed there:

```json
{
  "mcpServers": {
    "coldiq": {
      "command": "npx",
      "args": ["-y", "@coldiq/mcp@latest"],
      "env": { "COLDIQ_API_KEY": "${COLDIQ_API_KEY}" }
    }
  }
}
```

That entry is ColdIQ's own, from its public GTM skills repo, and the key comes from the API keys page in the ColdIQ marketplace. The shape is the same for every MCP server you add: the tool's docs give you the command or URL, and the key comes from your environment.

## The keys file.

Tools you call from a script read their key from .env. Each key comes from the tool's own settings page, usually under API or Developers. One line per tool, grouped by layer, so a missing key is obvious at a glance:

```bash
# layer 1 · data
COLDIQ_API_KEY=
APOLLO_API_KEY=
PROSPEO_API_KEY=
FULLENRICH_API_KEY=
LEADMAGIC_API_KEY=
FINDYMAIL_API_KEY=
EXA_API_KEY=

# layer 2 · intent
THEIRSTACK_API_KEY=
PREDICTLEADS_API_KEY=
SUMBLE_API_KEY=

# layers 3 + 5 · outreach, infrastructure
INSTANTLY_API_KEY=
LEMLIST_API_KEY=
SUPABASE_URL=
SUPABASE_SERVICE_KEY=
```

Add .env to .gitignore before the first commit, since the folder lives in a repo and the keys stay on the machine that runs it. The .mcp.json can stay in the repo: the value in it points at your environment, so the key itself never touches the file.

Claude Code expands ${COLDIQ_API_KEY} from your shell, so load the file before each session or the first MCP call fails on authentication:

```bash
set -a; source .env; set +a   # load the keys into the shell
claude                        # start the session inside the client folder
```

## The rules file.

CLAUDE.md is the rules file the agent reads on its own at launch, so the operating rule lives there:

```markdown
# [client]: working rules
- Keys live in .env. Never print them, never paste them into a prompt.
- Every API result gets written to the leads table before the next step runs.
- Unsure rows go to review.csv, never to a live sequence.
- Email waterfall order: Findymail, LeadMagic, Prospeo, Apollo, Limadata.
  Stop at the first verified hit. Catch-alls stay out of live sequences.
```

## The onboarding prompt.

This is the prompt I give the agent for every new tool, and the reason you never read a doc yourself:

> Fetch the API documentation for [tool]. Work out how to authenticate with the key in .env, make one test call that returns a single record, print the raw response, and list every action I can take with this API.

Read that raw response once. The field names you see in it are the ones every later prompt will use.

## The one-key shortcut.

14 of the 28 below sit behind the ColdIQ API, which is one key and one credit balance across 43 data providers and 700+ endpoints on its marketplace as I write this. The endpoint pattern is the provider name followed by the resource, so a test call looks like this:

```bash
curl -X POST https://api.coldiq.com/v1/apollo/people/search \
  -H "Authorization: Bearer $COLDIQ_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"person_titles": ["Head of Sales"], "q_organization_domains": ["example.com"]}'
```

The free tier carries 300 credits and includes the MCP server, so the wiring above costs nothing to test.

---

# Layer 1. Data: the 10 APIs that find people

A lead moves through four stages in this layer, always in the same direction: search, build, find, verify. Each stage has its own APIs and its own input.

Search: what exists on the web?

- Exa, a search API. You give it a plain-English query and it returns pages and domains: "companies like [domain]", "[role] at [industry] in [country]", "pages that mention [competitor]". The domains it returns are the input for the next stage.

Build: who is in the market?

- Apollo, the all-in-one GTM platform, with 240M+ contacts and 30M+ accounts behind its API. The broadest net in the list, and the right first pass on a segment you have never worked. An email costs 1 credit, and a mobile number adds 8.

- Prospeo, a B2B database plus an email and phone finder in one, which is why it also shows up in the email waterfall below. One credit buys one verified business email, a mobile number costs 10, and the Starter plan is $49 for 2,000 credits a month.

- AI Ark, a B2B database with lookalike targeting. Feed it your ten best clients and ask for the next hundred that look like them.

- Explorium, the aggregator of the group: 100+ sources behind one data API, and the engine under Vibe Prospecting further down.

- Limadata, a real-time B2B data API with 50+ endpoints, priced at around $0.02 a credit on the Starter plan. The one to reach for when freshness matters more than breadth.

Find: how do I reach them?

- FullEnrich, a waterfall email and phone finder that already cascades across 20+ vendors on its own and quotes finding 80%+ of what it is asked for. A work email is 1 credit, a mobile is 10, and 1,000 credits cost $55.

- LeadMagic, a mobile and email finder with a verifier attached. Email validation costs 0.25 credits against 1 for a find, which is why it runs the verify stage for everything the other finders return.

- Findymail, a mobile and email finder, first in the ColdIQ default order. One email is 1 credit, one phone is 10, and they refund credits when more than 5% of the addresses bounce.

- GetLeads, B2B email and phone enrichment sold as unlimited. The unlimited part is the price, a flat $497 a month. The capacity has a fair-use cap of 500,000 rows a day, which still suits a team that enriches every single day.

Verify: is the address real?

Every found address goes through validation before it goes anywhere near a sequence. Three verdicts, three actions:

- verified: keep it and stop the waterfall.

- catch-all: keep the row, hold it out of live sequences.

- not found: ask the next finder. A miss is free.

That stop rule is the entire economics of this layer. You pay for the address that comes back. A finder that returns nothing charges nothing, so the order of the finders is your only cost lever.

Here is the logic the agent runs, written out so you can hand it over or check it. It is pseudocode: call and validate are the two functions you write against each tool's docs.

```python
FINDERS = ["findymail", "leadmagic", "prospeo", "apollo", "limadata"]   # the first five of the default order

def find_email(lead):
    held = None
    for finder in FINDERS:
        email = call(finder, lead)                 # one HTTP call, key read from .env
        if not email:
            continue                               # a miss is free, ask the next finder
        verdict = validate(email)                  # LeadMagic email validation
        if verdict == "verified":
            return email, "verified", finder       # stop here
        if verdict == "catch-all" and held is None:
            held = (email, "catch-all", finder)    # keep it, out of live sequences
    return held or (None, "not found", None)
```

Through the ColdIQ MCP the same waterfall is one call, find_emails, with seven finders in its default order: Findymail, LeadMagic, Prospeo, Apollo, Limadata, Icypeas, Wiza. The example math on the same list: one provider finds around 40%, the waterfall finds around 80%. Twice the people you can write to, from a list you already own.

The prompt that runs the whole layer:

> Read leads.csv. For each row, confirm the company domain with Exa, then run the email waterfall in the default order and validate every hit with LeadMagic. Keep verified addresses for the live list, hold catch-alls in a separate column, and mark the rows where nothing came back. Write the result to clean-list.csv with the columns: company, domain, person, title, email, email_status, found_by.

---

# Layer 2. Intent: the 5 APIs behind "why this week"

A verified address gets you into the inbox. A reason gets you a reply. This layer produces the reason, and each API gets at it from a different side.

- TheirStack: technology lookup plus hiring signals, drawn from 243 million job postings across 195 countries. Ask it for companies that posted [role] in the last 30 days and run [tool]. A company hiring three SDRs while running HubSpot has told you what it is about to buy.

- Sumble: intent signals plus account research: the teams, technologies and active initiatives inside an account. Ask it what [account] is building, who owns the problem, and what moved this quarter. Run it before every tier 1 email. The free tier gives you 500 credits a month to try that on.

- RB2B: person-level visitor identification, for US visitors. Ask it who was on your pricing page this week, matched to a name and a company. It arrives by webhook, which is all the loop below needs. The warmest list you will ever get, and the one that goes stale fastest.

- PredictLeads: company intelligence, the raw material intent gets inferred from: job openings, news, technographics and financing events on 120M+ companies. Ask for everything that moved across [list] in the last 90 days. The first 100 API calls a month are free.

- Adyntel: the ad intelligence API, covering LinkedIn, Google, Meta and TikTok. Which competitors run ads, on which platform, since when. It works as a map of who is spending to reach your buyer, and you are only charged for calls that return data.

The one window I can give you from our own account scoring at the agency: someone moving jobs in the past 90 days counted as a recent signal, worth points on its own. For everything else, let the posting date, the event date and your own review cadence set the window.

The rule that ties this layer to the last one: the signal writes the first line. The other two layers find the person and send it, which is why the prompt below chains them:

> Use TheirStack to pull companies in [country] that posted a Head of Sales or SDR role in the last 30 days and run HubSpot. For each one, find the head of sales with Prospeo, run the email waterfall, and validate with LeadMagic. Write every row to the leads table with signal = "hiring" and the posting date. Show me the first 20 rows before anything is loaded into a sequence.

---

# Layers 3 and 5. Outreach and infrastructure: sending, and landing

Three APIs send. Two make sure the sending is worth anything.

## Outreach

- Instantly: the email outreach platform, and the volume channel, with deliverability tools and a 450M-contact database attached. Every tier goes through it. The v2 API creates the campaign, uploads the leads with their merge fields, and reads the replies back out.

- lemlist: the multichannel outreach platform. Email, LinkedIn, calls, WhatsApp and SMS in one sequence, which is where tier 1 and tier 2 accounts go when one channel is not enough.

- Expandi: the LinkedIn outreach platform, priced per seat. Tier 1 only, because a LinkedIn touch spends a scarce resource, your own profile's daily limits.

## Infrastructure

- Hypertide: cold email infrastructure for high-volume outreach across Google, Microsoft and Entra. Domains and inboxes at around $3.30 per Google inbox a month, provisioned before a single sequence loads. Published vendor guidance across the sequencers sits at 30 to 50 sends per inbox per day, so volume is an infrastructure decision, and this is where it gets made. At the agency we sent 500K+ cold emails a month across four sending platforms. Hypertide sells the inbox and domain step of that volume as a product.

- Supabase: your internal system of record, a Postgres database that generates a REST API for every table you create. One table that every layer writes to and every prompt can read back. The free tier holds 500 MB, which is years of leads.

The tier decides the channel and the channel decides the tool. Whether any of it lands is settled one layer down, in the infrastructure, which is why Hypertide comes before the first sequence.

The table is the part most people skip, and the part I would build first now. Here is a schema to start from:

```sql
create table leads (
  id            bigint generated always as identity primary key,
  company       text,
  domain        text,
  person        text,
  title         text,
  email         text,
  email_status  text check (email_status in ('verified', 'catch-all', 'not found')),
  found_by      text,
  signal        text,
  signal_date   date,
  tier          smallint,
  channel       text,
  sequence_id   text,
  status        text default 'new',
  updated_at    timestamptz default now()
);
```

Four columns carry the whole system. found_by is the finder that returned the address, signal and signal_date are the reason for this week, tier is 1, 2 or 3, and sequence_id is the Instantly or lemlist campaign the row was loaded into.

One rule for the copy, from the framework we built on 1,000,000+ emails analyzed in Instantly: value first in email 1. Let them raise a hand before anyone asks for a calendar slot.

> Take the verified tier 1 rows with signal = "hiring". Create an Instantly campaign named [client]-hiring-[month], map company, person and signal as merge fields, and upload the leads. Do not activate it. Write the campaign id back to sequence_id for every row you uploaded.

---

# Layers 4 and 6. Automation and sales: the loop that updates the record

The first three layers produce a campaign. These two keep it moving after a reply.

## Automation

- Zapier: the glue between an event and an action. A reply in Instantly becomes a row update in the table and a message in Slack, with no code written, across 30,000+ actions in 9,000+ apps. We ran this layer on n8n at the agency, 13 workflows at one point, every one of them written by Claude Code, and Zapier does the same job for a team that would rather host nothing. Its MCP comes with every plan and each call costs two tasks from your quota, so keep it for the glue and let scripts carry the volume.

- Airtop: the browser steps. Some work has no API behind it: a supplier portal that needs a login, a form with no endpoint. Airtop runs those in a cloud browser on your instruction, and the free tier's 1,000 monthly credits plus its one-time 10,000-credit bonus are enough to prove it on one job.

- Vibe Prospecting: the next list, in chat. You describe who you want in plain English and it builds the list on Explorium's data, 146M+ business entities underneath. Airtop and Vibe Prospecting earn their place for what they cover. Test each on one job before it goes into the loop.

## Sales

- folk: the relationship. The row becomes a contact with an owner the moment a reply is positive. At the agency the record lived in Attio, and the rule I would give you for folk is the one we ran there: the CRM reads from the table, and the table stays the source. Its API comes with the Premium plan, so budget for that tier from the start.

- Claap: the meeting, captured. At the agency we recorded every sales call and searched the transcripts by script for competitor mentions, which is the job this layer does. Claap's own line is that it captures every call, meeting and email with no bot in the conversation, then puts the notes back on the record. Owned by lemlist since October 2025.

Every step, from the Zapier route to the Claap notes, writes its result to Supabase before the next one starts, and a step that cannot write its result does not run.

> Every morning, read the replies from Instantly for the last 24 hours. Mark each row in the leads table as positive, neutral or negative. For positive replies, create the contact in folk with me as owner, and post the company, the signal and the reply text to Slack.

---

# Layers 7 and 8. SEO, AEO and affiliation: the layers that compound

Everything above is outbound. These three make the inbound side readable from the same terminal, and this is where the terminal surprised me most at the agency: we ran the SEO analysis through the Google Analytics MCP, and ranking first on Google for high-competition keywords within weeks was one of the results the coding-agent stack produced.

- AirOps: the AI-search read. It tells you where AI search engines mention you and where they mention competitors, and what to fix on the page.

- Ahrefs: the keyword read, plus Brand Radar for how AI answers mention you. API and MCP access start on the Lite plan, and the agent pulls the same report a person used to pull from a dashboard.

- PartnerStack: other people selling for you. ColdIQ began as an affiliate site reviewing sales tools, so I have sat on the partner side of this channel. PartnerStack covers affiliate, referral and co-sell partners: they get recruited and paid through it, and every referral shows up as a row you can query, which earns it the same weekly read as the rest.

These run on a clock:

```bash
# Monday 07:00: keywords, AI answers, competitor ads, account research
0 7 * * 1  cd ~/gtm && claude -p "$(cat prompts/weekly-monitor.md)" >> logs/weekly.md
```

The prompt file is the whole job description:

> Pull last week's ranking changes from Ahrefs for our tracked keywords. Pull the AI-search mentions from AirOps for us and for [competitor]. Pull new competitor ads from Adyntel. Write one page: what moved, what we should publish this week, and which three accounts Sumble says moved. Save it to reports/[date].md.

---

# Why it works, and what it does to the numbers

Cold email works when three things are true at once: the address is real, there is a specific reason to be in that inbox this week, and the follow-up arrives before the reason expires. Layers 1 and 2 produce the first two. The API layer removes the delay that used to kill the third, the days between a signal appearing and a person finding the time to act on it.

Small lists win, and they are expensive to keep full by hand.

In that same framework, lists of 500 to 1,000 hyper-targeted prospects replied at 20 to 30% while 100,000-contact blasts got 2 to 3%. Refilling a small list every week is exactly the work that pushed teams toward blasts in the first place. When the refill is a prompt, small lists stop being expensive.

- Capacity. Before Claude Code, one GTM engineer at the agency managed three clients. By the time it was calling the tools, that number was ten.

- Speed. We got to three times the campaign speed by building the API layer one connection at a time.

- Cost of a mistake. Every step is a row, so a bad campaign shows up in the table before it shows up in your replies.

Tonight this needs three files in one folder, one key in .env, the onboarding prompt run against one tool, and a single row written to the table. The rest arrive one at a time, each time you catch yourself doing a step by hand.

Fourteen of the 28 above are on the ColdIQ provider list, including the seven-finder email waterfall. Come schedule a chat directly with me on [coldiq.com](http://coldiq.com/) and I will let you know honestly whether it fits the list you have.
