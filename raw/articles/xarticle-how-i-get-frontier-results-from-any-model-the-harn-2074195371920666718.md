---
source_url: https://x.com/phosphenq/status/2074195371920666718
ingested: 2026-07-08
sha256: acaa4e177314f51ce584e77df4cec2f7c595534ddcf0df68721c9778e122a700
---

---
title: "How I Get Frontier Results From any Model (the Harness Guide)"
source: "x-bookmarks"
tweet_id: "2074195371920666718"
tweet_url: "https://x.com/phosphenq/status/2074195371920666718"
author_name: "Phosphen"
author_handle: "@phosphenq"
tweet_date: "Mon Jul 06 18:14:48 +0000 2026"
bookmark_date: "2026-07-06"
content_type: "x_article"
character_count: 26497
retweet_count: 15
like_count: 153
external_urls:
  - "https://claude.ai/install.ps1"
  - "https://claude.ai/install.sh"
---

# How I Get Frontier Results From any Model (the Harness Guide)

How I Get Frontier Results From any Model (the Harness Guide)

The full harness I run, the exact steps and install blocks to build your own, and the receipt from a mid-tier model hitting frontier-level output.

Bookmark this and let's begin.

> I am Phosphen. I write long-form breakdowns of the systems the best AI labs actually run. Follow @phosphenq. DMs open.

I used to lose a weekend rebuilding my whole setup every time a new model dropped.

Now I barely notice the releases. I get frontier-level output from almost any model I point it at, because I spent the last year building the harness instead of chasing the model.

The model, it turns out, is the part you swap. The harness is the part you keep.

Most people are still doing the opposite.

They upgrade the model and leave the setup around it untouched, then wonder why the new model feels like the old one with a different logo.

The leverage stopped being the model months ago. It moved to the scaffolding, and almost nobody has noticed.

This is the guide I wish I had a year ago. It is sourced from three things:

- Anthropic's own engineering docs.

- A year of my own builds.

- One very public accident in June, where the most capable model available got pulled for eighteen days and my work never slowed down.

Fourteen steps. Three parts. Five rungs on one ladder. Stop chasing models. Start building the body they plug into.

> PART 1 · The shift

## 01. The model was never the variable.

For two years the game was the model.

A better one dropped, you moved your whole workflow onto it, you got better output, you waited for the next release. The model was the thing you held, and the thing that decided your results.

That is over, and most people have not noticed yet.

Here is the uncomfortable version.

The gap between the number one model and the number ten model is smaller than the gap between a good harness and a bad one.

Put a weak setup around the best model on the leaderboard and you get demos that fall apart on contact. Put a strong setup around a mid-tier model and you get work that ships.

The ranking of the model stopped being the deciding factor. The quality of the system around it took over.

The leverage moved. It moved off the model and onto the scaffolding:

- The context you feed it.

- The loop it runs in.

- The tools it can reach.

- The checks that catch it.

- The memory that survives between runs.

That scaffolding is the harness. It is the part almost nobody is building, and it is the whole game now.

Boris Cherny, who built Claude Code, keeps saying a version of this in public, and it is the quiet argument running through this guide.

The work did not get easier. The leverage point just moved one floor up, from the model to the system that drives it.

You can measure the shift, roughly.

Anthropic has said its own engineers now merge on the order of eight times as much code per day as they did in 2024, a number Anthropic itself calls almost certainly an overstatement of the true gain.

Argue about the multiple all you want. The mechanism is not in dispute. The people getting outsized output are not typing better prompts. They built the loop that prompts for them.

## 02. The test: same harness, two models.

You do not have to take my word for any of this. Run the test yourself, today.

Take a real task from your week. Run it twice:

- Run 1: your setup on a cheap, mid-tier model.

- Run 2: the exact same setup on the most expensive frontier model you can access.

Then read the gap:

- If your setup is just a prompt, the gap will be enormous, and you will conclude, correctly, that you need the best model.

- If your setup is a real harness, the two outputs will land close enough that you will stop caring which model was underneath.

Luck has nothing to do with it. This is the whole thesis in one experiment: the results were never coming from the model.

They come from the system you wrap around it, and that system does not change when the model does.

A harness, in plain English, is five things stacked on top of each other:

- Context. The right files, rules, and memory reach the model at the right time. A cleverer sentence will not do that.

- A loop. The model gets a goal and works toward it, instead of waiting for your next message.

- Tools. It can read, run, and edit real things, not just describe them.

- Checks. Something can fail the work without you in the room.

