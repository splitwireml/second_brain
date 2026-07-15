---
source_url: https://x.com/cyrilXBT/status/2059461814333673705
ingested: 2026-06-11
sha256: 992e24fb2789b062ce2122c9a9545a073a84f598ba714bc6c9657c9ddec4da9e
---

---
title: "How To Use Obsidian + Vellum To Build A Second Brain That Thinks 24/7"
source: "x-bookmarks"
tweet_id: "2059461814333673705"
tweet_url: "https://x.com/cyrilXBT/status/2059461814333673705"
author_name: "CyrilXBT"
author_handle: "@cyrilXBT"
tweet_date: "Wed May 27 02:28:54 +0000 2026"
bookmark_date: "2026-05-27"
content_type: "x_article"
character_count: 14394
retweet_count: 55
like_count: 347
---

# How To Use Obsidian + Vellum To Build A Second Brain That Thinks 24/7

How To Use Obsidian + Vellum To Build A Second Brain That Thinks 24/7

A chief of staff reads everything you've read, remembers everything you've forgotten, and briefs you every morning on what matters.

Here's how to build one for $0.

What You Need Before You Start

Obsidian — download at obsidian.md. Free for personal use. Your notes are plain markdown files stored locally on your machine.

Vellum — create your account at vellum.ai. Credits are prepaid and passed through at cost with zero markup. Light daily usage runs a few dollars a month.

Readwise — readwise.io. Aggregates every highlight you make across articles, Kindle, Twitter bookmarks, and Pocket into one place. Has a native Obsidian integration that routes everything automatically.

N8N — n8n.io. Open source automation tool. Runs the workflows that connect your capture sources to your vault. Self-host it or use their cloud version.

Now you have everything you need, go through these next steps.

Step One: Build The Vault Architecture

Open Obsidian. Create a new vault. Name it CHIEF.

Now create this exact folder structure:

CHIEF/

├── 00-INBOX/

├── 01-CAPTURES/

│   ├── articles/

│   ├── ideas/

│   ├── patterns/

│   ├── questions/

│   └── numbers/

├── 02-CONNECTIONS/

├── 03-PROJECTS/

└── 04-VELLUM/

├── VELLUM.md

└── workflows/

This structure is not arbitrary. Every folder has exactly one job.

00-INBOX is where everything lands first. Unprocessed. Raw. The goal at capture time is speed not structure. You never sort things manually at capture time.

01-CAPTURES is organized by note type not topic. This is the most important architectural decision in the entire system. When you organize by topic a note about a crypto pattern and a note about a psychological principle never meet. When you organize by type they both land in the patterns folder and Vellum finds the connection between them automatically.

02-CONNECTIONS is where synthesized insights live. These are not raw captures. They are new ideas that emerge from the relationship between two or more notes. This is where your best thinking comes from.

03-PROJECTS is for active work. One subfolder per project. Everything related to what you are currently researching or building lives here.

04-VELLUM is the intelligence layer's working directory. This is where Vellum reads its instructions and stores its working files.

Step Two: Install The Essential Plugins

In Obsidian go to Settings → Community Plugins → turn off Safe Mode → Browse.

Install these three:

Templater — runs dynamic templates with real logic. You will use this for automated note formatting when captures arrive from N8N.

Dataview — queries your vault like a database. Surfaces notes by tag, date, or any property you define. Essential for the weekly connection sessions.

Obsidian Git — backs up your entire vault to a private GitHub repository automatically every hour. Set it once. Never think about it again.

Step Three: Set Up Automated Capture

The capture layer has one job. Collect everything without asking anything of you.

Every friction point in capture is a future gap in your knowledge base. Set this up once. Never touch it again.

Articles and highlights:

Install Readwise at readwise.io.

Add the browser extension. Every article you read, highlight the sentences that matter. Readwise stores them automatically. You do nothing else. No tagging. No summarizing. Highlight and move on.

Enable the native Obsidian sync inside Readwise settings. Every highlight flows into your 01-CAPTURES/articles/ folder automatically as a formatted markdown file.

Quick capture from anywhere:

Build a Telegram bot that accepts any message you send and routes it directly to your 00-INBOX folder.

Copy this N8N workflow exactly:

Node 1: Telegram Trigger → Event: message → Chat ID: your_bot_id

Node 2: Code Node → Filename: 00-INBOX/{{date}}-capture.md → Content:

## Quick Capture

