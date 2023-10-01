# https://www.moveworks.com/insights/how-machines-understand-language

By checking this box, I agree to receive company news and updates. Learn more in the Privacy Policy.







  Close this modal
  



Jing Chen, Tech Lead


![ | ](https://www.moveworks.com/hubfs/19_MW_Blog_Conversational_AI_Part1_final.png)

![ | ](https://www.moveworks.com/hubfs/19_MW_Blog_Conversational_AI_Part1_final.png)

 

For most of our history together, people and machines have faced a sizable language barrier.

We’ve reconciled ourselves to a status quo of clicking buttons, scrolling through submenus, and navigating to new windows. However, this method of interacting with computers — a Graphical User Interface, or GUI — is neither efficient nor natural.

When GUIs were introduced in the 1980s, they ushered in a new era when anyone, including people without programming skills, could suddenly use a computer. We should be careful not to take GUIs for granted: previously, operating a PC required memorizing complex commands to accomplish even the most simple tasks. But at a time when unfamiliar devices and SaaS applications enter our lives every week, the graphical user interface is no longer a sustainable approach, since it entails a significant learning curve to become proficient with these new tools.

Figure 1: While commonplace, the graphical user interface requires time and trainingto complete complex tasks.

![GUI | Menu « Select style Lines Backgrounds Links « Embedded External images pa Hypertinks Filename-(saved) ®H\|\° 60 8) © tt eo CUGEVELTS](https://www.moveworks.com/hs-fs/hubfs/GUI.png)

In short, GUIs risk being unintuitive. No matter how much engineering and design work goes into creating a “natural” interface, it’s impossible to create buttons that capture every conceivable user intention. Fundamentally, our natural form of communication isn’t buttons, but language. And as our technology becomes increasingly complex, the ability to operate that technology with simple, conversational language will pave the way for users to derive even more benefit from their applications, in much the same way that GUIs did for a previous generation.

In this post, we’ll dive deep into the modern history of human-computer interaction, from the rocky beginnings of early chatbots, to today’s AI-powered conversation engines.

Figure 2: Probabilistic chatbots are the next step in the evolution of human-machine communication.

![Continuum human-computer interaction | Continuum of Human-Computer Interaction Command-line interface Graphical user interface (GUI) Deterministic chatbot Probabilistic chatbot Requires users to communicate Still involves a significant learning Attempts to engage users in Allows users to interact with on the computer's terms with curve for users to navigate menus. conversation — but results in computers on their terms, in complex commands and buttons robotic interactions natural conversation — Less natural More natural](https://www.moveworks.com/hs-fs/hubfs/Continuum.png)

Despite their shortcomings, it's no surprise that chatbots are growing in popularity. Yet the experience of using most chatbots is even less intuitive than the average GUI. The fundamental problem is conversation itself, which is ambiguous, contextual, and dynamic. Conventional chatbots take a deterministic approach: that is, they rely on pre-scripted conversations that can’t keep pace with the vastness and versatility of language.

Let’s explore why these early bots failed to understand their users:

Figure 3: Deterministic chatbots with pre-scripted responses aren’t able to keep up with unexpected user responses.

![Deterministic chatbots | Before we get started, where are you located? Let us know by selecting an option below. I’m still not sure | understand. Perhaps the answer is in our FAQs? If not, feel free to click ‘contact Us’ below to get in touch vwith one of our Tepresentatives. FAQs Contact Us](https://www.moveworks.com/hs-fs/hubfs/blog-figure-03b-mobile@2x.png)

The challenge with this real-world e-commerce bot is that people prefer to interact with language, rather than with buttons. So when users predictably type “US” into the dialog box instead of clicking the American flag icon, the bot is incapable of understanding the typed reply.

This kind of hardcoded chatbot simply breaks down when confronted with an unexpected response. Building any chatbot requires an incredibly high amount of technical effort, but all this work is thrown out the window when a user makes one unexpected choice. Here, the bot cannot understand or properly respond, so it instead directs the user to read an FAQ document or visit a contact page. It might not be perfect, but a predictable GUI is better than wasting time on a bot that can’t communicate.

Figure 4: Chatbots with only basic keyword matching fail to anticipate user intent and are forced to fall back on a static response, in this case, a suggestion to email customer service.

![Chatbots basic keyword matching | oo e Here’s what | found! - -- -|QSutton Leather Sandal Luxe Leather Construction And A Stiletto Heel Combine To Refined Effect On Our H... See All Colors What sizes do these shoes come in \ We're sorry to hear about your | |- - L\ problem with your shoes. To best assist you, please email CustomerService@shoesmak](https://www.moveworks.com/hs-fs/hubfs/blog-figure-04-mobile_x2.png)

 

Next, let’s take a look at a slightly smarter bot. These One-Hit Wonder Bots are designed to fulfill one specific use case by applying basic keyword matching. In this scenario, everything works as expected, until a follow-up question comes into play. That's when the conversation fractures.

This bot is not equipped to deal with shifts in topic — a critical shortcoming, since conversation is defined by changing topics. In this example, a customer at a brick-and-mortar store would expect the salesperson to immediately answer her simple question about shoe sizes. But, unable to answer, this bot has lost a potential sale, and the customer leaves empty-handed.

The problem is clear: anticipating all possible directions a conversation can go is impossible. Deterministic models are incapable of conducting an organic conversation, because they have been pre-programmed with strict scenarios and can’t adapt in all the ways that language can.

Figure 5: A deterministic bot based on “if-this, then-that” rules is easily confused when a user jumps in and out of the manually scripted flow.

![deterministic bot | '@ —_ 1 match 1 Failed to match intent 1 1 1 1 ' No topic switching 1 i Greedy slot filling 1 Looking for flights from| Price, |- UT to Boston, MA. When do you want to fly out? ooking for flights from Changé, layenne, France to San Francisco, CA. When do you want to fly out?](https://www.moveworks.com/hs-fs/hubfs/blog-figure-05b-mobile@2x.png)

In a final example, we’ll turn to the travel industry, featuring a bot that is supposed to help find and book flights. Any frequent traveler would be excited about this bot — if it worked. It applies a naive keyword and pattern matching approach and, unfortunately, is overeager to extract a city name out of user utterance: it matches a price inquiry to the city name “Price, UT.”

Compounding this first error, it's painful for a user to point the bot in the right direction when it goes down the wrong path. See above how the bot misinterprets the user’s intention to course-correct back to the original question of the best price. Instead, the bot misconstrues this request as asking a new question about flights to Change, France. While what the user is trying to say would be obvious to any person reading this conversation, the bot continued to misunderstand, making this whole exchange an exercise in futility.

Clearly, building a conversational platform that works intuitively is a challenge. Pre-scripted answers and decision tree models open Pandora’s box — creating more frustration than function. Given a particular input, deterministic models will always produce the same output. Much in the world, particularly language, is too complex to be reduced to unbending rules.

The reality is that language is unbound and conversation is rarely, if ever, unidirectional. None of these example chatbots are equipped to keep up, because all these bots have an approach in common: they use “if-this, then-that” logic to determine next steps. Practically speaking, the workflow engineer who attempts to build a solution using this deterministic approach will struggle. Somehow, they must anticipate all possible directions that a conversation could go. Even in a very defined environment — for example, a bot that exclusively helps sell shoes — there is no way to predict what a user will do next.

The unpredictability of human conversation means that deterministic chatbots are destined for disappointment. In contrast, a probabilistic approach opens the door for a bot to have naturally high-level and complex conversations with real users.

If you learn one thing from this post, it’s that understanding users is difficult. A deterministic approach can’t keep up with how people engage with one another. In conversations, we naturally take uncertainty into account, but for most of their history, computers haven’t been able to overcome this ambiguity. On the other hand, when powered by a probabilistic approach, chatbots can adapt to changeability.

Figure 6: The two core components of a conversational AI system are natural language understanding and conversation flow management.

![conversational AI system | Intent Enti Recognition \ Recognition Conversation Dialog Flow Generation Natural Language Understanding (NLU) What does the user want? Conversation Flow Management (CFM) What is the next step?](https://www.moveworks.com/hs-fs/hubfs/blog-figure-06-box%20chart@2x.png)

So what does it mean to have a real conversational bot? At its core, there are two components that work in tandem: natural language understanding (NLU) and conversational flow management (CFM). NLU works on understanding what the user wants, while CFM determines next steps. Conventional chatbots struggle with both of these pieces. In fact, most are limited to very basic NLU, while almost none make any attempt at intelligent conversation flow.

It might not be that difficult to hardcode a few user utterances and build some fixed dialogue flows as a response. But, without incorporating a probabilistic approach to both your natural language understanding and conversation flow management, a chatbot is unable to naturally navigate a real conversation that involves taking next steps, addressing follow-up questions, and managing changes in conversational direction.

At Moveworks, we’ve built our company on the idea that communication between people and machines should be seamless. We’ve spent years solving this problem in the domain of IT support, and what we've learned applies across the board. In Part 2 of this series, we’ll dive deep into our attempts to converse with employees in their language, on their terms.

Contact  Moveworks to learn how AI can supercharge your workforce productivity.

![Image | ](https://www.moveworks.com/hs-fs/hubfs/AIOps-featured-image.png)


          Discover how AIOps transforms IT operations from reactive to proactive. Understand the AIOps revolution and shift from firefighters to innovators.
        

![Image | ](https://www.moveworks.com/hs-fs/hubfs/Public-Sector-Convo-AI.png)


          Learn how AI & automation can immediately provide ROI and elevate service experience at scale for federal and state government and the public sector as a whole.
        

![Image | Ay TECHNOLOGY &](https://www.moveworks.com/hs-fs/hubfs/Forrester%20T%26I%20%281%29.png)


          3 key takeaways from the Forrester Technology & Innovation Summit: 1. Make generative AI your #1 priority. 2. Balance Risk 3. Deploy Copilots. Read the recap.
        

![Image | ](https://www.moveworks.com/hs-fs/hubfs/healthcare-test.png)


          Conversational AI is improving healthcare delivery by automating tasks, surfacing knowledge, and supporting staff. Learn how leading providers use this technology.
        

![Image | a . oe ° ° * ° ° ° ra](https://www.moveworks.com/hs-fs/hubfs/Moveworks_LLM_Feature.png)


          From spelling correction to intent classification, get to know the large language models that power Moveworks' conversational AI platform.
        

![Image | ](https://www.moveworks.com/hs-fs/hubfs/ITOA_feature.png)


          AI is transforming IT operations analytics (ITOA). Here are the key benefits and challenges of implementing AI-driven ITOA, including real-world examples.
        

