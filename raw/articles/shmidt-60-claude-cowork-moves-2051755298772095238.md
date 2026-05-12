---
tweet_id: "2051755298772095238"
tweet_url: "https://x.com/shmidtqq/status/2051755298772095238"
author_handle: "@shmidtqq"
author_name: "shmidt"
published_date: "Tue May 05 20:05:57 +0000 2026"
likes: 178
retweets: 13
replies: 24
source: "x.com/shmidtqq/status/2051755298772095238"
type: "article"
title: "The 60 Claude Cowork Moves That Replaced Half My Job (Most Users Know 6)"
tags:
  - ai
  - automation
  - claude
  - productivity
  - workflows
---

# The 60 Claude Cowork Moves That Replaced Half My Job (Most Users Know 6)

I open Cowork before I open my email.

That sentence used to sound insane. After four months of running every workday through it, it's the most honest description of how I actually operate now.

Here's what nobody tells new users: Cowork has six layers, and most people never scratch past the first one.

- Slash commands
- Custom skills
- Scheduled tasks
- Connector chains
- Sub-agent patterns
- The .claude/ folder convention

Each layer alone is useful. Stack them, and Cowork stops being "an AI tool I open sometimes" and starts running the boring 70% of your work in the background while you do the part only you can do.

---

## If you only read 3 things, read these

Most readers will scroll. Fine. At minimum, learn these three. Highest leverage in the entire piece.

- **#8 - /cost**: the command that prevents you from torching your token budget on Wednesday.
- **#31 - The custom skills folder**: the single hidden feature that turns Cowork from chatbot into your personal AI.
- **#46 - Daily 7am inbox automation**: pays for the entire $20/month plan in week one.

If you do nothing else from this article, do those.

---

## Part 1. Slash Commands Hiding in Plain Sight (1–12)

> **1. /schedule - Beginner.**
> The single most underused feature on the platform. Type /schedule, describe a task, set the cadence. It runs in the background, even with your laptop closed on Max, or while Cowork is open on Pro. Your 7am triage. Your Friday status report. Your Sunday calendar prep. Set once, forget forever.
> `/schedule> Every weekday 7:30am: triage Gmail, summarize calendar, save to /Daily/[date].md`

> **2. /loop - Beginner.**
> The lighter cousin of /schedule. Polls something at an interval inside your current session and stops when the session ends. "Every 3 minutes, check if the deploy log shows green and tell me." No more babysitting builds.

> **3. /plan - Beginner.**
> Forces Cowork to write a step-by-step plan before touching anything. Review. Approve. Then execute. The cost of typing /plan is 3 seconds. The cost of skipping it on a complex task is sometimes a corrupted folder. Always /plan if a task touches more than 3 files.

> **4. /compact - Beginner.**
> Compresses a long conversation while keeping the meaningful parts. Saves 40–60% of your context window. Run it before Claude starts repeating mistakes, not after.

> **5. /clear - Beginner.**
> Nuclear reset. Wipes the thread. Use when context is so polluted Claude is fighting you. Don't get sentimental about a long thread, start clean.

> **6. /resume - Intermediate.**
> Pick up exactly where you left a previous conversation. Pair with /rename so you can find it later by something other than "New chat 47."

> **7. /rename - Intermediate.**
> Auto-renames the current thread based on its content. Without this, your sidebar fills with identical "New chat" entries. With it, your sidebar becomes a searchable index of your work.

> **8. /cost - Intermediate.**
> Shows estimated token cost before you run a task. On Pro, this is the difference between finishing your week and burning out by Wednesday. If a task shows 3× normal cost, scope it down before you press go.

> **9. /memory - Intermediate.**
> Shows which memory files and context Claude has loaded. The first thing to check when Claude is acting weird. If the context you assumed was loaded isn't there, congratulations, you found your bug.

> **10. /doctor - Intermediate.**
> Diagnostic command. Lists connected apps, loaded skills, available commands, current permissions. Faster than asking on Reddit.

> **11. /voice - Pro.**
> Push-to-talk dictation directly into the Cowork input. Hold Space, talk, release. Mix typing and voice in the same prompt. Once you try it, you stop typing long prompts forever.

