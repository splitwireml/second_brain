---
title: Loop Engineering
created: 2026-06-11
updated: 2026-08-03
type: concept
tags: [workflow, orchestration, agent, claude-code, codex, ai-research, training, evaluation]
sources: [raw/articles/xarticle-loop-engineering-2064127981161959567.md, raw/articles/xarticle-from-prompting-agents-to-loop-engineering-2068008743153832264.md, raw/articles/xarticle-wtf-is-a-loop-part-2-the-15-loops-people-are-actua-2068426104088748331.md, raw/articles/thread-zodchiii-2070809778153832264.md, raw/articles/thread-eng_khairallah1-2071964839916802354.md, raw/articles/xarticle-loop-engineering-in-5-minutes-no-code-required-2073391903819608421.md, raw/articles/xarticle-what-the-hell-is-a-loop-anyway-2073492320159510869.md, raw/articles/xarticle-getting-started-with-loops-2074208949205881033.md, raw/articles/xarticle-how-i-get-frontier-results-from-any-model-the-harn-2074195371920666718.md, raw/articles/xarticle-own-the-outer-loop-2074927530482835916.md, raw/articles/xarticle-codex-built-8-features-overnight-5-step-pr-loop-2073470146115490230.md, raw/articles/xarticle-the-engineering-loop-that-powers-1-of-builders-2076880438677946396.md, raw/articles/thread-alex_prompter-2076727080402948561.md, raw/articles/thread-NVIDIAAI-2077061428998013279.md, raw/articles/xarticle-the-dark-arts-of-skill-engineering-2077114326985687525.md, raw/articles/xarticle-a-beginners-guide-to-metacognition-2079624266707054825.md, raw/articles/xarticle-graph-engineering-how-to-run-1000-ai-agents-in-par-2079899723947712845.md, raw/articles/xarticle-eval-engineering-build-the-gate-that-lets-your-age-2083540339147567268.md]
related_entity: [[claude-code]]
---

# Loop Engineering

Loop engineering is the practice of replacing manual turn-by-turn prompting with a repeatable control system that finds work, runs agents, checks outcomes, and persists state outside any one context window. The shift is not "use more agents" so much as "design the loop that decides when and how agents run."

A short June 27 bookmark quoting a [[shopify]] engineering leader compresses the argument into its cleanest social form: strong engineers are no longer optimizing one-off [[prompt-engineering]] tactics; they are building loops that keep making progress without constant manual steering.^[raw/articles/thread-zodchiii-2070809778150953343.md]

A later Khairallah bookmark adds a more file-native version of the same idea: whether or not the claimed [[andrej-karpathy]] / [[anthropic]] backstory is literally true, the memorable takeaway is that a `LOOPS.md` operating file can materially change model behavior by externalizing workflow, evaluation style, and preferred recurrence. In that framing, the operator is no longer "talking to the model" so much as maintaining the control surface that talks to the model for them.^[raw/articles/thread-eng_khairallah1-2071964839916802354.md]

## What people mean by "loop"

Across the ingested sources, *loop* is being used for at least five different layers of the same idea:

1. **ReAct-style iteration** — reason, act, observe, repeat
2. **Goal loops** — self-prompting until a task is done or fails to converge
3. **Context-reset loops** — deliberate fresh-context reruns to avoid drowning in prior history
4. **Built-in agent loops** — runtime primitives like [[goal-primitive]] and `/loop` that keep acting until a measurable condition is satisfied or cleared
5. **Full orchestration** — one controller coordinating many agents, tools, and queues over time

The useful synthesis is that loop engineering sits above all of them: the engineer chooses which kind of repetition is needed, how progress is checked, and when the system must stop.

Aparna Dhinakaran's July 2026 field guide makes the vocabulary conflict explicit by separating four architectures that were being collapsed into the same word: the agent execution loop, Ralph-style task loop, product-level software factory loop, and autoresearch/system loop. It also names the outer human oversight loop: the layer that sets goals, allocates budgets, decides what to cull, and chooses how far to turn the autonomy dial for each inner loop.^[raw/articles/xarticle-what-the-hell-is-a-loop-anyway-2073492320159510869.md]

Addy Osmani's July 2026 follow-up sharpens that oversight layer into **outer-loop ownership**. The inner loop is capability: investigate, implement, verify, and repeat inside a harness. The outer loop is agency: set constraints, choose sampling and audit policies, decide the production verdict, and remain answerable for the result. His quality → verdict → answerability chain reframes loop engineering as an accountability system rather than a pure automation pattern.^[raw/articles/xarticle-own-the-outer-loop-2074927530482835916.md]

