---
title: Claude Skills Ranked List
created: 2026-05-09
updated: 2026-05-09
type: concept
tags: [claude-code, productivity, ai-tools, skill-management, context-window, workflow-optimization]
sources: [raw/articles/xarticle-Mnilax-2051701429987897712.md]
author: [[mnilax]]
likes: 966
retweets: 98
---

# Claude Skills Ranked List

Tested 247 Claude Skills over 6 weeks, kept 23. Full methodology, Tier S/A/B ranking, and install order to avoid context window burnout.

## Core Content

The article tests Claude Skills against a rigorous benchmark:
- **5-point quality scale** improvement ≥1.5
- **30% time savings** on core task
- **Made possible** something baseline couldn't do

Fail criteria: no improvement, more context overhead than value, skill conflicts, or unupdated since Feb 2026.

### Tier S — Install on Every Machine (5 skills)

1. **frontend-design** (Anthropic, 277K+ installs) — forces real design direction; eliminates AI-slop aesthetic
2. **superpowers** (obra, 177K+ stars) — 7-phase TDD workflow; fastest growing Claude Code project 2026
3. **simplify** (Anthropic, ~133K weekly installs) — cleans code without changing behavior
4. **skill-creator** (Anthropic) — meta-skill for building skills; enabled by default in Claude Code v2.1+
5. **web-design-guidelines** (vercel-labs, 19.5K stars) — 100+ rules for accessibility, performance, UX

### Tier A — Install if Work Matches Niche (8 skills)

- ui-ux-pro-max, composition-patterns, valyu, claude-seo, agent-browser, excalidraw-diagram, notebooklm-integration, remotion-best-practices

### Tier B — Useful but Specific (10 skills)

- pdf, docx, pptx, xlsx, marketing-skills, mattpocock/skills, claude-deep-research-skill, firecrawl, obsidian-skills, awesome-claude-skills

## Key Insight: Install Order Matters

Installing all 23 at once burns through context window. Recommended:

- **Week 1:** Foundation (skill-creator, simplify, superpowers, pick ONE design skill)
- **Week 2:** Gap-filling based on domain (UI → web-design-guidelines; TS → mattpocock; research → valyu)
- **Week 3+:** Domain-specific 1-2 more

**Sweet spot: 5-7 active skills.** Each adds ~1,500 tokens overhead; 9+ active = 13,500 tokens baseline tax per task before prompt.

## Mental Model: Two Types of Skills

- **Capability skills** — give Claude new abilities (firecrawl, valyu, pdf, agent-browser)
- **Discipline skills** — make Claude execute in your style (frontend-design, simplify, superpowers, web-design-guidelines)

Most quality improvement comes from discipline skills. Without them, output looks generic.

## Why 224 Were Deleted

- ~80: "Cursor-style" prompt collections with no SKILL.md schema
- ~50: Duplicated better-maintained skills (produced contradictory output)
- ~40: No commits since Feb 2026 (hook spec changed in v2.1)
- ~25: Malicious/compromised (high stars, new repo, no contributor history)
- ~20: Did nothing measurable (net effect zero + context tax)
- ~9: Excellent but redundant with one of the 23

## Weekly Audit Ritual

```bash
# 1. Which skills did Claude actually use?
grep -h "skill_invoked" ~/.claude/logs/*.log | sort | uniq -c | sort -rn

# 2. Which haven't fired in 14 days? → disable
# 3. Run security audit: npx ecc-agentshield scan
# 4. Check marketplace for new skills in your domain
```

If a skill hasn't fired in 30 days, uninstall. Context tax doesn't justify keeping it.

## Related Concepts

- [[claude-skills-service-business]] — selling skills as productized service; related business model
- [[claude-code]] — primary subject
- [[ai-workflow-setup-service]] — similar AI implementation consulting
- [[prompt-engineering-patterns]] — underpins skill design
- [[agent]] — broader domain