- Memory. What it learns today survives to tomorrow instead of resetting.

None of that lives inside the model. All of it is yours to build.

The rest of this guide is how I build it, one rung at a time, with the exact commands.

## 03. The honest gate: do you even need one yet?

Before you build anything, the honest question, the one most guides skip to keep you reading.

You probably do not need the full harness yet.

Forcing it is how people end up maintaining a system nobody uses.

A single well-aimed prompt still wins in three cases:

- A genuine one-off. The task happens once.

- Exploratory work. You do not yet know what "done" looks like.

- A judgment call. "Done" is something only you can make.

In all three, a harness is slower, more expensive, and more fragile than just asking.

The harness earns its cost under a narrower set of conditions. Miss one and it costs more than it returns:

- The work repeats. A harness amortizes its setup across many runs. Build it for something you do once and you just did extra work to save yourself nothing.

- The check is automatic. Something has to fail the work without you reading every line: a test, a type check, a build, a linter. No automatic gate and you are back in the chair, doing the exact job the harness was supposed to remove.

- The budget can absorb the waste. A loop re-reads, retries, and explores. That spends tokens whether or not anything ships. The technique reads as obvious to people with effectively free tokens and reckless to people on a metered plan, and both are right about their own situation.

- The agent has real tools. Logs, a way to run the code it writes, an environment where it can see what breaks. Without that, the loop iterates blind.

If you fail one of these, bookmark this and keep prompting by hand for now.

You are not behind. You are being honest about your workload.

If you pass, keep reading. The climb is worth it.

> PART 2 · Build the harness

## 04. Rung one: the prompt, and its ceiling.

Everyone starts here, and there is nothing wrong with it. My first real setup was exactly this: one great prompt I had tuned over weeks, copied from a note every time I sat down.

Then the task got bigger, and the prompt broke.

Not because the model got worse. Because a one-shot prompt has a ceiling built into it. Three ways that ceiling shows up:

- It forgets everything the moment the context window fills.

- It cannot hold a plan across ten steps without losing the thread.

- It cannot check its own work, so you check all of it.

The prompt did not fail you. The absence of anything around the prompt failed you.

- Good for: quick answers, one-off edits, throwaway scripts, exploring a question where you do not yet know the shape of the answer.

- Caps out the moment: the task repeats, spans many steps, depends on what happened last time, or has to be checked before it ships.

The fix is never a cleverer prompt.

Past a certain point, tuning the prompt is rearranging furniture in a room that is too small.

The fix is to build the next rung. Every rung from here adds a piece a bare prompt cannot have.

## 05. Rung two: context, feed the model, don't out-clever it.

The model is smart, but it is blind. It knows only what you put in front of it.

Most people respond to a weak answer by rewording the question.

The people getting frontier results respond by fixing what the model can see.

This is the discipline the whole field moved to this year, and it has a name.

Prompt engineering optimizes the question. Context engineering optimizes everything the question lands in:

- The standing rules.

- The actual code.

- The relevant memory.

- The tools within reach.

It is a system you design, not a sentence you polish.

The concrete move is to give your agent a home and a memory that outlive the chat. I use Claude Code, because it is the best body I have found for a harness and it reads all of this for free.

Do this now. Install Claude Code:

```
# Windows (PowerShell)
irm https://claude.ai/install.ps1 | iex

# macOS / Linux
curl -fsSL https://claude.ai/install.sh | bash

# or, if you already live in Node
npm install -g @anthropic-ai/claude-code
```

Then drop a CLAUDE.md in the root of your project. This is the single highest-leverage file in your whole setup. Claude reads it at the start of every session, forever, without you asking:

```
# CLAUDE.md

## what this is
[one line: what the project does]

## run it
install: [your install command]
test:    [your test command]

## rules
- [your conventions]
- never touch [x]
- always [y]
```

Keep it under two hundred lines. It is a set of instructions, not a novel, and a bloated file gets ignored.

That one file is the difference between two agents:

- Without it: an agent that rebuilds your whole project from zero every session, like a goldfish.

- With it: one that shows up already knowing where it is and what the rules are.

Everything else in this rung is more of the same. Fix what the model can see, and most of the answers fix themselves.

## 06. Context, deeper: what belongs in the window and what does not.

The mistake at this rung is thinking more context is better context. It is not.

The window is a budget. Everything you spend on noise is spent twice: once on tokens, once on the model's attention.

A useful way to think about it: the context window is a desk, not a library.

