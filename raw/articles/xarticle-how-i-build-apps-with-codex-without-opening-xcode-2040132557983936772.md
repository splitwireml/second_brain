---
source_url: https://x.com/paulsolt/status/2040132557983936772
ingested: 2026-07-11
sha256: faa3e2ba8e06021dba5da3d1180e5c46b930411a1750fb8e73f15987af0d6f5d
---

---
title: "How I Build Apps With Codex Without Opening Xcode"
source: "x-twitter"
tweet_id: "2040132557983936772"
tweet_url: "https://x.com/paulsolt/status/2040132557983936772"
author_name: "Paul Solt"
author_handle: "@PaulSolt"
tweet_date: "Fri Apr 03 18:21:20 +0000 2026"
content_type: "x_article"
character_count: 8319
retweet_count: 73
like_count: 759
reply_count: 14
---
How I Build Apps With Codex Without Opening Xcode

Do you want to build iOS or macOS apps with Codex?

[Embedded Tweet: https://x.com/i/status/2013349868144591295]

I have a new Agent Skill that will help you make apps. Without this skill you're going to waste a lot of time. Let me explain.

I was building a Dangerous Spider app with Codex when I noticed the agent kept missing its own build and test failures. It was looking at the wrong status codes. It genuinely couldn't find the error and would say everything worked (when it didn't).

Xcode compiler build output is extremely verbose. Actual errors get buried in thousands of lines of text. Trying to find an error in Xcode build output is like finding a needle in a haystack.

When you layer in agents, you're wasting time and context by asking them to find the errors.

Agents need to know what worked and what didn't work. It needs to be pass/fail, so I created an agent-designed workflow to do just that.

Here's the 7-step workflow I use every day:

## 1. Make Xcode Projects Agent Friendly with AppCreator

