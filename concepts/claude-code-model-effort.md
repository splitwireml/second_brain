---
title: Claude Code Model/Effort Routing
created: 2026-07-10
updated: 2026-07-10
type: concept
tags: [claude-code, model, reasoning, token-economics, cost-optimization]
sources: [raw/articles/xarticle-model-and-effort-in-claude-code-knowing-more-vs-tr-2074900291062034618.md]
related_entity: [[claude-code]]
---

# Claude Code Model/Effort Routing

Claude Code model/effort routing is the operator decision of whether a bad result needs a more capable [[claude]] model, a higher effort setting, or simply better context. The key distinction from [[claude-devs]] is that model selection swaps the frozen weights that know and generalize, while effort changes how much work the chosen model is trained to do before it returns: plan depth, file reads, verification, and persistence through multi-step tasks.^[raw/articles/xarticle-model-and-effort-in-claude-code-knowing-more-vs-tr-2074900291062034618.md]

## Mental model

- **Model = what it can know or infer.** Switching from a smaller to a larger model changes the parameter set, benchmark capability, ambiguity handling, and price per output token.
- **Effort = how far it travels.** Raising effort tells the same model to spend more output tokens on thinking, tool calls, verification, and follow-through before checking in.
- **Context = what it can use right now.** Prompts, repository files, docs, skills, and tool access steer the request but do not update the underlying weights.

That means the first fix is usually not a settings change. If Claude lacked the right files, docs, tools, or task scope, the failure was a context problem. Settings become the lever only after the context was adequate.^[raw/articles/xarticle-model-and-effort-in-claude-code-knowing-more-vs-tr-2074900291062034618.md]

## Routing rule

Use a stronger model when Claude did not know enough: subtle bugs, unfamiliar domains, architectural choices, high ambiguity, or a smaller model that remains confidently wrong after receiving the right context. Use higher effort when Claude did not try hard enough: it skipped file reads, tests, checks, or failed to push through a bounded multi-step task before asking for help.^[raw/articles/xarticle-model-and-effort-in-claude-code-knowing-more-vs-tr-2074900291062034618.md]

The cost implication is not simply "bigger model costs more." On routine work, smaller models at normal effort can finish correctly with less spend. On hard multi-step work, a stronger model can sometimes use fewer total iterations than a weaker model grinding at high effort. Effort affects token consumption, but it is not a hard cap; task budgets and max-token limits are separate, softer or blunter controls.^[raw/articles/xarticle-model-and-effort-in-claude-code-knowing-more-vs-tr-2074900291062034618.md]

## Relation to loop design

This concept complements [[loop-engineering]] and [[goal-primitive]]. Loops and goals define the stop condition, evidence, retry budget, and verification surface; model/effort routing chooses the worker's capability tier and persistence level inside that bounded loop. A good agent harness should make both choices explicit: which model is allowed to act, how much effort it may spend, what evidence proves success, and when to escalate or stop.^[raw/articles/xarticle-model-and-effort-in-claude-code-knowing-more-vs-tr-2074900291062034618.md]

## Related

- [[claude-code]]
- [[claude-devs]]
- [[claude]]
- [[loop-engineering]]
- [[goal-primitive]]
- [[ai-cost-optimization]]