> **12. /agents - Pro.**
> Spawns a project-specific sub-agent that lives inside your repo or folder. Build a "test writer" agent that knows your testing conventions, or a "PR reviewer" agent that knows your team's style. Cowork uses them automatically when relevant.

---

## Part 2. Custom Skills That Replace Entire Workflows (13–24)

Skills are reusable mini-programs Cowork loads automatically when relevant. Drop a SKILL.md into your /skills folder and Claude uses it whenever the request matches. Smart loading means skills don't eat your context window.

The Claude Skills marketplace now hosts 2,300+ free skills. Most users have installed zero. The opportunity gap is enormous.

> **13. Brand voice skill - Beginner.**
> Drop 5–10 of your best articles into /skills/brand-voice/examples. Add a SKILL.md saying "match the tone of these examples." Now every writing task sounds like you, not Claude. Single highest-leverage skill for anyone who writes online.

> **14. Email triage skill - Beginner.**
> Encodes your personal triage rules: what's urgent, what gets a one-liner, what gets archived without reading. Every email task uses your judgment, not Claude's defaults.

> **15. Meeting transcript skill - Beginner.**
> Takes any raw transcript and outputs structured notes: decisions made, action items with owners and deadlines, open questions, follow-ups. Auto-triggers when you upload a transcript.

> **16. PDF report generator skill - Beginner.**
> Generates branded PDF reports from markdown, title page, table of contents, footer. Pair with your brand-voice skill and every report looks like your team produced it.

> **17. Code review skill - Intermediate.**
> Encodes your team's standards, naming conventions, and common review comments. Every PR review uses it automatically. Replaces the senior engineer's monthly "remember our style guide" reminder.

> **18. Customer support response skill - Intermediate.**
> Trained on your past Zendesk or Intercom replies. Drafts every new response in your team's voice with your team's solutions. Saves the average support agent 4+ hours per week.

> **19. Proposal generator skill - Intermediate.**
> Reads a client brief and your proposal template. Generates a customized proposal in your tone, with your pricing logic. Train on 3 winning proposals, every new proposal takes 10 minutes instead of 3 hours.

> **20. Investor update skill - Pro.**
> Encodes your KPIs, your narrative arc, your structure. Every monthly update follows the same logic. Pull metrics, format the update, attach the right context. 2-hour task becomes 15 minutes.

> **21. Contract review skill - Pro.**
> Reads any contract PDF and flags key terms, deadlines, auto-renewals, liability caps, unusual clauses. Not legal advice, a first-pass review that saves 1–2 hours per contract before it goes to your lawyer.

> **22. Hiring screen skill - Pro.**
> Reads any resume against your role description and outputs a structured assessment: strengths, gaps, red flags, suggested interview questions. Replaces the hour you spent on each first-pass screen.

> **23. Stakeholder communication skill - Elite.**
> One skill, four output formats: 50-word for the CEO, 200-word for your manager, 500-word technical for engineering, public-facing for the blog. Every announcement gets all four versions in one prompt.

> **24. Pricing skill - Elite.**
> Reads any product description, generates 3 pricing tiers with rationale, anchored to comparable products. Used by SaaS founders to price-test before launch.

---

## Part 3. File System Power Moves (25–33)

> **25. Screenshot library organizer - Beginner.**
> "Read every screenshot in /Screenshots. OCR each one. Detect what it is - code error, chart, UI design, meeting slide. Move into the matching subfolder. Add a description as the filename." 800 screenshots become a searchable archive in 5 minutes.

> **26. Smart attachment processor - Beginner.**
> "Look in /Attachments. Group emails by sender, contracts into /Legal, invoices into /Finance/[year]/[month], everything else into /Misc. Rename invoices with vendor + amount + date." Inbox attachments stop being a black hole.

> **27. Code repo cleanup - Intermediate.**
> "Read all my project repos in /Code. Identify dead branches, unused dependencies, abandoned experiments older than 90 days. Move abandoned repos to /Code/archive. Generate a cleanup report." Reclaims tens of GB and zero mental load.

