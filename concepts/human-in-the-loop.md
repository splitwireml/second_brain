---
title: Human in the Loop
created: 2026-07-02
updated: 2026-07-10
type: concept
tags: [agent, workflow, prompting, evaluation]
sources: [raw/articles/xarticle-human-in-the-loop-2072003526755266744.md, raw/articles/xarticle-own-the-outer-loop-2074927530482835916.md]
related_entity: [[alex-prompter]]
---

# Human in the Loop

Human in the loop is best understood as a workflow architecture, not a requirement that a person approve every single action an AI system takes. The durable pattern is to place human judgment at the checkpoints that matter most — task framing, plan review, drift correction, and final evaluation — while letting the model handle routine execution.

## The three checkpoints

This source breaks the pattern into three practical layers:

1. **Input** — define the goal, constraints, and examples before execution starts.
2. **Steering** — review the plan, monitor trajectory, and intervene when the work drifts.
3. **Output review** — compare the result against explicit criteria before accepting it.

The key claim is that most people underinvest in the first and third layers, then compensate with expensive midstream corrections.

## Why per-action approval fails

The article anchors its case in [[anthropic]] telemetry from roughly 400,000 Claude Code sessions: users approved 93% of permission prompts, which Anthropic's own team described as consent fatigue. That makes the human technically present but functionally disengaged.

The better operating model is closer to [[loop-engineering]] than to button-click supervision. Humans review plans and watch for drift; the agent executes the routine middle of the task.

Addy's outer-loop framing makes the boundary more explicit: humans should own constraints, sampling policy, audit evidence, and the final production verdict, not every inner-loop token or tool call. The scarce resource is judgment backed by quality signals; if the agent can ship more than a person can review, the control surface must decide what evidence is enough and who is answerable when it is wrong.^[raw/articles/xarticle-own-the-outer-loop-2074927530482835916.md]

## Evaluation improves quality

A strong human-in-the-loop system does not just slow automation down; it improves outcomes by adding explicit grading. The article points to rubric-based output checks such as Outcomes in [[claude-code]] as evidence that a meaningful share of weak AI output is an evaluation failure rather than a raw model failure.

This pushes the practical leverage point upward from one-off [[prompt-engineering]] tricks toward reusable review criteria, steering documents, and operating constraints.

## Practical takeaway

If a workflow already uses AI for drafts, research, coding, or summarization, the first upgrade is usually not "more autonomy." It is a better control surface:

- write the goal in one sentence
- define hard constraints up front
- ask for a plan before execution
- review the final output against a short rubric

That pattern keeps human judgment where it adds the most value and removes it from the repetitive approval loop where it adds the least.

## Related

- [[alex-prompter]]
- [[anthropic]]
- [[claude-code]]
- [[loop-engineering]]
- [[prompt-engineering]]
- [[addy-osmani]]
