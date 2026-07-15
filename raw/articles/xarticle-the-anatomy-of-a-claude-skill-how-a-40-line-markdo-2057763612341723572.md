---
source_url: https://x.com/heynavtoor/status/2057763612341723572
ingested: 2026-06-11
sha256: e16c8b8f96402270c258b80b39bf6ae643cba1da22aaeeedfa97ebe06059c9ae
---
---
title: "The Anatomy of a Claude Skill: How a 40-Line Markdown File Replaces a $1,200/Month Contractor"
source: "x-bookmarks"
tweet_id: "2057763612341723572"
tweet_url: "https://x.com/heynavtoor/status/2057763612341723572"
author_name: "Nav Toor"
author_handle: "@heynavtoor"
tweet_date: "Fri May 22 10:00:51 +0000 2026"
bookmark_date: "2026-05-22"
content_type: "x_article"
character_count: 12312
retweet_count: 26
like_count: 118
---

# The Anatomy of a Claude Skill: How a 40-Line Markdown File Replaces a $1,200/Month Contractor

The Anatomy of a Claude Skill: How a 40-Line Markdown File Replaces a $1,200/Month Contractor

You've built a great prompt. Maybe two. They work for a week.

Save this :)

Then you open Claude on a different machine, or a week later, and the magic is gone. The model forgot the rules. It forgot the format. It forgot your client. You're typing the same instructions for the fourth time this month, and you start to wonder if you're the assistant.

The problem isn't the model. It's everything around the model.

Most teams pay $400 to $1,200 a month for tools that do less than what a 40-line markdown file can do for free. A copy editor on retainer. A research VA. A "social media assistant" who ghosts you in week three. The skill is the cheapest senior hire you'll ever make, and almost nobody knows what one actually is.

That ends today. This is the anatomy.

## A skill is procedural memory you can read.

A prompt tells the model what to do once. A skill tells the model how you do things, every time, in every session, on every machine, forever. A prompt is a sentence. A skill is a job description.

Anthropic shipped the Skills feature in early 2026. The community shipped 600 more in the next 90 days. Lobehub alone has over 500 community skills. Anthropic's own marketplace ships 16 official ones. They are the most under-explained primitive in the whole Claude stack, and they are the one that quietly does the most work.

Let's open one up.

## The 6 components of a production-grade skill.

Every real skill, the ones that survive a week, has the same six parts. Miss one and the skill rots. Get all six and you have a worker.

1. Frontmatter. Three lines at the top of the file. A name. A description. A trigger phrase. The frontmatter is what the model reads first when it scans your skill library. If the description is vague, the skill never gets loaded. If the trigger is sharp, the skill gets called on the right job every time.

2. Trigger. The signal that tells Claude "use this skill now." It can be a word, a file type, a task pattern. Good triggers are concrete. "When the user asks for a tweet draft" beats "for social media tasks." The trigger is the difference between a skill that fires and a skill that sleeps.

3. Instructions. The body of the skill. The voice, the rules, the format, the do-nots. This is where your taste lives. A junior writes 50 lines of instructions. A senior writes 10 sharp ones. Every line you cut is a token saved on every call.

4. References. Sub-files the skill can pull in on demand. A style guide. A glossary. A list of clients. The skill stays small, but the references give it depth. Claude only loads them when needed, so you pay no tokens for unused knowledge.

5. Scripts. Optional code the skill can run. A Python file that formats a CSV. A shell command that hits an API. Most skills don't need scripts. The ones that do become unstoppable, because now the skill doesn't just write, it also does.

6. Examples. Two or three sample inputs and outputs. This is the part beginners skip. It is the part that decides whether the skill works on day one or day twelve. The model learns more from one good example than from ten lines of instruction.

That's the whole anatomy. Frontmatter, trigger, instructions, references, scripts, examples. Six pieces. One folder.

## How a skill loads: the trick that makes it cheap.

