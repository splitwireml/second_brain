---
title: Model-Agnostic Agent Harness
created: 2026-07-08
updated: 2026-07-16
type: concept
tags: [agent, workflow, orchestration, claude-code, ai-agent, tools]
sources: [raw/articles/xarticle-how-i-get-frontier-results-from-any-model-the-harn-2074195371920666718.md, raw/articles/xarticle-you-have-a-few-days-to-clone-fable-5-into-opus-48-2074198124898181121.md, raw/articles/xarticle-how-to-become-an-applied-ai-engineer-2074519552277336571.md, raw/articles/xarticle-building-against-the-big-labs-that-are-trying-to-e-2076767931053294017.md, raw/articles/thread-alex_prompter-2076727080402948561.md, raw/articles/xarticle-the-dark-arts-of-skill-engineering-2077114326985687525.md]
related_entity: [[phosphenq]]
---

# Model-Agnostic Agent Harness

A model-agnostic agent harness is the reusable scaffolding around an LLM that makes the underlying model swappable. [[phosphenq]] frames the harness as five stacked layers — context, loop, tools, checks, and memory — and argues that the gap between a good and bad harness can now exceed the gap between the top model and a mid-tier model.^[raw/articles/xarticle-how-i-get-frontier-results-from-any-model-the-harn-2074195371920666718.md]

## Core thesis

The source's practical claim is that the model is the replaceable part and the harness is the asset. A bare prompt still works for one-off, exploratory, or judgment-heavy work, but repeated work with automatic checks and real tool access should be moved into an operating loop. That makes the comparison test simple: run the same task through the same harness on a cheap model and on a frontier model; if outputs converge, the durable leverage came from the system rather than the model.^[raw/articles/xarticle-how-i-get-frontier-results-from-any-model-the-harn-2074195371920666718.md]

## Five layers

1. **Context** — standing project rules, relevant files, task memory, and tool scope, not a maximal context dump. The guide uses `CLAUDE.md` as the canonical always-loaded context file for [[claude-code]].
2. **Loop** — the operator gives a goal once and lets the agent act, observe, and retry until a separate checker accepts the finish condition or the hard stop fires.
3. **Tools** — the agent can read, run, edit, inspect logs, and exercise the environment instead of merely describing the work.
4. **Checks** — objective tests, builds, lint, or separate verifier agents keep the maker from grading its own homework.
5. **Memory** — files such as `STATE.md`, skills, and MCP-connected systems preserve lessons between runs instead of relying on closed chat history.^[raw/articles/xarticle-how-i-get-frontier-results-from-any-model-the-harn-2074195371920666718.md]

## Manual-layer variant

The manual-layer version is lighter than a full tool harness but follows the same ownership logic. The operator pays the frontier model once to encode its procedures, stores the result as a durable file or skill, then routes routine future work through cheaper models. The required check is behavioral rather than aesthetic: a trap such as a false percentage claim should force the manual-loaded model to re-derive the number instead of accepting fluent prose.

Alex Prompter's Fable-method thread gives a source-described instance of that transfer: a plugin separates the operating method, adversarial task loop, and independent judge, then tests the package across models. Alex reports Sonnet plus the method matching Fable 10/10 on a five-part research task, while Haiku improved on wrong-test and planted-fraud checks. The same thread explicitly says the package adds little to ordinary tasks with capable models, reinforcing that a harness is useful when it supplies missing verification discipline rather than knowledge.^[raw/articles/thread-alex_prompter-2076727080402948561.md]

## Domain focus and model choice

[[peter-wang]]'s [[shortcut]] case study adds a product-level version of the same thesis. A narrow workflow lets the builder remove general-purpose tools and instructions, keep context light, and tune the harness against the exact tasks customers care about. The source reports that Shortcut's internal spreadsheet evals were cheaper and more accurate than Claude for Excel even with the same base model; these figures are source-reported, not independently audited here. ^[raw/articles/xarticle-building-against-the-big-labs-that-are-trying-to-e-2076767931053294017.md]

The case also makes model agnosticism operational rather than rhetorical: route different subproblems to the model that best fits its accuracy, latency, modality, or cost profile, and keep the task harness stable while the underlying model changes. That combination—focused domain scope plus model choice—gives a small product a way to compete without matching a general-purpose lab's breadth. ^[raw/articles/xarticle-building-against-the-big-labs-that-are-trying-to-e-2076767931053294017.md]

## Applied AI engineering lens

[[eyad-khrais]] frames harness engineering as the day-to-day operating system of applied AI work: models only emit text or structured requests, so the harness must validate tool calls, execute real operations, feed results back, manage context, persist state, enforce guardrails, and repeat until the task is done. This makes the harness less a wrapper and more the reliability boundary between a non-deterministic model and deterministic business software.

## Skills as harness components

The local skill-engineering article makes skills a concrete harness layer. [[impeccable]] is presented as a case where the skill supplies adversarial review, forced divergence, internal routing, persistent snapshots, scripts that emit just-in-time instructions, passive hooks, browser events, and per-harness builds rather than relying on prose alone. These are source-described techniques, not independently tested claims.^[raw/articles/xarticle-the-dark-arts-of-skill-engineering-2077114326985687525.md]

This sharpens the five-layer model: skills are part of context and memory, but their scripts, hooks, and routing also shape the loop, tools, and checks. The portability test is behavioral—compile the same skill for each harness and model, then verify that the gates still fire and the result remains acceptable.^[raw/articles/xarticle-the-dark-arts-of-skill-engineering-2077114326985687525.md]

## Safety and economics

The guide is unusually explicit about when not to build the harness: if the work does not repeat, has no automatic check, lacks real tools, or cannot absorb token waste, the setup cost is not earned back. Its failure list maps directly onto existing [[loop-engineering]] concerns: silent early success, goal drift across long sessions, self-preferential checking, comprehension debt, and unattended security blast radius.^[raw/articles/xarticle-how-i-get-frontier-results-from-any-model-the-harn-2074195371920666718.md]

## Related

- [[phosphenq]]
- [[alex-prompter]]
- [[prompt-engineering]]
- [[loop-engineering]]
- [[goal-primitive]]
- [[dynamic-workflows-in-claude-code]]
- [[agent-memory-architecture]]
- [[claude-code-subagents]]
- [[hermes-skills-workflow]]
- [[eyad-khrais]]
- [[peter-wang]]
- [[shortcut]]
- [[ai-cost-optimization]]
