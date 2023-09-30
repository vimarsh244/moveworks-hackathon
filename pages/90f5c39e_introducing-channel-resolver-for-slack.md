# https://www.moveworks.com/insights/introducing-channel-resolver-for-slack

Forrester names Moveworks a leader in Chatbot for IT operations. Read the report today.

Moveworks named a Forrester leader in Chatbot for IT operations. 

![Image | ](https://www.moveworks.com/hubfs/img/site/qr-demo.png)

Schedule a meeting with a Moveworks representative and learn how we can help reduce employee issue resolution from days to seconds.

By checking this box, I agree to receive company news and updates. Learn more in the Privacy Policy.

Thank you.

A member of the Moveworks team will be in touch within the next 24 hours.



  Close this modal
  



Sushanth Bhaskarabhatla, Product Manager



Jing Chen, Tech Lead and Manager


![ | ](https://www.moveworks.com/hubfs/img/blog/07_MW_Blog_Feature_ChannelResolver_Dark-2.jpg)

![ | ](https://www.moveworks.com/hubfs/img/blog/07_MW_Blog_Feature_ChannelResolver_Dark-2.jpg)

The premise of a Slack channel is simple: strength in numbers. Over the last few years, IT teams have embraced employee-facing chat channels as an alternative way to provide support, since there’s a good chance that someone in the group is experiencing the same issue, or has created a workaround, or even knows the solution. 

In reality, of course, these helpful messages will be mixed in with just as many unhelpful ones, meaning that service desk agents must read through each thread to determine the best course of action. It all amounts to lots of extra work for IT teams that are already overextended.

Now imagine the ideal team member in the IT support channel. They read every single message — day or night, weekend or holiday — and always respond when they can help. They go beyond giving advice; in many cases, they resolve the problem for you in seconds, without any effort from the IT team. Well, after extensive R&D and field testing, that ideal team member is ready for action. Introducing Moveworks’ Channel Resolver for Slack:

Figure 1: Channel Resolver messages the employee directly, then updates the channel.

![Channel_Resolver_Light-2 | Thread
#ask-it

Alex Today at 10:10 AM
5) e@ Do we have a license for Microsoft Word?

71 1
2 replies

hh Moveworks APP imago
WV y Hi @Alex - | think you are asking for software. I’ve DM’ed you for next steps.
€3 Click on «= @moveworks and then Message Moveworks to continue.

Nw Moveworks APP imago

WW @Alex|have granted access to Microsoft Word for you. Once you click on the
Office 365 chiclet in Okta, you should be able to get access to Microsoft Word.
I’m marking this thread as resolved. If you need to come back to this, here is
your ticket number: ITHELP-4460](https://www.moveworks.com/hs-fs/hubfs/Channel_Resolver_Light-2.jpg?noresize&width=650&name=Channel_Resolver_Light-2.jpg)

Moveworks understands the challenges employees face when trying to get a support issue resolved — and how delays in resolution hinder their productivity. Our vision has always been to make it easy to solve employee issues through the use of natural language understanding and conversational AI: resolution should come instantly, no matter where those issues are reported. Channel Resolver represents a major step toward realizing that vision of frictionless IT support.

Available to all Moveworks customers who use Slack, Channel Resolver is a version of our AI bot that resides in a public chat channel. It analyzes each employee question, and if our natural language understanding (NLU) and resolution platform predicts that it can remediate the issue, it jumps in. In fact, an initial group of a dozen customers — including AppDynamics — have already transformed their IT support with Channel Resolver. 

Unsurprisingly, the trend toward Slack channels extends across most enterprise workstreams, since they promote transparency and enable teams to benefit from the wisdom of the crowd. IT teams in particular have adopted this open communication approach, using a dedicated channel where employees can raise issues and get assistance. Such “Ask-IT” channels are becoming increasingly popular places for employees to raise common questions:

Figure 2: Using standard emojis, Channel Resolver indicates both that it’s analyzed an employee’s message (the eyes) and that the issue’s been resolved (the checkmark).

![05_MW_Blog_ContentImage01_DesktopChannelResolver | Acme Co.
@ Ale

aT co

Channels
cacclela

Eola) 4

# recruiting

Direct Messages

 

pet GOS A@w

| 583) 0

Today

Alex Today at 1

Hi, | need Lucidchart for some diagrams I'm
working on for a marketing deck. How can | get a
license for that? Thank you so much! Jj,

oo 1

 

PP 2replies Last 1:04 /

 

John 2¢
“4 What's the guest wifi password?

by 2replies Last reply today at 11:46 AN

Grace

Does anyone have an hdmi adaptor | can use? Took mine
home last night and forgot to bring it.

oo 1

 

2replies Last reply toda](https://www.moveworks.com/hs-fs/hubfs/img/blog/05_MW_Blog_ContentImage01_DesktopChannelResolver.jpg?noresize&width=600&name=05_MW_Blog_ContentImage01_DesktopChannelResolver.jpg)

From a broader perspective, IT channels complement the modern, chat-first business strategy, which integrates formerly separate workflows on the chat tool that employees use every day. There’s no longer any need to log in to specialized tools like portals, as we explained in our post, "Anytime, anywhere, automatic." But resolving employees’ issues over chat also presents challenges for IT teams. How do you stay on top of so many questions and requests? And how do you respond fast enough that employees feel they're being heard?

We recognized that natural language understanding and conversational AI could address these challenges, and we built the Channel Resolver capability to do just that.

As a machine learning company, we learn a lot from data, which we augment with customer feedback from onsite usability studies, interviews, and pilot programs to bridge the gap between theory and reality. A recurring theme in our research and customer discussions was that, with company-wide IT channels exploding in popularity, keeping pace with requests in those channels was becoming impractical for IT support teams.

Our task, then, was to build a mechanism through which we could do the following:

This would all have to be done with extremely high precision because, when you make a mistake in a public channel, everybody can see it. And at the same time, we would have to maintain high coverage — the percentage of requests handled by the bot — to ensure issues wouldn’t pile up in IT agents’ queues. Needless to say, building this capability is not trivial. Below, we explore the reasons why supporting channels is even harder than supporting requests that come in via direct message (DM).

Channels are significantly “noisier” than DMs or emails: they contain broadcast announcements from service desk agents, non-IT-related interactions between employees, reposted questions, jokes, memes, and everything in between. All of this makes understanding in-channel messages much more difficult than those sent in a direct, employee-to-bot conversation. 

To illustrate the point, consider this example of signal intermixed with noise — a broadcast announcement followed by an actual employee issue:

Figure 3: Separating the signal from the noise is intuitive for humans, but profoundly difficult for machines.

![Filtering Noise_Combo | #ask-it

faskcit COG Aw:

saa John 8:43AM —
© Sounds like it’s time to Update your Zoom 9

No, you are not on mute & . If you are having trouble
hearing your colleagues on Zoom calls, fear not, a fix is
on the way.

Please update to version 4.5.4 (5416.0929) for Mac a
and 4.5.4 (5422.0930) for Windows

Go to your Managed Software Center or your Task
Manager to install the new client today. Mi

-—— Noise

Alex im ago —
es) I’m going to be working remotely - how do | get set up
with VPN? -+—— Request

oo1](https://www.moveworks.com/hs-fs/hubfs/Filtering%20Noise_Combo.jpg?noresize&width=512&name=Filtering%20Noise_Combo.jpg)

The overarching challenge here is that the structure of messages, comments, and responses is unpredictable. Our NLU system needs to be able to parse these complex utterances and provide users with the right answers when needed, an objective that requires many machine learning models to achieve.

As we’ve seen, channels are not a good place for trigger-happy bots. Given the public nature of the channel setting, it’s critical for a bot to jump in only when it’s confident it can resolve an employee issue. The machine learning model thresholds for in-channel responses must therefore be tuned to trigger at higher confidence level than for DMs. 

So how does Moveworks actually decide which, if any, response is appropriate for each employee question? As we’ll examine at length in an upcoming blog series, our conversational AI platform was created explicitly to address the shortcomings of historical chatbots that relied on hard-coded decision trees. In the figure below, for example, a hard-coded model focused on keywords could easily misclassify the request for Microsoft Office as a problem with Okta:

Figure 4: A typical, noisy message in an IT support channel, filled with red herrings and irrelevant details that would confuse historical chatbots.

![Channel_Resolver_Light-1 | Thread
#ask-it

Alex 8:25AM

Hi team can | please get access to Microsoft

office prod suite please? When i try office365

from okta i guess message that its not assigned
Thank you so much!

@@)1 i i](https://www.moveworks.com/hs-fs/hubfs/Channel_Resolver_Light-1.jpg?noresize&width=550&name=Channel_Resolver_Light-1.jpg)

By contrast, Moveworks’ probabilistic engine weighs a number of variables — including syntax, semantics, previous IT tickets from the company, and even the employee’s department — to tackle the nuances of natural human language. Each of our resolution skills, such as our Software Access skill, then “bids” on the right to resolve an employee’s issue, with higher bids corresponding to higher levels of confidence in the model’s prediction. In this case, the Software Access skill generates the only bid that exceeds the confidence threshold, prompting the bot to autonomously provision Microsoft Office.

Figure 5: Moveworks’ probabilistic engine uses an auction system to determine the best action.

![05_MW_Blog_ContentImage_BiddingSystem | Monitor channel

 

8

Step in if it has
confidence it can help

   

Confidence ~~ -—% -----.----------
Threshold

>

Issue not solved
Allow agent to pick up issue

Issue solved
Mark as resolved](https://www.moveworks.com/hs-fs/hubfs/05_MW_Blog_ContentImage_BiddingSystem.png?noresize&width=600&name=05_MW_Blog_ContentImage_BiddingSystem.png)

When our bot can’t fully resolve an issue, it must seamlessly hand off to the right person on the service desk. We met this goal by developing a new system of interaction that allows Channel Resolver to provide the necessary information for agents to step in and pick up where the bot left off, facilitating faster response.

Figure 6: For employees awaiting IT support, Channel Resolver turns days into seconds.

![05_MW_Blog_ContentImage_ChannelResolver_Callouts-3 | Thread
< #ask-it

sush
Oct 25th at 10:51 AM

Hi there - | have a guest visiting. What's the guest
WiFi password?

 

 

0 Bot is confident and jumps in oo. M1-¢

 

Bot direct messages user
with next steps to resolve
the issue

 

2 replies L >
& moveworks APP. Oct 25th
Xs Hi @sush, I'm sending you a DM with
related article(s).

 

 

© Click on «& @moveworks and then
Message moveworksus2 to continue.

moveworks APP Oct 25th

@sush rated my answers as helpful.
Marking this as resolved.

 

Indicates the Bot resolved

© the issue and no agent

involvement is needed

 

 

Posts the answer to the

* What is the WiFi? —__@ channel for visibility if user

Guest network: moveworks-guest
Password: hello_moveworks!

Employee network: moveworks
Password: Ask an admin Qi

«& Try DM'ing @moveworksus? for other
Tissues!

 

marks the answer as helpful](https://www.moveworks.com/hs-fs/hubfs/05_MW_Blog_ContentImage_ChannelResolver_Callouts-3.png?noresize&width=600&name=05_MW_Blog_ContentImage_ChannelResolver_Callouts-3.png)

For the first time, employees can get instant resolution directly in the IT support channel — from software provisioning to account unlocks to installation instructions to the guest WiFi password. And for IT teams, Channel Resolver means that Ask-IT channels no longer require an army of agents to maintain. The verdict is clear: it’s time to supercharge your Slack workspace with AI.

Contact Moveworks to demo and deploy Channel Resolver on your IT support channel.

![Image | in](https://www.moveworks.com/hs-fs/hubfs/AIOps-featured-image.png?length=50&name=AIOps-featured-image.png)


          Discover how AIOps transforms IT operations from reactive to proactive. Understand the AIOps revolution and shift from firefighters to innovators.
        

![Image | ](https://www.moveworks.com/hs-fs/hubfs/Public-Sector-Convo-AI.png?length=50&name=Public-Sector-Convo-AI.png)


          Learn how AI & automation can immediately provide ROI and elevate service experience at scale for federal and state government and the public sector as a whole.
        

![Image | ](https://www.moveworks.com/hs-fs/hubfs/Forrester%20T%26I%20%281%29.png?length=50&name=Forrester%20T&I%20%281%29.png)


          3 key takeaways from the Forrester Technology & Innovation Summit: 1. Make generative AI your #1 priority. 2. Balance Risk 3. Deploy Copilots. Read the recap.
        

![Image | ](https://www.moveworks.com/hs-fs/hubfs/healthcare-test.png?length=50&name=healthcare-test.png)


          Conversational AI is improving healthcare delivery by automating tasks, surfacing knowledge, and supporting staff. Learn how leading providers use this technology.
        

![Image | ](https://www.moveworks.com/hs-fs/hubfs/Moveworks_LLM_Feature.png?length=50&name=Moveworks_LLM_Feature.png)


          From spelling correction to intent classification, get to know the large language models that power Moveworks' conversational AI platform.
        

![Image | 8](https://www.moveworks.com/hs-fs/hubfs/ITOA_feature.png?length=50&name=ITOA_feature.png)


          AI is transforming IT operations analytics (ITOA). Here are the key benefits and challenges of implementing AI-driven ITOA, including real-world examples.
        