Here's the part that changes everything.

Skills use progressive disclosure. The model doesn't load every skill in your library on every call. It loads them in three levels, paying tokens only for what it actually uses.

Level 0. Claude sees only the name and description of every skill. A typical library of 40 skills costs about 3,000 tokens. That's it. The full catalog lives in the model's head for the cost of one paragraph.

Level 1. When the trigger fires, Claude loads the full SKILL.md file. Now it has the rules, the format, the do-nots. About 500 to 800 tokens per skill.

Level 2. If the skill needs a reference file or a script, Claude pulls those in on demand. The 5,000-word brand guide costs you nothing until the skill that needs it is actually called.

This is why a skill is so cheap. A SaaS tool charges you for every feature on the menu, every month, whether you use it or not. A skill charges you only when you call it. The library can be huge. The runtime cost stays small.

## The primitives, side by side.

Most people use the words "skill," "sub-agent," "plugin," "MCP," and "style" interchangeably. They are not the same thing. They do not cost the same. They do not replace the same hire.

A skill is procedural memory in a folder. It tells Claude how to do a job. It replaces a junior with a runbook. Replaces about $400 to $800 a month of contractor time.

A sub-agent is a specialist with its own context window. It tells Claude to spawn a focused helper for a bounded task. It replaces a senior on retainer. Replaces about $1,200 a month.

A plugin is a bundle of skills, sub-agents, and MCP servers shipped together. It replaces a whole micro-team in a folder. Replaces about $2,000 a month of tooling and people.

An MCP is a bridge to an external tool or service. It replaces a SaaS integration line item. About $50 to $200 a month.

A style is the output formatter. It tells Claude how the final answer should look. It replaces a copy editor. About $300 a month.

Five shapes. Same model underneath. Different price tags on the SaaS bill you stop paying.

The whole point is that you don't need five tools to do the work of one team. You need one model with five shapes.

A prompt is a sentence. A skill is a job description. The model is the worker. The folder is the office.

## The 5 decisions that define every skill.

Once you understand the anatomy, the next question is taste. Two writers can build a skill for the same job and get wildly different results. The difference is five choices.

Decision 1: Scope. Narrow or wide? A narrow skill ("write a Tuesday X thread in my voice") fires reliably and ages well. A wide skill ("handle all my social media") sounds powerful but bloats fast. Start narrow. You can always fork.

Decision 2: Voice or recipe? Some skills capture how you think. Others capture what you do. A voice skill needs examples. A recipe skill needs steps. Mixing the two creates mush. Pick one.

Decision 3: Tokens or files? Should the skill carry its knowledge in the SKILL.md, or in reference files it pulls on demand? If the knowledge is used every time, it goes in the body. If it's used 20% of the time, it goes in a reference. The wrong choice doubles your token cost.

Decision 4: Trigger sharpness. A vague trigger is a skill that sleeps. A sharp trigger is a skill that earns its keep. Write the trigger as if you're hiring for the job. "Use this when the user asks for a cold email to a SaaS founder" beats "use this for outreach."

Decision 5: Examples or no examples? Beginners skip examples to save lines. Seniors put two examples in every skill, every time. The model learns more from one good example than from ten lines of instruction. Always include at least one.

Five choices. Make them once, the skill works for a year.

## The lifecycle: skills are alive.

Most people think of a skill as a static file. It's not. A skill goes through a loop. Knowing the loop is how you keep your library clean instead of drowning in 200 stale playbooks.

Born. You write the first version. It's rough. The trigger fires sometimes. The output is okay. Ship it anyway.

Used. The skill runs in real work. You see the gaps. You see the wins. The model surprises you in both directions.

Patched. You make a 3-line fix. Better example. Tighter trigger. New rule. Patches are cheap because the skill is small. This is the part where the magic compounds.

Archived. A skill that hasn't fired in 90 days goes to the archive folder. It's not deleted. It's resting. Your library stays light. Your tokens stay cheap.

