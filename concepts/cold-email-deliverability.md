---
title: Cold Email Deliverability
created: 2026-10-07
updated: 2026-10-07
type: concept
tags: [cold-email, infrastructure, configuration, workflow, mcp]
sources: [raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]
related_entity: [[michel-lieben]]
---

# Cold Email Deliverability

Infrastructure, DNS, warmup, launch/placement gates, ramp limits, read-only morning review and approval-gated remediation for cold email. This source separates warmup Health Score from actual-message inbox placement; watch status does not authorize changes. Day 15’s extra seven warmup days and the later 14+ day remediation rule are retained as distinct source instructions, not silently reconciled. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

Michel Lieben’s October 6, 2026 course is preserved below as source material, not independently verified tool documentation, legal advice, pricing, platform policy or measured results. First-person statements belong to the author. Commands, prompts and templates are archival examples only: none were executed and no campaign was created. Only the source’s stated privacy, private-key, opt-out and approval constraints are retained. Linked destinations were not retrieved. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

## Source-preserved operational detail

# Step 1: Stay out of spam (day 1)

> 100 emails an hour from one inbox lands in spam. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

That's the warning box on my cheat sheet. Every other step depends on staying far below it. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

## Part 1: the mailboxes

My rule: tenant isolated, live in hours. We order ours from Hypertide. It takes the domains, the mailbox names and your stack (Google or Microsoft), then buys the domains, writes the DNS records and creates the mailboxes, typically within 4 to 6 hours. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

- Google inboxes carry the second half of that rule: live in hours, with no tenant isolation, at $3.30 each a month. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

- Microsoft (Entra) inboxes carry both halves: one isolated tenant per domain, with its own sending quota, so a suspension stays inside it. Sends still share Microsoft's IP ranges. At $25 a month for 25 inboxes, they're the step up for volume. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

Then plan the domains (the math is for Google inboxes): ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

1. Keep your main domain out of cold email. Everyday email stays on yourbrand.com. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

2. Use multiple new domains that read like your brand, like getyourbrand.com, each one its own domain. Google counts a subdomain like mail.yourbrand.com toward the main domain's volume. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

