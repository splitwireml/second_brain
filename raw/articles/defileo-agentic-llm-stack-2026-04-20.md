---
title: "defileo"
source: "x-bookmarks"
tweet_id: "2046305855054721187"
tweet_url: "https://x.com/defileo/status/2046305855054721187"
author_name: "Defileo🔮"
author_handle: "@defileo"
tweet_date: "2026-04-23"
bookmark_date: "2026-04-20"
content_type: "x_article"
character_count: 9591
retweet_count: 0
like_count: 0
---

external_urls:
  - "https://www.skool.com/ai-builderss/classroom"
---

# Claude is dumb by default, one file changes that

Claude is dumb by default, one file changes that

Don't you think Claude is literally pretends to be stupid? It doesn't listen to you properly, and many people ignore this so they're burning more tokens.

I've been scrolling on the Github and found the repo that fully changes the game.

One file, 44k+ new stars in seven days, and most people using Claude Code have never heard of it.

Here is what it is, why it exists, and how to install it in two minutes.

---

🚨 Before we start, me and @noisyb0y1 are launching a completely free AI course, everything you need to go from zero to building real projects with AI in a weekend.

Leaving all details at the end of this article, let's get started:

---

Andrej Karpathy, co-founder of OpenAI, former Tesla AI director, shifted to roughly 80% agent-driven development. 

Then he posted an honest breakdown of everything that was wrong with how AI coding tools actually behave.

Three quotes read them slowly:

> "The models make wrong assumptions on your behalf and just run along with them without checking. They don't manage their confusion, don't seek clarifications, don't surface inconsistencies, don't present tradeoffs, don't push back when they should"

> "They really like to overcomplicate code and APIs, bloat abstractions, don't clean up dead code. Implement a bloated construction over 1000 lines when 100 would do"

> "They still sometimes change and remove comments and code they don't sufficiently understand as side effects, even if orthogonal to the task"

## Every developer using Claude Code recognized this instantly.

A developer named Forrest Chang read the post and built a fix, one CLAUDE.md file, four principles, it rewires how Claude Code behaves on every task and 45,000 people installed it this week.

---

## What it actually does

A CLAUDE.md file is a behavior configuration that Claude Code reads automatically at the start of every session, whatever is in it becomes part of how Claude thinks about your project.

This file adds four principles derived directly from Karpathy's complaints. Each one fixes a specific habit.

Here is the full file, copy it right now.

```
# CLAUDE.md

Behavioral guidelines to reduce common LLM coding mistakes. 
Merge with project-specific instructions as needed.

**Tradeoff:** These guidelines bias toward caution over speed. 
For trivial tasks, use judgment.

## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them. Don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" 
If yes, simplify.

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it. Don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: every changed line should trace directly to the user's request.

## 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]

Strong success criteria let you loop independently. 
Weak criteria ("make it work") require constant clarification.

---

**These guidelines are working if:** fewer unnecessary changes in diffs, 
fewer rewrites due to overcomplication, and clarifying questions come 
before implementation rather than after mistakes.
```

That is the whole thing, four principles, one file.

## What each principle actually changes

Principle 1: Think Before Coding, before this file:

```
You: "Add a caching layer to this API endpoint."

Claude: [builds Redis integration with TTL config, 
cache invalidation hooks, fallback logic, 
and a full abstraction layer]

You: "I just meant in-memory caching for now."
```

After this file:

```
You: "Add a caching layer to this API endpoint."

Claude: "Before I start, two interpretations:
1. In-memory cache for this session only
2. Persistent cache like Redis across requests

Which did you mean? Also, should cache 
invalidation be time-based or manual?"

You: "In-memory, time-based, 60 seconds."

Claude: [builds exactly that. Nothing else.]
```

The confusion surfaces before the work happens, not after.

Principle 2: Simplicity First, before this file:

```
# You asked for: "a function that checks if a user is an admin"

class UserPermissionManager:
    def __init__(self, config=None, cache_ttl=300):
        self.config = config or {}
        self.cache = {}
        self.cache_ttl = cache_ttl
        self._permission_registry = defaultdict(list)
    
    def check_permission(self, user_id, permission_type, 
                         context=None, fallback=True):
        # 47 more lines...
```

After this file:

```
# You asked for: "a function that checks if a user is an admin"

def is_admin(user_id: str) -> bool:
    return user_id in ADMIN_USER_IDS
```

Would a senior engineer say the first version is overcomplicated? Yes. So Claude rewrites it.

## Principle 3: Surgical Changes

Before this file, you ask Claude to fix one bug in a 200-line file. You get back:

```
- def process_order(order_id, user):
+ def process_order(order_id: str, user: User) -> dict:
    # Fixed the null check bug
-   if order == None:
+   if order is None:
        return None
+   
+   # Refactored for clarity
-   x = get_order(order_id)
+   order = get_order(order_id)
-   # check user
+   # Validate user permissions before processing
    if not user.can_access(order):
```

You asked it to fix a null check. It added type hints, renamed variables, rewrote comments, and refactored the function signature.

After this file:

```
-   if order == None:
+   if order is None:
        return None
```

One change. The one you asked for. Nothing else.

## Principle 4: Goal-Driven Execution

This is the one Karpathy called the key insight.

> "LLMs are exceptionally good at looping until they meet specific goals. Don't tell it what to do. Give it success criteria and watch it go."

Before this file:

```
You: "Fix the login bug."
Claude: [makes a change]
You: "That didn't fix it."
Claude: [makes another change]
You: "Still broken."
Claude: [makes another change]
```

After this file:

```
You: "Fix the login bug."

Claude: "Here is my plan:
1. Write a test that reproduces the bug → verify: test fails
2. Identify root cause → verify: can explain why test fails
3. Implement fix → verify: test passes
4. Check no other tests broke → verify: full suite green

Starting now."

[Claude loops independently until all four checks pass]
[You review finished work]
```

You stop babysitting -> you start reviewing.

---

## The most important part, How to install it:

Two options, pick one.

Option A: Plugin (installs across all your projects)

> Open Claude Code and run these two commands one after the other:

```
/plugin marketplace add forrestchang/andrej-karpathy-skills
```

```
/plugin install andrej-karpathy-skills@karpathy-skills
```

Active immediately. Works in every project from this session forward.

Option B: Per-project (drop it into one repo) you can find it in the repo on github link that I left at the start of this article.

## How to Add Your Own Rules On Top

The file is designed to be merged with project-specific instructions. After the four principles, add a section like this:

```
## Project-Specific Guidelines

- Use TypeScript strict mode
- All API endpoints must have integration tests
- Follow error handling patterns in src/utils/errors.ts
- Never commit directly to main
```

Your project rules sit on top of the four principles, both apply

## How you know it is working:

Three things change that you will notice immediately.

Your diffs get cleaner. Only what you asked for shows up. No reformatted functions. No renamed variables. No improved comments you never mentioned.

Clarifying questions come before implementation, claude stops guessing and starts asking. You spend less time throwing away wrong work.

Code is simpler the first time. No rewrites because it overengineered the solution. No abstractions that made sense to Claude but nobody asked for.

---

## Cherry on top for the AI frens:

if you made it this far, you deserve it: a completely free AI course, built for people who actually want to learn.

> https://www.skool.com/ai-builderss/classroom

More is coming, and it's going to be bigger than anything we've dropped so far stay tuned, grab your spot early, and get ready to fall deep into the AI rabbit hole.

- Leo
