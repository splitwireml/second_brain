---
title: "Your local LLM is 10x slower v2.json"
created: 2026-04-11
updated: 2026-04-21
type: transcript
tags: []
sources: []
---

# Your local LLM is 10x slower v2.json


**Speaker 0**


[00:00](#t=0) You're probably familiar with Ollama, right? This is what it looks like. You can launch it, you can talk to it. Never mind that we're using Qwen3-4B, that's just the standardized thing that I'm doing. And the prompt.

[00:10](#t=10) doesn't matter what it is. 100 tokens per second is what Ollama gives us. Ollama runs on Llama CPP. It has a little bit of overhead, but you can also run Llama CPP directly and query it remotely, which is what software developers are going to be interested in if they're going to be using it as a code assistant, for example, or with agents.

[00:26](#t=26) Hold on a minute. And that's going to be key here in a moment. I'm going to start up Llama Server, pointing to the same model by the way. And Llama Server has this nice user interface that we can also say hello to. And this one gives us tokens per second. 124. So a little bit better. So that's chat.

[00:40](#t=40) We're chatting with one model, one request at a time, and it's not even how code assistants work because code assistants requires a lot of different chats going on at the same time. What if I query this remotely? Here I wrote a little script, basically this is from my race to 1 million episode, but this one will do a thousand. And I'm going to be communicating from my laptop here to my Mac Studio that's running Llama Server. Boom. And there it goes. And now I'm twiddling my thumbs.

[01:05](#t=65) Boom boom boom. Look at that.

[01:07](#t=68) 120 tokens per second. Very close numbers, right? You know who you don't want to twiddle their thumbs? Your agents that are working away at your code base, sometimes tens of them or hundreds of them. And we're even going to increase our target tokens to 1,000 so we have a little bit of room to walk around.

[01:23](#t=84) Boom I'm gonna watch this in real time. Check this out. This is gonna be insane.

[01:29](#t=89) What? 826 tokens per second from Llama CPP. And you might think, oh, okay. I've seen this trick before, right?

[01:37](#t=97) on my channel probably. Uh concurrency is set to 128. Well, I'm about to show you a new trick because even with concurrency 128, without that trick, you still get 231 tokens per second, which is still better, but we're limited to what Llama CPP is capable of just by itself. It can handle as many concurrent connections as something like VLLM for example, and I've got other videos to show that. So what am I doing?

[02:03](#t=124) Well.

[02:04](#t=125) I wrote this little launcher. This is actually inspired by Donato Capitella's distributed launcher. I recently featured that in a video about this thing, separate video. You can watch that if you want. But here we're just running this on one machine. So I created this launcher, which allows you to tweak a few knobs that Llama CPP provides for tweaking, along with sweeping and exploring what your machine is capable of. For example, I have this running on a Mac Studio, but what if you have a Mac Mini for example? Well, you can run this on there.

[02:33](#t=154) if you have a Windows laptop or another Linux laptop or an Nvidia one, it doesn't matter because Llama CPP will run on all those and this launcher is going to run on any of those as well because it's just Python and it'll find the best combination for you to run Llama CPP as a server while twisting those knobs. I probably shouldn't say that on YouTube. Um, somebody might complain.

[02:56](#t=176) [Noise]

[02:59](#t=179) some sensitive soul out there. Let me show you how this works. First we've got some tests. We can do a single request, select your model, select where you're running it, and run. And now this will just query Llama CPP, get your tokens per second for that configuration, which is 127, very close to what we've seen. You can do

[03:16](#t=196) concurrent requests There we go. Concurrent requests count 128, concurrency 128, total tokens, average request tokens per second. and then throughput

[03:24](#t=205) So we got a throughput 240 tokens per second on the same model. By the way, all this stuff is documented in the repository. If you're getting into cyber right now, there's an awkward gap between I watch the videos and I can handle real situations. And the gap is exactly what this is for. This is TryHackMe, where you learn cyber by doing it. Interactive labs, real scenarios, all browser-based with a global community of over 6 million people. They just launched an entry-level cert called Cybersecurity 101, also known as Sec1. Quick tour only, no exam spoilers. The big idea here is applied fundamentals.

[04:02](#t=242) You train hands-on, then Sec1 checks you can actually perform the basics in realistic situations, not just memorized definitions. This is for students going for their first cyber role, career switchers, and interns or junior folks, like zero to two years, who want proof they can actually do the fundamentals. High-level, it touches what you'll actually run into: operating systems, networking, web-based security basics, a little bit of blue team fundamentals, a little bit of red team fundamentals, and malware analysis at a beginner level. And this is what makes it different. A lot of beginner certs feel like vocabulary quizzes. Sec1 is trying to be a hands-on checkpoint instead.

[04:40](#t=280) When you finish, you get an instant result, a digital certificate, and a shareable badge. If you're getting started in cybersecurity and want a hands-on way to prove your fundamentals,

[04:49](#t=290) [Speech]

[05:01](#t=301) link below. All this stuff is documented in the repository. It's called Llama Throughput Lab. There's other tests in here, but there's one really interesting one and it's called Full Sweep. This takes a while.

[05:13](#t=313) there's 308 different combinations of how many instances of Llama server you start. That's the key here. Hint, hint.

[05:20](#t=321) So you run multiple instances of Llama Server to be able to reply because a machine that's as powerful as this has a lot of memory these days. This one has 64 gigs of VRAM or it's called unified memory in Apple Silicon terms.

[05:35](#t=335) This Mac Studio has 512. But that's not the limiting factor when it comes to running these. The limiting factor here is the compute on the GPU. We're running all this on the GPU because we don't want to do it on the CPU, it's going to be extra slow. That's why we're using the GPU here. And you can

[05:49](#t=349) you can only do so much when you're running multiple Llama servers at the same time. You're no longer limited by memory, obviously, unless you're running huge models, which you can do here. You can run on a 512 gigabyte machine, you can run like four Llama 70 billion parameter models at the same time in four instances of Llama Server. So those are instances.

[06:10](#t=371) then parallel. Llama Server exposes a parameter called parallel, and this has been documented pretty well on the GitHub repository under llama.cpp by the creator of llama.cpp himself, Georgi Gerganov. Another knob you can twist.

[06:25](#t=385) Uh, maybe I should stop it with that. Um, somebody's going to get mad. I'm not twisting any knots. Concurrency is another uh parameter you can alter. And that's what I showed before in my videos where we can send multiple requests to Llama Server. Why do we care about that? Well, if you're just doing chat, then by all means, go ahead and chat and wait for it to finish. But a lot of times we want to go beyond that. Imagine a folder with thousands of photographs that you want to analyze. Or a video with millions of frames. You don't want to be sitting there and waiting for one frame at a time to be analyzed, do you? Or imagine another scenario where you have a bunch of agents orchestrated together. Some are doing planning, some are doing implementation. You want them working at the same time. So that's where concurrency comes in.

[07:05](#t=426) Getting back to the sweep, this will do a full sweep. So instances, parallel, and concurrencies, and it'll find out where the optimal spot is on your computer, whatever computer you're using. You can select that test, sweeps, and then click on run selected test, and off it goes.

[07:21](#t=441) There it goes.

[07:22](#t=442) uh just keep in mind that this will take a while. Also, on a slower system it'll take a real long while. So right now we're on four out of 308 different combinations. But as it's sweeping, you can see the numbers coming in. 128 tokens per second, 193, 263, 314. So you can see how these different parameters are affecting that output. If I go to my results folder here, I did a full sweep on this Mac Studio, of course. Now, I should probably create a nice looking chart, but this is also on GitHub and open source, so feel free to muck with it if you want to.

[07:55](#t=475) Look at these numbers. 1226 tokens per second. That's with 16 instances. In other words, I started Llama Server 16 times. Parallel flag set to 64.

[08:05](#t=485) 1024 concurrency. Now keep in mind, this is just a benchmark. If you want to do real-world cases, this will only give you some guidance and point you in the right direction, but always make sure you actually test your real-world scenarios. And finally,

[08:17](#t=498) Let's discuss how I actually run this. Well, I run it by using this command right here. It's an executable Python command, run llama tests. Boom. Not very creative, I know. And here you can select the test, select the model. Boom

[08:29](#t=510) And there's one more thing, which is this number six here. It's number six for now, but it's probably going to change. Configure and run round robin. Well, this is the thing that's actually going to start up multiple services for you. You can do it manually, of course, but that's going to be, Not fun.

[08:44](#t=525) Uh, so here you can configure how many instances you want to start. Let's say I want to start up 16. Parallelism, that's Llama servers parameter. This is going to be the starting port of the first Llama server and that is going to plus one for each one of the servers you start up. So this is going to go up to 9015. And then finally, this is the key right here.

[09:03](#t=543) Nginx

[09:03](#t=544) This is the thing you should not be afraid of. I was for a long time, but this is really cool because it's a little server that sits in front of your Llama servers that you talk to. It's just pass-through basically, but it has the nice little capability of doing round robin, which means imagine you have Llama servers running on each one of these things. The first request comes in, it goes here. The second request comes in, send it here, and so on. And it's going to round robin these requests so that they're not all handled by one server. So let's set that up. I like to use 8000 because it's easy.

[09:35](#t=576) Now host, this is localhost if you're running locally, but you can set it to 0000 if you're going to be querying this remotely. And then you have start round robin servers and stop round robin servers. Let's try that.

[09:47](#t=588) Now here's Mac Studio and there's Activity Monitor and you'll see 16 happy little Llama servers running there waiting to handle requests. Now you might be familiar with Open Web UI. I actually made a tutorial, a whole tutorial setting this up with Ollama at the time, but Open Web UI can work with a bunch of different servers. So I pointed it at my Nginx endpoint, which is basically the IP address and port 8000 like we configured it. Let's do a new chat.

[10:14](#t=614) Hello Boom. And there it is. It's responding.

[10:16](#t=617) Now, I didn't exactly configure this to handle long stories, which is why a short prompt works, like say hello, because it doesn't have to think for a long time. But the thinking is actually part of inference. It's actually generating tokens while it's thinking, so that's using up tokens. And I set a maximum of tokens that need to be generated, which you can adjust if you need to. What's the capital of France? Say hi to me in Español, and they're doing this pretty much at the same time.

[10:41](#t=641) So go on. Go check this out. Play with Llama throughput lab and see what you think. Let me know. You can open issues, deploy requests, and so on. If you like this video, you're probably going to like the video I did about this framework cluster. That's going to be right over here. Thanks for watching and I'll see you next time.

[10:56](#t=656) [Music]