{{message}} Date: {{date}} Source: Telegram

Node 3: Write File → Path: /your-vault/00-INBOX/ → Operation: create

Takes 30 minutes to build. Runs forever after that.

An idea that hits you at 2am. A wallet you want to track. A pattern you noticed in the market. Send it to the bot. It lands in your vault automatically.

Voice notes:

Record anything longer than a quick thought as a voice memo. Run it through Whisper for a clean transcript. Paste the transcript into your Telegram bot. It lands in INBOX automatically.

Step Four: Write The VELLUM.md File

This is the most important file in the entire system.

Without it Vellum starts every session knowing nothing about who you are, what you are working on, or what you want from it. With it Vellum is a collaborator who has been reading your notes for months.

Create this file at 04-VELLUM/VELLUM.md. Copy this template exactly:

## CHIEF SYSTEM — VELLUM.md

Identity

My name is [YOUR NAME]. I am [WHAT YOU DO — be specific]. My focus right now: [The one thing you are trying to get better at]. My goals for 2026: [3 specific outcomes you are working toward].

This Vault

This is my permanent knowledge base and thinking system. Every note is raw material for decisions, research, and original thinking. Nothing here is decoration.

Vault Structure

- 00-INBOX: unprocessed captures — always check here first

- 01-CAPTURES/articles: processed highlights and article notes

- 01-CAPTURES/ideas: my own thinking and observations

- 01-CAPTURES/patterns: the same principle appearing in different domains

- 01-CAPTURES/questions: things I genuinely do not know the answer to

- 01-CAPTURES/numbers: real data points with specific numbers attached

- 02-CONNECTIONS: synthesized insights from two or more captured notes

- 03-PROJECTS: active research and work folders

- 04-VELLUM: your working directory

Current Projects

Active: [What you are building or researching right now] Stuck on: [Where you need the most thinking help] Next milestone: [What done looks like for your current sprint]

What I Want From You

- Surface connections I have not seen across my notes

- Find patterns in what I am reading before I consciously recognize them

- When I ask what to focus on, answer from the vault context not generically

- Flag when something I currently believe contradicts something I saved earlier

- Challenge my assumptions before agreeing with them

## What I Am Reading And Thinking About Right Now

[Update this every Monday — current obsessions, active questions, things puzzling you]

Update the Current Projects and What I Am Reading sections every Monday morning.

Five minutes. This single habit is what keeps Vellum's context accurate as your thinking evolves.

A stale VELLUM.md produces stale output.

Step Five: Connect Vellum To Your Vault

Go to vellum.ai and create your account.

Connect Vellum to your Obsidian vault folder on your local machine.

Test the connection immediately with this prompt:

Read my VELLUM.md file and tell me in one paragraph what you understand about this vault, who I am, and what your role is inside this system.

If the response is specific and accurate your connection is working.

If it is vague your VELLUM.md needs more detail. Go back and be more specific. The quality of Vellum's output is directly proportional to the quality of the context you give it in this file.

Step Six: Build The Four Core Workflows

Save each of these as a markdown file inside your 04-VELLUM/workflows/ folder. Call them by name whenever you need them.

Workflow One: Process Inbox

Save as: 04-VELLUM/workflows/process-inbox.md

Trigger phrases: "process my inbox" / "clear the inbox" / "morning processing"

Prompt to copy:

"Read every note in my 00-INBOX folder from the last 24 hours. For each note: determine which 01-CAPTURES subfolder it belongs in, sharpen the raw capture into one specific punchy sentence, move it to the correct subfolder. After processing all notes tell me: total notes processed and where each went, any patterns you noticed across today's captures, and one connection worth exploring from today's batch. A sharpened note should be specific enough that a stranger understands exactly what was observed without any additional context. If it still needs explanation it is not sharp enough."

Workflow Two: The Daily Brief

Save as: 04-VELLUM/workflows/daily-brief.md

Set this to run automatically every morning at 6am via N8N.

Prompt to copy:

"Read everything in my 00-INBOX from the last 24 hours and everything in 01-CAPTURES from the last 7 days. Then do three things. CONNECTIONS: find the 3 most interesting connections between recent captures and older notes I probably have not noticed. Be specific. Quote the relevant passages from my actual notes. PATTERN: identify one pattern across everything I have been reading this week. What is my brain clearly working on even if I have not stated it explicitly? QUESTION: give me one question worth sitting with today based on the pattern you identified. Not a task. A question. Save this as a markdown file in my 00-INBOX folder named brief-{{date}}.md."