> **28. PDF metadata extractor - Intermediate.**
> "For every PDF in /Research, extract title, authors, publication date, abstract, key findings. Save as a CSV index. When I ask for research on [topic], use this index first." 200-PDF dump becomes an instantly searchable knowledge base.

> **29. Photo library curator - Intermediate.**
> "Look at every photo taken this year in /Photos. Find blurry duplicates and near-duplicates. Identify the best version of each shot using sharpness and composition heuristics. Move the rest to /Photos/cull-review for final approval." Replaces the 4 hours of manual culling.

> **30. Voice note → article pipeline - Pro.**
> "Read all transcripts in /Voice-Notes from this week. For each, draft a 1,500-word article in my brand voice. Keep my natural cadence but cut rambling and add structure. Save publication-ready drafts to /Drafts." A solo content shop, fully voice-driven.

> **31. Custom skill folder setup - Pro.**
> Create ~/skills with a subfolder for each skill: brand-voice/, email-triage/, pdf-report/, etc. Each subfolder has a SKILL.md describing when and how Claude should use it. Cowork auto-discovers and uses them whenever the request matches.
> This single setup turns Cowork from chat app into your personal AI. The most underrated configuration on the platform.
> ```
> ~/skills/brand-voice/SKILL.md
> ~/skills/email-triage/SKILL.md
> ~/skills/pdf-report/SKILL.md
> ~/skills/proposal/SKILL.md
> ```

> **32. Git history miner - Pro.**
> "Read the last 90 days of git history across all my projects. Identify which features I shipped, which bugs I fixed, what skills I used most. Generate a quarterly engineering self-review I can paste into my performance doc." Annual review writes itself.

> **33. Backup audit with intelligence - Elite.**
> "Compare /Documents to my last backup. Show which files changed, which are new, which were deleted. Flag any deletion of files modified in the last 30 days as suspicious. Estimate full backup time given current size." Backup hygiene without thinking about it.

---

## Part 4. Connector Workflows That Replace Real Jobs (34–45)

> **34. Calendar conflict resolver - Beginner.**
> "Look at my Google Calendar for next week. Identify meeting conflicts, back-to-back meetings with no buffer, and meetings I should probably decline based on relevance. Suggest reschedules with proposed alternative times." Replaces 30 minutes of Sunday calendar Tetris.

> **35. Slack thread → executive brief - Beginner.**
> "Read this Slack thread. Identify the decision being debated, each participant's position, the emerging consensus, and the open questions. Output a 1-paragraph brief I can forward to my boss." Long threads become decisions in seconds.

> **36. Gmail → CRM logger - Intermediate.**
> "Scan my Gmail for emails to or from any contact in our HubSpot CRM. Log each as an activity against the matching contact record. Include subject, snippet, timestamp. Skip anything already logged." Sales rep activity logging on autopilot.

> **37. Drive → data warehouse pipeline - Intermediate.**
> "Read every Google Sheet in /Drive/Reports. For each, infer the schema, normalize column names, append data to the matching BigQuery table. Note any sheets that don't match an existing table." Replaces the data engineer's ETL ticket queue.

> **38. Notion → Linear ticket pipeline - Intermediate.**
> "Read this Notion PRD. Generate Linear tickets for each requirement. Group by component, assign by team based on our team-component mapping, add to current sprint. Output a summary." Specs become work in 90 seconds.

> **39. Multi-source weekly status report - Pro.**
> "Pull this week's sales numbers from Salesforce. Product metrics from Mixpanel. Customer feedback from Intercom. Team activity from GitHub. Combine into a 1-page weekly status report. Save as PDF." Replaces a full-time RevOps coordinator.

> **40. Cross-platform context retrieval - Pro.**
> "I'm about to start a meeting with [client]. Pull all context: recent emails, related Drive docs, Slack mentions, open Linear tickets they care about, last call notes. Compile a 1-page meeting prep doc." Walk in fully briefed every time.

