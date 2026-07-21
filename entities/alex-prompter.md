---
title: Alex Prompter
created: 2026-07-02
updated: 2026-07-16
type: entity
tags: [person, x-creator, ai-agent, workflow]
sources: [raw/articles/xarticle-human-in-the-loop-2072003526755266744.md, raw/articles/xarticle-you-have-a-few-days-to-clone-fable-5-into-opus-48-2074198124898181121.md, raw/articles/thread-alex_prompter-2076727080402948561.md]
---

# Alex Prompter

X creator (@alex_prompter) writing about agentic workflow design, portable model-operating manuals, and AI skill packaging. His articles emphasize moving human oversight away from low-value permission clicking and toward higher-value planning, steering, review, and reusable instruction layers.

## Core framing

- Recasts **human in the loop** as workflow architecture rather than constant per-action approval.
- Uses [[anthropic]]'s published Claude Code telemetry to argue that permission-heavy oversight creates consent fatigue instead of real supervision.
- Pushes operators toward plan review, active monitoring, and explicit output criteria instead of rubber-stamping individual tool calls.

## Practical advice

- Start with output review before trying to automate everything.
- Add a steering layer with a written operating file or plan review step.
- Improve results by strengthening the input layer: clearer goals, tighter constraints, and examples of what good looks like.
- Treat high-end model access as a temporary harvesting window: extract a procedural operating manual or workflow skill from the stronger model, then run that reusable instruction layer on cheaper successor models.

## Portable reasoning manuals

Alex's Fable-to-Opus article extends the same operating-layer thesis from agent supervision to model economics. The reusable asset is not the transient frontier model itself, but a written procedure for reading intent, decomposing risk, re-deriving claims, labeling uncertainty, attacking conclusions, and communicating answer-first. That manual can be loaded into [[claude]] Project instructions or an API system prompt and tested with trap questions before the operator trusts the cheaper model.

Alex's July 13 thread adds a concrete validation case: the source-described `fable-method` plugin packages Fable's problem-solving loop into `fable-method`, `fable-loop`, and `fable-judge`. Across 159 agent runs, Alex reports Sonnet plus the plugin matched Fable 10/10 on a five-part research task; Haiku improved from 0/4 to 4/4 on wrong-test detection, and the judge improved Haiku from 3/5 to 5/5 on planted-fraud checks. The source also emphasizes limits: ordinary tasks with capable models may gain nothing, and the README documents those non-beneficial cases. These are source-reported results, not independent wiki benchmarks.^[raw/articles/thread-alex_prompter-2076727080402948561.md]

## Related

- [[human-in-the-loop]]
- [[anthropic]]
- [[claude]]
- [[claude-code]]
- [[prompt-engineering]]
- [[model-agnostic-agent-harness]]
- [[loop-engineering]]