3. Plan 3 inboxes per domain, named after you and your teammates (Instantly's guidance is 3 to 5 at most). ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

4. Forward each new domain to your website at its registrar. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

5. Start with 150 emails a day: 5 inboxes on 2 domains. The math, for any other volume: ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

```plaintext
inboxes = emails per day ÷ 30, rounded up
domains = inboxes ÷ 3, rounded up
```
^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

Five inboxes fit Instantly's Growth plan: $47 a month for 1,000 uploaded contacts and 5,000 emails. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

Check the DNS. Hypertide publishes the records. Then run Instantly's Test domain setup on every domain and confirm MX, SPF, DKIM and DMARC all pass. Together they route your replies and prove your emails really come from your domain. Keep one DMARC record per domain, because two on the same domain cancel each other out. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

---

## Part 2: the warmup

My rule: 2 weeks of warmup before the first send, Instantly's own minimum. Warmup trades emails between real inboxes, so a new inbox builds a normal history. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

1. Connect every inbox to Instantly. Hypertide can upload its Google inboxes straight in. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

2. Switch warmup on at Instantly's recommended settings: increase per day 1, daily warmup limit 10, reply rate 30%. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

3. Send no cold email from these inboxes for 14 days. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

4. Read the Health Score on day 14: the share of warmup emails that landed in the inbox over the last 7 days. Instantly rates above 90% as good, our launch gate. My running target is 99+. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

5. Keep warmup on for good. Instantly advises never switching it off, and warmup emails don't count against your campaign limit. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

---

## Part 3: the settings (in the campaign, days 11 to 14)

My rule: tracking off, plain text, ESP match. Instantly's deliverability guide recommends a plain-text first email with no links and no open tracking, plus provider matching. Link tracking off on every step is our call. In each campaign's Options tab: ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

- Open and link tracking: off. Open tracking hides a remote image in each email, and link tracking routes links through a shared tracking domain. Duplicated campaigns keep the old setting, so check each new one. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

- Plain text: Delivery optimization → Send emails as text-only (no HTML), with no links in email 1. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

- ESP match (email service provider): Advanced Options → Provider Matching pairs Google inboxes with Google users and Outlook inboxes with Outlook users. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

- An opt-out in every email: a last line like "Reply stop and I won't email you again", your postal address in the signature, and every stop reply on Instantly's block list the same day. Instantly's guide calls an opt-out a legal requirement under laws like CAN-SPAM and GDPR. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

---

## Part 4: the daily limits and the lists (from day 15)

- 30 emails per inbox per day, at most. Each inbox sends 10 a day in its first week of sending, 20 in its second and 30 from its third. Each Monday, check two numbers before you raise an inbox's Daily Campaign limit: bounces under 2% and a Health Score above 95. Set the campaign's Daily Limit to inboxes × the per-inbox limit, and keep Instantly's default gap (9 minutes plus a random delay) to hold each inbox far below 100 an hour. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

- Clean, validated lists. Tick Verify leads on upload (0.25 Instantly credits per lead, a separate plan), keep the default that skips invalid and risky addresses, and put catch-alls (domains that accept every email, so no checker can confirm the person) in their own small list. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

- Bounces under 3%. A bounce is an email returned because the address doesn't exist. 3% is my ceiling and the morning check's flag. Instantly's High Bounce Auto-Pause, on by default, stops a campaign at 5% bounces after its first 200 emails. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

Five inboxes send 150 a day from week three: about 3,300 a month over 22 weekdays, enough for 1,000 people through all 3 emails. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

---

# The 15-day launch plan

- Day 1: order the inboxes from Hypertide, run Test domain setup, connect them to Instantly and switch on warmup. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

- Days 2 to 5: set up Claude Code and folk, then map, score, research and tier the TAM. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

- Days 6 to 10: pick a play per tier, pull each list, then write the offer line and two versions of email 1. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

- Days 11 to 14: write emails 2 and 3, run the 9-rule check, load the campaign as a draft with the step 1 settings, and write tier 1 by hand. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

- Day 14: the Health Score only covers warmup, so run an inbox placement test on your real email 1 (Instantly's Inbox Placement plan from $47 a month, GlockApps or MailReach). Hold back the inboxes it lands in spam. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

- Day 15: set up and run the morning check from the next section, keep its flagged inboxes on warmup 7 more days, and start the rest at 10 emails a day, rising to 20 and then 30. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

- Then: keep the email 1 version with the higher reply rate each week, and rerun the placement test monthly. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

---

# From day 15: the 90-second morning check

> Every mailbox read in 90 seconds, and every sender ranked by bounce and reply rate. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

We built this check in Claude Code as a skill, so one sentence runs the whole review, through Instantly's hosted MCP server and its full API (version 2). ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

Create an API key under Settings → Integrations → API Keys with the all:all scope, which covers the check and the fixes. Keep it private, and connect it the same way: ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

```plaintext
claude mcp add -t http -s user instantly https://mcp.instantly.ai/mcp -H "Authorization: Bearer YOUR_API_KEY"
```
^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

Paste this into Claude Code once to save the skill: ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

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
^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

Every morning after that, type: run the deliverability check. A watch status means no change today. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

---

# The bulk fixes: pause, re-warm, suppress, verify

My targets for every inbox are bounce under 3% and a Health Score of 99+. Every flagged inbox gets four fixes: ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

- Pause it, so it stops sending. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

- Re-warm it: keep warmup on, untick it under the campaign's Options → Accounts to use for 14+ days, and bring it back at 10 a day at a Health Score above 90. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

- Suppress its bounced addresses, so no campaign emails them again. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

- Verify the leads still waiting in the campaign, and remove the invalid ones. ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

Claude Code runs all four through the same MCP, with your OK first: ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

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
^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

Pausing an account can pause its warmup too, per Instantly's docs, so check the warmup column after each pause and switch warmup back on wherever it stopped. The full build is in [How to Stop Landing in Spam With AI Agents](https://x.com/MichLieben/status/2095919072907272404). ^[raw/articles/xarticle-how-to-book-meetings-with-cold-email-in-2026-full--2107499997906514147.md]

## Related

- [[cold-email]]
- [[cold-email-automation]]
- [[api-led-gtm]]
- [[michel-lieben]]