> **41. Salesforce pipeline hygiene - Pro.**
> "Query opportunities in Salesforce. If stage is Proposal Sent and last activity was 14+ days ago with no response logged, move to Needs Review. Show preview of all changes before executing." 3 hours of manual cleanup → 8 minutes.

> **42. GitHub PR auto-review - Pro.**
> "Watch our GitHub repo. When a new PR opens, run our code-review skill against it. Post structured review comments. Approve if it passes our checklist. Tag a senior engineer if it fails." First-pass review, automated.

> **43. Stripe → bookkeeping reconciliation - Elite.**
> "Pull all Stripe transactions from last month. Match each to an invoice in our Google Sheet. Flag mismatches: payments without invoices, invoices without payments. Update bookkeeping sheet with reconciliation status." Replaces a part-time bookkeeper.

> **44. Customer churn early warning - Elite.**
> "Cross-reference Intercom support tickets, Mixpanel usage data, Stripe payment history. Identify accounts showing 3+ churn signals (declining usage, support friction, payment delays). Output a list ranked by ARR at risk." A retention team in one prompt.

> **45. Investor pipeline tracker - Elite.**
> "Read every email I've exchanged with investors in the last 6 months. Categorize each conversation by stage: cold intro, first meeting, second meeting, due diligence, term sheet, closed, passed. Identify investors gone quiet for 21+ days and draft a follow-up. Output a CRM-style pipeline view." Replaces a fundraising-ops hire.

---

## Part 5. Automations That Run While You Sleep (46–53)

> **46. Daily 7am inbox processor - Beginner.**
> Schedule daily 7am: "Triage Gmail. Categorize unread. Draft responses for routine emails. Flag urgent ones. Save the summary to /Daily/inbox-[date].md." Wake up to a triaged inbox every day. The first automation everyone should set up.

> **47. Sunday week-ahead brief - Beginner.**
> Schedule Sunday 6pm: "Pull next week's calendar. For every meeting, attach the relevant prep docs from Drive. Flag any meeting where I have no context yet. Generate a 1-page weekly brief with priorities, prep gaps, outstanding action items." Walk into Monday already informed.

> **48. Daily metric snapshot - Intermediate.**
> Schedule daily 8am: "Pull yesterday's key metrics from Mixpanel, Stripe, our database. Calculate WoW and MoM deltas. Flag anything outside expected ranges. Save to /Metrics/[date].md and post a summary to #metrics." Replaces the daily metrics standup.

> **49. Weekly content recycler - Intermediate.**
> Schedule Friday 5pm: "Read every article I published this week. Generate 8 standalone tweets, 2 LinkedIn posts, 3 short-form video scripts, and 1 newsletter teaser per article. Save to /Content/recycled/[week]." One article → 14 distribution assets, automatically.

> **50. Monthly competitor scan - Pro.**
> Schedule first of every month: "Search news, ProductHunt, Crunchbase, X for updates on [3 named competitors]. Track pricing changes, product launches, hiring, funding. Compare to last month. Output a competitive landscape brief." Strategic intelligence on autopilot.

> **51. Quarterly OKR self-review - Pro.**
> Schedule first day of each quarter: "Read all Q[X] OKRs. Pull progress data from Notion, Linear, Drive. For each OKR, calculate completion percentage, identify blockers, recommend Q[X+1] adjustments." Replaces the consultant.

> **52. Annual highlights compiler - Elite.**
> Schedule December 28: "Read every weekly status doc, every quarterly review, every shipped feature from the year. Identify the 10 highest-impact moves I made. Generate a year-end wrap I can use for performance review, social posts, and personal reflection." Year ends with the highlight reel already done.

> **53. Birthday & relationship maintenance - Elite.**
> Schedule weekly Sunday 4pm: "Look up everyone in my contacts whose birthday or work anniversary falls in the next 14 days. Draft a personal message for each based on our last conversation. Save to /Relationships/[week].md for me to review and send." The hardest soft skill, automated.

---

## Part 6. Pro Patterns Most People Don't Know Exist (54–60)

