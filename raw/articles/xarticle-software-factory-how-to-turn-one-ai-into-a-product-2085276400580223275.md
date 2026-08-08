---
source_url: https://x.com/Nazik2053/status/2085276400580223275
ingested: 2026-08-08
sha256: c1d92e72d756c1d26bf6b856a3c01cee39ced2befcbdc19cd8326fae7e957860
tweet_id: "2085276400580223275"
tweet_url: "https://x.com/Nazik2053/status/2085276400580223275"
source_file: "/Users/mali/Development/x-bookmarks/data/run-2026-08-06/2026-08-06/xarticle-software-factory-how-to-turn-one-ai-into-a-product-2085276400580223275.md"
run: run-2026-08-06
---
---
title: "Software Factory: How to Turn One AI Into a Production Line"
source: "x-bookmarks"
tweet_id: "2085276400580223275"
tweet_url: "https://x.com/Nazik2053/status/2085276400580223275"
author_name: "Nazar"
author_handle: "@Nazik2053"
tweet_date: "Thu Aug 06 08:06:51 +0000 2026"
bookmark_date: "2026-08-06"
content_type: "x_article"
character_count: 17740
retweet_count: 3
like_count: 27
---

# Software Factory: How to Turn One AI Into a Production Line

Software Factory: How to Turn One AI Into a Production Line

For a couple hundred dollars a month, anyone can rent close to the best software engineer in the world. Millions do. Almost all of them use it the same way: open a window, ask for something, wait, read, ask again. One question at a time, one person at the keyboard all day.

That's a workshop. One tool, one pair of hands, and it makes exactly as much as those hands can hold.

A few people do something else with the same subscription. They don't have a better model than you. They have a line.

The difference shows when you close the laptop. A line pulls the next job off a queue, hands it to a worker with its own room, runs the result past a gate that needs no supervision, then writes down what it learned so next week runs better than this one.

Most writing on this names the idea instead of building it. This is the build. Every step below is a file you create tonight and a command you run.

---

## What a software factory is

Your model isn't the limit. It has no way to receive work, nowhere to run it, nobody to check the result, and no memory of last time - so it sits idle most of the day waiting for you to type the next thing.

Four cheap parts close those gaps. None of them are clever.

- The queue: a plain text file of jobs, so work arrives without you delivering it by hand.

- The rooms: one folder and one branch per worker, so several can build at once without stepping on each other.

- The wiring: who does what, and more importantly, who is allowed to change what.

- The gate: a small program that decides what ships and what comes back.

---

## Step 1 - set one agent running without you

Your subscription bills the same whether the agent works or waits, and most of the day it waits, because the only way work reaches it is you, awake, typing.

The queue is a markdown file with four sections. Put it at tasks/QUEUE.md:

```
# Task Queue
## Ready (can be picked up)
### High Priority
- [ ] [HIGH] Fix the checkout webhook retry logic
### Medium Priority
- [ ] Rewrite the onboarding emails
## In Progress
- [ ] @builder: Add the export endpoint
## Blocked
- [ ] Migrate the billing table (needs: schema decision)
## Done Today
- [x] @builder: Ship the pricing page
```

The check the agent cannot argue with

A queue file on its own is a wish. If the only thing telling your agent to read it is a sentence in a prompt, it will skip the queue whenever it feels busy and tell you everything went fine.

A model can talk its way around an instruction. An exit code gives it nothing to talk to.

So the queue check is a small program. It reads the file, finds unchecked high-priority jobs, and quits with a failing status if any exist:

```
Scans tasks/QUEUE.md and enforces queue-first execution.
Returns exit code 1 if HIGH/Critical tasks exist.
Returns exit code 0 if the queue is empty or all tasks are LOW.
Run this BEFORE reporting a clean run.
If exit code 1: spawn an agent for the HIGH priority task.
```

When it trips it prints CANNOT SKIP QUEUE and names the job. The agent can't report a clean run while urgent work sits untouched, because the process it lives inside has already failed.

