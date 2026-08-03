---
title: Eval Engineering
created: 2026-08-03
updated: 2026-08-03
type: concept
tags: [ai-agent, evaluation, benchmark, testing, reliability, workflow]
sources: [raw/articles/xarticle-eval-engineering-build-the-gate-that-lets-your-age-2083540339147567268.md]
related_entity: [[hanako]]
---

# Eval Engineering

Eval engineering is the design of evaluation evidence, verdicts, and control rules that let an agent system act on its own without turning model confidence into an unsafe merge decision. The target is not trust in the model; it is a constraint tight enough that trust stops being the question. Hanako's six-step course is a source-described operating pattern, not an independently validated benchmark. ^[raw/articles/xarticle-eval-engineering-build-the-gate-that-lets-your-age-2083540339147567268.md]

## 1. Treat the judge as part of the measurement

Automated evaluation began with the 2023 UC Berkeley result attributed to Zheng and colleagues: GPT-4 agreed with human raters over 80% of the time, roughly the human-to-human agreement rate. The article says follow-up work found that judges react to properties besides the content being judged. ^[raw/articles/xarticle-eval-engineering-build-the-gate-that-lets-your-age-2083540339147567268.md]

The article reports a 2026 benchmark in which GPT-5.2 and Gemini 3.1 Pro gave their own model families 75–84% win rates, while Claude Opus 4.7 under-rated its own family at 10.6–41.2%. Across judges on ArenaHard, measured bias ranged from -38% to +90%. The same outputs scored 93.3% with one judge and 39.5% with another. Verbosity bias also rewards longer answers even when the extra words add no information. These are source-reported figures; the local export does not include the benchmark dataset or implementation. ^[raw/articles/xarticle-eval-engineering-build-the-gate-that-lets-your-age-2083540339147567268.md]

Three setup rules follow:

- Judge with a different model family from the generator to avoid shared blind spots.
- For high-stakes work, use a panel from different vendors so correlated judge errors are less likely to dominate.
- Send objectively checkable questions to code: did the test pass, does the file exist, or did the state change?

A gate fed by a biased judge can launder a guess into a number and then act on it. This is the operational version of the [[generation-evaluation-gap]]: evaluation quality is part of the system being measured. ^[raw/articles/xarticle-eval-engineering-build-the-gate-that-lets-your-age-2083540339147567268.md]

## 2. A verdict must control the run

A score that only changes a dashboard is a report, not a guardrail. The article's proposed evals run inside the agent and turn verdicts into structural actions: low grounding rejects a handoff, a schema failure blocks an edge, suspected fabrication quarantines a branch, and only verified completion may end the run. Stopping tool calls is not proof of finishing the task; an external check must distinguish an ended turn from verified completion. ^[raw/articles/xarticle-eval-engineering-build-the-gate-that-lets-your-age-2083540339147567268.md]

This makes eval engineering a control surface for [[loop-engineering]] and [[goal-primitive]], not a post-run reporting layer. Each verdict needs an explicit consequence for tools, handoffs, escalation, quarantine, or termination. ^[raw/articles/xarticle-eval-engineering-build-the-gate-that-lets-your-age-2083540339147567268.md]

## 3. Grade the path as well as the answer

The course separates three levels:

1. **End to end** — whether the task succeeded.
2. **Trajectory** — whether the path was sound, exposing loops, redundant calls, and wasted steps.
3. **Component** — which retriever, tool, or sub-agent broke and therefore where to repair the system.

Its starting metrics are faithfulness (the answer is grounded in tool results rather than filled in after an empty response), tool-parameter accuracy (the right tool with the right arguments), and task completion judged against a real signal rather than the agent's own claim. The same final diff is a different risk when one path is clean and another arrived after forty steps of thrashing. This extends [[viv-deep-agents-evals]]'s outcome-versus-trajectory split with a component-level repair lens. ^[raw/articles/xarticle-eval-engineering-build-the-gate-that-lets-your-age-2083540339147567268.md]

## 4. Turn traces into permanent tests

The expensive test cases are already in production traces. Start with a small set of complete runs where working and broken behavior sit next to each other:

- a clean request as the baseline;
- a request the user rephrased or corrected, treating the correction as a free label;
- a run where a tool returned empty or was called twice with identical arguments;
- an external timeout, testing how the agent behaves when the world says no.

Write each case in four lines: what the agent did; what worked and what failed; whether the cause was the agent or a dependency; and which capability the eval should protect. The trace says what happened, not what should have happened, so the answer key must come from tests, records, policy, or a person. Test the verifier itself with one clearly correct result and one plausible wrong result before trusting its rubric. A repeated identical lookup is an agent loop; a rate limit is a dependency failure unless recovery was part of the agent's contract. ^[raw/articles/xarticle-eval-engineering-build-the-gate-that-lets-your-age-2083540339147567268.md]

## 5. Pin judges and write observable rubrics

Judges are software with versions. Pin the version and log it with every score or old and new measurements become incomparable after silent upgrades. Use a one-line rubric of the form “pass if the independently observable outcome happened,” rather than a bundle of proxy scores. Do not reward answer length, keyword presence, citation count, or similarity to a reference; optimizing those shapes can make the agent look right instead of be right, turning the defense into an attack surface. This is Goodhart's law with a model in the loop. ^[raw/articles/xarticle-eval-engineering-build-the-gate-that-lets-your-age-2083540339147567268.md]

The article cites Huang and colleagues at DeepMind's ICLR 2024 work as evidence that intrinsic self-correction — asking a model to review and revise without external grounding — does not reliably help and can make results worse. External grounding is therefore part of the evaluator contract. It also gives practical sizing guidance: at least 500 cases before trusting an aggregate number, with a suite short enough to fit inside a coffee break rather than become a quarterly ritual. These citations and thresholds remain source-described. ^[raw/articles/xarticle-eval-engineering-build-the-gate-that-lets-your-age-2083540339147567268.md]

## 6. Open by blast radius, not confidence

Do not gate every change with one confidence threshold. Split work by the cost of being wrong:

- **Reversible and contained** — a copy change, a test, or an isolated function with coverage; one bad merge costs a revert, so this lane can open first.
- **Reversible but wide** — a shared utility or schema addition touched by a dozen callers; require deterministic checks plus a clean trajectory.
- **Hard to reverse** — migrations, deletions, production-data writes, or money movement; this lane does not open regardless of score.

Within an open lane, read evidence in order: deterministic tests, types, schema checks, or sandbox execution; then the eval trajectory for the agent version; then historical rollback frequency on that surface. Weight the model's own assessment least because it is the only input the model can influence. Start in shadow mode, merging nothing while the gate scores real changes. Track gate-versus-human disagreement and keep the gate closed while disagreement remains meaningfully above zero. Green is evidence, not proof. ^[raw/articles/xarticle-eval-engineering-build-the-gate-that-lets-your-age-2083540339147567268.md]

## Related

- [[hanako]]
- [[generation-evaluation-gap]]
- [[viv-deep-agents-evals]]
- [[loop-engineering]]
- [[goal-primitive]]
- [[human-in-the-loop]]
- [[model-agnostic-agent-harness]]