Revived. Three months later, the job comes back. You pull the skill out of the archive. The hire returns. You owe the file nothing.

A skill that goes through this loop twice is worth ten that never moved. The ones that survive earn their keep.

## A worked example: a skill from my own library.

Let me dissect one of the skills from the 40 Skills article. I'll pick the simplest one because the simple ones earn the most money.

The skill is called *tuesday-thread*. The job: write a Twitter thread in my voice, every Tuesday morning, from a one-paragraph idea.

The frontmatter is three lines. Name, description, trigger. The trigger is the phrase "draft a Tuesday thread."

The instructions are eight lines. No em dashes. No exclamation points. Open with a market-gap line. "Save this :)" on line two. Bold rest-stops every 3 to 5 paragraphs. Locked CTA. Personal signoff.

There are two references. A list of past threads that worked. A list of phrases I never use.

There are no scripts.

There are three examples. Each one is a real thread I shipped, with the original idea on top.

The whole file is 41 lines.

The skill runs about 40 times a month. Each run replaces about 90 minutes of writing time. At a $30 contractor rate, that's $1,800 of work, every month, from a 41-line file.

That's one skill. Now imagine ten.

## The Anatomy Test.

Here's how you grade any skill in 60 seconds. Five questions. If a skill fails two of them, archive it. If it passes all five, pin it.

1. Can you read the whole file in under 60 seconds?

2. Does the trigger name a specific job, not a vague topic?

3. Are there at least two examples?

4. Have you patched it in the last 30 days?

5. Would you hand this file to a junior on day one?

That's it. No framework. No worksheet. No course. Five questions, two minutes, every skill in your library audited.

The math.

Now let's stack it up. This is the screenshot.

- Claude Pro: $20 a month.

- One skill replaces about $400 to $1,200 a month of contractor work.

- Ten skills replace about $4,000 to $12,000 a month.

- Twenty skills replace about $8,000 to $24,000 a month.

- A serious library of 40, the kind from the 40 Skills article, replaces a $15,000 to $30,000 a month operations layer.

The ROI on month one is 600x at the low end. 1,500x at the high end.

You're not paying $20 for a chatbot. You're paying $20 to keep a 10-person team in a folder.

The people I know who get this stopped buying SaaS in 2026. They cancelled the writing tool. They cancelled the scheduling tool. They cancelled the research VA. They built four skills, three sub-agents, one plugin, and called it a year.

The bill went from $2,000 a month to $20.

The work got better.

## The 3 to install first.

If you're starting today, don't build 40 skills. Build three. The ones that pay back the same week.

Skill 1: Your voice. A skill that captures how you write. Tone, rules, phrases you use, phrases you never use. Every other skill leans on this one.

Skill 2: Your weekly post. Whatever you ship every week. A newsletter intro. A Tuesday thread. A LinkedIn post. The skill that turns a one-paragraph idea into a finished draft.

Skill 3: Your inbox response. A skill that drafts replies in your tone, with your rules, for your most common email types. The hour you save every day is the hour you spend building skill four.

Three skills. One weekend. The ROI is paid back in the first week.

Uncomfortable truth.

The window on this is 18 months.

Right now, knowing how a skill works is a quiet advantage. The people who built skill libraries in early 2026 are running businesses out of folders that competitors are paying $5,000 a month to replicate badly. The asymmetry is real and it is short.

In 18 months, every Claude user will have skills. Every team will have a library. The advantage moves from having skills to having taste in skills. The early movers will have 100 patched, archived, revived, sharpened files. The late movers will have 100 vague ones written by an AI that didn't know them yet.

The library compounds. The taste compounds. The time you start compounding is the only variable you control.

The next time a SaaS tool tries to charge you $400 a month for what a 40-line markdown file can do, don't blame the tool. Look at the folder you haven't built yet.

hope this was useful. Nav ❤️