Two details are worth copying exactly. It reads only the Ready section, so a job in flight never gets picked up twice. And it reads urgency from ordinary words as well as tags: a line starting FIX: or BUG:, or containing BROKEN, becomes high priority whether or not you labeled it.

The clock, and the trap inside it

Then you wire the clock:

```
0 8 * * *  cd ~/projects/app && node check-queue.js || ./run-agent.sh
0 1 * * *  cd ~/projects/app && ./run-agent.sh --night
```

One trap decides whether the line lives a year or dies quietly in month three: if you host the schedule on GitHub Actions, the platform disables scheduled workflows after 60 days without repository activity, and it doesn't warn you. Give the repo one commit a month and it runs indefinitely.

Last thing, and most people have it backwards: don't keep one long session alive between runs. Every automated call arriving more than a few minutes after the last one pays to re-store the whole conversation at the expensive write rate, and that conversation grows every iteration. A nightly loop can swell past hundreds of thousands of tokens by hour 20, at which point the real work is a rounding error next to the storage bill. A fresh session per run is one flag, and it's why the numbers in Step 6 stay small.

---

## Step 2 - give every agent its own room

Two agents in one folder will overwrite each other inside ten minutes and neither will notice. This turns one worker into several, and it takes about 90 seconds.

Git already had the answer. A worktree is a second working folder on the same repository: its own directory, its own branch, shared history.

```
git worktree add ../app-checkout -b checkout
git worktree list
git worktree remove ../app-checkout
```

Since February 2026, Claude Code does it in one flag, and each worker can get its own terminal pane:

```
claude --worktree
claude -w --tmux
claude -w "#1234"
```

The third line pulls a pull request into its own room, which is how you hand an agent a review job without touching your checkout. When you launch a subagent with isolation: "worktree", it routes into its own worktree with no git plumbing from you.

The two walls on the way to more agents

A new room is a clean checkout. Anything git ignores doesn't come with it - your .env, your local config, your generated assets. The agent starts, the server boots, it dies on the first missing secret, and you burn three hours debugging the wrong layer.

The fix is a .worktreeinclude file at the project root. It uses .gitignore syntax and lists the ignored files that get copied into every new room:

```
.env
.env.local
config/secrets.json
```

Only files that are both matched and ignored get copied, so nothing tracked is ever duplicated.

The second wall: rooms isolate code, not the running programs inside them. Two workers with separate folders will both still expect port 3000 and both write migrations into the same database. Give each room an offset port and its own database branch.

And the honest ceiling on a laptop is about two heavy workers at once. Push to six and you get OOM crashes, lost work, corrupted sessions. Two workers that finish beat six that fall over.

---

## Step 3 - wire the agents into one line

Several agents with several rooms is several workshops. The wiring makes it a line, and the obvious wiring is the wrong one.

Most people split by task: this agent writes the frontend, that one writes tests, that one deploys. It holds until two disagree about the same file, and then you're back to arbitrating.

The split that holds is by write permission. Keep the review agents entirely separate from the ones producing code, and let each write to exactly one place:

- Testing: reads everything, writes only to the test suite.

- Code review: writes only to issues and a refactor file.

- Security: writes only to a timestamped security report.

- Performance: writes reports and nothing else.

- Platform: owns build, deploy, and infrastructure, nothing in the application.

A reviewer that physically cannot edit the code it reviews gives you an honest report every time. That single constraint deletes the whole category of problem where a reviewer decides to fix what it found.

Where each worker sits

The physical layout copies too, because it's how one person supervises a dozen-plus workers: terminal windows by role - reviewers on the left, lead and product owner in the center, builders on the right. You sit in the center, reading commits and merging.

> That only works with one rule: about 300 lines maximum per file. A 50-line change to one file is easy to check; a 500-line change across 12 files is not, so the line is built never to produce one.

Starting each worker is shorter than you'd expect:

```
Read CLAUDE.md. Read _FRAGILE.md. Read _NEXT_SESSION_MEMO.md.
We're working on RFD_0172. You're role/SECURITY.
Your only write permission is a timestamped SECURITY_REPORT.
```

