---
source_url: https://x.com/levikmunneke/status/2071370444285124950
ingested: 2026-07-01
sha256: 7d54d7c2abe270858893034d1651f6c70cce4d235a7529b5020560271c7404e4
---
---
title: "building a $3m ai sdr team"
source: "x-bookmarks"
tweet_id: "2071370444285124950"
tweet_url: "https://x.com/levikmunneke/status/2071370444285124950"
author_name: "Levi Munneke"
author_handle: "@levikmunneke"
tweet_date: "Sun Jun 28 23:09:32 +0000 2026"
bookmark_date: "2026-06-28"
content_type: "x_article"
character_count: 7590
retweet_count: 4
like_count: 99
---

# building a $3m ai sdr team

building a $3m ai sdr team

this is a build guide for a multichannel outbound system: eight linkedin accounts and their supporting email infrastructure, run by real low-cost reps, coordinated through one crm, with ai handling research and reply-drafting at each step.

---

want 500 free google maps leads? -> maps.hiivearts.com

---

the core idea worth understanding before you start: linkedin and email do different jobs.

linkedin is your warm, relationship-first channel, but it caps how much you can send. email has no real ceiling on volume, so it becomes your testing ground for what actually works. you run wide on email to find which industries, pains, and titles respond, then feed that signal into tighter linkedin targeting. email finds the signal, linkedin closes it. almost every decision in the build comes back to that split.

the rest of this breaks down each layer: the rep bench, the linkedin sequence, the email setup, the crm that ties them together, and where ai removes the bottlenecks.

the bench

the foundation is eight real linkedin accounts. the cheapest legitimate way to get them is to bring on reps from regions where the cost of labor is low, places like poland, romania, ukraine, colombia, or argentina, for roughly $100 a month each. the key word is real. these are aged, genuine profiles belonging to actual people, not burner accounts spun up last week. that distinction matters more than anything else in the build, because fresh fake profiles get flagged and restricted fast, and aged real ones don't.

(there are resellers that can help you with this)

connect a reseller sales navigator license to each account, around $30 to $60 a month, and each profile becomes a usable linkedin sending channel for about $150 all in. one account is just a person. eight running in parallel is a distribution engine, and the whole system is built on top of these as the base unit.

the linkedin layer

each account runs the same daily structure: a set of icp-targeted connection requests, a set of messages to existing connections moving through the sequence, and a set of inmails to reach open profiles outside the network. doing this by hand across eight accounts would be a full-time job, so you connect a tool like heyreach to each profile to run it. one sales nav search loads enough targeted leads to keep a profile busy for weeks.

the sequence itself should be short. the structure that works:

- day 1: blank connection request, no message

- day 2: first message after they connect, one-sentence offer plus a clear cta

- day 4: follow-up that doubles down on risk reversal

- day 6: follow-up that drops one real client result as proof

- day 10: final touch, "timing off?", left easy to reply to

resist the urge to make this longer. eight-step sequences and long messages don't lift reply rates, they just irritate more people and burn the account's standing. short, direct, and human wins because it reads like a person, not a campaign. this layer is your warm channel, so the goal is relationship and relevance, not volume.

the email layer

email is where volume lives, and where you do most of your learning. under each rep's name you build a small, clean email setup: a handful of domains, a few inboxes per domain, each inbox sending a conservative number of emails per day after a proper two to three week warmup. spread across eight reps, that adds up to a few thousand sends a day.

the thing to internalize is that email isn't just "more linkedin." it plays a different role. because you can send wide and get fast feedback, email is how you discover what your messaging should be. it answers the questions you can't afford to guess at: which industries reply, which pain points actually land, which titles convert. you run broad to surface that signal, then push it back into your linkedin targeting where the warmer channel can convert it. linkedin is precision; email is discovery.

the crm glue

this is where most teams fall apart, so build it before you scale sends. with eight reps working two channels, replies come in everywhere at once: someone responds on linkedin, someone else by email, and a third rep is mid-thread with a person another rep already contacted last week. without a single system, leads rot in the cracks and prospects get contacted twice by different people.

the fix is one source of truth. every interested lead, from any rep, on any channel, flows into one shared crm such as ghl or hubspot. it tracks who owns the relationship, which channel first contact happened on, what stage the lead is in, and what was said last.

then enforce one rule: the next touch always comes from wherever the prospect replied. if they answered on linkedin, the follow-up comes from that same rep's linkedin account. if they replied by email, it comes from that same inbox under the same name. to the prospect it feels like one person who remembers them. most companies break this constantly by switching reps and channels and losing context, and that continuity is most of what makes the system feel professional instead of spammy.

ai behind every rep

ai is what lets each rep punch above their cost. outbound usually fails in the follow-through, the dozens of small "remember to circle back with this person" moments that a human rep inevitably drops when they're running hundreds of conversations at once. ai never drops them.

at the top of the funnel, the system enriches each prospect before outreach goes out, pulling their linkedin and company data to generate a specific angle, so every first message is built on something real instead of a guess.

when a reply comes in, it drafts a researched, personalized response on its own. the messages read human because the sequencer sends them under the rep's name, but the research and drafting underneath are fully automated.

the bigger win is everything after a positive reply. a setter workflow, built in a self-hosted tool like n8n, owns the entire follow-through so nothing depends on a rep remembering. it listens for replies through a webhook, categorizes them by intent, and then runs every downstream stage itself:

- lead to booking follow-ups

- booking to show reminders

- 1st to 2nd call reminders

- OOO follow-ups

- "lets do it next month" follow-ups

positive replies then also get a response in under 90 seconds automatically, because a lead is warmest the second they reply. When a lead is worth a live call, the system pings a slack channel with their name and phone number so a rep can dial immediately, while intent is still fresh.

put together, the ai is the memory and reflexes of the whole team. That's what turns eight cheap reps into something that performs like a far more expensive, far more disciplined team.

putting it together

the build order is straightforward, and spreading it over a few weeks keeps it manageable:

week 1-2:

- buy the linkedin infrastructure (accounts, sales nav, heyreach) and the email infrastructure (domains, inboxes, sequencer)

- warm the inboxes and build your lead lists from sales nav and scraped sources

- write the sequences and launch the first campaigns

week 3-4:

- cut the losing a/b tests and start new ones

- repeat the test-and-iterate loop

by month two you have a full bench running across both channels.

the hard part is not the system. it's deciding to build it and then actually maintaining it onward.

-

if you want the scripts, list-building systems, infrastructure, and sops for running a system like this, or you'd rather have it built for you, let's talk. cal.com/leviwelch/30min