The [[claude-devs]] article adds the official Claude Code operator taxonomy: classify loops by trigger, stop condition, primitive, and task fit. In that taxonomy, turn-based loops are just normal prompt cycles, goal-based loops hand off the stop condition to [[goal-primitive]], time-based loops use `/loop` or `/schedule` for watch-and-react work, and proactive loops compose schedules, goals, dynamic workflows, and auto mode for recurring streams of bounded work.^[raw/articles/xarticle-getting-started-with-loops-2074208949205881033.md]

The NVIDIA AI thread supplies a concrete autoresearch/system loop outside software delivery: a coding agent used a five-hour budget plus NeMo RL, NeMo Gym, and reusable skills to set up training, evaluate a vision model, and propose a next experiment while the researcher steered priorities. The reported 25% → 96.9% accuracy jump is source-reported; the durable pattern is that the time budget bounds search while the human owns direction and standards of evidence.^[raw/articles/thread-NVIDIAAI-2077061428998013279.md]

## Metacognition as the outer-loop diagnostic

Will Chen's article makes outer-loop ownership actionable as a human-side debugging practice. When work feels stuck, inspect the operating level, whether the search is diverging or converging, whether anything has touched reality, and what budget remains; then change the mechanism instead of grading the person. The four readings complement the machine-side loop by helping the operator decide when to regenerate, narrow scope, sample the world, or stop adding branches. [[metacognition-human-ai-systems]] develops this diagnostic in detail.^[raw/articles/xarticle-a-beginners-guide-to-metacognition-2079624266707054825.md]

## When a loop becomes a graph

[[0xwast3]]'s article draws a useful boundary: a loop is one unit's act → check → adjust cycle, while a graph is a network of such units whose edges encode actual dependencies. A chain can therefore be a graph with too many edges; removing fake edges exposes independent work without abandoning verification or bounded iteration.^[raw/articles/xarticle-graph-engineering-how-to-run-1000-ai-agents-in-par-2079899723947712845.md]

This is a complement to loop engineering rather than a replacement for it. Each node can still run a bounded improvement loop, while [[graph-engineering]] determines which nodes may run concurrently, where fan-in barriers belong, and how missing results are surfaced before synthesis.^[raw/articles/xarticle-graph-engineering-how-to-run-1000-ai-agents-in-par-2079899723947712845.md]

## Core building blocks

Addy Osmani's earlier framing emphasizes five operational building blocks plus external memory. The later @omarsar0 article lands on a nearly equivalent six-part checklist:

1. **Triggers / automations** — schedules, webhooks, or lifecycle events that start work without manual prompting
2. **Isolation** — worktrees or private checkouts so parallel agents do not overwrite each other
3. **Written context / skills** — durable instructions, conventions, and project rules that the loop can reload every run
4. **Connectors and tool reach** — issue trackers, CI, chat, browsers, databases, and other systems the loop must inspect or update
5. **Independent verification** — a distinct checker, reviewer, or evaluator so the producer is not grading itself
6. **External state** — markdown files, boards, or queues that survive compaction and session boundaries

That convergence matters because it suggests loop engineering is stabilizing into infrastructure rather than remaining a bag of hacks.

Alex Prompter's July 13 plugin thread supplies a concrete model-transfer and verification case. The source-described Fable method has three separable surfaces: `fable-method` encodes a structured loop with hard failure thresholds, `fable-loop` runs tasks with adversarial verification agents, and `fable-judge` independently reruns completion claims. Alex reports 159 runs in which Sonnet plus the plugin matched Fable 10/10 on a five-part research task; Haiku moved from 0/4 to 4/4 on catching a wrong test, while the judge moved Haiku from 3/5 to 5/5 on planted-fraud checks. The thread also records v1 → v2 → v3 self-tests of 0/4, 1/4, and 4/4, with failed versions and raw judge transcripts retained. These are source-reported evaluations, not independent wiki benchmarks.^[raw/articles/thread-alex_prompter-2076727080402948561.md]

The documented limit is part of the result: on ordinary tasks with capable models, the plugin may add nothing. That makes the pattern a targeted reliability layer for wrong tests, false completion claims, and unattended weaker-model work—not a universal substitute for model capability or domain knowledge.^[raw/articles/thread-alex_prompter-2076727080402948561.md]

