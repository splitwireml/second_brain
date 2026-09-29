---
title: Claude Code Model/Effort Routing
created: 2026-07-10
updated: 2026-09-29
type: concept
tags: [claude-code, model, reasoning, token-economics, cost-optimization]
sources: [raw/articles/xarticle-model-and-effort-in-claude-code-knowing-more-vs-tr-2074900291062034618.md, raw/articles/thread-trq212-2103576349499855160.md]
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

## Thariq’s effort-routing article (September 25, 2026)^[raw/articles/thread-trq212-2103576349499855160.md]

Thariq’s September 25 local thread presents effort as an approximation of requested compute that changes verification, edge-case testing, and how much independent judgment Claude takes; it says Claude Code can change effort without breaking the prompt cache. The source’s default feature loop is: give Claude a spec and ask it to interview for missing details; implement at low effort; review and iterate at low effort; then verify and test at high effort. In its rule of thumb, low is for in-the-loop brainstorming, sketching, and easy changes; medium for regular software engineering and new features; high where verification or edge cases matter, such as a brownfield bug; and max for fully autonomous difficult work, including end-to-end app build/verification or finding security vulnerabilities in critical software. The thread specifically names Fable 5.1, Opus 5.5, Terminal-Bench 3.0, and Claude Code’s `/effort` command, which it says can be used mid-conversation. These are source-described product/benchmark observations, not independent capability, cache, security, or cost validation.

On underspecified work, the source’s fitness-tracker example contrasts a low-effort log plus simple graph with higher-detail variants and a max-effort heat chart; it treats low as the faster base for iteration and max as a best one-shot with more model-made choices. For a specified `/config` redesign, it reports a one-minute low-effort interactive sketch versus a 28-minute max-effort Claude-Code-like mockup plus flow walkthroughs. After an in-depth interview/spec, different effort levels produced more similar implementations, with max spending time simplifying details. The source therefore separates verification gain from delegated design choice: higher effort can reduce missed edge cases but does not repair a wrong approach.

The post’s Terminal-Bench 3.0 examples span security, hardware, ML, science, software, operations, and media: `retro-console-soc` (an 8-bit Verilog console for a small FPGA rendering a test ROM), `takens-embedding-lean` (Takens’ embedding theorem in Lean 4), `mp-checkpoint-consolidation` (merge 16 mixture-of-experts checkpoint shards while reproducing reference logits), `intrastat-meldung` (month-end EU trade-statistics filing), and `layout-config-recreation` (rebuild a poster as an editable layout file). For `html-js-filter`, the source reports Fable 5.1 moving from 1/5 at low to 5/5 at xhigh: the low attempt took about two minutes, wrote one filter pass, and tested one hand-written page; the high run took about 33 minutes, adversarially reviewed its first draft, read the installed parser source, ran clean cases and a standard XSS suite, and wrote a random-document fuzzer.

Three additional source-described comparisons make the verification distinction concrete: `mvcc-lsm-compaction` moves Opus 5.5 from 0/5 at low to 4/5 at xhigh after reproducing the crash, writing a randomized test against a never-compacting reference, and checking that half-finished fixes fail; `cli-2ph-simple` moves from 0/5 at low to 5/5 at high after random-problem comparisons with a separate brute-force solver, larger timing runs, and search rework; and `gsea-proteomics` moves from 0/5 at low to 4/5 at high after trying two data-preparation approaches, seeing different significant-treatment lists, and investigating before selecting one. The source says high effort is especially useful when hidden edge cases are likely, but a user in the loop can instead answer an unresolved setup question. It supplies no command implementation, API, configuration schema, prompt template, benchmark harness, source code, or independent reproduction beyond the named `/effort` interface and these source-reported procedures/results.

The remainder of the exported thread is reply-thread material. It is retained byte-for-byte in the raw capture but is not treated as author-endorsed product documentation or independent validation; third-party requests, reported experiments, tool mentions, and proposed auto-effort designs are raw-only evidence.

## Related

- [[claude-code]]
- [[claude-devs]]
- [[claude]]
- [[loop-engineering]]
- [[goal-primitive]]
- [[ai-cost-optimization]]