Read this brief before you open any app. Every morning without exception.

Workflow Three: Weekly Connections

Save as: 04-VELLUM/workflows/weekly-connections.md

Trigger phrases: "run weekly connections" / "find this week's connections"

Run this every Sunday.

Prompt to copy:

"Read all notes added to my 01-CAPTURES folder in the last 7 days. Search for connections across all subfolders simultaneously. A strong connection is one of these four types.

TYPE A: the same underlying principle appearing in two completely different domains. TYPE B: a contradiction between two notes that creates interesting tension. 
TYPE C: a pattern connecting three or more notes into one unnamed insight. 
TYPE D: a question from one note that another note accidentally answers. For each strong connection: name the connection type, write a one sentence bridge between the ideas, and create a new note in my 02-CONNECTIONS folder linking the source notes. Only surface connections that would genuinely surprise me. Minimum three connections. Maximum five. Quality over quantity."

Workflow Four: Deep Research Session

Save as: 04-VELLUM/workflows/deep-research.md

Trigger phrases: "deep research on [topic]" / "what do I know about [topic]"

Run this whenever you are going deep on a specific topic or decision.

Prompt to copy:

"Read everything in my vault related to [topic]. Tell me four things. First: what do I already believe about this based on my actual notes, not generically. Second: what have I saved that contradicts that belief — show me both sides from my own notes. Third: what perspective is clearly missing from my research based on what I am and am not reading. Fourth: what is the single most important question I have not asked yet about this topic. Be direct. Challenge me. Do not summarize what I already know."

## Step Seven: The Daily Ritual

This is how you run the system every morning. Total time: fifteen minutes.

Open Vellum. Connect to your vault.

## Minutes one to five — capture:

Before you open any app spend five minutes sending raw captures to your Telegram bot. Things you noticed yesterday. A pattern you observed. A question that came up. A number you saw. Raw. Unpolished. Just get it in.

Minutes six to ten — process:

Run the Process Inbox workflow.

Read the report. Note what got filed and what patterns Vellum noticed across today's captures.

## Minutes eleven to fifteen — brief:

Read the daily brief that Vellum generated at 6am.

This is the moment the system earns its place. You are reading a synthesis of everything you have been consuming across the past week, with the connections you missed surfaced automatically, before you have opened a single social media platform.

The rest of the day is execution not ideation.

## Step Eight: The Weekly Connection Session

Every Sunday run this full session.

Run the Weekly Connections workflow on all captures from the last 7 days.

Let Vellum read the full week of captures across all subfolders simultaneously. The connections it surfaces from a full week of inputs will be stronger than anything the daily session finds.

Review the connection notes it creates in 02-CONNECTIONS.

Pick the two strongest.

Those are your two best ideas for the week. Everything else is secondary.

## Step Nine: Close The Loop

This is the step that makes the system compound over time.

Every time a thesis plays out, a pattern you identified proves correct, or a connection leads somewhere significant — open the relevant note and add what happened.

Vellum reads these updates.

Over time it learns not just what you think but what kinds of thinking have been right for you specifically.

Once a month run this prompt:

"Read everything I have added to my vault in the last 30 days. Tell me: what beliefs am I forming that I have not stated explicitly yet, what pattern keeps appearing across different domains in my notes, what is the single highest leverage thing I could be thinking about right now based on everything in this vault, and what am I clearly not reading that the gaps in my notes suggest I should be. Only give me insights specific to my actual notes. No generic advice."

## What This System Produces

At 30 days the vault feels like a useful tool.

The daily brief occasionally surfaces something you had completely forgotten that turns out to be exactly relevant to what you are working on today.

At 90 days it starts feeling different.

Vellum begins connecting things from month one to things from month three. You ask it a question about something you are researching and it finds the note from eight weeks ago you had no memory of saving. The vault knows things about your thinking that you do not consciously remember.

At 6 months it is something else entirely.

You have a record of every belief you held and changed. Every pattern that appeared in your thinking before you consciously recognized it as an obsession. Every connection that turned into an insight that turned into a decision that turned into an outcome.

The intelligence you have after 6 months of this is not the same intelligence you started with.

It has been compounding while you were busy living your life.

Most people are starting from zero every single day.

This system makes sure you never do.

love what vellum.ai is doing. check them out