You do not pile the whole library on the desk. You put the three things it needs for this task and clear the rest.

Good context engineering is as much about what you leave out as what you put in.

What earns its place on the desk:

- Standing rules. Your CLAUDE.md. Read every run. The cheapest, highest-return context you own.

- The relevant code. The files this task actually touches, not the whole repo. Point the agent at the module and let it pull the rest when it needs it.

- The task's own memory. What happened on the last run of this same job: what was tried, what failed, what the decision was. Written down, not left in a chat you closed.

- The tools. The set of things it is allowed to call for this task, and no more.

What to keep off the desk:

- Stale files.

- The entire git history.

- Three months of prior conversation.

- Anything you are including because it feels thorough.

Thoroughness is a context tax.

The agent that gets a clean, relevant window outperforms the one drowning in everything, every time.

Context is the rung most people skip straight past on their way to something that sounds more impressive. Do not.

A great loop on top of bad context is a fast way to be confidently wrong at scale.

## 07. Rung three: the loop, stop prompting and start looping.

This is the rung where it clicked for me, and it is the one that feels strangest the first time.

For two years I prompted every step by hand. Type, wait, read the diff, type again. I was the loop.

The shift is to stop being the thing that prompts.

You give the agent a goal and the tools to chase it, and you let it run:

- Pick the next step.

- Call a tool.

- Check the result against the goal.

- Go again until the check passes.

You design that loop once. The loop prompts the agent from then on.

In Claude Code the whole thing is one command. /goal runs the agent turn after turn until the finish condition is met, and the condition is plain text, no quotes:

```
# Claude runs turns until a SEPARATE fast model confirms the
# finish condition, not until the maker feels done.
/goal all tests in tests/auth pass and lint is clean, or stop after 6 turns
```

Here is the part that makes it work.

After every turn, /goal hands the condition and the conversation to a separate small fast model, Haiku by default, and asks one question: is this actually done?

The model that wrote the code is not the model that decides it is finished. That built-in second opinion is the whole trick, and it is the subject of the next step.

You stop prompting the steps. You prompt the loop once, and it runs itself.

## 08. The stop condition: keep the maker away from the checker.

Here is where loops quietly go wrong, and where the token bills come from.

A loop needs a finish line the loop cannot move.

The failure mode is letting the agent that wrote the code decide whether the code is done. In Addy Osmani's exact words on loop engineering, "the model that wrote the code is way too nice grading its own homework." It talks itself into "good enough" and fires the done signal on a half-finished job.

The fix has a name. Anthropic documented it back in its December 2024 engineering post as the evaluator-optimizer pattern, long before the vocabulary went viral.

The pattern: one agent generates, a different one critiques, and you repeat until the critic is satisfied. The maker and the checker are not the same model, and ideally not even the same instructions.

That is exactly what /goal does under the hood. The separate checker runs after every turn, so the finish line is never the maker's opinion:

```
# the checker is a different, fresh model; the hard stop
# lives inside the condition itself.
/goal tests/auth all pass and lint is clean and no new TODOs, or stop after 6 turns
```

Two rules make this safe, and neither is optional:

- The check is objective. A test that passes or fails. A build that compiles or does not. A linter that returns zero or non-zero. Not a second agent with an opinion, which is just two optimists agreeing.

- The loop has a hard stop. An iteration cap, a token budget, or a time limit, written into the condition. Without one, an ambitious loop runs until the rate limit or the invoice notices for you.

One more tool, so you do not confuse them. /goal runs until a condition holds. /loop is the separate command for running on a schedule, a nightly triage pass on a timer rather than a run-until-done. Different jobs. Do not nest them.

Get this rung wrong and the loop fails silently and expensively. Get it right and you can walk away, which is the entire reason you built it.

## 09. Rung four: the harness, subagents.

A raw loop drifts and trusts itself. What turns it into a harness you can leave alone is a set of parts wrapped around it. The first and most important is subagents.

A subagent is a specialized helper that runs in its own context window, with its own instructions, its own tools, and sometimes its own model. Two reasons it matters:

- It keeps side work out of the main thread. Searching, reading logs, exploring: none of it clutters your main conversation.

- It makes the checker a different mind than the maker. This is the one that pays for itself.

Drop a file in .claude/agents/ and Claude will delegate to it when the work matches:

```
---
name: reviewer
description: Reviews a diff for bugs, missing tests, and risky changes.
tools: Read, Grep
model: sonnet
---
You are a strict code reviewer. For the given diff, list real problems only:
missing tests, unhandled errors, hardcoded values, security risks.
For each, name the file and give the one-line fix. Do not praise. Do not soften.
```

