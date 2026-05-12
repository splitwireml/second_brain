---
title: Vibe Coding in Production
created: 2026-04-20
updated: 2026-04-20
type: concept
tags: [vibe-coding, agent, reasoning, productivity]
sources: [raw/transcripts/0xMovez_full.md]
author: [[eric-mishra]]
---

# Vibe Coding in Production

Concept from Eric Mishra ([[eric-mishra]]) at [[Anthropic]]: how to vibe code responsibly in production systems where stakes are high.

## Definition

Using Andrej Karpathy's definition: vibe coding is when you *fully give into the vibes, embrace exponentials, and forget that the code even exists.* The key distinction from Cursor/Copilot usage is that those still keep you in a tight feedback loop with generated code — true vibe coding means relinquishing awareness of the code layer entirely.

## Why It Matters Now

AI capability (measured in task length) doubles every ~7 months. Currently ~1 hour of autonomous code generation. Within 1-2 years: full days or weeks of work per prompt. At that point, lockstep code review — where you read every line — becomes a bottleneck you can't scale past.

The compiler analogy: early developers didn't trust compilers and read generated assembly. At scale, that became untenable. The same transition is coming for AI-generated code.

## The Framework

### 1. Be Claude's PM

"Ask not what Claude can do for you, but what you can do for Claude." Act as a product manager guiding a new employee. Provide context, direction, guardrails. The more Claude understands the product intent, the better it executes.

### 2. Verifiability Over Code Reading

Find ways to verify correctness without reading the code. Use tests (prefer end-to-end over implementation-specific), property-based checks, and product-level assertions. The goal: know if a change is correct without opening a code file.

### 3. Know the Danger Zone

Non-technical users vibe coding toy projects is fine. Non-technical users vibe coding production business systems is dangerous — they can't ask the right questions, identify edge cases, or recognize when Claude is going off-track. "No business vibe coding in production for an important system."

### 4. Embrace the Exponential

It's okay not to vibe code today if the task fits within an hour. But in a year or two, refusing to relinquish code-level oversight means refusing to take advantage of the next wave of model capabilities. The cost of staying in lockstep grows over time.

## Relationship to Vibe Coding Tools

This framework is distinct from vibe coding *products* like [[open-lovable]], [[lovable-dev]], or [[gsd-2-ai-vibe-coding-framework]] — those are tools. Vibe coding in production is a *practice* that can be applied with any agentic coding tool, including raw [[claude-code]].

## Related Concepts

- [[building-effective-agents]] — [[eric-mishra]]'s paper with Barry Zhang; foundational agentic AI reference
- [[claude-code]] — tool most associated with vibe coding in production workflows
- [[gsd-2-ai-vibe-coding-framework]] — dedicated vibe coding framework
- [[open-lovable]] — open-source vibe coding platform
