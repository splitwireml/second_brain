---
source_url: "https://x.com/bateshkaaa/status/2079218516150862086"
ingested: 2026-07-24
sha256: 4c1f05211d96e470bd556a957393ce2b7412041d7f71ab518dd13b58e5439fe7
tweet_id: "2079218516150862086"
tweet_url: "https://x.com/bateshkaaa/status/2079218516150862086"
author_name: "Romario"
author_handle: "@bateshkaaa"
tweet_date: "Mon Jul 20 14:54:58 +0000 2026"
content_type: x_article
character_count: 5870
retweet_count: 12
like_count: 78
---
Build Agency-Quality $10K Websites With Claude Code

Agencies charge $8,000–$12,000 for a marketing site. 3 weeks of calls. 2 rounds of revisions. 1 invoice that makes you sit down.

Claude Code builds the same site in 1 afternoon. Most people still get template-looking output. Here's why - and the exact fix.

The standard approach fails because people type "build me a beautiful website" and pray. Claude defaults to safe: Inter font, purple gradients, 3 feature cards. This is an amateurish website, and you’ll get almost nothing in return. The $10K look comes from constraints, not vibes.

---

## Part 1 - Load the design brain (15 minutes)

Claude's default taste is a $500 template: Inter font, purple gradient, 3 feature cards. Skills fix that. A skill is just a folder with a [SKILL.md](http://skill.md/) file that Claude reads before designing.

Install Claude Code first:

1. Open your terminal, run: npm install -g @anthropic-ai/claude-code

2. Run: claude - log in with your account.

Now add the 2 skills:

1. Go to the anthropics/skills repo on GitHub and download the frontend-design folder.

2. Grab a UI/UX ruleset skill (ui-ux-pro-max is the popular one, also on GitHub).

3. Create a folder in your project: .claude/skills/

4. Drop both skill folders inside. Structure looks like: .claude/skills/frontend-design/SKILL.md

5. Restart Claude Code. Type /skills or just ask "what skills do you have" - both should show up.

Or just ask Cloud to download these skills—simply send them a link to them.
Paste this into Claude Code

```
install github. com/anthropics/skills/tree/main/skills/frontend-design
```

```
install github. com/nextlevelbuilder/ui-ux-pro-max-skill
```

That's it. No API, no config. Claude now checks these rules before every design decision.

---

## Part 2 - Steal the direction (20 minutes)

Adjectives don't work. "Make it premium" produces nothing. Screenshots work.

1. Open Awwwards and Dribbble. Search your niche: "SaaS landing", "portfolio", "law firm".

2. Pick 3 sites. Not 10 - 3. More references confuse the model.

3. Screenshot the hero section, 1 content section, and the footer of each. 9 screenshots total.

4. Save them into your project folder as ref-1.png, ref-2.png, ref-3.png.

5. In Claude Code, drag the files in or reference them by path with this exact line: "Match the typography scale, spacing rhythm, and motion of these references. Do not copy the layouts."

The "do not copy" part matters. Without it Claude clones reference 1 and you get a lawsuit-adjacent lookalike.

---

## Part 3 - The build prompt (5 minutes to write, 6 minutes to run)

One prompt, 5 blocks. Fill in the brackets:

1. Audience: "This site is for [freelance photographers charging $2K+ per shoot]."

2. The 1 action: "Every page pushes toward [booking a call]. One CTA, repeated."

3. References: "Use ref-1.png, ref-2.png, ref-3.png as the quality bar."

4. Stack: "Astro, Tailwind, deployed to Cloudflare Pages. Static, fast, no CMS."

5. Ban list: "Banned: purple gradients, emoji as icons, Inter as the display font, generic stock-photo placeholders, centered-everything layouts."

Paste all 5 blocks as 1 message. First working version lands in 4–6 minutes.

```
1. Audience: "This site is for freelance photographers charging $2K+ per shoot."
2. The 1 action: "Every page pushes toward booking a call. One CTA, repeated."
3. References: "Use ref-1.png, ref-2.png, ref-3.png as the quality bar."
4. Stack: "Astro, Tailwind, deployed to Cloudflare Pages. Static, fast, no CMS."
5. Ban list: "Banned: purple gradients, emoji as icons, Inter as the display font, generic stock-photo placeholders, centered-everything layouts."
```

It will be 70% there. That's expected — nobody ships version 1.

After Part 3, you'll have the first version of the website

---

## Part 4 - The polish pass (1–2 hours, this is the $10K part)

Agencies bill 40% of the project for this stage. Run 3 passes, in order, as 3 separate messages:

Pass 1 — typography only: "Review every heading and body size. Establish a strict type scale. Fix line-height and letter-spacing. Touch nothing else."

Pass 2 — spacing only: "Audit vertical rhythm section by section. Double the whitespace where sections feel cramped. Touch nothing else."

Pass 3 — motion only: "Add scroll-reveal and hover states. Subtle. 200–300ms. Nothing bounces."

Why separate: ask for all 3 at once and Claude fixes 1 dimension well and 2 badly.

Then the mobile check: "Show me every page at 375px width and fix what breaks." 60%+ of your traffic is a phone. Agencies check this last too — they just don't tell you.

If there's anything you don't like, ask Cloud to fix it.
Just attach a screenshot and describe what you'd like to see.

Life Hack: To add animations to your website, you can simply send a reference site and ask them to create something similar.

---

## Part 5 - Ship it (15 minutes, $0/month)

1. Run: git init, commit, push to a new GitHub repo. Claude Code does this for you if you ask.

2. Go to Cloudflare Pages → Create project → connect the repo.

3. Build command: npm run build. Output directory: dist. Deploy.

4. Add your domain in the Cloudflare dashboard - DNS propagates in minutes.

Live site. Free hosting. The agency charges $150/month to babysit the same thing.

---

Realistic progression: site 1 takes 6 hours and looks like $3K
Site 3 takes 3 hours and looks like $7K
By site 5 you have a 2-hour pipeline and a portfolio that closes clients at agency prices.

The agency sells 3 weeks of process.
The process was always 1 afternoon.

RESULT:

You'll end up with a solid website - not a perfect one.

The first version will always have rough edges. Maybe the mobile layout needs work. Maybe an animation feels off.

That's the process.

Ship it. Find one thing to improve each day. Repeat.

That's how good websites become great ones.