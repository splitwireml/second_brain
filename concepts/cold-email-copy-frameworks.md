---
title: Cold Email Copy Frameworks
created: 2026-10-07
updated: 2026-10-07
type: concept
tags: [cold-email, copywriting, framework, templates, claude-code]
sources: [raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]
related_entity: [[michel-lieben]]
---

# Cold Email Copy Frameworks

Reusable copy-framework library and evidence-gated field generation: frameworks 1–3, exact author credits, skeletons, samples, templates and Campaign Ideas research prompt. All twelve are retained across this page and two linked detail pages; each number is a placeholder until supported by the sender’s own customer or a named source. The results.md/source/MISSING gate and complete/gap output files are literal source contracts. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

Michel Lieben’s October 6, 2026 course is preserved below as source material, not independently verified tool documentation, legal advice, pricing, platform policy or measured results. First-person statements belong to the author. Commands, prompts and templates are archival examples only: none were executed and no campaign was created. Only the source’s stated privacy, private-key, opt-out and approval constraints are retained. Linked destinations were not retrieved. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

## Source-preserved operational detail

# Step 4: Write email 1 with one of 12 frameworks (days 8 to 10)

> No copy saves a bad offer. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

That's rule 2 of my nine, so the offer comes first: one line at the top of a new doc for this campaign, saying what they get for replying, like a free audit of their last 3 campaigns with 3 fixes in 48 hours. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

Then pick one of the 12 frameworks from the top 1%: the skeleton your sentences follow, from the opener to the CTA (the question at the end). ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

How to use the 12: ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

1. Copy the template paired with your play into Instantly as email 1, ending with your signature, postal address and the step 1 opt-out line. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

2. Treat every number in the sample lines as a placeholder. The numbers you send come from your own customers or a source you can name. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

3. Add a second version of email 1, on another framework, as step 1's second variant. Instantly splits the list between them. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

For tiers 2 and 3, save the templates below as frameworks.md and your customer results as results.md, one per line: ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

```plaintext
customer | situation before | what changed | result | source
```
^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

Claude Code fills the fields, here for the Hiring Surge list: ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

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
^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

Upload hiring_surge_email1.csv with Verify leads ticked, map each column to its field, and rerun research on the gaps file on day 10. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

---

## 1. AIDA (Monika Grycz's version)

Skeleton: attention → interest → desire → action ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

Sample line: "Too many no-show demos this week? Teams like {{company}} cut them by 37% in 30 days." ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

Best for: a customer result that answers a pain they feel this week. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

```plaintext
Subject: {{pain_in_two_words}}

{{pain_question}} at {{companyName}} this week?
{{customer}} had the same problem with {{their_old_way}}.
They cut it by {{real_result}} in {{real_timeframe}}.
Worth a look at how they did it?
```
^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

---

## 2. 3 Campaign Ideas (Dujam Dunato's version)

Skeleton: engagement hook → 3 AI ideas → imagine at scale → worth it? ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

Sample line: "Our AI analyzed {{company}} and came up with 3 campaign ideas you could implement." ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

Best for: the Campaign Ideas play. It's built on Eric Nowoslawski's "Creative Ideas" campaign. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

Get the ideas first: ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

```plaintext
Read {{company_website}}: the homepage, pricing page and case studies.
Write 3 outbound campaign ideas for {{companyName}}, each naming
who to target, the reason to reach out and the email's first line.
Tie every idea to one quoted detail from their site.
Use results from my case studies only, with the customer named.
```
^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

Then the email: ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

```plaintext
Subject: 3 ideas for {{companyName}}

Our AI analyzed {{companyName}} and came up with 3 campaign ideas for you:

1. {{idea_1}}
2. {{idea_2}}
3. {{idea_3}}

Imagine a new set like this for every account on your list, every month.

Worth it?
```
^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

---

## 3. Right Person?

Skeleton: right person? → recap and proof → 2 benefits → point me ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

Sample line: "Are you the right person to speak with about {{problem}}?" ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

Best for: a company that fits, with no clear owner of the problem. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

```plaintext
Subject: right person?

Hi {{firstName}}, are you the right person to speak with about {{problem}} at {{companyName}}?

We help {{type_of_company}} {{outcome}}. {{customer}} {{real_result}}.

Two things teams get from it:
- {{benefit_1}}
- {{benefit_2}}

Who on your team owns this? Happy to be pointed their way.
```
^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

---

## Related

- [[cold-email]]
- [[cold-email-campaign-plays]]
- [[cold-email-automation]]
- [[cold-email-copy-frameworks-pain-and-team]]
- [[cold-email-copy-frameworks-trigger-and-offer]]