I built an [Agent Skill called AppCreator](https://super-easy-apps.kit.com/app-creator). Run it once, and it scaffolds a new Xcode project or retrofits an existing one. Now your project is agent-ready.

At the heart of it: a `Makefile` wraps the CLI `xcodebuild` commands using [xcbeautify](https://github.com/cpisciotta/xcbeautify). Clean, readable output from Xcode app builds and tests. The agent sees what failed, fixes it, and moves on. No verbose output to search. It works for iPhone and Mac apps.

Download and install the [AppCreator Skill](https://super-easy-apps.kit.com/app-creator) to make your app project agent-friendly.

## 2. make Is the Only Build Command I Use

The skill is designed so that one command builds and runs your app:

make

Your agent knows how to work with Makefiles, so this is just the starting point. You can extend it however you want.

I ask agents to set the default action to "build-and-run", and to use special build scripts so the freshly built app is always relaunched, just like Xcode.

- In Codex CLI, type "make" to check the agent's work.

- In the Codex app, set up a custom run action:  Click on the Play button and set it to: make.

Finding the setting later requires a few more steps: Go to Environments → Project → View → Edit Local Actions → Actions → Set Action Script to `make`.

With a Makefile, you have a fast, repeatable way to build and run your apps (via the up-arrow on the CLI or the Run button in the Codex app).

## 3. Just Talk to It

If you want to get good results, you need to actively steer your agent.

Agents are good, but they'll do things you don't want, and the only way to prevent that is to steer the ship as they work.

I frequently double-check the work and redirect when I see agents doing the wrong thing.

I use [Wispr Flow](https://wisprflow.ai) to talk out loud — describe what I want, how it should behave, what needs to change. After an agent hands back work, I start Wispr Flow as I play-test the new changes. This gives me the chance to talk through what works and what doesn't, and then, when I'm done, I can paste the transcript directly into the Codex app.

Plan mode is helpful for sparking thoughts about how features and edge cases. However, I have found that the plan mode isn't good enough.

[Embedded Tweet: https://x.com/i/status/2039551079621566812]

Instead, I would use plan mode to help you think through the feature as a starting point. Use it to spark discussion so you can refine which features you actually build.

Software is nuanced, and if you take it feature by feature, you're going to get better software in the end.

## 4. Tests Keeps Agents Accountable

Without tests, agents can get sloppy. Tests allow agents to catch their own mistakes.

Ask Codex to write unit tests as it builds. Your goal is fast tests. UI tests are helpful for verification, but they can be annoying and slow to run. I like to have agents use UI tests to catch errors that are impossible to test with unit tests alone.

My recommendation is that you separate your tests into at least two targets:

- make test

- make ui-test

When an agent runs UI tests, it takes over your machine, which can be disruptive if you need to do anything else (This is where having a second Mac can be useful).

UI tests will slow everything down, so it's best to test them only at hand-off points. When your agent has wrapped up one task or several tasks. Don't do full regression testing for incremental work; instead, ask the agent to test only the smallest subset to verify their work and remain fast.

Have your agents read this article from Peter Steinberger, @steipete: [Running UI Tests on iOS With Ludicrous Speed](https://www.nutrient.io/blog/running-ui-tests-with-ludicrous-speed/). Using that, you can help keep your test suite from becoming a bottleneck.

## 5. Log Runtime Results

Another indispensable tool is the use of logs and app artifacts. Have your agent add logging to your app. This gives it another tool for seeing what went wrong in real time.

Agents can stream development logs to a file or read them in real time to fix problems that are not immediately obvious.

When my agent repeatedly fails to complete a task properly, I know it's time to introduce more detailed logs.

Just ask your agent:

> Please add verbose logs around XYZ so that you can see what is happening and fix the problem.

Now your agent has tools to test logic and to verify results at runtime.

## 6. AGENTS.md Rules You Should Add

These are some helpful rules that have worked for me. You may need to adapt them for your own workflow.

I have two scripts included with the [AppCreator skill](https://super-easy-apps.kit.com/app-creator) that prevent dangerous git commands and file deletions.

```markdown
* Never add fallbacks or workarounds without my explicit written approval. If unsure, ask.
* Do not treat “continue” or silence as approval for any fallback behaviors.
* Use one code path per action. Buttons, menus, pop-up buttons, keyboard shortcuts, and gestures must call the same implementation.
* Do not add backward compatibility for new code. Only preserve backward compatibility when shipped behavior already exists. Ask if unclear.
* Add verbose logs for user actions, mode switches, monitor targeting, and input. Use these logs to triage problems at runtime.
* Never run destructive git commands without my explicit written approval.
* Forbidden git commands: `git reset --hard`, `git checkout --`, `git restore`, `git revert`, `git clean`, force push, and `git amend`.
* Always make atomic commits. One task or fix per commit. Use the `scripts/atomic_commit.sh Agent <NAME>: <intent>" <file1> <file2> ...`
* Never use `rm` for deleting files.
* Always use the trash script `scripts/move_to_trash.sh <paths...>` so that deletions can be reverted.
* Run fast, focused tests during implementation, and save the full regression suite for final handoff.
* Only run UI tests when requested.
* Do not claim verification passed if tooling or environment issues blocked it.
```

## 7. Your Agent Needs Documentation

Want next-level results? Give Codex real Apple documentation with [DocSetQuery](https://github.com/PaulSolt/DocSetQuery).

I build sets of local Apple docs using DocSet bundles and have agents create guides.

Agents have a fuzzy understanding of code. You need to give them concrete code so they use the actual APIs instead of guessing.

Another option is https://sosumi.ai

## Here's what I use — Steal it:

- [AppCreator skill](https://super-easy-apps.kit.com/app-creator): Scaffolds new projects and retrofits existing ones.

- Just talk to it: Keep the focus small and easy to reason about.

- [DocSetQuery](https://github.com/PaulSolt/DocSetQuery): Have agents leverage fast local Apple documentation.

What does your Codex workflow look like? Reply below.

Follow @PaulSolt for the Codex workflows I'm actually using to build and ship iOS and macOS apps.

P.S. [Super Easy Slides](https://apps.apple.com/us/app/super-easy-slides/id6738591861?mt=12) is on the Mac App Store (built with this workflow). And you can preview my [Dangerous Spider app here](https://www.youtube.com/watch?v=A_wwY0QlY3U&list=PLLYKjb-Uo9cxLIivNCn9dMhTNP5sntESG&index=1).