The usual split inside a working loop is three roles:

- Explorer. Finds the work.

- Implementer. Writes it.

- Verifier. Checks against the spec, with no exposure to how the implementer talked itself into its choices.

The verifier is the one that lets you sleep. Give it the strong model and the strict instructions, even when it costs more.

One caution.

Subagents each do their own model and tool work, so they burn more tokens than a single pass. Spend them where a second, independent opinion is actually worth paying for, which is mostly the check.

Do not spin up a swarm because it looks impressive. A loop with one good verifier beats a loop with five chatty helpers and no real gate.

## 10. The harness: hooks and permissions.

Subagents decide who does the work. Hooks and permissions decide what the work is allowed to do while you are not watching.

A hook runs a command automatically at a fixed point in the loop, so a rule holds without anyone remembering to enforce it.

Formatting, linting, a guard that blocks a dangerous command before it runs.

Put them in .claude/settings.json:

```
{
  "hooks": {
    "PostToolUse": [
      { "matcher": "Edit", "hooks": [
        { "type": "command", "command": "npm run lint -- --fix" }
      ]}
    ]
  }
}
```

That one hook means every edit the loop makes gets linted the instant it lands, forever, whether or not the agent remembered to. Hooks turn "please always do X" from a hope into a fact.

Permissions are the other half.

The loop runs while you are asleep, which means its blast radius is whatever you allowed. Decide up front what is off limits, and it stays off limits no matter what the agent decides mid-run:

- Read-only by default. Start every new loop with the narrowest permissions that let it do the job, and widen only when you hit a real wall.

- Hard walls around the dangerous things. Payments, auth, production config, anything irreversible. The loop does not get to touch these without a human in the path.

- Re-audit on a schedule. The classic drift is a loop that got "just one" write permission added for convenience and never had it removed. Permission scope creep is how a helpful loop becomes an unattended liability.

Hooks and permissions are unglamorous. They are also the reason the whole thing is safe to leave running.

A harness you cannot trust unattended is not a harness. It is a very expensive way to watch an agent work.

## 11. The harness: skills, memory, and MCP.

Three more parts turn a loop that works today into one that gets better over time and reaches your real tools.

Skills are how you write project knowledge once and have it read on every run.

A skill is a folder with a SKILL.md inside, holding instructions and metadata, plus optional scripts and references.

The point for a loop is compounding. Without skills, a loop re-derives your conventions from zero every cycle. Add skills and it starts each run already knowing them.

The "we do not do it this way because of that one incident" lives on the outside, written once, obeyed every run.

Memory is the piece that sounds too dumb to matter. It is actually the spine of every loop that survives more than a day.

Agents forget by default. What they learn this session is gone tomorrow unless you write it down.

So write it down, in a file that lives outside the conversation:

```
# STATE.md - auth quality loop

## last run
2026-07-05 03:30 · 7 failures triaged, 3 fixes drafted, 4 escalated

## in progress
- claude/fix-auth-token-refresh - tests green locally, awaiting CI

## lessons (write here, not in chat)
- 2026-07-04: this runner hits a TLS issue in PowerShell. use bash.
- 2026-07-03: tests/e2e needs the Stripe webhook secret in env. skip if missing.
```

The rule is simple: the agent forgets, the file does not.

A loop with state resumes tomorrow where it stopped. A loop without state starts over every morning, which is most of the reason loops feel like they are not learning.

MCP is how the loop touches your real tools instead of only your files.

Built on the Model Context Protocol, connectors let the agent:

- Read your issue tracker.

- Query a database.

- Hit a staging API.

- Drop a message in Slack.

This is the difference between an agent that says "here is the fix" and a loop that opens the PR, links the ticket, and pings the channel once the checks are green.

This is also where I will stop, because the deepest version of memory, a harness that remembers you across weeks rather than a single run, is a whole guide of its own. For now, a STATE.md and a couple of skills are enough to make the loop compound.

Put these parts together and the point of the whole guide shows up on its own. You stop tending the model.

> PART 3 · Keep it honest

## 12. The receipt: they pulled the best model on earth for 18 days, and I barely noticed.

I said the model is the swappable part. In June, the world ran the experiment for me, at full scale, with no warning.

On June 12 the US government put export controls on Fable 5, at the time the most capable model available. Anthropic pulled it worldwide to stay compliant.

For eighteen days the best model on earth was, for most of the world, simply gone.