[[phosphenq]]'s harness guide adds the model-swapping interpretation of the same stack: context, loop, tools, checks, and memory are the persistent control surface, while the LLM underneath can be replaced. That makes loop engineering less about a clever prompt cadence and more about building a [[model-agnostic-agent-harness]] whose verifier, state, and permissions survive model churn.^[raw/articles/xarticle-how-i-get-frontier-results-from-any-model-the-harn-2074195371920666718.md]

## Practical shape

The recurring control pattern is simple: set a goal, act, check, feed back the error, and repeat until the check passes or the loop halts on budget. In practice, good loops add explicit limits on runtime, attempts, changed files, or spend.

One concrete example from the newer source is a **PR babysitter**:

- wake on a schedule
- inspect open PRs with a specific label
- attempt one deterministic CI fix or one rebase
- stop after a bounded budget
- hand back to a human when green or exhausted

That same pattern generalizes to failing-CI clustering, deploy verification, and feedback triage. The point is not the specific task; it is that the loop owns recurrence, verification, and stop conditions.

## Spec-driven autonomous coding loops

[[jacob-klug]]'s article turns the general loop pattern into a software-factory recipe: a plain-text spec enumerates features and user stories, and each item has a concrete "done" condition that acts as the contract. An orchestrator then runs a bounded build → test → fix cycle, while an independent verifier exercises user behavior, a live tracker records status and failures, and parallel runs keep work moving.^[raw/articles/xarticle-the-engineering-loop-that-powers-1-of-builders-2076880438677946396.md]

The case study compares [[lovable-dev]] multi-task mode with [[claude-code]] `/loops` on an Asana-like clone. The anatomy is tool-independent: spec, orchestrator, verifier, tracker, and parallel execution. The reported under-$10 run and unattended completion are source claims, not independently audited here; the article still retains a short human pass for UI quirks, unverified behaviors, and deliberate deployment.^[raw/articles/xarticle-the-engineering-loop-that-powers-1-of-builders-2076880438677946396.md]

## Manager-worker PR loop

[[manager-worker-pr-loop]] is a concrete software-shipping instance of the same architecture: a manager thread owns recurrence and coordination, workers operate in isolated worktrees, PRs provide the handoff boundary, and CI/manual checks provide the finish line. The source's 5–10 minute heartbeat and `/goal` on every worker make the recurrence and completion contract explicit, while the reported UI failures show why a loop still needs human judgment.^[raw/articles/xarticle-codex-built-8-features-overnight-5-step-pr-loop-2073470146115490230.md]

## The three command surfaces

The new Matt Van Horn synthesis sharpens the vocabulary that earlier loop-discourse often blurred: `/goal` means keep working until an outcome is proven, `/loop` means repeat on a cadence while a human is present, and `/schedule` or cloud automation means keep working while the operator is away.^[raw/articles/xarticle-wtf-is-a-loop-part-2-the-15-loops-people-are-actua-2068426104088748331.md] This distinction matters because many examples that look like the same "agent loop" are actually different control surfaces with different safety and cost profiles.

That article also usefully grounds loop engineering in concrete examples rather than architecture talk alone: build-test-fix loops, verifier loops, repository-maintainer cadences, post-commit review hooks, human-approval pauses, and overnight PR babysitters all share the same skeleton but differ in trigger, verifier, and stop condition.^[raw/articles/xarticle-wtf-is-a-loop-part-2-the-15-loops-people-are-actua-2068426104088748331.md]

## Why /goal matters

The newer sources make a useful distinction: a strong `/goal` behaves less like a prompt and more like a contract. Good goal loops specify four things clearly:

- the desired end state
- the evidence that proves it
- the constraints that must remain intact
- the budget the agent is allowed to spend

This connects loop engineering directly to [[claude-code]] runtime behavior. Once completion conditions, turn cadence, and evaluator roles are built into the tool, the leverage point moves further upward into architecture design and verifier quality.

The AI Guides walkthrough restates the same pattern for non-technical operators: stop writing instructions and start writing conditions. Its four-part anatomy — goal, scope, checker, and stop rule — is useful because it makes loop design testable even when the loop is just a single `/goal` command rather than a larger scheduler or multi-agent system.^[raw/articles/xarticle-loop-engineering-in-5-minutes-no-code-required-2073391903819608421.md]

## Skills as loop infrastructure

The local article's Impeccable case study shows how a skill can supply loop machinery instead of merely starting a prompt. Blind sub-agents provide independent review, snapshots carry a fix backlog across sessions, scripts emit computed next steps, hooks re-check uninvoked edits, and a blocking browser poll turns live interaction into the next loop input.^[raw/articles/xarticle-the-dark-arts-of-skill-engineering-2077114326985687525.md]

