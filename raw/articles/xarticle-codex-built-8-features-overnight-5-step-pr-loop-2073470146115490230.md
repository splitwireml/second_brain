---
source_url: https://x.com/paulsolt/status/2073470146115490230
ingested: 2026-07-11
sha256: de2f8f5fe35f9eaf2b322072bf68024eb8ffbabb693a3693439ab8dae58acb18
---

---
title: "Codex Built 8 Features Overnight: My 5-Step PR Loop"
source: "x-twitter"
tweet_id: "2073470146115490230"
tweet_url: "https://x.com/paulsolt/status/2073470146115490230"
author_name: "Paul Solt"
author_handle: "@PaulSolt"
tweet_date: "Sat Jul 04 18:13:00 +0000 2026"
content_type: "x_article"
character_count: 5696
retweet_count: 10
like_count: 136
reply_count: 9
---
Codex Built 8 Features Overnight: My 5-Step PR Loop

This week, I woke up to 8 new features moving toward release in Super Easy Timer, including stopwatch, clock, pomodoro, and autocomplete. One Codex thread ran for 12 hours and 19 minutes. Part of that happened while I slept.

Those features are shipped on [TestFlight](https://testflight.apple.com/join/1jm4arcH). Testers are already using them while I wait on [App Store](https://apps.apple.com/us/app/super-easy-timer/id1353137878?mt=12) approval.

How? I have one Codex thread that manages all my other threads.

The PR loop is simple:

1. Create task threads on worktrees

2. Worker threads complete tasks and create PRs

3. Code review happens on GitHub (Codex plugin)

4. The manager sends feedback to the worker threads

5. Repeat until the branch is merge-ready

[→ Get my Codex Chief of Staff Prompt](https://super-easy-apps.kit.com/codex-manager-thread)

I didn't set this up blind. I first ran a proof of concept with four tasks. Once those worked, I picked out another set of tasks.

First proof post from that morning:

## The Shift: Single Prompts → Loops

Credit where it started: @steipete pushed the idea of designing [agent loops](https://x.com/steipete/status/2063697162748260627) instead of writing one-off prompts.

[Embedded Tweet: https://x.com/i/status/2063697162748260627]

Theo explained the pattern more clearly with [examples on YouTube](https://www.youtube.com/watch?v=iJVJwmCKW9o).

It didn't sink in because I was traveling, so after seeing both @Dimillian  and @emanueledpt post about it again. I was ready to give it a shot.

Use this article to jumpstart your own manager threads (Chief of Staff)

## Step 1: Create a Manager Thread

Open one Codex thread with a single job: manage the other threads. It doesn't own feature implementation. It owns coordination — scheduling work, watching PRs, reporting status.

I named mine Chief of Staff at first. That's a mouthful, so now it's just "Chief" (or "Manager"). Keep it short.

I knew from @Dimillian that this manager thread could become my inbox for bugs (I'm already doing that for sponsor requests). So it was a natural extension to lean on one to help manage, shape, and move the work along.

[Embedded Tweet: https://x.com/i/status/2070850643963597153]

Any time I had an issue come up, I used WisprFlow to dictate my issue and track my task using my simple-tasks skill from [AppCreator](https://super-easy-apps.kit.com/app-creator).

My markdown plans live in the repository, so every worker thread has the context without me having to repeat it.

## Step 2: Add a Heartbeat (Loop)

Tell your manager thread to create a heartbeat: every 5-10 minutes, check open PRs, code review feedback, and CI status.

The heartbeat is what makes this a loop instead of a longer prompt. Without it, everything dies the moment a worker finishes or stalls.

## Step 3: Put /goal on Every Worker Thread

Make your manager run /goal on each worker so it pushes to merge-ready instead of stopping at "I've implemented the feature" with failing tests. This is the fix for agents who quit early.

My 12h19m run happened because goals kept the manager thread going with task threads. I didn't have to keep asking to fix XYZ. One kick-off prompt and the work keeps on going.

## Step 4: Route PR Feedback Back to Workers

Have your manager read code review comments as they land, assign fixes to the right worker, and re-test. This used to be my job, and it was annoying. I just want the work finished and tested.

Codex plugin was doing my code reviews, but you can use any plugin here. I just enabled the Cursor bug bot to do one PR pass on first open, so we'll see how that helps ensure code quality.

## Step 5: Gate Merges

Require tests to pass before anything is merge-ready. For UI facing changes, you'll want to test them yourself. Right now, for Mac development, this is probably the slowest process.

I have both unit tests and slower UI tests, but these tests never seem to exercise all the weird windowing problems that can occur in a Mac app. I still find regressions, so manual testing is still key for me.

In the Codex environment, I have Command + R set to run my Makefile's "make" target, which builds and runs the macOS app. All I need to do is go to the thread, and I can test the new work instantly.

For non-UI changes, I trust Codex to do a good job, so some of these get merged automatically.

## What Broke?

My process isn't entirely hands-free. On the same run:

- Agents struggled with UI interactions

- My SwiftUI/AppKit window logic was too brittle for them

- One thread got stuck and unresponsive, so we spun up a replacement thread

- Managers + Workers didn't always follow my AGENTS.md rules

The loop moves work forward. It doesn't replace taste.

## Here Are 5 Things You Can Steal

- One manager thread (mine's named Chief) that owns coordination, not implementation

- A heartbeat every 5-10 minutes: PRs, review feedback, CI

- /goal on every worker so agents finish

- PR feedback is routed back to workers on each heartbeat

- Merges gated on CI + your own manual tests

I packaged the exact prompt I'm using, along with the self-learning prompts, so your agent can document and resolve issues as they work. Download the prompt below:

[→ Get my Codex Chief of Staff Prompt](https://super-easy-apps.kit.com/codex-manager-thread)

What have you pushed forward with an agent loop — a feature, a bug backlog, a release? Reply below.

Enjoy your next app!

P.S. Working on an iOS/macOS app? I do 1:1 App Strategy Sessions. [Book a time and let's talk about yours](https://calendly.com/paulsolt-super-easy-apps/1-1-app-strategy-session).