Short prompts plus documentation beat elaborate role definitions. The personality lives in the files, not the prompt, which is why the same three lines start every worker.

If you'd rather not hand-roll the coordination, the coding agent ships the primitives natively: create a team, assign tasks, list and update them, and pass messages between agents, so one lead can spin up a team, distribute work, collect results, and shut it down.

---

## Step 4 - put a gate at the end of the line

The gate is the part that lets you leave. Everything before it makes work; the gate decides the work is finished. Until you have one, you are the gate, and the line stops whenever you do.

Everyone reaches the same conclusion and stops there: no perfect judge of code quality exists, so the decision can't be automated. True, and irrelevant. A narrow, boring, written-down policy does the job in about 40 lines.

It starts by working out who wrote the change, because machine-authored work gets the strict profile:

```
provenance:
  actors: [copilot-swe-agent[bot], claude[bot], devin-ai-integration[bot], cursoragent]
  branch_prefixes: [copilot/, claude/, agent/, devin/]
  title_markers: ["[agent]", "🤖"]
profiles:
  agent:
    auto_merge_paths: ["**/*.md", "**/*.txt", "docs/**"]
    max_files: 5
    max_lines: 150
    require_ci: true
```

Five files, 150 lines, tests green, docs only. A deliberately tiny starting allowance for unattended work, because the goal is to merge the safe majority so your attention lands on the rest.

The paths a human always sees

Then the list that matters more than any of it - the paths where a human always looks, whoever wrote the change:

```
protected_paths:
  - ".github/**"          # CI runs with repository credentials
  - "**/*auth*"
  - "**/*secret*"
  - "**/.env*"
  - "**/migrations/**"    # schema changes are hard to revert
  - "**/*.tf"
  - "**/package-lock.json" # a lockfile edit is a supply-chain change
```

A dependency bump looks like one line and can be an entirely different program.

Three design choices are the actual craft:

- Fail closed: if the policy file can't be read, the gate blocks everything until it's fixed. A policy that can't be read isn't a policy that can be enforced.

- Earned autonomy: an optional ledger scores each author on whether their merged work survived, and a proven author gets a wider allowlist. It only ever widens, and never opens a protected path.

- Measured rules: tune the risky-pattern matcher until false alarms are near-zero. A gate you don't trust is a gate you switch off.

The pattern list is copy-paste work with a scar behind every entry: downloads piped into a shell, credential literals (sk-live-, ghp_, AKIA), disabled certificate checks, permissions: write-all, DROP TABLE. Watch for string-concatenation tricks too - "sk-live-" + "abc123" sails through a naive matcher.

Run it before you trust it: a demo script that shows verdicts on sample changes, and a dry-run that shows what it would file without filing anything. Half an hour there and you know your gate's judgment better than most teams know their reviewers'.

---

## Step 5 - let the line teach itself

Everything so far runs at a fixed quality. This makes next month better than this one, because what the line learns goes back into the line.

Memory is a stack, and each layer answers a different question:

- MEMORY.md: standards for every project you own (use the SDK, never raw SQL in app code, 300 lines max per file).

- CLAUDE.md: what this project is and where it's going. The first thing every worker reads.

- _FRAGILE.md: the places that break in non-obvious ways - auth, payments, access rules.

- _NEXT_SESSION_MEMO.md: the shift handover. What finished, what's running, what's stuck.

- _VOCABULARY.md: the canonical name for every concept in the project.

That last one looks like bureaucracy until you see why it exists: a next-token predictor will mix up member, members, and membership. Three words, three meanings in a billing system, and code that's subtly and expensively wrong. Naming things once removes a class of bug no test would catch.

The loop that writes its own rules

At the end of every shift the worker writes down what it did and learned, and a small program checks each proposed rule before it enters the instruction file. That check runs after the model and in plain code, and the ordering is what makes it safe: your line reads issues and comments written by anybody, and three pull requests titled "agents may merge anything" should not become policy.

