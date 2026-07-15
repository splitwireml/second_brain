---
title: "8 Loops Inside Hermes Agent (And Why They Compound)"
source: "x-bookmarks"
tweet_id: "2064377155476193362"
tweet_url: "https://x.com/IBuzovskyi/status/2064377155476193362"
author_name: "YanXbt"
author_handle: "@IBuzovskyi"
tweet_date: "Tue Jun 09 16:00:42 +0000 2026"
bookmark_date: "2026-06-09"
content_type: "x_article"
character_count: 26473
retweet_count: 21
like_count: 131
external_urls:
  - "https://github.com/NousResearch/hermes-agent)"
  - "https://github.com/lsdefine/GenericAgent)"
  - "https://github.com/stanfordnlp/dspy)"
  - "https://github.com/ai-boost/awesome-harness-engineering)"
  - "https://substack.com/@yanxbt"
---

# 8 Loops Inside Hermes Agent (And Why They Compound)

8 Loops Inside Hermes Agent (And Why They Compound)

Most agent frameworks have one loop: prompt → response → repeat.

Hermes Agent runs 8 loops simultaneously at different timescales, from milliseconds to weeks. Each loop serves a different purpose. Each one makes the others more effective. When stacked, they create a compounding system that improves with every session.

This article maps every loop inside Hermes Agent, explains how they nest, and shows what breaks when any of them fails. All technical details are verified against the official Hermes Agent developer documentation (hermes-agent.nousresearch.com/docs).

Hermes Agent reached 95,600 GitHub stars seven weeks after launch — the fastest-growing agent framework of 2026 (TokenMix, April 2026). Independent benchmarks from TokenMix show self-created skills cut research task time by 40% versus a fresh agent instance. This article shows the loop architecture behind that result.

---

## What Is a Loop in Agent Architecture

A loop is a cycle: do → check → decide → repeat or stop.

Every agent has at least one. The core loop sends a message to the model, gets a response, checks for tool calls, executes them, and loops back. Without it, there is no agent. There is only a single API call.