> **54. Sub-agent parallelization - Pro.**
> Spawn sub-agents for any task that would pollute your main thread. "Run 3 sub-agents in parallel: one researches competitor pricing, one drafts the strategy memo, one prepares the slide outline. Return only the final outputs to me." Massive parallel work, clean main context.

> **55. Connector chains for compound output - Pro.**
> Chain multiple connectors in one command. "Read the latest email from [client]. Search Drive for related contracts. Check Slack for any team discussion of them. Pull their open Linear tickets. Compile a complete client status doc." 4 tools, 1 prompt, 1 deliverable.

> **56. Skill stacking for compounding leverage - Pro.**
> Combine multiple skills in a single task. "Use the brand-voice skill plus the email-triage skill plus the meeting-notes skill to draft a follow-up email to yesterday's call." Skills compose like Lego. Stack 3 and you have a function nobody else has built.

> **57. Plan mode for token discipline - Pro.**
> Always /plan before tasks on Pro. The plan output shows you the full token budget upfront. Adjust scope before execution. The single move that saves the most token allocation each week.

> **58. The .claude/ folder convention - Elite.**
> Every serious Cowork user keeps a .claude/ folder in each project. Inside: commands/, skills/, agents/, CLAUDE.md (project context). When you open Cowork in this project, all of it loads automatically.
> Your .claude/ folder is your real resume now. Hiring managers in 2026 will check it before checking your LinkedIn.

> **59. Off-peak scheduling for 2× throughput - Elite.**
> Anthropic doubled off-peak usage limits in March 2026. Schedule heavy automations for evenings and weekends. You get 2× throughput on the same plan. Most users don't know this and waste their best automations on peak hours.

> **60. Persistent Dispatch threads across devices - Elite.**
> Cowork Dispatch keeps a persistent thread that survives across devices. Start a task on your laptop. Pick it up on your phone during your commute. Finish it on your tablet at home. The thread retains all context, all memory, all skill state. The closest thing to a real personal AI yet built.

---

## 5 Pro Tips That Multiply Everything Above

1. Treat Cowork like a junior employee, not a search box. Junior employees need context, examples, and clear acceptance criteria. So does Cowork. The 30 seconds you spend setting context save the 5 minutes of bad output you'd otherwise correct.

2. Build your skill library in the first month, not as you go. Spending 4 hours on day 1 setting up 5-8 personal skills returns hundreds of hours over the next year. Most people build skills only when they're already overloaded. Do it before.

3. /plan is free insurance. The cost of typing /plan is 3 seconds. The cost of skipping it on a complex task is sometimes a corrupted folder, a deleted file, or a wasted day. Type /plan.

4. Schedule the boring stuff first. Your 7am inbox triage. Your Friday status report. Your Sunday week-ahead brief. These aren't glamorous. They are the foundation. Once they run automatically, you have hours each week back.

5. The .claude/ folder is your new resume. Every serious project should have one. Hiring managers in 2026 already check for it. Your Cowork setup signals how you work better than any LinkedIn bio.

---

## Where to Start Based on Your Level

- **Beginner (this week)**: Pick 5 commands from Section 1. Use them daily until they're automatic.
- **Intermediate (next 3 weeks)**: Set up your /skills folder. Build 3 custom skills for your most repeated tasks. Schedule the daily 7am inbox processor and the Sunday week-ahead brief.
- **Pro (month 2)**: Set up connector chains. Run weekly automations across multiple tools. Use /agents to specialize Cowork per project. Track your token budget with /cost.
- **Elite (month 3+)**: Build the .claude/ folder convention into every project. Use Dispatch for persistent threads. Schedule heavy work off-peak. Stack skills for compound output.

---

60 commands, skills, and workflows. Tested daily for 4 months. Most users know maybe 8 of them.

Cowork is not a chatbot with file access. It's an autonomous operating system. The people who win in 2026 are the ones who treat it that way.

Save this list. Bookmark the 3 you'll try this week. Come back when you've learned them. There are 57 more waiting.

I post stuff like this every week. Real workflows, real numbers, real results from daily use. No fluff.

Follow if you want the next one.

Also don't forget about my TG channel: https://t.me/+JmDeelv5UCwwMTcy
