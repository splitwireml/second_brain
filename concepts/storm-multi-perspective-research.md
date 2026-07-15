---
title: STORM Multi-Perspective Research
created: 2026-07-01
updated: 2026-07-01
type: concept
tags: [ai-research, multi-agent, workflow, prompt-engineering, claude-code]
sources: [raw/articles/xarticle-stanfords-method-turns-claude-into-a-phd-level-res-2071588017878249890.md]
related_entity: [[nate-herk]]
confidence: medium
---

# STORM Multi-Perspective Research

A research workflow adapted from Stanford's STORM method and packaged by [[nate-herk]] as a reusable Claude skill. The core idea is to replace one-shot research prompting with a fixed set of parallel lenses plus a separate verification pass, producing a structured briefing instead of a loose transcript.

## Core pattern

The workflow runs a topic through five recurring perspectives:

- practitioner
- academic
- skeptic
- economist
- historian

Each lens investigates the same topic from a different angle, then the outputs are merged into a contradiction map before final synthesis. The practical claim is that perspective diversity catches blind spots that a single-prompt research pass misses.

## Verification layer

STORM does not stop at synthesis. A second wave of verifier agents checks citations against primary sources and marks them as confirmed, corrected, or demoted. That makes the method a specific instance of the adversarial-verification pattern described in [[dynamic-workflows-in-claude-code]], but applied to research briefing generation rather than general task execution.

## Why this matters

The strongest takeaway is not the exact five personas, but the architecture:

1. fan out across deliberately different viewpoints
2. map disagreement explicitly
3. synthesize into one report
4. run an independent verification pass before presenting the result

That puts STORM close to [[multi-agent-orchestration]] and [[claude-code-subagents]] in spirit, but with tighter emphasis on evidence quality and structured research output.

## Report shape

The source says the generated briefing is returned as a consistent HTML template with:

- a short executive summary
- key findings ranked by reliability
- per-finding support and challenge signals from the different lenses
- a source appendix labeled by verification status
- explicit missing-lens and core-assumption callouts

This is a useful reminder that research quality comes from output structure as much as from model intelligence.

## Comparison claim vs Claude Deep Research

[[nate-herk]] presents STORM as a cheaper, smaller, more controllable alternative to Claude Code's built-in deep-research workflow. In the reported test, STORM used roughly a dozen agents versus 103 for Claude's dynamic workflow and produced a more decision-ready report. That comparison should be treated as author-reported rather than independently benchmarked, but it does surface a durable design point: a small fixed council can outperform a large unconstrained swarm when the roles and synthesis rules are clearer.

## Practical implication

For operators building their own [[claude-code]] or [[anthropic]] research workflows, the portable lesson is to encode perspective diversity on purpose instead of hoping one powerful model will spontaneously reason from every stakeholder position.

## Related

- [[nate-herk]]
- [[dynamic-workflows-in-claude-code]]
- [[claude-code-subagents]]
- [[multi-agent-orchestration]]
- [[claude-code]]
