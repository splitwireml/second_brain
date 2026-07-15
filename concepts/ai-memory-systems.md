---
title: AI Memory Systems
created: 2026-05-11
updated: 2026-06-14
type: concept
tags: [tools, ai, architecture]
sources: [raw/articles/personal-ai-os-2053772855691690278.md]
related_entity: [[noisy]]
---

# AI Memory Systems

AI memory systems enable AI assistants to maintain persistent context across sessions, eliminating the need to re-explain who you are, what you're working on, and what decisions you've already made.

## The Core Problem

Most AI interactions are session-based — every conversation starts from zero. This is the biggest productivity leak in AI-assisted work: re-explaining context that was already established in previous sessions.

## Memory Type Framework

From [[personal-ai-infrastructure]] (PAI), the four-memory model:

| Memory Type | Function | Example |
|-------------|----------|---------|
| Work memory | Active projects, current decisions | "I'm building a React dashboard with authentication" |
| Knowledge memory | Domain expertise, research | Industry knowledge, frameworks, past research |
| People memory | Contacts, companies, relationships | Client names, stakeholder contexts |
| Learning memory | Patterns, mistakes, what works | "Don't suggest Tailwind for this codebase" |

## Plain Text as Memory Architecture

PAI uses Markdown files as the memory substrate instead of vector databases or embeddings. This makes memory:
- Readable with `cat`
- Searchable with `ripgrep`
- Version-controllable with Git
- Human-inspectable at any time

## Related Concepts

- [[personal-ai-infrastructure]] — the system that implements these memory types
- [[claude-code-workflows]] — execution layer that uses persistent memory
- [[agent-memory-architecture]] — broader patterns for agent memory
- [[factual-memory]] and [[action-memory]] — sub-types sometimes distinguished in agent frameworks

## Related
- [[noisy]] — related entity from frontmatter; explicit cross-link