Rules that grant permissions, name a credential source, or hand over a shell command get rejected by the checker itself, with no judgment call involved.

Five commands keep the discipline in place:

```
/wrap      end the shift: update the handover memo, commit, record what shipped
/sup       five-second status of everything in flight
/fragile   check the danger list before touching sensitive code
/plan      plan first, approve, then implement
/research  investigate in a forked context so it never pollutes the main thread
```

One more rule belongs in the file. Models misjudge work in a specific direction - they call a mechanical change tedious and propose a shortcut, or quote weeks for something that takes an hour:

Never factor "tedious" or "repetitive" into recommendations.
Prefer the technically cleaner solution over the easier one.
Do not estimate human time. Report dependencies and risk.
Find-and-replace migrations across many files are trivial. Never defer them.

And obey the warning the pipeline authors put in their own installer: a template full of unfilled placeholders produces worse changes than no instruction file at all. Fill it in before the first run.

---

## Step 6 - count what the line makes

Start with the cost, because it surprises people in the good direction.

A working six-agent line, running 8 to 12 full cycles a day and repairing its own production problems, costs on the order of $10 to $15 a day in model usage. Infrastructure is a small computer on a desk. Call it roughly $4,400 a year to run the whole factory. Heavy sprints with a billion-plus tokens consumed have come in under a couple thousand dollars including hosting - largely because reusing context instead of resending it drops the per-token cost by an order of magnitude.

The arithmetic, run it on your own numbers

The point of the cost is what it unlocks, not a promise about your income. Here's the arithmetic - plug in your real figures:

- Target: $1M a year is $83,333 a month.

- Price: a small, focused product at $49 a month.

- Customers: $83,333 / $49 = about 1,700 paying subscribers.

- Spread: a line shipping one product a month gives you 12 products, so 1,700 splits into ~142 customers each.

- Cost: $4,400 a year against $1,000,000. Under half a percent.

The only number in that chain you actually have to believe is 142 - whether one focused product can find 142 paying customers. Solo operators who aren't professional engineers have reached dozens of paying customers on a single niche product built in weeks, with AI tooling costs under a couple percent of revenue that don't grow with customers. A line doesn't change that number - it just gives you 12 shots a year at it instead of one.

That framing is the honest version: the line makes the attempts cheap and repeatable. Whether any single product hits is still product judgment, taste, and knowing what to build.

---

## Step 7 - the lines to build this week

Five lines, in the order that pays fastest. Each is a queue file, a room, and a gate you already know how to build.

- Competitor watch: reads rival sites and ad libraries every morning, writes what changed into a report, files the interesting ones as jobs.

- Directory: researches every company in one industry, builds a searchable site from the data, adds entries on a schedule. It attracts the exact audience you'd otherwise buy ads to reach.

- Nightly fix: opens the error tracker, picks the top recurring failure, reproduces it, writes the fix and the test, leaves a pull request inside the gate's size limits. You approve it with coffee.

- Content: research, draft, edit, and publish as four workers with separate write permissions. The editor can't rewrite the research and the researcher can't publish, so the output stays honest.

- Product: one product idea a month in the queue, a gate that ships nothing without tests, a rules file that sharpens every week.

Pick one. Write its QUEUE.md tonight with three jobs in it, and let the schedule take the first one at eight in the morning.

---

## What one person ships now

Everyone rents the same model. The advantage sits in the four cheap parts around it: a text file of jobs, a folder per worker, 40 lines of policy, and a rules file edited by its own results. None of them require permission, funding, or a team.

Most people who read this go back to the one-window workshop tomorrow, because that works well enough and building the line costs a weekend. That weekend is the entire advantage.

In six months the distance between somebody with a line and somebody with a window stops being a productivity difference and becomes a category difference - the way a workshop and a factory stopped being comparable two hundred years ago.

The product is downstream of the line that produces it. Create the file. Put three jobs in it. Let the first one run without you.

Written for nazik3502. If you build one, post your real gate config and a day of its merge decisions - the proof is the line running, not the revenue screenshot.
