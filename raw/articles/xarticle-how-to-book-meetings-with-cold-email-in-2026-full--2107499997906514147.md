---
source_url: "https://x.com/MichLieben/status/2107499997906514147"
ingested: 2026-10-07
tweet_id: "2107499997906514147"
sha256: 205350567db18050f78b00a5003bc193e8272cd39cabf17e8f07d1c765cbd8fc
---
---
title: "How to Book Meetings With Cold Email in 2026 (Full Course)"
source: "x-bookmarks"
tweet_id: "2107499997906514147"
tweet_url: "https://x.com/MichLieben/status/2107499997906514147"
author_name: "Michel Lieben"
author_handle: "@MichLieben"
tweet_date: "Tue Oct 06 15:55:29 +0000 2026"
bookmark_date: "2026-10-07"
content_type: "x_article"
character_count: 36811
retweet_count: 3
like_count: 61
external_urls:
  - "https://claude.ai/install.sh"
  - "https://mcp.folk.app/mcp"
  - "https://mcp.predictleads.com/"
  - "https://mcp.instantly.ai/mcp"
  - "http://coldiq.com/)"
---

# How to Book Meetings With Cold Email in 2026 (Full Course)

How to Book Meetings With Cold Email in 2026 (Full Course)

Cold email is how a company nobody has heard of starts a conversation with the people it wants to sell to.

I learned it the slow way. My first 4,000 cold emails got me 1 lead. I kept sending, kept reading the replies, kept fixing what broke, and the agency we built after that grew to $7M ARR and 275+ clients. Everything that worked went onto one page, my 2026 Cold Email Cheat Sheet.

This playbook walks you through that page in the order you build it. By day 15 you'll have:

- Five warmed inboxes, set up and checked before they send a single cold email

- Your best 500 accounts, scored against your own closed-won deals and split into 3 tiers

- A play for each tier, so every stranger gets a real reason to reply

- Email 1 and a 3-step sequence, written on one of 12 frameworks from the top 1%

- A 90-second morning check that spots a struggling inbox before it hurts your domain

Every setting, prompt and template is here to copy. Your first campaign goes out on day 15.

---

# What every reply needs, in order

Gmail and Outlook decide where an email lands from the reputation of the domain it comes from and of the IP that sends it, and a new domain has no reputation yet.

A reply needs three layers, in this order:

1. An inbox Gmail and Outlook already trust, so the email lands where it gets read.

2. A reason to reply this week, given to the one person who owns the problem.

3. Words a reader takes in on a phone, carrying one idea about them.

---

# Step 1: Stay out of spam (day 1)

> 100 emails an hour from one inbox lands in spam.

That's the warning box on my cheat sheet. Every other step depends on staying far below it.

## Part 1: the mailboxes

My rule: tenant isolated, live in hours. We order ours from Hypertide. It takes the domains, the mailbox names and your stack (Google or Microsoft), then buys the domains, writes the DNS records and creates the mailboxes, typically within 4 to 6 hours.

- Google inboxes carry the second half of that rule: live in hours, with no tenant isolation, at $3.30 each a month.

- Microsoft (Entra) inboxes carry both halves: one isolated tenant per domain, with its own sending quota, so a suspension stays inside it. Sends still share Microsoft's IP ranges. At $25 a month for 25 inboxes, they're the step up for volume.

Then plan the domains (the math is for Google inboxes):

1. Keep your main domain out of cold email. Everyday email stays on yourbrand.com.

2. Use multiple new domains that read like your brand, like getyourbrand.com, each one its own domain. Google counts a subdomain like mail.yourbrand.com toward the main domain's volume.