What separates agent frameworks is how many loops they run, at what timescales, and whether those loops feed into each other. Four types of loops exist in agent systems (per FlowZap's taxonomy):

1. Retry loops — run again after failure. Simplest form.

2. Reflection loops — one agent critiques the output before the next pass.

3. Memory loops — store a lesson that influences a future run.

4. Skill loops — encode a procedure that changes how future runs execute.

Most frameworks implement types 1 and 2. A few implement type 3. Hermes implements all four natively, plus orchestration loops that coordinate across agents and time.

---

## Loop 1 — The Core Agent Loop

---

Timescale: milliseconds to minutes per turn.

This is the heartbeat. Everything else runs on top of it.

The core loop lives in run_agent.py (AIAgent class, 15,000+ lines). Each turn follows this sequence:

```
1. Receive user message (or continuation from /goal judge)
2. Append to conversation history
3. Build or reuse cached system prompt (prompt_builder.py)
4. Check if compression is needed (>50% context)
5. Build API messages from history
6. Inject ephemeral prompt layers (budget warnings, context pressure)
7. Apply prompt caching markers (Anthropic)
8. Make interruptible API call
9. Parse response:
   → tool calls? Execute, append results, go to step 5
   → text response? Persist session, flush memory, return
```

Three API modes resolve automatically based on provider:S

All three converge on the same internal format (OpenAI-style role/content/tool_calls dicts) before and after API calls.

Tool execution within the loop:

Single tool call → executed in main thread. Multiple tool calls → executed concurrently via ThreadPoolExecutor. Results reinserted in original call order regardless of completion order.

Some tools are intercepted before reaching the registry:

Iteration budget:Default 90 iterations per session (configurable via agent.max_turns). At 100%, the agent stops and returns a summary. Subagents get independent budgets capped at delegation.max_iterations (default 50).

Interruptible calls:API requests run in a background thread while monitoring an interrupt event. When interrupted (user sends new message, /stop, or signal), the API thread is abandoned. No partial response enters conversation history.

What breaks without this loop: everything. This is the kernel.

---

## Loop 2 — The Ralph Loop (/goal)

---

Timescale: minutes to hours per goal.

Named after Ralph Wiggum. Inspired by Codex CLI 0.128.0 by Eric Traut (OpenAI). Hermes's implementation is independent, adapted to its architecture.

The core idea: keep a goal alive across turns. An auxiliary judge model evaluates after each turn: done or continue?

```
User sets /goal →
  Turn 1: agent works toward objective
  Judge evaluates: done? → no
  ↻ Continuing toward goal (1/20): [judge's reason]
  Turn 2: agent takes next step
  Judge evaluates: done? → no
  ↻ Continuing toward goal (2/20): [judge's reason]
  ...
  Turn N: agent completes
  Judge evaluates: done? → yes
  ✓ Goal achieved: [reason]
```

Technical details from official docs:

- Default max_turns: 20 (configurable via goals.max_turns)

- /goal resume resets the turn counter to zero and continues

- /subgoal adds acceptance criteria mid-loop without resetting

- Judge prompt rewrites to include all subgoals — goal is only done when original objective AND every subgoal are met

- Works identically on CLI and every gateway platform

- Goal state persists in SessionDB.state_meta

- The judge runs on the auxiliary client (can be a cheaper model than the main one)

Kanban integration:Pass --goal to kanban_create (CLI) or goal_mode=True (dashboard/tool) and the kanban worker runs in a goal loop. The judge checks the worker's output against the card's title + body as acceptance criteria.

```
/goal [description]     # start
/goal status            # check progress
/goal pause             # pause, preserve context
/goal resume            # continue, reset counter
/goal clear             # end
/subgoal [text]         # add criteria mid-run
/undo [N]               # take back last N turns
```

What breaks without this loop: agent completes one turn and stops. No multi-step reasoning. No persistent objectives. Every task must be manually supervised turn by turn.

---

## Loop 3 — The Self-Improvement Loop

---

Timescale: runs after completed tasks (minutes to hours).

This is the loop that makes Hermes different from most other agent frameworks. Official documentation describes it as "a closed learning loop."

The cycle:

```
1. Agent completes a task
2. Agent reviews what worked
3. Agent identifies reusable patterns
4. Agent saves procedure as a skill file
   → ~/.hermes/skills/[skill-name].md
5. Next similar task: agent finds the skill via search
6. Agent loads skill body into context
7. Agent executes faster using the documented procedure
8. If the procedure improves during use, agent updates the skill
```

Skills are not prompt templates. They are full procedures containing:

- When to use (trigger conditions)

- Step-by-step procedure

- Known pitfalls to avoid

- Verification steps (how to confirm it worked)

- Required tools and dependencies

The agent creates and updates skills using the skill_manage tool. After solving a complex problem, Hermes may offer to save the approach as a skill for next time.

The compounding math:From verified user benchmarks (TokenMix study, cited in official user stories): agents with 20+ self-created skills cut research-task time by ~40% compared to a fresh agent instance.

This improvement compounds. Each completed task potentially creates or refines a skill. Month 3 looks different from day 1 because the agent has accumulated 40-60 skills encoding procedures that used to require full instructions.

Nudge system:The self-improvement loop is triggered by "nudges" — periodic checks that spawn a background fork of AIAgent (same pattern used by the Curator). The fork runs in its own prompt cache and never touches the active conversation.

What breaks without this loop: every session starts from zero. The agent never learns. Day 90 output quality equals day 1. You explain the same process every time.

---

## Loop 4 — The Curator Loop

---

Timescale: runs every 7 days (default), during idle periods.

Skills accumulate. Without maintenance, you end up with dozens of narrow near-duplicates that pollute the catalog and waste tokens.

The Curator solves this.

```
Check: has interval_hours elapsed since last run? (default: 7 days)
Check: has agent been idle for min_idle_hours? (default: 2 hours)
Both true → spawn background AIAgent fork
  → scan ~/.hermes/skills/
  → identify redundant or overlapping skills
  → archive unused skills to ~/.hermes/skills/.archive/
  → compress and consolidate related procedures
  → optimize descriptions for better searchability
  → log what changed
```

From official documentation:

- Triggered by inactivity check, not a cron daemon

- Fires on CLI session start and on recurring tick inside gateway's cron-ticker thread

- First run defers by one full interval_hours on new installs (gives you time to review before it touches anything)

- Never auto-deletes. Worst outcome is archival to .archive/ (recoverable)

- By default (prune_builtins: true) can archive unused bundled skills after archive_after_days of non-use

- Hub-installed skills (from agentskills.io) are always off-limits

```yaml
curator:
  interval_hours: 168        # 7 days
  min_idle_hours: 2           # only runs when idle
  prune_builtins: true        # can archive unused built-in skills
  archive_after_days: 30      # unused threshold
```

```
hermes curator status        # check last run
hermes curator pause         # skip next run
hermes curator resume        # re-enable
```

Why this loop matters for Loop 3:The Self-Improvement Loop creates skills. The Curator Loop maintains them. Without the Curator, Loop 3 eventually degrades the system by flooding the skill index with noise. Tool Search (Loop 7) relies on accurate skill names and descriptions for retrieval. Poorly maintained descriptions degrade search accuracy.

What breaks without this loop: skill bloat. The agent accumulates hundreds of narrow, overlapping skills. Context gets polluted. Search returns wrong skills. Token usage grows without corresponding quality improvement.

---

## Loop 5 — The Memory Loop

---

Timescale: after each session and periodically during sessions.

Memory in Hermes operates across three layers:

Layer 1 — Session memory (active context):The conversation history of the current session. Lives in RAM and SQLite.

Layer 2 — Persistent memory (MEMORY.md + USER.md):Facts, preferences, and insights that survive across sessions. Auto-written by the agent when it identifies important information.

```yaml
memory:
  memory_enabled: true
  user_profile_enabled: true
  memory_char_limit: 2200    # ~800 tokens, injected every turn
  user_char_limit: 1375      # ~500 tokens, injected every turn
```

Layer 3 — Session recall (FTS5 full-text search):Every CLI and messaging session stored in SQLite (~/.hermes/state.db) with FTS5 full-text search. Search queries return actual messages from the DB — no LLM summarization, no truncation.

The memory loop cycle:

```
1. Agent processes conversation turn
2. Periodic check: is there important information to persist?
3. If yes: write to MEMORY.md or USER.md (capped by char limits)
4. On session end: flush all pending memory writes
5. Next session: MEMORY.md and USER.md injected into system prompt
6. Agent has accumulated context without re-explanation
```

Memory nudges follow the same background-fork pattern as the self-improvement loop and the Curator.

External memory providers (8 plugins):For deeper intelligence beyond built-in memory:

- Mem0 (knowledge graph + semantic retrieval, 72% fewer tokens vs naive injection)

- Honcho (two-peer dialectic: USER observations + AI observations)

- Hindsight, Holographic, RetainDB, ByteRover, Supermemory, OpenViking

Built-in memory continues to work alongside external providers. The external provider is additive.

What breaks without this loop: the agent forgets everything between sessions. You re-explain your preferences, your projects, your workflow every time you start a new conversation. No compounding.

---

## Loop 6 — The Kanban Dispatcher Loop

---

Timescale: every 60 seconds.

The Kanban system is the orchestration layer that coordinates multiple agents and tasks.

```
Every 60 seconds:
  1. Scan kanban board (SQLite: ~/.hermes/kanban.db)
  2. Find tasks in Ready status
  3. Assign to available workers
  4. Track heartbeats on Running tasks
  5. Detect zombie processes (worker died but card still Running)
  6. Reclaim zombie cards (reset to Ready for retry)
  7. Check retry budgets (don't retry infinitely)
  8. Report blocked tasks for human review
```

Statuses: Triage → To-Do → Ready → Running → Blocked → Done → Archived

Kanban Swarm architecture:

```
hermes kanban swarm
```

Spawns: root orchestrator + parallel workers + gated verifier + gated synthesizer + shared blackboard.

Human-in-the-loop:When a task enters Blocked status, execution pauses until a human provides input. Approval buttons are native in Telegram and Slack.

Kanban is deliberately single-host. kanban.db is a local SQLite file. The dispatcher spawns workers on the same machine. Multi-host is not supported — there is no coordination primitive for workers across hosts. For multi-host setups, run an independent board per host and use delegate_task or a message queue to bridge them.

Integration with /goal (Loop 2):Pass --goal or goal_mode=True when creating a kanban card. The worker runs in a goal loop instead of single-shot mode. The judge checks worker output against the card's title + body as acceptance criteria.

What breaks without this loop: multi-agent work becomes manual coordination. You track tasks in your head or in a spreadsheet. Crashed tasks go unnoticed. No retry. No visibility.

---

## Loop 7 — The Compression Loop

---

Timescale: fires when context usage exceeds thresholds.

Hermes runs a dual compression system:

```
Layer 1 — Gateway Session Hygiene (85% threshold)
  Safety net. Fires before the agent processes a message.
  Prevents API failures when sessions grow too large
  between turns (overnight accumulation in Telegram).
  Uses rough character-based token estimate.

Layer 2 — Agent ContextCompressor (50% threshold, configurable)
  Primary compression system. Fires inside the agent's
  tool loop with access to accurate API-reported token counts.
```

The compression algorithm (4 phases):

```
Phase 1 — Prune old tool results (cheap, no LLM call)
  Tool results > 200 chars outside the protected tail
  get replaced with:
  [Old tool output cleared to save context space]

Phase 2 — Check if Phase 1 was enough
  Re-estimate tokens. If below threshold: done.
  If still over: proceed to Phase 3.

Phase 3 — Summarize middle conversation turns
  LLM call to summarize the compressible region.
  Protected: first 3 messages + last 20 messages.
  Tool call/result pairs never split.

Phase 4 — Create new session lineage
  Compression creates a "child" session ID.
  Memory flushed to disk BEFORE compression
  to prevent data loss.
```

Configuration:

```yaml
compression:
  enabled: true
  threshold: 0.50         # compress at 50% of context window
  target_ratio: 0.20      # how much of threshold to keep as tail
  protect_last_n: 20      # recent messages always preserved

auxiliary:
  compression:
    model: null            # cheaper model for summaries
    provider: auto
```

Pluggable context engine:

```yaml
context:
  engine: "compressor"    # default, lossy summarization
  engine: "lcm"           # plugin, lossless context management
```

Plugins can replace the built-in engine. The user must explicitly set context.engine — plugins are never auto-activated.

What breaks without this loop: long sessions hit context window limits. API calls fail. The agent either crashes or the provider returns truncated responses. Multi-turn /goal runs become impossible beyond 15-20 turns.

---

## Loop 8 — The Sub-Agent Loop

---

Timescale: minutes per sub-agent, parallel execution.

delegate_task spawns child agents with isolated context. Each child runs its own core loop (Loop 1) independently.

Token cost note: each sub-agent runs its own full Loop 1 session. 3 concurrent sub-agents ≈ 3x your single session cost. Use cheaper models for sub-agents doing routine or research work. Reserve expensive models for the parent orchestrator where output quality matters.

```
Parent agent receives complex task
  → Spawns sub-agent 1 (own context, own tools)
  → Spawns sub-agent 2 (own context, own tools)
  → Spawns sub-agent 3 (own context, own tools)
  
  Max concurrent: delegation.max_concurrent_children (default 3)
  
  Each sub-agent:
    → Runs core loop (Loop 1)
    → Can use /goal (Loop 2) if goal_mode=True
    → Creates skills (Loop 3) from completed work
    → Writes to memory (Loop 5) if relevant
    → Runs compression (Loop 7) if needed
    
  Sub-agents return summaries to parent
  Parent's context stays light
  
  Roles:
    leaf (default): cannot re-delegate
    orchestrator: can spawn its own workers
    bounded by delegation.max_spawn_depth
```

Single task:

> delegate_task(goal="research X", context="...", toolsets=[...])

Batch (parallel):

> delegate_task(tasks=[
  {goal: "research topic A", ...},
  {goal: "research topic B", ...},
  {goal: "research topic C", ...}
])

Children run in parallel, capped by max_concurrent_children. Total iterations across parent + subagents can exceed the parent's cap (each gets its own budget).

What breaks without this loop: every task runs sequentially in one context. Complex tasks requiring parallel research, analysis from multiple angles, or simultaneous code review across modules all bottleneck on a single agent.

---

## How The Loops Nest

---

The loops do not run independently. They nest inside each other and across timescales:

```
WEEKLY:
  Loop 4 (Curator) runs → cleans skills from Loop 3
    → improves accuracy of Loop 7 (Tool Search in skills)

DAILY:
  Cron job fires →
    Loop 6 (Kanban) assigns task →
      Loop 2 (/goal) starts on the task →
        Loop 1 (Core) executes each turn →
          Loop 7 (Compression) fires if context grows →
          Loop 8 (Sub-agents) spawn for parallel work →
            Each sub-agent runs its own Loop 1
        Loop 3 (Self-improvement) fires after task completes →
          New skill saved
      Loop 5 (Memory) writes persistent facts

EVERY SESSION:
  Loop 5 (Memory) injects MEMORY.md + USER.md
  Loop 1 (Core) runs turns
  Loop 7 (Compression) manages context
  Loop 3 (Self-improvement) reviews and saves
```

The compounding chain:

- Loop 3 (skills) makes Loop 2 (/goal) faster because the agent has documented procedures

- Loop 4 (Curator) keeps Loop 3 clean so skills stay searchable

- Loop 5 (memory) gives Loop 1 context about you and your preferences

- Loop 6 (Kanban) orchestrates multiple Loop 2 instances in parallel

- Loop 7 (compression) keeps Loop 1 affordable across long runs

- Loop 8 (sub-agents) multiplies Loop 1 capacity for parallel work

Remove any single loop and the others degrade. Remove Loop 3 and the agent never improves. Remove Loop 4 and Loop 3 eventually bloats the system. Remove Loop 7 and long sessions crash. Remove Loop 5 and every session starts cold.

The system works because the loops are designed to feed each other.

## How Hermes Compares to Other Loop Architectures

Not every agent framework implements the same loops. Here is where the landscape stands:

GenericAgent (github.com/lsdefine/GenericAgent, 12.4K stars) takes a different approach: minimal seed code (~3K lines, 9 atomic tools) that self-evolves into a full system. Their goal mode uses time budgets instead of turn budgets ("keep optimizing X for N hours"). Token consumption is 6x lower than comparable frameworks per their technical report

DSPy (github.com/stanfordnlp/dspy, 25K+ stars, Stanford NLP) treats prompts as programs and optimizes them against metrics. Different philosophy from Hermes: DSPy optimizes the prompt through compilation. Hermes optimizes the procedure through skill creation. DSPy is the most serious optimization engine in the space. Hermes is the most complete self-improving runtime.

Hermes's advantage is that all 8 loops are native, integrated, and designed to feed each other. Most other frameworks implement 2-3 loops and leave the rest to the user.

## What Breaks When a Loop Fails

Each loop has a specific failure mode:

The most dangerous failure: Loop 3 saving a bad skill. A wrong procedure gets reused across future sessions, compounding the error. This is why Loop 4 (Curator) and human review both exist. The Curator catches stale skills. Human review catches wrong skills.

---

## Configuration Reference

---

All loop-related settings in one place:

```yaml
# Loop 1 — Core
agent:
  max_turns: 90                    # iteration budget per session

# Loop 2 — /goal
goals:
  max_turns: 20                    # turns per goal run

# Loop 3 — Self-improvement
# No direct config. Controlled by skill_manage tool availability
# and nudge system (background fork pattern)

# Loop 4 — Curator
curator:
  interval_hours: 168              # 7 days between runs
  min_idle_hours: 2                # only runs when idle
  prune_builtins: true             # can archive unused built-ins
  archive_after_days: 30           # unused threshold

# Loop 5 — Memory
memory:
  memory_enabled: true
  user_profile_enabled: true
  memory_char_limit: 2200          # ~800 tokens
  user_char_limit: 1375            # ~500 tokens

# Loop 6 — Kanban
# Dispatcher runs every 60 seconds (not configurable)
# Zombie detection and heartbeat tracking automatic

# Loop 7 — Compression
compression:
  enabled: true
  threshold: 0.50                  # compress at 50% of context
  target_ratio: 0.20
  protect_last_n: 20

context:
  engine: "compressor"             # or "lcm" for lossless

auxiliary:
  compression:
    model: null                    # cheaper model for summaries
    provider: auto

# Loop 8 — Sub-agents
delegation:
  max_concurrent_children: 3
  max_iterations: 50               # budget per sub-agent
  max_spawn_depth: 2               # orchestrator nesting limit
```

## Token Cost Per Loop

---

Not all loops cost tokens equally. Some are free. Some are the main cost driver.

Estimates based on typical usage patterns. Use /usage in Hermes to measure your actual numbers.

Cheapest loops: Kanban (zero), Curator (minimal), Compression (net saver). Most expensive: Sub-agents (multiplier), /goal (20x core turns), Core (base cost).

Optimization priority:

1. Use auxiliary model for /goal judge and compression (cheap model for side-jobs)

2. Lower memory char limits on profiles that don't need deep context

3. Set realistic max_turns per profile (20 for research, 50 only for code)

4. Enable Tool Search to avoid loading unused schemas

5. Run routine cron jobs on cheaper models (GPT-5.5 via Codex at $0)

For full token economics breakdown and monthly budget calculations, see: [Hermes Agent as a Personal AI Operating System](https://x.com/IBuzovskyi/status/2063645563241844823?s=20) — Section 3: Token Economics

---

## Start Here

---

Read about 8 loops and don't know where to begin. Three steps:

Step 1 — Get Loop 1 + Loop 5 running (5 minutes)

Install Hermes. Run hermes setup --portal. Start a session. Talk to it. Memory writes happen automatically. Loop 1 (core) and Loop 5 (memory) are active from the first message.

Step 2 — Add Loop 2 (next 10 minutes)

Run your first structured /goal:

```
/goal [what you want done]
using [what sources to check]
with constraints: [what to avoid]
deliverable: [what "done" looks like]
```

The agent works across multiple turns until the judge says done. Loop 3 (self-improvement) fires automatically after the goal completes.

Step 3 — Add time and orchestration (next 30 minutes)

Set your first cron job. Something small:

> Every morning at 8am send me a summary
of trending AI news to Telegram.

You now have 5 loops running: Core (1), /goal (2), Self-improvement (3), Memory (5), and Compression (7, fires automatically when needed).

Kanban (6), Curator (4), and Sub-agents (8) activate as your usage grows. The Curator starts after 7 days. Sub-agents spawn when you use delegate_task. Kanban activates when you track multiple tasks.

You don't configure all 8 on day one. You start with 2. The rest come online as your system expands.

---

## The Real Insight

---

Agent frameworks are defined by their loops. A framework with one loop (prompt → response) is a chat wrapper. A framework with two loops (prompt → response → retry) is slightly better. A framework with all 8 is an operating system.

Hermes runs 8 loops across timescales from milliseconds to weeks. Each loop feeds the others. Skills make goals faster. The Curator keeps skills clean. Memory gives every session context. Kanban orchestrates parallel work. Compression keeps costs manageable. Sub-agents multiply capacity.

The compounding happens in the intersection of these loops, not in any single one. An agent that improves its own procedures AND maintains those procedures AND remembers your preferences AND orchestrates parallel work AND manages its own context is a fundamentally different tool than one that responds to prompts.

That is the loop architecture of Hermes Agent.

For the full architectural mapping of all 17 layers, read: [Hermes Agent as a Personal AI Operating System](https://x.com/IBuzovskyi/status/2063645563241844823?s=20) — OS mapping, token economics, comparison table, practical setup paths.

## Related Articles

- [Hermes Agent as a Personal AI Operating System](https://x.com/IBuzovskyi/status/2063645563241844823?s=20) — 17-layer OS mapping, architecture deep-dive

- [10 Setups That Turned Hermes Agent From a Chat Window Into a 24/7 System](https://x.com/IBuzovskyi/status/2062101068842975409?s=20) — practical setup guide

- [HERMES AGENT: THE COMPLETE GUIDE](https://x.com/IBuzovskyi/status/2059675518966894767?s=20) — installation, models, dashboard, use cases

Referenced projects:

- [Hermes Agent](https://github.com/NousResearch/hermes-agent) — source, docs, issues

- [GenericAgent](https://github.com/lsdefine/GenericAgent) — self-evolving agent, 12.4K stars, minimal seed code

- [DSPy](https://github.com/stanfordnlp/dspy) — prompt optimization framework, 25K+ stars, Stanford NLP

- [awesome-harness-engineering](https://github.com/ai-boost/awesome-harness-engineering) — comprehensive agent engineering list

All technical details verified against Hermes Agent developer documentation (v0.16.0) and official source code references. Loop architecture diagrams based on run_agent.py, context_compressor.py, gateway/run.py, and curator module documentation.

Too read new articles days and hours before X release subcribe to my Substack: https://substack.com/@yanxbt

@Teknium @NousResearch
