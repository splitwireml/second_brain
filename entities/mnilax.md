---
title: Mnilax
created: 2026-04-23
updated: 2026-05-12
type: entity
tags: [x-creator]
sources: [raw/articles/xarticle-karpathy-claude-md-12-rules-2053116311132155938.md]
---

# Mnilax

X creator (@Mnilax) who tested and extended Karpathy's CLAUDE.md rules from 4 to 12 rules after applying them across 30 codebases over 6 weeks.

## Profile
- Handle: @Mnilax
- Posts about: Claude Code, AI coding agents, prompt engineering, coding reliability

## Key Findings

**Original Karpathy 4 rules** reduced Claude coding mistakes from ~41% to ~11% on tasks that played to their strengths.

**Mnilax's extension (2026-05-09):** After testing on 30 codebases, 4 additional failure modes were identified specific to the May 2026 Claude Code ecosystem:
- Agent fights between skill-loaders
- Hook cascades across sessions
- Multi-step workflows breaking across context windows
- Skill loading conflicts

The extended 12-rule template builds on [[karpathy-claude-md]] principles, adding rules to handle agent-specific failure modes.

Source: [[xarticle-karpathy-claude-md-12-rules-2053116311132155938]]

## Related Concepts
- [[karpathy-claude-md]]
- [[12-rule-claude-md-template]]
- [[claude-code]]