The durable synthesis is a bounded loop with explicit gates: route only the needed expert, force divergence when the model clusters around safe defaults, compile behavior for the target harness, and design stop conditions that weaker models cannot silently skip. Impeccable is the source-described example; the techniques remain claims from the article rather than independent benchmarks.^[raw/articles/xarticle-the-dark-arts-of-skill-engineering-2077114326985687525.md]

## Why verification and budgets dominate

The June 20 article makes the community consensus explicit: a loop without an independent judge simply automates being wrong faster, while a loop without a budget becomes a token-burning machine.^[raw/articles/xarticle-wtf-is-a-loop-part-2-the-15-loops-people-are-actua-2068426104088748331.md] That reframes loop engineering away from hype and toward operational economics: the hard part is not getting an agent to keep going, but getting it to stop at the right moment for the right reason.

That is why the strongest loop patterns converge on the same constraints:

- independent verifier or adversarial reviewer
- explicit retry / iteration caps
- cost ceilings or daily budgets
- durable state so crashes do not erase progress
- escalation paths when the loop stalls or hits ambiguous terrain

## Verdict-driven loops and merge gates

Hanako's eval-engineering course makes the verdict part of the loop rather than a dashboard afterthought: low grounding rejects a handoff, schema failure blocks an edge, suspected fabrication quarantines a branch, and only verified completion ends a run. The source distinguishes an agent stopping tool calls from actually finishing, so an external check must own the finish line. ^[raw/articles/xarticle-eval-engineering-build-the-gate-that-lets-your-age-2083540339147567268.md]

The same gate opens by blast radius instead of one confidence threshold. Reversible contained changes can open after evidence; wide changes such as shared utilities or schemas need deterministic checks plus a clean trajectory; migrations, deletions, production-data writes, and money movement remain closed regardless of score. Evidence is read in order: tests/types/schema/sandbox, then the agent-version trajectory, then rollback history, with the model's self-assessment weighted least. Shadow mode and gate-versus-human disagreement tracking provide the rollout boundary. This is the operational form of [[eval-engineering]] for a [[manager-worker-pr-loop]]. ^[raw/articles/xarticle-eval-engineering-build-the-gate-that-lets-your-age-2083540339147567268.md]

## Why it matters

Once tools like [[claude-code]] and [[codex]] expose scheduling, isolated execution, and stopping-condition primitives, the main engineering task becomes designing the loop around them. The expensive part is no longer just a single model call; it is the number of iterations the loop burns before convergence.

That changes the optimization target:

- **iterations beat tokens** as the true budget line
- **weak verification** becomes the most expensive hidden bug
- **failing fast** is both a safety mechanism and a cost-control mechanism

## Failure modes

Loop engineering does not remove responsibility from the operator. Across these sources, the same risks keep showing up:

- **verification debt** — unattended loops can make unattended mistakes if the checker is weak
- **comprehension debt** — output can outpace the human's understanding of the system
- **cognitive surrender** — clean transcripts can tempt the operator to stop applying independent judgment
- **automation without a pass condition** — exploratory or one-shot work can turn into expensive churn if no cheap automated check exists
- **orchestration tax** — spinning up many agents is easy, but human attention does not parallelize; the operator still has to prioritize, scope, audit evidence, and decide when not to fix something
- **answerability gaps** — long-horizon agent choices can be hard to reconstruct unless logs, tests, verdict criteria, and ownership contracts are designed before the work enters production

## Practical takeaway

A good loop combines explicit stop conditions like [[goal-primitive]], isolation patterns similar to [[dynamic-workflows-in-claude-code]], reusable context capture such as [[hermes-skills-workflow]], and operating cadences closer to [[the-hive-claude-code-architecture]]. The engineer's job shifts from composing perfect one-off prompts to designing the runtime that makes repeated agent work safe, bounded, and reviewable.

## Related

- [[claude-code]]
- [[codex]]
- [[goal-primitive]]
- [[model-agnostic-agent-harness]]
- [[dynamic-workflows-in-claude-code]]
- [[hermes-skills-workflow]]
- [[the-hive-claude-code-architecture]]
- [[matt-van-horn]]
- [[matthew-berman]]
- [[addy-osmani]]
- [[aparna-dhinakaran]]
- [[omarsar0]]
- [[phosphenq]]
- [[human-in-the-loop]]
- [[nvidia-ai]]
- [[manager-worker-pr-loop]]
- [[paul-solt]]
- [[metacognition-human-ai-systems]]
- [[will-chen]]
