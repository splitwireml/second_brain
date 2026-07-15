---
source_url: https://x.com/Jacobsklug/status/2076880438677946396
ingested: 2026-07-15
sha256: 20f4a2c0ac1a38793443ffbc68b8238d092a9e1328e731e0490ae8f404fd0b8e
tweet_id: "2076880438677946396"
tweet_url: https://x.com/Jacobsklug/status/2076880438677946396
source_file: "/Users/mali/Development/x-bookmarks/data/run-2026-07-14/2026-07-14/xarticle-the-engineering-loop-that-powers-1-of-builders-2076880438677946396.md"
run: run-2026-07-14
---

---
title: "The Engineering Loop That Powers 1% Of Builders"
source: "x-bookmarks"
tweet_id: "2076880438677946396"
tweet_url: "https://x.com/Jacobsklug/status/2076880438677946396"
author_name: "Jacob Klug"
author_handle: "@Jacobsklug"
tweet_date: "Tue Jul 14 04:04:17 +0000 2026"
bookmark_date: "2026-07-14"
content_type: "x_article"
character_count: 13928
retweet_count: 5
like_count: 15
external_urls:
  - "https://jacobklug.com/lm/autonomous-coding-loop?utm_source=X"
  - "https://jacobklug.com/lm/autonomous-coding-loop)"
---

# The Engineering Loop That Powers 1% Of Builders

The Engineering Loop That Powers 1% Of Builders

The top 1% of AI engineers stopped prompting one message at a time.

They build loops instead. Loops that write code, test it, catch their own mistakes, and fix them on repeat until the app is actually done. No one sitting at the keyboard. No one babysitting the output.

In the build this is based on, two of these loops built a full Asana clone from a single spec doc. Project views, list views, Kanban with drag and drop, subtasks, assignees, due dates. One of them deployed to a live URL without a single manual prompt after kickoff.

The total cost to run both loops start to finish was under $10.

This is the full system. How to write a spec that defines "done," build an orchestrator with phases and exit criteria, add a verifier that catches the builder's mistakes, run loops in parallel, and track everything with a live feature spreadsheet. Two ways to run it: Lovable for the non-technical route, Claude Code for the native route.

The core shift is the whole thing. You stop being the person typing prompts. You become the person who designs the loop. The loop does the typing.

## Why Loops Beat Prompting

Prompting is you and the model taking turns. You ask, it answers, you check, you ask again. You are the bottleneck. The work stops the second you stop typing.

A loop removes you from the middle. You define what "done" looks like once, then the system builds, tests against that definition, finds what is broken, fixes it, and tests again. It keeps cycling until every item passes.

The difference in output is not 20% better. It is the difference between shipping one feature in an afternoon and shipping a whole working app while you are asleep.

> A prompt gets you one answer. A loop gets you a finished product. Design the loop once and it runs without you.

## The Five Pieces of Every Loop

Every autonomous coding loop, whether you run it in Lovable or Claude Code, is built from the same five pieces. Get these right and the loop runs clean. Skip one and it drifts.

1. The Spec. A document that defines every feature and, for each one, what "done" means. This is the contract. The loop measures itself against this and nothing else.

2. The Orchestrator. The set of phases the loop moves through, with exit criteria for each phase. Build, then test, then fix. It does not move to the next phase until the current one is satisfied.

3. The Verifier. A checking step, or a separate agent, that tests the builder's work against the spec and logs every error. This is what catches the mistakes the builder makes on its own.

4. The Tracker. A single live spreadsheet or list of every feature and user story with a status column. The loop updates it as it goes so you can see exactly what passed, what failed, and what got fixed.

5. Parallel Runs. Once the pattern works, you run multiple loops at once so the work never sits idle.

> Spec, orchestrator, verifier, tracker, parallel. Same five pieces every time. The tool changes, the anatomy does not.

## Step 1: Write the Spec That Defines "Done"

The spec is where the whole thing lives or dies. A vague spec produces a vague app. A spec with clear "done" criteria produces a loop that knows exactly when to stop.

You do not write this by hand. Get Claude to draft it for you.

In the build, the spec was for an Asana clone: project views, list views, Kanban views. Simple app, but it is the perfect size to see how the loop works.

How to generate your spec:

- Tell Claude the app you want and ask it to write a full spec doc

- Have it list every feature as a discrete item

- Have it break features into user stories ("as a user I can create a project and change its color")

- For each feature and story, have it define the "done" condition, the expected behavior when it works

- Export the whole thing as a plain text document you can feed into your build tool

The magic line to include: for every feature, write down what determines it being "done." That single addition is what turns a feature list into a testable contract.

> "Done" is not "it exists." Done is "here is the exact behavior that proves it works." Write that for every feature or the loop has nothing to test against.

## Step 2: Build the Orchestrator (Phases and Exit Criteria)

The orchestrator is the prompt that tells the loop how to move. It runs in phases, and each phase has an exit condition that must be met before the next one starts.

The structure is always the same three-phase cycle:

Phase 1: Build. Read the spec. Go over every single feature. Define the expected behavior based on the actual code. Build each feature. Log each one in the tracker.

Phase 2: Test. Once building is done, switch the loop to testing mode. Run through every user story. Document every error you find. Do not fix yet, just catalog.

Phase 3: Fix. Once testing is done, go through the logged errors and fix every one. Then test each user behavior again against the fix to confirm it holds.

The exit criteria are what make it a loop instead of a one-shot. The loop does not leave build until every feature is logged. It does not leave test until every story has been checked. It does not finish fix until every error is cleared and re-verified.

Here is the orchestrator prompt pattern I feed into Claude Code /loops:

> Read this spec doc. Go over every single feature and define its expected behavior based on the code. Keep a single spreadsheet tracking every feature and its status. When that is done, switch the loop to testing every user story and documenting all errors. When that is done, fix everything against the logged errors and re-test every user behavior against the fix. Do not stop until every item passes.

Feed it the same spec doc from Step 1. That is it.

> Build, then test, then fix, with a hard exit condition on each. The exit criteria are the difference between a loop that finishes and a loop that wanders.

## Step 3: Add the Verifier

Left alone, a builder marks its own homework as correct. The verifier is the step that does not trust the builder.

In the loop, the verifier is Phase 2 doing real work. It takes each user story and actually runs it, then logs what breaks. This is what caught the bugs in the build.

One example. In the Lovable build, a list row would not open. The verifier found that the task title was being rendered as an input field at all times, so clicking the text opened the edit dialog instead of showing the task name. The loop logged it, then fixed it on the next pass, with a note in the tracker explaining exactly what happened.

No human flagged that. The verifier caught the builder's mistake and the fix phase cleaned it up.

What a good verifier step does:

- Tests each user story as a real user action, not just "does the code exist"

- Logs every failure with a note on what actually went wrong

- Feeds those logged errors straight into the fix phase

- Re-tests after the fix so a "fixed" item is actually confirmed, not assumed

> The builder is optimistic. The verifier is skeptical. You need both, because the whole point of a loop is that no human is there to catch the miss.

## Step 4: Track With a Live Feature Spreadsheet

The tracker is your window into the loop. It is a single spreadsheet or list, one row per feature and user story, with a status column the loop keeps current as it works.

In both builds the loop created the tracker itself, right inside the app, and updated it live. You could watch features move from built, to tested, to fixed, with notes attached to anything that had gone wrong along the way.

This is what lets you leave. You are not reading logs or watching the build. You glance at the tracker and see exactly where things stand.

What each row should carry:

- The feature or user story

- Its "done" condition from the spec

- Current status (built, tested, passed, failed, fixed)

- A note on any bug found and how it was resolved

One calibration point. Lovable created around 20 tracker items. Claude Code created around 40 for the same app because it broke things up far more granularly, arguably too granular. More items means more thorough, but also more overhead. Somewhere in the middle is usually right.

> If you cannot see it, you cannot trust it. The live tracker is what lets you walk away and still know the loop is honest.

## Step 5: Run Loops in Parallel

One loop is powerful. The real unlock is running several at once so nothing sits idle.

Both tools have a native way to do this.

In Lovable, use multi-task mode. It breaks the work into many smaller prompts that run at the same time. In the build, one prompt generated the files and spun up 12 separate tasks running in parallel off that single instruction. You turn on multi-task, click start, and walk away.

In Claude Code, use the /loops feature. It runs the orchestrated build-test-fix cycle natively and can hold multiple loops going at once.

