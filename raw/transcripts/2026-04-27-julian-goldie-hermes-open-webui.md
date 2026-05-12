---
title: "Julian Goldie SEO - Hermes + Open WebUI Setup"
created: 2026-04-27
updated: 2026-04-27
type: transcript
platform: x
source_type: video
author: juliangoldie
tweet_id: "2048440694382145776"
video_url: "https://x.com/JulianGoldieSEO/status/2048440694382145776/video/1"
duration: 550.43
segments: 13
transcription_model: mlx-community/VibeVoice-ASR-4bit
transcription_time: 259.36
sources: []
---

# Julian Goldie SEO — Hermes + Open WebUI Setup

**Video URL:** https://x.com/JulianGoldieSEO/status/2048440694382145776/video/1
**Author:** Julian Goldie SEO
**Duration:** 9m 10s (550.43s)
**Transcription:** VibeVoice ASR 4-bit | 259s | 11.06 tok/s

---

## Segments

**[0.0–32.6s | Speaker 0]**
Today we're going to be setting up Open WebUI with Hermes AI Agent. And this just makes Hermes way more powerful and easier to use. So you can do far more with your agents and manage them much more easily using Open WebUI. So let's get straight into it. I'm going to show you exactly how to use it. If you're wondering, okay, what are the benefits of this? Well, you can run it with Ollama, it's easy to set up, you get amazing designs, you get a nice UI for your Hermes AI Agent, you don't have to use the terminal UI, and it's going to look a lot better and it's easier to use. So let's get straight into it.

**[32.6–66.7s | Speaker 0]**
What we're going to do over here is we're going to take the GitHub information and then we're going to paste it into Hermes, which I've got running over here on the terminal. And we're going to set this up with Hermes and then we'll copy that. And then what we're also going to do is get the documentation for Hermes and what Open WebUI. So we've got the documentation on Open WebUI and Hermes here. And we'll come on to why this is so powerful in a minute, but basically it gives you a really nice UI, right? So you can see an example here. So we can use it basically as a messaging platform for our agent to handle and manage this. And we can get Hermes to set it up itself, right?

**[66.7–105.1s | Speaker 0]**
So you can see here how I've pasted in the information for it to get started and now it can just begin to install this, right? Now, of course, you need Hermes to set up from there, but also what you need to make sure is that you have the API server set up, right? So Hermes has to add an API server and an environment file so it can start using Open WebUI. And then from here, we can start running that directly with the gateway on Hermes. And you might be wondering, okay, why would you use Open WebUI? Well, basically, Open WebUI is the most popular self-hosted chat interface. So you can use this as a front-end agent to interact with Hermes, right?

**[105.1–145.2s | Speaker 0]**
You can for example have multiple accounts that you manage. You can have a modern chat interface. You don't have to use the terminal. And you get nice conversation management too. Now, if you've ever used Hermes before, you know that you get the Hermes dashboard, right, which looks something like this. We'll pull this up in a second. It's a web UI. And it's okay, but the biggest issue is that it doesn't actually give you a chat option here, right? So you can manage your scheduled tasks, you can manage your skills, you manage your sessions, but you can't actually speak to the agent directly through the official dashboard, which is a bit limited. So that's why we want to set up this directly with Open Web UI instead. So it's going to ask you like, do you want to run this?

**[145.2–171.1s | Speaker 0]**
You want to set up, etcetera. It's going to ask for a few permissions as you go along. We're just going to click yes to those. You can also run this with Docker as well. And bear in mind this is free to use, right? So Open WebUI is an open source project. Hermes is an open source project. Together, they are both free. Another interesting thing is you can actually use this with voice and video calls too. And it's available for mobile too. So you can manage your agents via Open WebUI on mobile as well.

**[171.5–209.9s | Speaker 0]**
It has web search options too, which is going to make it more powerful. And also web browsing capability. And also, one thing that's useful here is like if you're using, for example, the terminal UI here, you don't really have the ability to, you know, for example, create images inside the terminal, right? And open them up and preview them and that sort of thing. So what you can do instead is you can use Open WebUI with the image generation and editing integration instead. And you can also switch between models more easily too. So this is beginning to set this up inside Docker, which is previously how I've set up other tools, for example, like Paperclip and Multico, which are also other options for a sort of mission control for Hermes.

**[209.9–235.7s | Speaker 0]**
Open Web UI is not so much a mission control, but it's more of an agent interface where you can chat directly with it. So you can see that's beginning to build out now. And now you can see inside Docker we have this ready to go and it's hosted locally, right? So Hermes has just set the whole thing up, configured it, made sure it works, set it up in Docker, siloed it away in Docker, read through the GitHub documentation, and been like, right, boom, let's get this set up. And it also checks it works.

