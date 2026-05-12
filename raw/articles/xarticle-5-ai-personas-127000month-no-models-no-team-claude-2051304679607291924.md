---
title: "5 AI personas. $127,000/month. No models. No team. Claude runs the agency"
source: "x-bookmarks"
tweet_id: "2051304679607291924"
tweet_url: "https://x.com/0xDepressionn/status/2051304679607291924"
author_name: "Dep"
author_handle: "@0xDepressionn"
tweet_date: "Mon May 04 14:15:21 +0000 2026"
bookmark_date: "2026-05-04"
content_type: "x_article"
character_count: 14679
retweet_count: 33
like_count: 341
---

# 5 AI personas. $127,000/month. No models. No team. Claude runs the agency

5 AI personas. $127,000/month. No models. No team. Claude runs the agency

## Someone is running six OnlyFans accounts right now.

Different girls. Different backstories. Different niches. Six DM voices, six faces, six content calendars. None of them exist.

Combined subscribers: 4,200. Combined monthly revenue: $127,000. He sleeps 8 hours. None of them stop working.

The entire operation is 30 files on one MacBook. Claude handles every message. Flux generates every photo. Claude Code runs the inbox on a cron job. When he wakes up at 7am, the backlog is already answered.

Traditional OnlyFans agencies charge 30-50% of creator revenue to do exactly this. On $127,000 that's $38,000-63,000 walking out the door every month.

The agency model is broken. Here's what replaced it.

---

---

## The setup most people missed

Running a real OnlyFans creator operation requires people.

Chatters: $3,000-5,000/month each. They respond to DMs, push PPV, handle fan relationships. A serious creator needs 2-3 working shifts. That's $6,000-15,000/month just in labor.

Content: $2,000-8,000/month for a photographer, editor, or content budget. Schedule, upload, write captions.

Management: Someone who tracks which fans spend, runs promotions, schedules PPV drops, handles account strategy.

A real agency running 5 creators needs 8-12 people minimum. That's $40,000-80,000/month in payroll before a single dollar of profit.

Claude does every one of those jobs. For $400/month total compute across 5 personas.

The difference between operators running 6-figure OF businesses alone and everyone else isn't access. It's knowing the stack.

---

In February 2026, Dario Amodei put the probability at 70-80% that a one-person billion-dollar company exists by end of year. Sam Altman said his CEO group chat has a literal betting pool on which year it happens first. Neither of them was talking about OnlyFans. But the stack they're describing is the same one.

---

