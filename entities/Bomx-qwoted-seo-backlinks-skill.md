---
title: qwoted-seo-backlinks-skill
created: 2026-04-27
updated: 2026-04-27
type: entity
tags: [seo, backlink, outbound, automation, claude-code, skill, agent-tool]
sources:
  - raw/articles/github-Bomx-qwoted-seo-backlinks-skill-2026-04-27.md
url: https://github.com/Bomx/qwoted-seo-backlinks-skill
related_entity: []
---

# qwoted-seo-backlinks-skill

AI-powered PR automation skill for [Qwoted](https://qwoted.com) — the HARO replacement connecting experts with journalists at TechCrunch, Forbes, Inc., Adweek, and 6,000+ publications. Teaches [Claude Code](https://github.com/anthropics/claude-code) (or any shell-capable AI agent) to find journalist requests, research and generate sourced statistics pages as linkable SEO assets, and submit pitches that earn press mentions and recurring high-DR backlinks.

## Setup

Install as a Claude Code skill:

```bash
npx skills add Bomx/qwoted-seo-backlinks-skill
```

Or clone manually:

```bash
git clone https://github.com/Bomx/qwoted-seo-backlinks-skill.git
cd qwoted-seo-backlinks-skill
pip install -r requirements.txt
playwright install chromium
```

One-time onboarding (3 minutes):

1. Create free account at [qwoted.com](https://qwoted.com) — select "I am a source / brand"
2. Tell Claude: *"Set me up on Qwoted. My name is [X], I'm the founder of [Y], our website is [Z] and my LinkedIn is /in/[handle]. We do [topic]."*
3. Claude runs `qwoted_login.py` (opens Chromium for manual sign-in including MFA), saves cookies to `~/.qwoted/storage_state.json`, then runs `qwoted_profile.py --action create ...` to create your Source persona
4. Start pitching: *"Find Qwoted opportunities about [topic] this week, then pitch the top 3."*

## Key Features

- **4-stage pipeline**: Onboard (login + profile) → Find opportunities → Research and publish a sourced statistics page → Pitch with the page URL
- **Stage 3 multiplier**: Generates a comprehensive HTML statistics page (40–80 sourced stats, Chart.js charts, schema.org markup) — a pitch linking to a stats page earns recurring citations as reporters discover it via search, not just one-shot mentions
- **Dry-run by default**: Pitches are shown for approval before sending; sent pitches logged to `~/.qwoted/sent_pitches.json` to prevent duplicates
- **CLI fallback**: All scripts (`qwoted_login.py`, `qwoted_profile.py`, `qwoted_search.py`, `qwoted_pitch.py`) work standalone without AI, output `RESULT: { ... }` JSON for agent chaining
- **State directory**: `~/.qwoted/` stores session cookies, profile state, and opportunity JSONs; override with `QWOTED_HOME`
- **Privacy**: No telemetry — only Qwoted API calls, Algolia searches, or local file writes; MIT licensed

## Architecture / Technical Notes

- **Language/Stack**: Python with `requests` + `playwright`
- **Key files**:
  - `qwoted_login.py` — Chromium-based login, saves session cookies (~30-day expiry)
  - `qwoted_profile.py` — CRUD for Source persona (bio, employer, location, contact links)
  - `qwoted_search.py` — Algolia index search returning clean JSON (deadline, publication, request type, hashtags)
  - `qwoted_pitch.py` — Draft and submit pitches via Qwoted internal API; requires `--send` flag to fire
  - `STATISTICS_PAGE_PLAYBOOK.md` — Research methodology and anti-hallucination rules for Stage 3 stats pages
  - `templates/statistics_page_example.html` — Responsive HTML scaffold with Chart.js and Article + FAQPage schema markup
- **Output state**: `~/.qwoted/sent_pitches.json` tracks pitch history including linked `research_page_url` for traceability

## See Also

- [[claude-code]] — The CLI agent this skill extends for end-to-end PR workflows