The point of parallel is simple. The moment one piece of work finishes, another is already in flight. The work never stops because you are not the thing keeping it moving.

> Serial work waits on you. Parallel loops wait on nothing. Turn on multi-task or /loops and let the whole board build at once.

## The Two Routes, Side by Side

Same framework, two tools. Pick based on where you sit.

Route A: Lovable (easier, less technical)

- Export your spec doc as a plain text document

- Write a prompt (get Claude to help) telling Lovable to create a tracking list of every feature and user story, each with its "done" condition

- Instruct it to track continuously and keep building until everything is fixed, including QA and fixing anything that breaks

- Turn on multi-task mode so the work splits into parallel prompts

- Click start and leave

In the build, Lovable returned its first full version in about 20 minutes. One prompt built a multi-page working application: seeded users and dummy data, create-project flow, project color changes, list view, empty-project CTA, tasks with assignees and due dates, cross-out on completion, subtasks with per-subtask assignment, a delete flow, and a full Kanban board with drag and drop and sections. Bugs were caught and fixed along the way, each logged with a note.

Route B: Claude Code (native /loops)

- Feed it the same spec doc

- Use the /loops feature with the orchestrator prompt from Step 2

- Let it build the tracker, run the build-test-fix phases, and cycle until every item passes

In the build, Claude Code produced the same class of app: grouping, tasks, section columns, list view, check-marking, side nav, drag and drop, add-section, create-project, all working. It broke the work into roughly 40 tracker items, more granular than Lovable.

> Not technical? Start in Lovable with multi-task. Comfortable in the terminal? Run /loops in Claude Code. The loop is identical either way.

## The Cost Reality

This is the part that reframes everything.

Lovable ran the full autonomous build for 14.4 credits.

Claude Code ran it for about $5 (roughly 147,000 input tokens on Sonnet 5).

Both came in under $10 for a complete autonomous build, test, and fix of a working multi-page app. No dev team. No hourly rate. No one monitoring.

That is the whole pitch in one number. A full app, built and QA'd and bug-fixed by a loop, for less than the cost of lunch.

> Under $10 to autonomously build, test, and fix a real app. The bottleneck was never money or talent. It was the fact that you were doing it one prompt at a time.

## Gotchas to Watch

Loops are powerful, not magic. Here is what to keep an eye on.

Over-granular tracking. Claude Code split the same app into 40 items versus Lovable's 20. Too granular and you drown in overhead for no extra quality. Tell it to keep tracker items at the feature and user-story level, not every micro-step.

A few things will not fully test. In the build a handful of items could not be fully verified by the loop. Expect a small manual pass at the end on anything the verifier flags as "could not confirm."

UI quirks slip through. Claude Code's build pulled up a native browser element instead of the built-in UI when adding a task. Loops nail logic and flows but can miss small UI mismatches. A quick human look at the final product catches these.

The spec is the ceiling. The loop can only build and test what the spec defines. If a feature is missing its "done" condition, the loop has nothing to check it against. Weak spec, weak result. Spend your effort here.

You still deploy on purpose. The loop builds and verifies. Pushing to a live URL is the moment to give the final product one real look before it is in front of users.

> The loop handles the volume. You handle the spec going in and a short sanity pass coming out. That is the whole job now.

## Your First Loop This Week

- Pick one small app you actually want (an internal tool, a simple clone, a dashboard)

- Get Claude to write the spec with a "done" condition on every feature

- Export it as plain text

- Choose your route: Lovable multi-task or Claude Code /loops

- Write the orchestrator prompt: build every feature, then test every story and log errors, then fix and re-test

- Tell it to keep a single live tracker

- Turn on parallel mode, hit start, and walk away

- Come back, check the tracker, do a short manual pass, deploy

You will spend under $10 and end up with a working app you never typed a prompt to build past kickoff.

That is the loop. Design it once, and it ships while you do something else.

## Run It, Don't Just Read It

Everything here also ships as a plug-and-play kit inside the community: a run-order checklist, every prompt and file ready to paste, the gotchas I hit building it, and the finished example to check yours against.

Get the full playbook and kit here: [https://jacobklug.com/lm/autonomous-coding-loop?utm_source=X](https://jacobklug.com/lm/autonomous-coding-loop)
