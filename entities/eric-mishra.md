---
title: Eric Mishra
created: 2026-04-20
updated: 2026-04-20
type: entity
tags: [person, agent, anthropic]
sources: [raw/transcripts/0xMovez_full.md]
---

# Eric Mishra

Researcher at [[Anthropic]] focused on coding agents. Co-authored "[Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)" with Barry Zhang — the canonical guide to building agents across any application domain.

## Key Work

- **Building Effective Agents** — Research paper outlining best science and practices for creating agents; cited widely as the foundational reference for agentic AI development.
- **Vibe Coding in Production** — Talk at 0xMovez on responsible vibe coding: being Claude's PM, verifiability over reading code, and embracing the exponential.

## Vibe Coding Framework (from 0xMovez talk)

Core principles from Eric's talk:

1. **Be Claude's PM** — "Ask not what Claude can do for you, but what you can do for Claude." Act as a product manager guiding a new employee.
2. **Think in verifiability** — Find ways to verify correctness without reading code. Use tests as the verification layer.
3. **Remember the exponential** — AI capability (task length) doubles every ~7 months. At ~1 hour today → full days/weeks within a year or two. Lockstep code review won't scale.
4. **Know your danger zone** — Non-technical users vibe coding important systems is dangerous. Not everyone should vibe code prod.

### On Vibe Coding Definition

Eric uses Andrej Karpathy's definition: *vibe coding is where you fully give into the vibes, embrace exponentials, and forget that the code even exists.* Key distinction from Cursor/Copilot use: the tight feedback loop still keeps you aware of code; true vibe coding means forgetting it exists.

### Compiler Analogy

Vibe coding responsibly → like trusting a compiler. You know assembly exists, but you don't read it. Similarly, you'll forget code exists but remember the product. The challenge: how to do this safely in production.

## Related

- [[building-effective-agents]] — The paper itself
- [[vibe-coding-in-production]] — This talk's concept
- [[open-lovable]] — vibe coding platform
- [[lovable-dev]] — commercial SaaS vibe coding
- [[gsd-2-ai-vibe-coding-framework]] — vibe coding framework
