---
title: Opik
created: 2026-09-22
updated: 2026-09-22
type: entity
tags: [product, open-source, evaluation, observability]
sources: [raw/articles/xarticle-build-a-jev-judge-2102087107410002345.md]
---

# Opik

**Opik** is an open-source experiment and observability layer around agent evaluation. In Akshay Pachaar's Jev-as-a-judge tutorial, it is explicitly not the judge: [[jev]] produces the bounded semantic decisions, while Opik stores traces, datasets, experiments, trace-level feedback, and evaluation results so failures and disagreements can be inspected.^[raw/articles/xarticle-build-a-jev-judge-2102087107410002345.md]

## Jev metric adapter

The source uses Opik's custom-metric extension point rather than claiming a native Jev integration or setting `model="jev"` on a generative metric. `JevSupportMetric(base_metric.BaseMetric)` owns a `JevClient`, sends `request`, `policy`, `tool_calls`, and `final_answer` to `client.evaluate(...)`, then maps the response through `map_scores` into named `score_result.ScoreResult` values. The full adapter also records structural checks, verdict metrics, tracing, audit metadata, the resolved judge model, rubric version, and raw answers. Because Jev supplies no written explanation, the tutorial deliberately does not manufacture an Opik `reason` field.^[raw/articles/xarticle-build-a-jev-judge-2102087107410002345.md]

## Experiment boundary

The source calls `opik.evaluation.evaluate(dataset=dataset, task=replay, scoring_metrics=[JevSupportMetric()], experiment_name="jev-support-v1", project_name="jev-support-judge", task_threads=1, error_tolerance=0)`. `replay` returns a frozen final answer while the dataset supplies the remaining state; serial task execution is for first-run inspection and does not remove Jev's within-request parallel questions. The accompanying runner creates the dataset and unique experiment names and fails on metric errors rather than treating absent evaluations as clean results.^[raw/articles/xarticle-build-a-jev-judge-2102087107410002345.md]

## Operational constraints

The repository path is `patchy631/jev-as-judge`. Its offline demonstration command, `python -m jev_judge.cli --mode demo`, uses hand-authored probabilities and is explicitly not performance evidence. The optional live path is `pip install -e '.[opik]'`, `opik configure`, `export TYPESAFE_API_KEY="your-key"`, then `python -m jev_judge.opik_eval --project jev-support-judge`; it sends supplied cases to TypeSafe and records them in the configured Opik workspace. Redact sensitive data before substituting real traces for the synthetic examples.^[raw/articles/xarticle-build-a-jev-judge-2102087107410002345.md]

## Evidence boundary

This local source describes an integration workflow; it supplies no independent Opik benchmark, deployment configuration, retention policy, schema, pricing, or security assessment. Its claims about TypeSafe/Jev latency, cost, and quality remain source-described and must be validated against representative, domain-reviewed labeled traces before production use.

## Related

- [[jev]]
- [[system-one-models]]
- [[eval-engineering]]
- [[model-agnostic-agent-harness]]