It came back on July 1, at ten dollars per million input tokens and fifty per million output, about double the price of the tier below it.

If your results lived inside that one model, you lost eighteen days and then paid double to get them back.

My work never slowed down for an afternoon, because a model-agnostic harness does not care which model is underneath.

The loop kept running. Context still loaded, checks still passed, and I swapped a different model in underneath without touching anything else. The output barely moved.

That is the thesis, proven by a real and slightly absurd event.

Build the harness, and a frontier model getting rug-pulled by a government becomes a footnote in your week instead of a hole in it.

Chase the model instead, and someone else's policy decision is now your outage.

## 13. How this fails quietly.

The dangerous failures of a harness are not the loud ones. A crash you can see.

The failures that cost you are the ones that keep running while looking fine.

- The loop that fails silently. An agent meant to signal "done" only when finished signals it early, and the loop exits on a half-done job while the dashboard stays green. The fix is the objective gate from step 8. Without a real check, a loop does not stop when it is done. It stops when it has convinced itself.

- Goal drift. Over a long session, every summarization step loses a little. The "never touch payments" rule you set at the start quietly evaporates by step forty. The fix is a standing spec (a VISION.md or the rules block in your CLAUDE.md) reread on every run, so the goal cannot erode.

- Self-preferential bias. The maker is too soft on itself, covered in step 9, and worth repeating because it is the single most common reason a loop produces confident garbage. The only cure is a checker the maker never sees.

- Comprehension debt. The faster your harness ships code you did not write, the wider the gap between what the repo contains and what you understand. The token bill is not the one that hurts. The one that hurts is the day you have to debug a system nobody on the team has read. Pay it down by reading the diffs, every time, even the boring ones.

- The security tax. A loop running unattended is an attack surface running unattended. Three ways it bites, and the guard for each:

- It opens PRs faster than a human reads them. Gate merges with security checks.

- It will install a skill with a prompt injection buried in its description. Audit any skill before you install it.

- It scatters secrets into logs nobody monitors. Keep verbose logging out of anything that runs while you sleep.

None of these mean do not build the harness. They mean build it with your eyes open.

The harness removes the typing. It must not remove the thinking.

The moment you let it, every failure above compounds instead of getting caught.

## 14. Rung five: the environment, the horizon.

There is one rung above the harness, and it is where the frontier labs are already fighting.

Once the model is a swappable part, the competition moves to everything around it:

- The environments agents are trained and evaluated in.

- The memory that lets them compound across weeks instead of runs.

- The evals that decide whether any of it actually works.

This is the rung you do not build in a weekend. It is the one that tells you where all of this is heading.

You do not need it to get frontier results today.

You need it to understand why the harness works at all, and why it keeps working as the models change under it.

Standing on rung four already puts you ahead of almost everyone still typing prompts by hand.

Rung five is the next guide. For now, the climb below it is enough.

---

## § The mistakes that keep you stuck at the prompt

- Chasing every model release instead of building the one thing that survives all of them.

- Skipping the honest gate. Building a harness for a one-off, or for work with no automatic check, and paying setup cost you will never earn back.

- A loop with no objective check. A second agent that "reviews" with no test behind it just rubber-stamps the first.

- One agent writing and checking. The maker is too soft on its own work, and it always passes

- No CLAUDE.md. The agent rebuilds its understanding of your project from scratch every session.

- No memory. Tomorrow's run restarts from zero instead of resuming.

- No hard stop on the loop. It runs until your rate limit or your invoice cuts it off.

- Permission scope creep. One convenience write-permission, never re-audited, and now an unattended loop can touch things it never should.

- Reading none of the diffs. Comprehension debt at compound interest. The day you debug a system nobody has read costs more than the tokens ever did.

---

## Conclusion: the model was never the variable.

For two years the leverage was at the model. A better model, a better prompt, a better one-shot answer.

That phase is ending.

The models got good enough that the next leverage point is one floor up: the harness that decides:

- What they see.

- When they run.

- What can stop them.

- What survives between runs.

You now have the whole thing. The map. The install. A CLAUDE.md. A loop that runs itself against an objective gate. A harness with subagents, hooks, permissions, skills, and memory wrapped around it. And the honest test for whether you need any of it yet.

The winners this year will not have the smartest model. They will have the harness the smartest model plugs into.

When the next release drops, they will swap it in under a system that already works and keep going, while everyone else spends another weekend rebuilding.

Build the first rung tonight, the one thing you still do by hand, and let the model become the easy part.
