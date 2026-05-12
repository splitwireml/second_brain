---
title: "HowHermesAgent"
created: 2026-04-21
updated: 2026-04-21
type: transcript
tags: []
sources: []
---

# HowHermesAgent


**Speaker 0**


[00:00](#t=0) So I've been doing kind of a deep dive into Hermes agent and the different functions it has, and this was one thing that I thought was pretty interesting. And I don't know, I haven't heard a lot of people talking about it, but I want to do a video on it because I thought it was a pretty nice feature. So, Hermes agent, eight hidden models, and you've been running them the whole time. And this is about auxiliary models. Most people never mess with them, but it could save you a lot of money and could improve your Hermes agent performance if you take a look at it. So today I'm going to show you what they are, which ones matter, and the one config that can cut your auxiliary cost by 90%.

[00:36](#t=37) So if you use your Hermes agent a lot for heavy duty software engineering coding tasks, you're probably using a frontier model, Opus, Sonnet, GPT-5, something that can be quite expensive because you want quality, but Hermes just doesn't use your model for the chat itself. And for the specific task you give it, Hermes silently runs eight background tasks on top of your chat. Things like compressing your conversation when the context gets too big, summarizing web pages after it fetches them, analyzing images, and writing to persistent memory.

[01:09](#t=70) On the default config, those tasks are either inherited by your main model, which can be quite expensive, or it falls back to Gemini Flash through an auto-detect chain. And this goes from OpenRouter to New Portal and then into Codex. So if you have OpenRouter configured like I do, it'll automatically use Gemini Flash 3 for most of these tasks. But each task has different needs, so summarizing a page is different from analyzing an image. Compressing a long conversation is different from classifying whether a command is dangerous. So you may want to use different models for these different tasks.

[01:46](#t=106) So here are the eight tasks. The the top four here are the ones that cost the most in terms of spend. Compression is for uh long summarizing your conversation when the context hits the threshold. Web Extract is to summarize a web page after Hermes fetches it. Vision is analyzing image and browser screenshots, and obviously certain models are better at that than others. Flush Memories is a task that writes durable facts from your chat to your memory files when a session ends. Session Search here, uh this summarizes past sessions when you search them. Skills Hub matches your query to an installed skill.

[02:26](#t=147) MCP dispatches MCP tool calls and approval classifies risky commands if you're in smart approval mode. So like I said, the top four here are the ones where you're going to spend the most and I should say that this is all based on the current version of Hermes as of this date, which is April 15th, 2026. They've been updating it a lot, so you may want to double-check if you're watching this at a later date to see exactly what kind of auxiliary tasks they have here. So where the spend actually lives, and number one by far is compression. It fires every time your context fills up to the threshold.

[03:05](#t=186) So for heavy users, if you're live coding or have complex automated workflows, this could fire 10 to 20 times a day. And this is your biggest cost by far. Flush Memories fires on every session end. So if you do /new or do /end exit, this Flush Memories will work and it basically looks back at the context and summarizes and stores memories. It's cost less than compression, but it still does add up. Web Extract fires on every web page that the agent summarizes. So if you use Hermes a lot for research, this is going to get hit constantly. And then Vision

[03:44](#t=224) Vision fires on every image and browser screenshot that you send it. It's lower frequency for some people, but it can be expensive per call because the images eat a lot of tokens. And certain models are specifically designed for vision tasks. So setting this is less about cost but more about having the right model for the task.

[04:03](#t=243) Okay, so where are these actually? These are in the config. Let me show you this myself. Now, I'm using this with WSL on Windows. It's going to be different if you're using this in a Mac. Sorry, this is small, but on the bottom of your file explorer here, you're going to see something called Linux.

[04:21](#t=261) And this is the WSL workspace basically. Um and then you're going to have a folder, it's probably going to be called Ubuntu. Mine's called Debian, which is a different uh WSL provider. But yours, the default is Ubuntu, so you might have it as that. Then you look under the home folder and then whatever your user ID is, and then you're going to do dot Hermes, dot Hermes directory. And then you're going to see all of them here and this is the file you want, config.yaml. Sorry, once again that the the text is small here.

[04:56](#t=296) So this is the config file and it's going to have everything that you uh put in during the setup phase. This is just the config file that has it and you can edit this directly. You're going to look down here around line 100, depending. But you're going to see this line for auxiliary and this is where all the auxiliary models are set. You can see here the ones that I just talked about: vision, web extract, compression, session search, skills hub, flush memories is down here. So you can see you can set these here and the base the base way you're going to do this is set the provider and set the model.

[05:32](#t=332) So for instance, if you're going to be using this Gemini Flash one provider OpenRouter, that's what you're using. And then you set the model.

[05:42](#t=343) and say if you want to do haiku for web extract, provider Anthropic, model Claude Haiku 4.5. That's how you basically change it in the configurations. So by default the auto, which you saw, all these are set to uh auto right now.

[06:00](#t=360) These walks through OpenRouter, uh new portal, Codex, Gemini Flash. So I have OpenRouter configured and I was wondering why I have all these very tiny Gemini Flash charges even though I I wasn't using Gemini Flash. It's because of this, they were set to the auto for the auxiliary tasks. So which model do you want to choose? So this is up to you. You can experiment with this, but just to give you a couple of ideas, a couple of options here. For compression, some good choices are uh models that have clean summaries that can handle long context. Kimi K2 is good, Claude Haiku 4.5, Gemini Flash 2.5 Flash.

[06:38](#t=399) These are all good for flush memories. You want something that's good at small, fast, structured extraction. So GPT-4o Mini is quite good. And once again, Gemini 4.5 Flash. You'll see this one a lot and this is why it's kind of the default because it's really well balanced and very fast at a lot of these tasks. And comparatively cheap. Web Extract, uh Claude Haiku 4.5 is great. And once again, Gemini and for this you really want factual preservation for the research. So if you're going to use a little bit of a heavier model, Web Extract is a good one if you're doing a lot of research. And then Vision. So Vision has to be a multimodal model.

[07:19](#t=439) and multimodal just means it can handle images as well. So Gemini 2.5 Flash is good, but also GPT-4o. Um I last week or so I used GLM-5V Turbo, which is really nice. And most of your frontier models will also do this well, but you may want to pick a specific vision model that you like and that might be cheaper than your frontier model. And one of the big benefits obviously is going local with these. If you are able to run a local model that is pretty good and can handle these tasks, you're obviously going to be taking a background task that can cost you some money and making it cost nothing by going local.

[07:58](#t=478) So you could continue to use your frontier model, continue to use your Opus or GPT-5-4, but then in the background tasks you can use this for local. And the way you do this in the configuration is like this. Um, this is going to be vary a little bit based on how you're using it, but the base URL is going to be your localhost, which is whatever your local provider is pointing to. So you can see a lot of the common ones here, Ollama, LM Studio, VLLM, and Llama.cpp. If you've watched my videos, you've seen me set up Ollama and Llama.cpp. So that'll just point to a certain local server.

[08:39](#t=519) And then you just set that as the base URL here in the configuration. You choose whichever model it is you're using. API key, you have to put something here, but it's not actually used, so you can actually just literally just write placeholder. And then whatever the timeout is, which is why you want to make this a little bit larger than normal because local can be run slower depending. And the base, if you set base URL, this will override provider. So if you set it, Hermes will go to your endpoint, your local endpoint here and use your local model. So a little bit of a caveat, if you're doing this for compression, there's actually two configs. Uh, if we look at it here, there's actually a top-level one. I showed you the one down here, right?

[09:19](#t=560) uh right here. This is under the auxiliary part. There's also if you go up a little bit, compression is here. So you can set um auxiliary compression provider and model. And I'll show you that when we do the live demo. Um as well as the auxiliary one. So if both are set, auxiliary.compression will win.

[09:42](#t=582) And if you set the provider to auto though, in the auxiliary it overrides your top-level choice and it'll fall back to Gemini. And before we continue, I want to quickly let you know about this free weekly newsletter that I'm going to be publishing. AI Garage Weekly will be released every Friday. It'll feature the weekly AI news, model releases, along with my thoughts on each of these, summary of interesting articles, papers, and research that I found during the week, and as well as what kind of research and projects that I'm working on and just a general roundup of my random brainstorming sessions. If anyone wants to take a peek behind on-chain AI garage.

[10:21](#t=622) Like I said, it's completely free. Just sign up. The link is in the description. It's also at ai-garage-weekly.beehive.com. Let's continue.

[10:31](#t=632) Okay, enough of me talking. It's demo time. So we're going to do the the one task that is probably cost the most, which is going to be the compression. I'm going to build out a context window with the same amount of tokens and then I'm going to run compression once using Claude Opus, the API from Anthropic, and one, uh, we're going to do it with OpenRouter using Kimi 2. Obviously, if you did this local with a local model, your cost would be zero. So you can do the math, the savings there. But uh, I want to do it with a cheaper model than what you would get with a frontier model just to show you the difference. In case you can't run a local model that can handle this task.

[11:09](#t=670) So let's move over to the Hermes agent.

[11:14](#t=675) Okay, so for our first test, you can see here I'm in Claude Opus 4.6 in my Hermes agent. I've been chatting, talking about different paper. We filled this up, uh, 50,000 tokens into the context window. Not a lot for Opus's context window, but for other smaller models it's a lot. But it's still sufficient for us to test out the compression cost. So you can see here, this is the API that I have. Um, you can see I haven't spent anything today, so this will obviously go up as we keep doing these experiments, but for now, no token cost.

[11:50](#t=711) So, the previous filling up of the context window was with a different model, different provider. So, we're going to do the compression, see much, see how much that cost in API costs. So, it's doing the compression of all the messages.

[12:07](#t=728) [Music]

[12:12](#t=733) And this is the task we're going to test to see with the auxiliary models. Right now it's just using Claude Opus 4.6 to compress.

[12:25](#t=746) [Music]

[12:28](#t=748) Okay

[12:29](#t=750) and you can see it compressed it down from 62 messages down to seven. Uh this says 36 but it was at 50 down here, so we'll just go with that. And we're down back to 1%. So, Claude Opus compressed it. So let's see how much that cost us. Okay, you can see 13 cents.

[12:49](#t=770) So not a lot, but keep in mind that was only a 50,000 token window. And that is going to be our baseline that we're going to compare it when we set the auxiliary model for this one task. So keep that in mind. Opus was 13 cents.

[13:07](#t=787) Okay, now we're ready for the comparison. We're at back at 50k tokens. So for this one, we're going to try the Kimi K2. And this is from Moonshot AI. Kimi K2

[13:21](#t=802) It's a little bit of an older one. Uh this is the version that was released on September 4th, but it's pretty reasonable and should do well for this task. I'm just using this just to give you an example of a couple different versions, but I'm sure there are other models that would do well. So now you need to configure this in the config.yaml file. Your auxiliary go to compression.

[13:49](#t=829) Open router

[13:52](#t=832) and then and then Moonshot AI Kimi K2. So after you change this, you have to start a new session so that it'll pick up the changes in the config. Okay, so I had to fill up this context window, but we're back at 50,000 tokens roughly. And now we're going to try this using the Kimi 2. So even though we have a different OpenRouter model running, uh if I do compress here, it's going to use the Kimi 2 automatically. So let's do this, compress.

[14:26](#t=867) [Music]

[14:31](#t=871) and it's compressing all of the messages. There you go. finish the compression

[14:39](#t=879) hundred and thirty four messages down to six Okay and this is the actual spend on the um the compression itself.

[14:48](#t=889) it was zero point zero one nine cents. Um there's some Gemini activity going on because I use this OpenRouter key a lot, but this is for the context compression. And so you can see it's one cent.

[15:05](#t=906) uh almost almost two cents but still a significant savings over thirteen cents doing the same compression with Opus. So that's a eighty-five percent

[15:19](#t=919) savings for each compression. And this was only 50,000 tokens, not a lot. If you're doing hour-long sessions, you're going to end up filling a lot of the the context window. And it doesn't sound like a big difference, 13 cents versus almost two cents, but over the long haul, that's going to cost you a lot. There you have it. Uh so one compression pass doesn't sound like much, right? We saw 13 cents with Opus and then one almost two cents with Kimi.

[15:52](#t=952) And the one pass isn't that big of a difference, but compression fires constantly. If you're on a real work day with multiple hour sessions and research tasks, browser activity, automated tasks, coding tasks, you can easily hit compression like 10, 15, 20 times a day. And this will add up, you know. The Opus, if you're just using Opus for this every single time with the API, it can easily hit $60 a month if you're doing 15 compressions a day. But obviously, if you're doing it locally, you'll save that total amount. But even using a cheaper model like Kimi K2 here, bumps that down to $9 a month.

[16:31](#t=992) So you could save at least $50 using these auxiliary tasks, and that's real savings. And this was just the compression demo. If you use local or cheaper models on the other auxiliary tasks, you're going to stack those savings even more. So just to wrap up, um Hermes has eight auxiliary tasks you can configure independently. Uh you might want to focus on these top four: compression, flush memories, web extract, and vision. Like I said, if you have a specific vision model that you like using that has better capabilities than whatever model you're using for day-to-day work, you want to match the model to the task. Make sure you have the right model for each task. And local models work on this task too.

[17:10](#t=1031) if you want, just to point your local model

[17:14](#t=1035) to the Hermes agent, you can set that up like I showed you before. And that's a really great way if maybe your local model doesn't can't handle the main project building or whatever you're doing with Hermes agent, but you could still use it for stuff like this to get a lot of savings out of it. So that's going to be it for this video. I just thought this was an interesting feature of Hermes agent. So I wanted to do a video on it. I hope you enjoyed it. If you want to see more Hermes agent focused uh videos, please subscribe, please leave a like, leave a comment, let me know.

[17:44](#t=1065) how you've been using your Hermes agent and stay tuned because we're going to have a lot of new Hermes agent related videos and the uh real deep dive masterclass is going to start in May I believe and do a couple of videos each week in May. But that's going to be it for this one. Thank you for watching.