**[235.7–275.8s | Speaker 0]**
So now we've got this ready to go as you can see. So, Open Web UI is set up. We'll click on get started. We're going to just plug in our details here. We set an account as you can see. Then you can see it comes up with an update page. We'll click on okay, let's go. And now we have Hermes, which is this one right here that we can chat with, right? So, we can start chatting with Hermes directly inside here. Now, how much nicer does that look than if you go inside here, right? Which one do you want to use? For 99% of people, it's going to be using the the chat web interface, right? As you can see. Now, it may ask for some more permissions once you've actually opened this up, and then we'll just make sure it works and configures it.

**[275.8–314.6s | Speaker 0]**
And boom, look at that. That is working beautifully. Now, the other useful thing about this is we also get a preview option here. So we can use this kind of like ChatGPT, but it's for our Hermes agent, which is awesome. And also, the other cool thing about this is you can switch between your models here. So you could link this to OpenClaw, you could link this to other models, you know, for example, we've got DeepSeek V4 Flash Cloud there. We've got our Llama models running right there. And you know, you can switch between your agents. You've also got local and external, right? So, it's quite easy to switch between them. There's a nice little workspace section here as well, where you can import new models. You've got your notes section, you can search between conversations.

**[314.6–351.5s | Speaker 0]**
But the main benefit of this is that you can interact with Hermes inside a kind of ChatGPT style setup. You can also have code interpreters set on too, and also you can upload things here, right? So if we go into, for example, Hermes like this, as you can see, this is a little bit more messy because we can't really upload files in there, right? It's pretty difficult to do that. We'd have to like type in the actual path of the file and everything else. If we go inside Open Web UI, well we can attach files, we can attach notes, we can attach knowledge, reference chats, etc., which is pretty cool, right?

**[351.5–391.8s | Speaker 0]**
And then if we just test something else, so if we say, okay, build a ping pong game, you know, just as a little example here, it's going to start going off and working its magic. Now, also you can manage your setup in terms of different profiles. So if you go to your workspace section here and you click on new model, you can see that you can select between different models, you can add a tag, and you can also insert a system prompt on that model. So this is like a completely different version of Hermes that you can set up. You can give it different tools like web search, image generation, etcetera. You can set up the built-in tools with that Hermes agent. And you can also, you don't have to use Hermes, right? You could switch between all these different APIs.

**[391.8–429.8s | Speaker 0]**
You can also add knowledge and context here and upload files. You can select different tools and skills to use, but basically you can have different agents working together. And you can also save prompts that you like, knowledge that you like, you can add context here, which is super useful. So, you know, one thing that would be super useful is you link this to something like Obsidian and you add Obsidian running right there. And then also you've got tools here. So you can insert a new tool and you just insert the details inside the chat like that. Right. You could probably get Hermes to actually set those up for you. Now, if we go back to this section, we can also have multiple tabs working together. So you know, you could have two different chats going on.

**[429.8–469.6s | Speaker 0]**
And then also if we go inside here and we say, okay, build a game, I just want to show you that Hermes actually works. So we've got the whole chat right here. Something else to note too is that you can also preview this kind of like, you know, ChatGPT where you can preview the code that you actually build. And if you have any problems like this, then you can say, okay, why are you not responding? And Hermes will actually just go off and fix it for you. And now you can see if we have a look at this chat right here, it's actually working now. So it said, right, it's saved. We can open this up in a browser and look at that. It's ready to go. So it's a really it's just a smooth way to use Hermes. And I think eventually, you know, inside the mission control that they've currently got, they will add a chat feature inside there.

**[469.6–508.8s | Speaker 0]**
But whilst you're waiting, you can use this with Open Web UI. It's really easy and simple. And also, you know, if you did want to preview something like this, for example, inside the chat, you would just go over here and say preview it, right? If you have any problems, just go inside Hermes and ask it to fix it like that, and that fixed it pretty well and got it working straight away. But that's basically how to use Open Web UI. Now, if you like this stuff, I will actually add full guide to Open Web UI inside the AI Profit Board. Link in the comments and description or just go to theaiprofitboard.com. And inside the community, we have an amazing community of people using AI agents, using them to grow, using them to build, etc. You can go inside the calendar and jump on weekly coaching calls where you can ask questions, share your screen, ask about your setup, etc.

**[508.8–548.8s | Speaker 0]**
You can get all of my new trainings inside the classroom here. So we add new advanced daily tutorials inside this section. And then also you can meet people in your local city who are using stuff like Hermes, OpenClaw, etc. to win with AI, save time and automate their business. So, thanks very much for watching. I've added the guide inside the AI Profit Boardroom. We've also got a two-hour full course on how to use Hermes, another six-hour course on how to use OpenClaw. We've got a full tutorial on how to build anything with DeepSeek. And we've also got a full video tutorial and step-by-step guide on exactly how to use Hermes V0.11, which is super powerful. So, thanks very much for watching. Hope to see you inside the AI Profit Boardroom. You can connect with me personally inside there too.

**[548.8–550.4s | Speaker 0]**
I'll see you in the next one. Cheers, bye bye.
