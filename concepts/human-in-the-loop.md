---
title: Human in the Loop
created: 2026-07-02
updated: 2026-08-08
type: concept
tags: [agent, workflow, prompting, evaluation]
sources: [raw/articles/xarticle-human-in-the-loop-2072003526755266744.md, raw/articles/xarticle-own-the-outer-loop-2074927530482835916.md, raw/articles/thread-NVIDIAAI-2077061428998013279.md, raw/articles/xarticle-how-id-make-10-million-with-ai-agents-2076733920834371585.md, raw/articles/xarticle-a-beginners-guide-to-metacognition-2079624266707054825.md, raw/articles/xarticle-eval-engineering-build-the-gate-that-lets-your-age-2083540339147567268.md, raw/articles/xarticle-software-factory-how-to-turn-one-ai-into-a-product-2085276400580223275.md, raw/articles/xarticle-gpt-6-astra-has-completely-changed-the-way-i-run-m-2102753461796262232.md]
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

The NVIDIA AI thread gives the same boundary in a training setting: the researcher steers the objective and priorities while a coding agent handles environment setup, training, evaluation, and a proposed next experiment under a fixed time budget. That is outer-loop steering rather than per-action babysitting; the reported Qwen3-VL-2B accuracy change is preserved as a source claim.^[raw/articles/thread-NVIDIAAI-2077061428998013279.md]

## Metacognitive preflight

Will Chen's metacognition frame adds a human-side debugging layer to these checkpoints: when work feels frustrating, ask what level is overloaded, whether the task is still diverging or should converge, whether new evidence has arrived, and what budget remains. The resulting intervention may be a narrower prompt, a fresh run, a deterministic test, an external note, or a deliberate stop rather than more approval clicks. This is a diagnostic complement to [[human-in-the-loop]], not a replacement for explicit output criteria.^[raw/articles/xarticle-a-beginners-guide-to-metacognition-2079624266707054825.md]

## Evaluation improves quality

A strong human-in-the-loop system does not just slow automation down; it improves outcomes by adding explicit grading. The article points to rubric-based output checks such as Outcomes in [[claude-code]] as evidence that a meaningful share of weak AI output is an evaluation failure rather than a raw model failure.

This pushes the practical leverage point upward from one-off [[prompt-engineering]] tricks toward reusable review criteria, steering documents, and operating constraints.

## Earned autonomy in product agents

[[greg-isenberg]] applies the same control-surface logic to new customer agents: start with draft-and-approve, run the system against 50 real examples, and only widen autonomy after the operator can measure what worked, what was flagged, and what failed. The evaluation set doubles as a sales demonstration, so human review is both a safety boundary and a product-discovery instrument.^[raw/articles/xarticle-how-id-make-10-million-with-ai-agents-2076733920834371585.md]

This is consistent with [[agent-saas-playbook]]: approval, escalation, and success criteria should be designed before the agent is allowed to act independently. The source's recommendation is not permanent manual supervision; it is earned autonomy backed by evidence.^[raw/articles/xarticle-how-id-make-10-million-with-ai-agents-2076733920834371585.md]

## Eval-gated autonomy

Hanako's eval-engineering course adds a rollout protocol for the human checkpoint: sort changes by blast radius, let reversible contained work open first, require deterministic checks plus a clean trajectory for wide-but-reversible changes, and keep migrations, deletions, production-data writes, and money movement closed regardless of score. Start in shadow mode, track gate-versus-human disagreement, and keep the gate closed while disagreement is meaningfully above zero. These are source-described controls rather than independently validated operating thresholds. ^[raw/articles/xarticle-eval-engineering-build-the-gate-that-lets-your-age-2083540339147567268.md]

The source also makes the evidence ordering explicit: deterministic tests, types, schema checks, or sandbox execution first; the agent-version trajectory second; rollback history third; and the model's own assessment least weighted. This sharpens the human role from approving every action to owning the sampling policy, audit evidence, and final production verdict alongside [[eval-engineering]]. ^[raw/articles/xarticle-eval-engineering-build-the-gate-that-lets-your-age-2083540339147567268.md]

## Practical takeaway

If a workflow already uses AI for drafts, research, coding, or summarization, the first upgrade is usually not "more autonomy." It is a better control surface:

- write the goal in one sentence
- define hard constraints up front
- ask for a plan before execution
- review the final output against a short rubric

That pattern keeps human judgment where it adds the most value and removes it from the repetitive approval loop where it adds the least.


## Policy gate and earned autonomy (Nazar, 2026-08-08)

Nazar's software-factory gate moves the human checkpoint from every tool call to policy and evidence. The source's agent profile auto-merges only `**/*.md`, `**/*.txt`, and `docs/**`, with `max_files: 5`, `max_lines: 150`, and `require_ci: true`; it keeps `.github/**`, `**/*auth*`, `**/*secret*`, `**/.env*`, `**/migrations/**`, `**/*.tf`, and `**/package-lock.json` protected for human review. A missing policy file fails closed. ^[raw/articles/xarticle-software-factory-how-to-turn-one-ai-into-a-product-2085276400580223275.md]

The source describes earned autonomy as an optional ledger that can widen an author's allowlist after merged work survives, but never open protected paths. It recommends a verdict demo and a non-mutating dry-run, and names shell downloads, credential literals (`sk-live-`, `ghp_`, `AKIA`), disabled certificate checks, `permissions: write-all`, `DROP TABLE`, and concatenated secrets as risky patterns. These are source-described controls; no policy implementation or independent false-positive rate is provided. ^[raw/articles/xarticle-software-factory-how-to-turn-one-ai-into-a-product-2085276400580223275.md]
## Deciding before doing (Dickie Bush, 2026-09-24)

Dickie Bush's Astra article gives a business-operations variant of the control boundary: split a project into **Decision Work** (choose outcome, requirements, required questions, offer/content/brand choices, and final review) and **Doing Work** (enter choices into tools, configure branding and routing, test paths, copy an embed, paste it into HTML, upload/schedule/format, typo-check, create graphics, and distribute). The human supplies a sufficiently concrete first pass, reviews the proposed build order and V1, resolves consequential questions, iterates in plain English, and accepts only after an end-to-end test; the agent is assigned the routine middle. ^[raw/articles/xarticle-gpt-6-astra-has-completely-changed-the-way-i-run-m-2102753461796262232.md]

For the cited Vortex build, the source reports browser/MCP access to eight systems, a working V1 after about 15 minutes versus a self-estimated 3–4 hours manually, subsequent offer/brand/form changes, and an application → Calendly → Airtable → Slack test. These are source-described performance and reliability claims, not independently reproduced. The source specifies neither authorization boundaries, secrets handling, connector schemas, failure recovery, nor test fixtures, so it should not be read as a deployment-safety recipe. [[decision-work-and-doing-work]] separates this task classification from the broader loop controls in [[loop-engineering]]. ^[raw/articles/xarticle-gpt-6-astra-has-completely-changed-the-way-i-run-m-2102753461796262232.md]


## Related

- [[alex-prompter]]
- [[anthropic]]
- [[claude-code]]
- [[loop-engineering]]
- [[prompt-engineering]]
- [[addy-osmani]]
- [[nvidia-ai]]
- [[metacognition-human-ai-systems]]
- [[will-chen]]