3. Plan 3 inboxes per domain, named after you and your teammates (Instantly's guidance is 3 to 5 at most).

4. Forward each new domain to your website at its registrar.

5. Start with 150 emails a day: 5 inboxes on 2 domains. The math, for any other volume:

```plaintext
inboxes = emails per day ÷ 30, rounded up
domains = inboxes ÷ 3, rounded up
```

Five inboxes fit Instantly's Growth plan: $47 a month for 1,000 uploaded contacts and 5,000 emails.

Check the DNS. Hypertide publishes the records. Then run Instantly's Test domain setup on every domain and confirm MX, SPF, DKIM and DMARC all pass. Together they route your replies and prove your emails really come from your domain. Keep one DMARC record per domain, because two on the same domain cancel each other out.

---

## Part 2: the warmup

My rule: 2 weeks of warmup before the first send, Instantly's own minimum. Warmup trades emails between real inboxes, so a new inbox builds a normal history.

1. Connect every inbox to Instantly. Hypertide can upload its Google inboxes straight in.

2. Switch warmup on at Instantly's recommended settings: increase per day 1, daily warmup limit 10, reply rate 30%.

3. Send no cold email from these inboxes for 14 days.

4. Read the Health Score on day 14: the share of warmup emails that landed in the inbox over the last 7 days. Instantly rates above 90% as good, our launch gate. My running target is 99+.

5. Keep warmup on for good. Instantly advises never switching it off, and warmup emails don't count against your campaign limit.

---

## Part 3: the settings (in the campaign, days 11 to 14)

My rule: tracking off, plain text, ESP match. Instantly's deliverability guide recommends a plain-text first email with no links and no open tracking, plus provider matching. Link tracking off on every step is our call. In each campaign's Options tab:

- Open and link tracking: off. Open tracking hides a remote image in each email, and link tracking routes links through a shared tracking domain. Duplicated campaigns keep the old setting, so check each new one.

- Plain text: Delivery optimization → Send emails as text-only (no HTML), with no links in email 1.

- ESP match (email service provider): Advanced Options → Provider Matching pairs Google inboxes with Google users and Outlook inboxes with Outlook users.

- An opt-out in every email: a last line like "Reply stop and I won't email you again", your postal address in the signature, and every stop reply on Instantly's block list the same day. Instantly's guide calls an opt-out a legal requirement under laws like CAN-SPAM and GDPR.

---

## Part 4: the daily limits and the lists (from day 15)

- 30 emails per inbox per day, at most. Each inbox sends 10 a day in its first week of sending, 20 in its second and 30 from its third. Each Monday, check two numbers before you raise an inbox's Daily Campaign limit: bounces under 2% and a Health Score above 95. Set the campaign's Daily Limit to inboxes × the per-inbox limit, and keep Instantly's default gap (9 minutes plus a random delay) to hold each inbox far below 100 an hour.

- Clean, validated lists. Tick Verify leads on upload (0.25 Instantly credits per lead, a separate plan), keep the default that skips invalid and risky addresses, and put catch-alls (domains that accept every email, so no checker can confirm the person) in their own small list.

- Bounces under 3%. A bounce is an email returned because the address doesn't exist. 3% is my ceiling and the morning check's flag. Instantly's High Bounce Auto-Pause, on by default, stops a campaign at 5% bounces after its first 200 emails.

Five inboxes send 150 a day from week three: about 3,300 a month over 22 weekdays, enough for 1,000 people through all 3 emails.

---

# Step 2: Map your TAM and split it into 3 tiers (days 2 to 5)

> Tier the effort.

Your TAM (total addressable market) is every company that matches your ICP (ideal customer profile): the kind of company, and the person in it, that buys from you.

## Set up Claude Code

Every prompt here runs in Claude Code, Anthropic's AI agent for your terminal: it takes a request in plain English and does the work. It comes with every paid Claude plan (Pro is $20 a month). Paste this into the Terminal app and press Enter:

```plaintext
curl -fsSL https://claude.ai/install.sh | bash
```

Then make a folder for this playbook, and always start Claude Code from it (log in on the first run):

```plaintext
mkdir cold-email && cd cold-email && claude
```

Keep every file this playbook names in that folder. Claude Code writes any of them for you: paste the text and ask it to save the file.

---

# Pull the four inputs from your CRM

It starts in folk, our CRM, with four inputs:

1. Closed won: every company that has paid you, sorted by deal size.

2. Fit criteria: what your best customers share, like industry, headcount, country, tools and the signer's title.

3. Buying signals: what happened at those companies in the months before they bought, like hiring, funding or a new leader on the buying team.

4. Warm accounts: companies that already know you, like past demos, newsletter readers, post engagers and the new companies of past users.

Import customers and past demos into folk as a CSV file, tag newsletter readers and post engagers, and list your 5 dream customers in dream.md, one per line, with the reason each fits.

folk's MCP server (a connector that lets Claude Code use folk directly) comes with every paid plan. Deal values live in its Deals object, from Premium ($48 per member a month, billed annually). Type /exit, paste this into the Terminal, then run claude again and type /mcp to sign in:

```plaintext
claude mcp add -t http -s user folk https://mcp.folk.app/mcp
```

```plaintext
Read every closed-won deal in folk, and read dream.md.
List what the top 20 by deal value have in common
(industry, headcount band, country, tools, signer's title)
and write it as a one-page ICP in icp.md.
Export every company that already knows us (past demos,
newsletter readers, post engagers, new companies of past users)
to warm.csv.
```

---

# Map the TAM

Turn icp.md into Apollo filters (industry, headcount, location, technologies) and export every match as tam.csv. Apollo's free plan selects 25 records at a time and Basic ($49 per seat a month, billed annually) selects 1,000, so run the full export on Basic. GetLeads and Explorium do the same job.

---

# Score, research and tier

Save this as score.md:

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

FIT only needs the Apollo export, so it's scored first, and the research runs on the 500 best fits. Your emails open on this hyper-enriched data: tech stack, funding, job posts, case studies and the LinkedIn headline, which comes with the people in step 3. PredictLeads covers the first four at $0.04 a call after 100 free a month, so 500 companies across 4 datasets is about 2,000 calls, roughly $80. Connect it the same way:

```plaintext
claude mcp add -t http -s user predictleads https://mcp.predictleads.com/
```

```plaintext
Score every company in tam.csv on FIT, using score.md.
For the 500 with the highest FIT score, add from PredictLeads
their technologies, last funding round and its date,
open job posts and new leaders hired in the last 90 days,
plus the customers named on their case studies page.
Save it as tam_research.csv.
```

Then tier the list:

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

## Work each tier its own way

- Tier 1: 1:1 lead selection → handwritten messages → manual outreach. You pick each person, write each message and send it yourself, by email and LinkedIn.

- Tier 2: identify the product user and the decision maker → personalized messaging → multichannel outreach. The daily user and the signer each get a framework email with a custom first line, plus Expandi LinkedIn touches.

- Tier 3: find the decision maker → messaging frameworks → email outreach. One decision maker per company, one framework from step 4.

All three end the same way: meeting booked → sales process → closed won. Each new closed-won deal goes back into folk for next month's scoring.

---

# Step 3: Pick a play for each tier (days 6 and 7)

> Every play gives your prospect a real reason to reply.

A play is a campaign built on one reason to reply, rated from ★ (quick win) to ★★★ (advanced). Start with a quick win. The full builds are in [Part 1](https://x.com/MichLieben/status/2102820264186970172) and [Part 2](https://x.com/MichLieben/status/2104609197707116605) of my GTM plays.

## Quick wins (★)

1. Post Engagers · inbound-led outbound

Every like on a post is a name worth chasing.

- The list: everyone who liked or commented on your company's LinkedIn posts, filtered to your ICP, minus your open deals in folk. GetLeads pulls them at $0.012 per engager (LinkedIn shows up to 3,000 likers per post).

- Reason to reply: they already picked the topic in public.

- Pair with: framework 11, Content Offer (Part 2, play 6).

2. Campaign Ideas · value-based

Three ideas written for that one company, before any ask.

- The list: tier 2 and 3 companies with a clear website.

- Reason to reply: three campaign ideas about their business, each backed by a named customer's result. A free audit works as the offer too.

- Pair with: framework 2, 3 Campaign Ideas (Part 1, play 10).

3. Is This Your Number? · value-based

The subject line is their own mobile number. The email is the demo.

- Who it's for: teams that sell data.

- Where I saw it: FullEnrich cold emailed me with my mobile number as the subject line, "is this you?" in the body and free credits as the offer.

- The list: sales leaders whose mobile your tool finds (here, FullEnrich's phone waterfall). Delete rows with no mobile, because the number is the whole email.

- Reason to reply: your product just proved itself on them.

- Pair with: framework 1, AIDA, with the number as the attention (Part 1, play 11).

- Check first: the data-protection rules where your prospects live (GDPR in the EU), since a mobile number is personal data.

---

## Medium (★★)

4. Champion Job Changes · signal-based

People who already used your product, now at a new company.

- The list: past customer contacts and power users from folk, saved as Sales Navigator leads (a paid LinkedIn plan) with the "A lead started a position at a new company" notification on, or saved as contacts in Apollo and tracked with its "Job Change" filter (paid plans). Keep the new companies that fit your ICP.

- Reason to reply: they already trust the product.

- Pair with: framework 9, Champion Play (Part 1, play 1).

5. Hiring Surge · signal-based

Find the sales or marketing teams that grew fastest in 6 months.

- The list: Apollo's "Headcount growth" filter on Sales or Marketing over 6 months (paid plans), plus the open roles in tam_research.csv.

- Reason to reply: new reps need pipeline from month one, and the open roles show more are coming.

- Pair with: framework 12, Do the Maths, or 6, Team Size (Part 1, play 3).

6. Lookalike Case Studies · cold outbound

Every case study is a campaign for the companies that look like that client.

- The list: one case study with a hard number, then that client's lookalikes from PredictLeads' Similar Companies or Apollo's company lookalikes (a paid-plan beta, up to 5 seed companies), kept to the client's business model.

- Reason to reply: a company like theirs already got the result.

- Pair with: framework 6, Team Size, whose third beat is the lookalike win (Part 2, play 14).

7. Replacing Who Left · recruiting

Reach the manager before the job post exists.

- Who it's for: recruiting agencies.

- The list: people in a role you recruit for who left a company you sell to. In Sales Navigator, set "Past company" to that company and "Changed jobs (in the last 90 days)". Then find their old manager, and check PredictLeads' Job Openings for the post.

- Reason to reply: the manager feels the empty seat the day it opens.

- Pair with: framework 3, Right Person?, asking whether they're hiring for that seat (Part 1, play 23).

---

## Advanced (★★★)

8. ABM Orchestration · multichannel

Ads warm the account, outbound books the meeting.

- The list: your tier 1 and 2 companies as a CSV with LinkedIn's company-list headers, uploaded in Campaign Manager under Plan → Audiences → Create audience → Matched Audience → Company / Contact → Company list. It needs 300+ rows and 300+ matched members before an ad set can run, and up to 48 hours to build (LinkedIn recommends 1,000+ companies).

- Reason to reply: they've seen your name in their feed before the email arrives.

- Pair with: framework 7, TIPS (Part 2, play 16).

9. High Net Worth Individuals · niche ICP

Every private jet has a registered owner, and the register is free.

- Who it's for: high-end property and wealth services.

- The list: the FAA's Releasable Aircraft Database, a free nightly download with no login: owner names and mailing addresses for US-registered aircraft, with no phones or emails. Most jets sit in an LLC or with a trustee bank, so you find the person behind each one, and owners can ask the FAA to withhold their details.

- Reason to reply: a handwritten note about something they care about, like property in their area, with no mention of the jet.

- Pair with: a tier 1 email written by hand (Part 2, play 18).

- Check first: the privacy and calling rules where these private individuals live.

Pull the list for each play

1. Find the people in Apollo's people search, by job title, at the play's companies (two per company in tier 2), and export first name, last name, company domain and LinkedIn headline as a CSV.

2. Find the emails: upload the CSV to Prospeo or FullEnrich and download it back with verified emails. FullEnrich's waterfall, which asks several data providers in turn, also finds mobiles for the accounts you'll call.

3. Join the research: have Claude Code add each company's tam_research.csv columns, matched on company domain, and save the file under the play's name, like hiring_surge.csv.

---

# Step 4: Write email 1 with one of 12 frameworks (days 8 to 10)

> No copy saves a bad offer.

That's rule 2 of my nine, so the offer comes first: one line at the top of a new doc for this campaign, saying what they get for replying, like a free audit of their last 3 campaigns with 3 fixes in 48 hours.

Then pick one of the 12 frameworks from the top 1%: the skeleton your sentences follow, from the opener to the CTA (the question at the end).

How to use the 12:

1. Copy the template paired with your play into Instantly as email 1, ending with your signature, postal address and the step 1 opt-out line.

2. Treat every number in the sample lines as a placeholder. The numbers you send come from your own customers or a source you can name.

3. Add a second version of email 1, on another framework, as step 1's second variant. Instantly splits the list between them.

For tiers 2 and 3, save the templates below as frameworks.md and your customer results as results.md, one per line:

```plaintext
customer | situation before | what changed | result | source
```

Claude Code fills the fields, here for the Hiring Surge list:

```plaintext
Read hiring_surge.csv, frameworks.md and results.md.
For each lead, write every {{field}} in both email 1 versions
(frameworks 12 and 6) and in emails 2 and 3 as new columns,
named exactly like the fields, one short line each.
Skip {{firstName}} and {{companyName}}: Instantly fills those.
Use only facts from that lead's research columns
and results from results.md.
Next to each field, name its source column or write MISSING.
Save complete rows as hiring_surge_email1.csv
and MISSING rows as hiring_surge_gaps.csv.
Change nothing in Instantly.
```

Upload hiring_surge_email1.csv with Verify leads ticked, map each column to its field, and rerun research on the gaps file on day 10.

---

## 1. AIDA (Monika Grycz's version)

Skeleton: attention → interest → desire → action

Sample line: "Too many no-show demos this week? Teams like {{company}} cut them by 37% in 30 days."

Best for: a customer result that answers a pain they feel this week.

```plaintext
Subject: {{pain_in_two_words}}

{{pain_question}} at {{companyName}} this week?
{{customer}} had the same problem with {{their_old_way}}.
They cut it by {{real_result}} in {{real_timeframe}}.
Worth a look at how they did it?
```

---

## 2. 3 Campaign Ideas (Dujam Dunato's version)

Skeleton: engagement hook → 3 AI ideas → imagine at scale → worth it?

Sample line: "Our AI analyzed {{company}} and came up with 3 campaign ideas you could implement."

Best for: the Campaign Ideas play. It's built on Eric Nowoslawski's "Creative Ideas" campaign.

Get the ideas first:

```plaintext
Read {{company_website}}: the homepage, pricing page and case studies.
Write 3 outbound campaign ideas for {{companyName}}, each naming
who to target, the reason to reach out and the email's first line.
Tie every idea to one quoted detail from their site.
Use results from my case studies only, with the customer named.
```

Then the email:

```plaintext
Subject: 3 ideas for {{companyName}}

Our AI analyzed {{companyName}} and came up with 3 campaign ideas for you:

1. {{idea_1}}
2. {{idea_2}}
3. {{idea_3}}

Imagine a new set like this for every account on your list, every month.

Worth it?
```

---

## 3. Right Person?

Skeleton: right person? → recap and proof → 2 benefits → point me

Sample line: "Are you the right person to speak with about {{problem}}?"

Best for: a company that fits, with no clear owner of the problem.

```plaintext
Subject: right person?

Hi {{firstName}}, are you the right person to speak with about {{problem}} at {{companyName}}?

We help {{type_of_company}} {{outcome}}. {{customer}} {{real_result}}.

Two things teams get from it:
- {{benefit_1}}
- {{benefit_2}}

Who on your team owns this? Happy to be pointed their way.
```

---

## 4. PAS (as Soheil Saeidmehr uses it)

Skeleton: pain → agitate → solve → soft CTA

Sample line: "Your energy bills keep climbing, even when your usage hasn't changed."

Best for: a big pain they notice every month, backed by a strong case study.

```plaintext
Subject: {{pain_in_two_words}}

{{pain}} at {{companyName}}, even after {{what_they_already_did}}.
Every month it stays that way costs {{what_it_costs}}.
{{your_product}} {{how_it_fixes_it}}. {{customer}} {{real_result}}.
Open to seeing how?
```

---

## 5. Industry Challenge (by Patrick Trümpi)

Skeleton: peers' challenge → personalize → solution → CTA → PS

Sample line: "Security officers at banks face losses of $9k per hour due to ransomware."

Best for: an industry-wide problem with a named source for every number.

```plaintext
Subject: {{industry}} and {{challenge}}

We work with {{role_plural}} at {{type_of_company}} like {{client_1}}, {{client_2}} and {{client_3}}, and most of them are dealing with {{challenge}}.
{{companyName}} {{specific_detail}}, so it's probably on your list too.
{{your_product}} {{how_it_helps}}, and {{client_1}} {{real_result}}.
Interested?

PS: {{something_personal_or_light}}
```

---

## 6. Team Size (credited to Nick Abraham)

Skeleton: team size → bottleneck → lookalike win → result → PS

Sample line: "Noticed your {{department}} team is around {{team_size}} people now."

Best for: Hiring Surge and Lookalike Case Studies.

```plaintext
Subject: {{department}} team

Noticed your {{department}} team is around {{team_size}} people now.
{{bottleneck}} usually starts to show at that size.
{{lookalike_customer}} hit the same point at {{their_size}}.
They {{real_result}} after {{what_they_changed}}.
Want to see how they did it?

PS: {{one_line_proof}}
```

---

## 7. TIPS (by Aaron Reeves)

Skeleton: trigger → implication → pain → proof and solution

Sample line: "Saw you're expanding to the US. At 3% FX fees, that could be $300,000."

Best for: a trigger you can put a number on. In the sample, 3% of $10M in US sales is $300,000.

```plaintext
Subject: {{trigger_in_two_words}}

Saw {{trigger}}.
{{fee_or_cost}} on that comes to about {{cost}}.
{{the_pain_that_follows}}.
{{customer}} {{real_result}} with {{your_product}}.
Worth a look?
```

---

## 8. Tal's Structure v3 (by Tal Baker-Phillips)

Skeleton: 2-word subject → trigger → current process → pain or symptom → root cause → value CTA

On my cheat sheet: "Subject line: two boring words, all lowercase." For example: sdr hiring.

Best for: an email that reads like a note from a peer.

```plaintext
Subject: {{two_boring_words}}

Noticed {{trigger}}.
You're likely {{current_process}} today.
That usually means {{pain_or_symptom}}.
Normally it comes down to {{root_cause}}.
Could I share {{resource}} that helps with {{outcome}}?
```

---

## 9. Champion Play (by Brian LaManna)

Skeleton: joined from a customer → skip the pitch → 3 value props → no-pressure ask

Sample line: "You're no stranger to this, so I'll spare you the pitch."

Best for: Champion Job Changes.

```plaintext
Subject: congrats on {{new_company}}

Congrats on the move to {{new_company}}. You used {{your_product}} at {{old_company}}, so you're no stranger to this. I'll spare you the pitch.

Three ways it helps at {{new_company}}:
1. {{value_prop_1}}
2. {{value_prop_2}}
3. {{value_prop_3}}

Happy to send a quick tour of what's new. No expectations.

PS: {{something_personal}}
```

---

## 10. Obvious Choice (credited to Leif Bisping)

Skeleton: everyday situation → obvious choice → their choice

Sample line: "Diet Coke for $0, $1 or $1.50. So why pay 1.5% in processing fees?"

Best for: a price or fee clearly lower than what they pay today.

```plaintext
Subject: {{everyday_item}}

{{everyday_item}} for {{price_1}}, {{price_2}} or {{price_3}}.
So why pay {{what_they_pay}} for {{their_thing}} at {{companyName}}?
{{your_product}} does it for {{your_price}}. Want the math?
```

---

## 11. Content Offer (by Ethan Parker)

Skeleton: name the asset → how it helps → can I send it? → PS reason

Sample line: "We compiled a cheat sheet on AEs self-sourcing 30% of pipeline. Can I send it over?"

Best for: Post Engagers, or any guide or benchmark worth sending.

```plaintext
Subject: {{asset_name}}

We put together {{asset}} on {{topic_they_engaged_with}}.
It shows {{how_it_helps_them}}.
Can I send it over?

PS: sending it your way because {{reason_tied_to_them}}.
```

---

## 12. Do the Maths (by Thibaut Souyris)

Skeleton: trigger with a number → quick pitch → napkin math → CTA

Sample line: "50 open roles. 15 mishires down to 5 at $30k each: $300,000 saved."

Best for: triggers that come with a number. In Thibaut's original, 15 and 5 come from cutting new-hire churn from 30% to 10% across 50 hires, and $30k is his typical mishire cost.

```plaintext
Subject: {{number}} {{things}}

Saw {{companyName}} has {{number}} {{trigger}}.
{{your_product}} {{one_line_pitch}}.
{{before}} down to {{after}} at {{cost_each}} each: {{total}} saved.
Want me to run the numbers for {{companyName}}?
```

---

# Step 5: Build the sequence and check every email (days 11 to 14)

> The opener does 90% of the work.

## The 6 habits

1. Small lists > broad lists. In the 1M+ emails we went through in Instantly, 500 to 1,000 hyper-targeted prospects got 20-30% reply rates, against 2-3% on 100k blasts. Keep every list at 1,000 people or fewer, one play per list.

2. Hyper-enriched > standard data. Tech stack, funding, job posts, case studies and the LinkedIn headline travel with every list.

3. Personal openers > generic ones. "Saw you're hiring 3 AEs..." > "hope all's well at [Company]".

4. 3-step sequence > single email. E1 opener plus value, E2 a new angle, E3 the breakup, 3 to 5 days apart.

5. Value-first > ask-first. "Want me to send a quick example?" > "Do you have 15 minutes?"

6. Fundamentals > fancy tactics. ICP: who exactly. Offer: what outcome. Copy: how you say it.

Pro tip: layer LinkedIn touches between your emails.

---

## The sequence

Add three steps in Instantly, 4 days apart:

1. Email 1: the opener plus value, your framework email.

2. Email 2: a new angle, with a second offer or proof point.

3. Email 3: the breakup, three short lines: your last note, one last offer and a question about timing.

Leave the subject empty on steps 2 and 3 to keep one thread, and turn on Stop sending emails on reply in Options. Between emails, tier 1 gets LinkedIn touches by hand and tier 2 through Expandi: a connection request with no note after email 1, a like or comment on their post after email 2.

Email 2:

```plaintext
{{firstName}}, one more idea for {{companyName}}: {{second_offer}}.
{{customer}} used it to {{real_result}}.
Want me to send the details?
```

Email 3:

```plaintext
{{firstName}}, last note from me on this.
One more idea for {{companyName}}: {{third_offer}}.
Want me to check back in {{month}}?
```

---

# The 9 copy rules, as a checklist

1. One message = one idea. Name the email's point in five words, and cut the rest.

2. No copy saves a bad offer. The offer line alone has to earn the reply.

3. Stack offers in your follow-ups. Emails 2 and 3 each bring a new offer, like a case study or an audit.

4. Every line should be about them. One "We" or "I" sentence at most: the proof line.

5. The goal is a reply. Nothing more. End on a question they can answer in one word, like "Worth a look?".

6. The opener does 90% of the work. The first line alone carries the reason to reply.

7. Cut the fluff. They read on mobile. The email fits on one phone screen.

8. Lead with the offer. The trigger gets one line at most, and the offer is the first thing the reader can say yes to.

9. Reuse your list. Reframe the angle. Next month, run the same list with a new play and framework.

---

# The stack, from signal to send

> Almost every tool in your GTM stack is a login screen wrapped around an API that does the actual work.

The stack below runs from signal to send, with entry prices.

## Signal

- PredictLeads (intent signals): job openings, funding, technologies and news for 120M+ companies. 100 free API calls a month, then $0.04 a call ($40 minimum).

## Data

- GetLeads (lead sourcing): 478M+ contacts, plus play 1's post engagers. 1,000 free credits once, Unlimited at $497 a month.

- Apollo (lead sourcing): 240M contacts and 30M companies. Free with a 25-record selection limit, Basic at $49 per seat a month (annual).

- Prospeo (enrichment): verified emails and mobiles. $49 a month for 2,000 credits (1 per email, 10 per mobile).

- FullEnrich (enrichment): a mobile-first waterfall across 20+ data sources. From $29 a month for 500 credits.

- Explorium (enrichment): data on 150M+ companies and 800M+ people. From $29.99 for 500 credits.

## Send

- Hypertide (email infrastructure): $3.30 per Google inbox a month, or $25 a month per Microsoft (Entra) domain with 25 inboxes.

- Instantly (outreach): warmup, sequences, limits and the API behind the morning check. Growth at $47 a month, lead-check credits from $47 for 1,500.

- Expandi (outreach): the LinkedIn touches. $99 per LinkedIn seat a month.

## Automate

- n8n (AI agents): scheduled workflows, like a daily signal check. Free to self-host, cloud from €20 a month (annual).

- Vibe Prospecting (AI agents): builds lists from plain-English requests inside Claude or ChatGPT, on Explorium's data. 200 free credits a month.

- Claude Code and Codex (orchestration): the coding agents that run this playbook's prompts. Codex comes with ChatGPT plans.

- ColdIQ (orchestration): one API key in front of 40+ data providers, with an MCP server for Claude Code and Codex. I run it, and its API resells PredictLeads, Apollo, Prospeo and FullEnrich from this stack.

---

# The 15-day launch plan

- Day 1: order the inboxes from Hypertide, run Test domain setup, connect them to Instantly and switch on warmup.

- Days 2 to 5: set up Claude Code and folk, then map, score, research and tier the TAM.

- Days 6 to 10: pick a play per tier, pull each list, then write the offer line and two versions of email 1.

- Days 11 to 14: write emails 2 and 3, run the 9-rule check, load the campaign as a draft with the step 1 settings, and write tier 1 by hand.

- Day 14: the Health Score only covers warmup, so run an inbox placement test on your real email 1 (Instantly's Inbox Placement plan from $47 a month, GlockApps or MailReach). Hold back the inboxes it lands in spam.

- Day 15: set up and run the morning check from the next section, keep its flagged inboxes on warmup 7 more days, and start the rest at 10 emails a day, rising to 20 and then 30.

- Then: keep the email 1 version with the higher reply rate each week, and rerun the placement test monthly.

---

# From day 15: the 90-second morning check

> Every mailbox read in 90 seconds, and every sender ranked by bounce and reply rate.

We built this check in Claude Code as a skill, so one sentence runs the whole review, through Instantly's hosted MCP server and its full API (version 2).

Create an API key under Settings → Integrations → API Keys with the all:all scope, which covers the check and the fixes. Keep it private, and connect it the same way:

```plaintext
claude mcp add -t http -s user instantly https://mcp.instantly.ai/mcp -H "Authorization: Bearer YOUR_API_KEY"
```

Paste this into Claude Code once to save the skill:

```plaintext
Create a skill called deliverability-check in
.claude/skills/deliverability-check/SKILL.md that does this:
Read every Instantly email account: its Health Score, and its
sent, bounced and unique replies for the last 7 days.
Bounce rate = bounced ÷ sent.
Reply rate = unique replies ÷ new leads contacted.
Group the inboxes by domain and rank them:
highest bounce rate first, then lowest reply rate.
Status: flag = bounce rate of 3% or more, or Health Score under 90.
watch = Health Score of 90 to 99. ok = the rest.
Raise: yes = bounces under 2% and Health Score above 95.
Show me the table. Change nothing yet.
```

Every morning after that, type: run the deliverability check. A watch status means no change today.

---

# The bulk fixes: pause, re-warm, suppress, verify

My targets for every inbox are bounce under 3% and a Health Score of 99+. Every flagged inbox gets four fixes:

- Pause it, so it stops sending.

- Re-warm it: keep warmup on, untick it under the campaign's Options → Accounts to use for 14+ days, and bring it back at 10 a day at a Health Score above 90.

- Suppress its bounced addresses, so no campaign emails them again.

- Verify the leads still waiting in the campaign, and remove the invalid ones.

Claude Code runs all four through the same MCP, with your OK first:

```plaintext
For each flagged inbox: pause it, keep its warmup on,
and log it in rewarming.md with today's date.
Block every address that bounced in the last 7 days.
Verify the leads waiting in my active campaigns
and remove the invalid ones.
For each inbox in rewarming.md with 14+ days on warmup
and a Health Score above 90: resume it at 10 a day.
Show me every change before you make it.
```

Pausing an account can pause its warmup too, per Instantly's docs, so check the warmup column after each pause and switch warmup back on wherever it stopped. The full build is in [How to Stop Landing in Spam With AI Agents](https://x.com/MichLieben/status/2095919072907272404).

---

# Why this works

- One play per list makes the first line true for everyone on it. The whole list shares the fact your email opens on.

- Custom details lift replies. In Hunter's 2026 report on 31M emails, two custom attributes (merge fields filled per lead) got 56% more replies than none.

- Tracking off lifts them too. Hunter measured 68% more replies with tracking off, and Spamhaus tells filters to check every domain in a message, including the ones in links.

- Offer CTAs get more replies. In the 30 Minutes to President's Club, Gong and Outbound Squad report on 85M+ cold emails, offer CTAs lifted reply rates by 28% and meeting asks cut them by 44%. All-lowercase subject lines got 11% more opens than sentence case, which backs the lowercase half of Tal's rule.

- Follow-ups bring in replies. Instantly's 2026 benchmark credits them with 42% of all replies.

---

# What this changes

- Speed: the 14-day warmup happens once. Every later play goes out on inboxes that are already warm.

- Cost: about $357 a month plus domains: $63.50 to send, about $178 for data and $115 for the workflow. The placement test (from $47 a month) and tier 2's Expandi seat ($99 a month) come on top, as do Sales Navigator, GetLeads engager pulls and ads for the plays that use them.

- Labor: you handwrite for about 20 tier 1 accounts a month, and Claude Code writes the fields for the other 1,000 people.

- Distribution: each extra Hypertide inbox adds up to 30 sends a day for $3.30 a month, plus a domain for every third inbox, and Instantly Growth covers 7 inboxes at full speed.

- Revenue: the tiers come from accounts scored against your own closed-won deals, so pipeline lands in the segments that already pay you.

Order two domains and five inboxes today, and switch on the warmup. The first warmup emails go out after midnight UTC, and day 15 is two weeks from there.

ColdIQ, the unified API for GTM I run, puts the data from steps 2 and 3 behind one key for Claude Code and Codex. The first 300 credits are free on [coldiq.com](http://coldiq.com/).