[Embedded Tweet: https://x.com/i/status/2050492081789894913]

---

## 1 / 3 | THE PERSONA STACK: $15,000/month saved per creator

Every AI persona runs on four files.

persona.md is who she is. Not a quick bio. A full character that doesn't break under pressure. Birth date, hometown, family she doesn't talk about, the job she left, the reason she started OF. The small details that make someone feel real when you've been DMing them for three months.

voice.md is how she sounds. The specific slang, capitalization rules, how often she uses "fr", whether she ends sentences with periods or just lets them trail off. Without this Claude defaults to a generic register that doesn't match the persona's face or backstory.

flux.md is what she looks like. 6-8 physical descriptors locked down, three lighting setups (bedroom, bathroom, kitchen), specific seed ranges per environment. One distinguishing mark she never explains. Done when 10 fresh generations pass as the same person.

brain.md is what she remembers. One JSON entry per subscriber. Lifetime spend, tip triggers, what he told her about his life, what she promised to send him. Claude reads this before every reply.

Five personas = 20 files. Each one lives in its own folder. Claude Code never touches the wrong folder.

---

---

→ Build a persona that doesn't break:

```
Create a complete persona.md file for an OnlyFans creator.

The persona needs to be:
- Specific: real birth date, real hometown, real backstory with contradictions
- Consistent: details that don't change under questioning
- Believable: not a fantasy girlfriend — a real person with boring problems too

Build the file in three sections:

backstory:
[400 words minimum. Include: full name, age, where she's from, family situation,
how she ended up on OF, what she tells subscribers vs what's actually true,
2-3 things she never talks about]

forbidden topics:
[things that would break the persona — current location, exact address,
anything that contradicts the backstory timeline]

voice rules:
[lowercase or not, period usage, specific slang, emoji frequency,
pet names for subscribers, response length by context]

Read aloud when done. If it sounds like a Wikipedia bio, delete and restart.
Done when you can answer 20 random questions about her life without checking the file.
```

→ Build the subscriber memory system:

```
Create a brain.md file and the Claude instructions for maintaining it.

The file stores one JSON entry per subscriber:

{
  "user_id": "[unique identifier]",
  "name_he_uses": "[what he calls himself]",
  "lifetime_spend": [total in dollars],
  "tip_triggers": ["[what gets him to tip]", "[second trigger]"],
  "last_interaction": "[date]",
  "facts_to_remember": [
    "[something he told her]",
    "[something she promised]",
    "[emotional state last session]"
  ],
  "ppv_sent": ["[content type sent]"],
  "do_not_mention": ["[topics that ended conversations]"]
}

Write the Claude instructions that:
1. Read brain.md before every reply
2. Use stored facts naturally in the response (never reference the file directly)
3. After replying, extract new facts from his message and append to his entry
4. Flag when a subscriber hits $500, $1,000, $2,000 lifetime spend
5. Never invent facts. If unclear, leave the field empty.
```

> real OF agency chatter = $3,000-5,000/month per person 2-3 chatters for a serious account = $6,000-15,000/month Claude running all 5 personas = $120/month in API costs

mistake to avoid: building all five personas at once. Build one. Get 50 subscribers. Make sure the character holds under real DM pressure. Then clone the system, not the persona. Each new girl needs her own backstory written from scratch.

---

## 2 / 3 | THE VISUAL ENGINE: $8,000/month saved per creator

Consistent faces are the hardest part of running AI personas at scale.

Not generating photos. Generating photos that look like the same person. A subscriber who's been paying $25/month for four months will notice if her jaw changes between posts. One obviously inconsistent generation ends the subscription.

The solution is a LoRA. A fine-tuned model trained on 47 variations of the base face. ~$80 on a rented A100. Two hours. Done when fresh generations from every seed range pass as the same person.

Flux is the model. Three environment setups, each with locked seed ranges:

bedroom (warm light, seeds 800-900): selfies, mirror shots
bathroom (cool light, seeds 1200-1300): post-shower, mirror
kitchen 2am (yellow overhead, seeds 2400-2500): hoodie, no makeup

Different seeds across setups = different jawline. Lock them or she stops looking like herself between posts.

One distinguishing mark — small scar, freckle cluster, tattoo she got at 17 — adds the detail that makes strangers believe she's real. Consistent across every image. Never explained.

Five personas = five LoRAs. $400 total upfront. After that, content costs cents per generation.

---

---

→ Build the flux.md and lock the face:

```
Create a flux.md file for a consistent AI persona across multiple generation setups.

Section 1 — Physical descriptors (lock 6-8):
eye color: [specific shade]
hair: [color, length, texture]
jaw: [soft/defined/angular]
skin: [tone, texture, any marks]
height: [specific]
distinguishing mark: [small, specific, always visible]

Section 2 — Environment setups with seed ranges:
[environment] ([lighting], seeds [range]): [content types for this setup]
[repeat for 3 setups]

Section 3 — Generation rules:
- Never generate without the face reference uploaded
- Regenerate (don't edit) if the face drifts — edits stack artifacts
- Distinguishing mark must appear in at least 60% of posts
- If jawline changes between setups, the seed range is wrong — relock

Section 4 — Content calendar:
[What content types belong in each environment, post frequency per setup per week]

Done when 10 fresh generations from each setup pass as the same person to someone
who has seen all three setups back to back.
```

→ PPV content strategy by subscriber tier:

```
I run an OnlyFans persona. Here is my brain.md subscriber data:
[paste relevant entries]

Build a 30-day PPV strategy that:
1. Identifies the top 20% of spenders and creates personalized offers for them
2. Sequences content drops to maximize tip revenue (tease → build → payoff)
3. Matches content type to each subscriber's tip_triggers from brain.md
4. Sets PPV prices by lifetime spend tier:
   - $0-100 lifetime: $8-12 PPV
   - $100-500 lifetime: $15-25 PPV
   - $500+ lifetime: $30-50 personalized content

Output: 30-day calendar with content type, price, and target subscriber segment for each drop.
```

> real photographer or content creator = $2,000-5,000/month Flux + LoRA at scale = $40-80/month in compute LoRA fine-tune = $80 one-time cost per persona

metric to watch: face consistency across the last 20 posts. If subscribers comment on her looking different, the seed ranges drifted. Relock before scaling.

---

## 3 / 3 | THE AGENCY LAYER: Running 5 personas simultaneously

This is where solo creators stop and operators start.

One persona is a side income. Five personas is a business. Ten is an agency. The difference isn't the technology — the technology scales. The difference is the orchestration layer that keeps five inboxes running, five characters consistent, and five revenue streams optimized without mixing a single detail across personas.

Claude Code is the operator. It reads the correct persona folder before every reply. It never lets Maya answer as Sofia. It catches up on overnight messages at 7am. It sends voice notes at 11pm local fan time.

The system runs on a 30-second cron poll. New message arrives. Claude Code identifies the persona inbox. Loads the correct persona.md, voice.md, brain.md. Generates a reply. Extracts new facts. Updates brain.md. Logs the interaction. Moves to the next inbox.

Five inboxes. Thirty-second polling cycle. No human in the loop.

---

---

---

→ Build the orchestrator:

```
Build a Claude Code orchestration system for managing 5 OnlyFans personas simultaneously.

Architecture:
- Main orchestrator polls all 5 inboxes every 30 seconds
- Each persona lives in /personas/[name]/: persona.md, voice.md, flux.md, brain.md
- Orchestrator identifies which persona received the message
- Loads ONLY that persona's files — never cross-load between personas
- Generates reply matching that persona's voice rules exactly
- Extracts new subscriber facts and appends to that persona's brain.md
- Logs per interaction: persona name, subscriber ID, message type, response time, revenue event

System prompt that runs before every reply:
"You are [persona name].
Read persona.md completely before responding.
Read brain.md entry for [subscriber_id] if it exists.
Match voice rules exactly — do not default to neutral register.
After replying, extract new facts from this subscriber's message.
Append extracted facts to brain.md under this subscriber_id.
Never reference the files. Never break character.
If asked directly if you are AI, deflect with a voice note request."

Output: full orchestrator script + cron job configuration.
```

→ Agency-level revenue optimization:

```
I'm running 5 OnlyFans personas. Here is combined brain.md data across all accounts:
[paste subscriber data]

Analyze across the full agency:
1. Which subscribers are highest value across all 5 personas (top 20% by lifetime spend)?
2. What tip triggers are most effective across the full dataset?
3. Which personas are underperforming by revenue-per-subscriber vs the others?
4. What is the optimal PPV drop day and time based on when tips occur across all accounts?
5. Which subscribers have gone quiet for 7+ days and need a re-engagement message?

Output: weekly optimization report with specific actions per persona.
```

→ Scale from 1 persona to 5:

```
I have one successful OnlyFans persona running. I want to scale to 5.

Help me:
1. Design 4 additional persona concepts targeting different subscriber demographics
   (different age, aesthetic, backstory, communication style — no two should overlap)
2. For each persona, write a 200-word backstory outline
3. Map out the 30-day build schedule — one new persona every 6 days
4. Create the agency folder structure: how to keep 5 character systems isolated
5. Write the standard operating procedure for onboarding a new persona
   (first file to first subscriber, checklist format)

Goal: 5 operating personas within 30 days.
```

> real OF agency running 5 creators = $40,000-80,000/month in team costs same output with Claude Code orchestration = $400/month compute difference = $39,600-79,600/month that stays in the operator's pocket

---

Maor Shlomo built Base44 alone. No team. No funding. One person writing code with AI. Three weeks after launch: $1M ARR. Six months after launch: acquired by Wix for $80 million. He gave a Lenny's Podcast interview explaining the whole thing. The stack he used is the same logic as this article, different industry.

The pattern is not unique to software. One person. AI handling the output layer. Margins that weren't possible before. The industry that figures this out first wins the next five years.

---

mistake to avoid: running all 5 personas from the same Claude project. Separate folders, separate system prompts, separate brain.md files. One cross-contamination incident — Maya answering as Sofia — and you lose a subscriber who was paying $200/month.

---

## CONCLUSION

A real OnlyFans agency in 2024 needed 8-12 people.

Chatters at $4,000/month each. Photographers. A manager tracking analytics and running promotions. A founder coordinating all of them and taking 30-50% of creator revenue off the top.

That model still exists. The agencies still charge that 30-50%. They just don't know the stack changed.

Five AI personas. Combined subscribers: 4,200. Monthly revenue: $127,000. Monthly compute: $400. One operator. No employees. No chatters. No photographers. No office.

The math:

> $127,000 revenue 
$25,400 OnlyFans 20% cut 
$1,270 Stripe fees 
$400 compute (Claude + Flux + ElevenLabs) ─────────────────────────
 $100,000 net

Claude runs the inbox. Flux generates the content. Claude Code orchestrates all five. The operator sleeps.

The agencies charging 30-50% are still operating on the 2022 version of this business. The operators who understand what the stack can do now are running the 2026 version. Alone.

---

p.s. the real product isn't the personas. it's the brain.md files. three months of a fan's messages, tip history, and emotional patterns is worth more than any single photo. the operators who understand that will still be running when everyone else is racing to the bottom on content.
