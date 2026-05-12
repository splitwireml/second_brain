---
title: Claude Code Source Leak
created: 2026-03-31
updated: 2026-04-13
type: concept
tags: [security, agent]
sources: [raw/articles/x-bookmarks-2026.md, raw/articles/the-smart-ape-github-repo-trust-2026-04-13.md]
---

# Claude Code Source Leak

## Definition

Anthropic accidentally shipped a source map with the Claude Code npm package, exposing a large readable TypeScript codebase. The leak mattered less because of messy implementation details and more because it revealed product internals, feature flags, and architecture choices that outside observers would not normally see.

## Core findings captured in the wiki

- the leak exposed roughly 712K lines of readable TypeScript according to the existing source summary
- exposed internals reportedly included roadmap-adjacent details such as Kairos and anti-distillation mechanisms
- the codebase reinforced that Claude Code's core agent loop is relatively simple: model response → tool call loop, not a deeply layered orchestration stack
- the operational significance was strategic visibility into product behavior, not embarrassment over code quality

## Architecture notes from the leaked source

### Anti-distillation

The prior source summary reports an `ANTI_DISTILLATION_CC` flag that could inject fake tools into responses to poison distillation attempts. Within the captured analysis, this is presented as a legal/deterrence measure more than a technically decisive defense.

### Undercover mode

The prior source summary also describes an `undercover.ts` path used to suppress Anthropic-internal references when the product runs in non-internal repositories.

### Agent loop simplicity

One of the most useful takeaways is architectural: Claude Code appears to rely on a straightforward iterative tool loop rather than a highly exotic planner stack. That makes this page relevant to [[research-code-agent-cli-automation]] and broader agent-design work represented elsewhere in the wiki.

## Why it matters

This leak is important for three separate reasons:

1. competitive visibility — roadmap and implementation details escaped public packaging boundaries
2. design insight — outsiders got a clearer view into how a major coding agent is actually structured
3. security follow-ons — once a leak becomes high-attention news, attackers can wrap it in fake repos, fake binaries, or trust-signal manipulation

## Post-leak abuse noted in later source

A later X article by [[the-smart-ape]] claims the March 2026 leak quickly became a social-engineering lure: a repo advertising itself as a usable fork of the leaked Claude Code source allegedly shipped credential-stealing malware instead of legitimate source. That later article positions the leak not just as an IP or product-exposure event, but as a catalyst for supply-chain abuse around AI tooling.

Evidence tier for this abuse claim:
- Confirmed: the later article explicitly makes the claim
- Likely: high-attention leaks commonly attract impersonation attempts
- Unverified here: the malware specifics have not been independently corroborated inside this wiki yet

This makes [[github-repo-trust-verification]] a natural adjacent concept rather than a separate topic.

## Practical implications

- operators should treat viral "leaked source" repos as high-risk until manually inspected
- trust signals such as stars, forks, and polished READMEs are not sufficient for evaluation
- install-time scripts, bundled binaries, and dependency hooks matter as much as source readability
- the incident provides useful context for evaluating local agent tooling such as [[hermes-agent]]

## Open questions

- What exactly did Kairos refer to in the leaked codebase?
- How broadly was anti-distillation enabled in production?
- Which parts of the leak were architectural reality versus dead code or inactive flags?
- Can the malware-impersonation claims be independently corroborated and documented in a dedicated security note?

## Related pages

- [[research-code-agent-cli-automation]] — CLI comparison context for Claude Code, Codex, and OpenCode
- [[github-repo-trust-verification]] — follow-on framework for screening suspicious repos and install flows
- [[the-smart-ape]] — later source author highlighting post-leak impersonation risk
- [[hermes-agent]] — comparable agent-tooling context where install-time trust matters

## References

- Raw source: `raw/articles/x-bookmarks-2026.md`
- Raw source: `raw/articles/the-smart-ape-github-repo-trust-2026-04-13.md`
- Reddit thread: https://www.reddit.com/r/ClaudeAI/comments/1s8lkkm/i_dug_through_claude_codes_leaked_source_and/
- Alex Kim analysis: https://alex000kim.com/posts/2026-03-31-claude-code-source-leak/
- Bruniaux architecture guide: https://cc.bruniaux.com/guide/architecture/
