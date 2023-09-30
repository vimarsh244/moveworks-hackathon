# https://www.moveworks.com/insights/how-ai-solves-support-issues

By checking this box, I agree to receive company news and updates. Learn more in the Privacy Policy.

Thank you.

A member of the Moveworks team will be in touch within the next 24 hours.



  Close this modal
  



Jiang Chen, VP of Machine Learning


![ | Og O Dynamic Flow a OR Language Core Action Bid Enterprise Cache «oh Semantic Match](https://www.moveworks.com/hubfs/MIE_Feature.jpeg)

![ | Og O Dynamic Flow a OR Language Core Action Bid Enterprise Cache «oh Semantic Match](https://www.moveworks.com/hubfs/MIE_Feature.jpeg)

At Moveworks, we’ve spent five years engineering an incredibly simple support experience to make work feel less like, well, work. In practice, this means taking complex processes like IT support and HR service delivery — which usually involve lots of manual effort from busy professionals — and automating them end-to-end, from the initial request for help to the full resolution of the issue.

Creating this simple experience forced us to build machine learning components that are the first of their kind — at every step of the support process. So we did. The result of our effort is what we call the Moveworks Intelligence Engine™. 

 

![Vaibhav_02 | ](https://www.moveworks.com/hs-fs/hubfs/Moveweb/photos/Vaibhav_02.jpg)

 

The Moveworks Intelligence Engine™

Large companies invest in hundreds of different systems to help employees work faster and be more productive. They fill their knowledge bases with pages upon pages of documentation, they create portals with forms for every type of request, and they even implement chatbots with a rudimentary understanding of language. But with so many convoluted and disconnected systems to navigate, the truth is that employees can’t get the resources they need quickly and easily. 

Take chatbots, for example. You’ve probably interacted with one in the last week, maybe even within the last 24 hours. They’re ubiquitous — and yet they’re often profoundly frustrating to use. Most chatbots either can’t understand what you need, or can’t ask the right follow-up questions, or can’t solve your problem without redirecting you to a person, whom you would’ve preferred to speak with in the first place.    

So here’s the question: What would it take to create a chatbot that people actually prefer to use for support? To give employees whatever they need, right away, directly through the bot? Enter the Intelligence Engine. In this blog post, we’ll distill our learnings from the past five years to show how the Intelligence Engine tackles the five challenges of automating support at work:



![MIE_GIF2](https://www.moveworks.com/hs-fs/hubfs/MIE_GIF2.gif?&name=MIE_GIF2.gif)

Figure 1: The Moveworks Intelligence Engine has five components, which work together to resolve employee support issues end-to-end. 

 

Language Core™: Knowing what employees need

To help employees, you need to understand what they are asking for. 

Understanding would be easy if everyone sought help in the same way, but they don’t. Sometimes employees use a lot of words or leave out context or mention something they think is relevant, but actually isn’t. And as we’ve discussed at length, it’s this ambiguity that makes it difficult for machines to figure out language. 

So in approaching this challenge, you need a layer cake of dozens of deep learning models to correct spelling mistakes, to identify unique employees and software applications at each company, and to separate the signal from noise in the context of a single user. That’s why we built Language Core.



![MIEBlog_LanguageCore | John 9:12 PM e Hey IT. Jenny Marshall just moved to another team howdo | take her off the Ul roadmap dl asap. thanks. Spelling correction models “howdo” —> “how do” Named entity models | SPERSON (Jenny Marshall) $GROUP (UI roadmap) | i Statistical grammar models | Remove — Group (Jenny Marshall, Ul roadmap) | Intent extraction models [Remove — Group 95%] [Query — Knowledge 62%]... | Record linkage models | Remove — Group (jmarshall@globex.com, ??) | Disambiguation models | Remove — Group (jmarshall@globex.com, Ul_roadmap@)](https://www.moveworks.com/hs-fs/hubfs/MIEBlog_LanguageCore.png)

Figure 2: Language Core breaks down and restructures complex requests to understand what an employee is looking for. 

Let’s look at an example. Here in Figure 2, John has quite a complex question, especially from the perspective of a computer. Does he need something provisioned? If so, which software? Could a knowledge base article solve his problem? Is he asking how to update his direct deposit? Request PTO? Troubleshoot his VPN connection? 

To answer these questions, we first use two techniques: natural language processing (NLP) and natural language understanding (NLU). NLP organizes language into structured data — disambiguating entities, analyzing grammar, and correcting typos — while NLU interprets that data to figure out what it means in context. While the traditional way to build a chatbot fixates on specific use cases, we take any support issue, for any line of business, and map it into this structured framework that a computer can understand and act on. 

Now, once we’ve given the employee’s request the kind of structure that machine learning needs to understand, the next challenge to overcome is that every company has different employees, applications, office spaces, job titles, and security permissions. Here is where we use Collective Learning to see the unique ways that employees talk about these same issues. By combining information from many different companies and industries, our chatbot can recognize and interpret company-specific jargon that our models have never seen before.

Using all these techniques, Language Core is able to understand exactly what employees need — the first and most important step in making help at work automatic.

 

Dynamic Flow™: Holding natural conversations

Understanding what a person says is one thing; keeping up with conversation in real-time is another. 

Most chatbots are terrible conversationalists simply because the unpredictability of real-world back-and-forth cannot be scripted out in advance. Instead of this rigid, hard-coded approach, a chatbot needs an adaptable framework for deciding next steps.

Dynamic Flow works to handle even the most erratic conversations by determining responses in real time. Instead of following a pre-programmed path, it analyzes conversational context to seamlessly shift between topics and generate dialog on the fly.



![MIEBlog_DynamicFlow | John 7:22 AM Hey -- can | get Jenny Marshall access to powerpoint? Moveworks 7:22 AM Ok, I’ve contacted Jenny Marshall to grant access to Microsoft Powerpoint. John 7:23 AM Actually, she’s moving to a different team howdo | take her off the UI roadmap dl thanks Moveworks 7:23 AM ® Good news, Jenny is removed from UI Roadmap (UI-Roadmap@moveworks.us)! John 7:23 AM Thanks much!](https://www.moveworks.com/hs-fs/hubfs/MIEBlog_DynamicFlow.png)

Figure 3: While some conversations are straightforward, more often than not, employees have complicated issues that require a deep understanding of past interactions and current context to resolve. 

So let’s return to John for a moment. Ideally, he would only have this one question about managing a distribution list. But we all know that the real world is more complicated. Much like John, we all jump between questions, reference past conversations, and don’t stick to a single topic. Adding even more complexity, issues themselves are fluid. Something that was once a priority might be irrelevant now. The only way for a chatbot to keep up is to be flexible.

That being said, most chatbots are not flexible. They dictate the flow of the conversation with scripted interactions. There’s no opportunity for a user to escape pre-set flow or add context. 

With Dynamic Flow, the user starts and leads the conversation, exploring their topics of choice. This hands-off approach means that our bot engages naturally, adjusting to changing circumstances as they happen.

And because the user is in command of the dialog, when they inevitably change their mind mid-conversation, there isn’t a pre-programmed loop to get stuck in. Instead, Dynamic Flow’s topic switching mechanism enables the chatbot to jump out of the recommended course at any time, moving the conversation in a different direction — all while remembering and returning to previous comments and questions, as needed.

With this approach, it’s possible for a chatbot to manage even the most ambiguous request — asking clarifying questions to further understand at every step of the conversation, presenting multiple solutions to move forward, adding comments to a ticket, and pulling information from the knowledge base.

By circumventing the hard-coded chatbot experience, Dynamic Flow creates a flexible conversation led by the user, ultimately transforming a frustrating interaction into a productive one.

 

Action Bid™: Determining the ideal solution

Now that we've understood and clarified what the employee needs, we have to serve up the most relevant solution available at their unique company.

We all know that the best way to make a decision is to consider all possible options. But businesses are highly complicated and constantly changing: they adopt new software, hire new employees, and announce new policies on a regular basis. The ideal solution to a given support issue today might become out-of-date tomorrow.

So the key to finding that ideal solution is keeping track of every possible solution to employee questions. Here’s where Action Bid comes into play.

 



![MIE_AB | Remove from email group = Provide contact information File a ticket](https://www.moveworks.com/hs-fs/hubfs/MIE_AB.png)

Figure 4: Different solutions bid for the opportunity to solve an issue. When one or multiple options reach the confidence threshold, a response is sent to the user in seconds.

When John asks his question, there’s an infinity of ways to potentially address his request: remove someone from an email group, show contact information, surface a form, file a ticket, offer up a knowledge base article. And within these larger categories, there’re even more specific solutions — remove Jenny from the marketing distribution list, show contact information on Marshall on the Accounting Team, surface a request form, file an IT ticket on JIRA, offer up a single line from the Employee Handbook. 

For every option, Action Bid weighs signals and context from across the company, considering every bit of information at its disposal — security permissions, job descriptions, business logic, location, past conversations — to calculate the relevance of each possible response to the employee’s question. Even as support teams add new content and the company ecosystem changes, Action Bid constantly improves to make sure that every decision is the best decision.

 

Enterprise Cache™: Transforming resources into bite-sized solutions

For each service department — IT, HR, Finance, Legal, Facilities — tons of valuable information lives deep inside different resources and systems. And when an employee has a problem, they don’t know that they should be going to Confluence to troubleshoot their VPN issues, to Sharepoint for information on how to submit an expense report, or to the Okta portal to request access to a certain application.

On top of this first challenge, when a subject-matter expert writes an article, they are trying to document everything. This kind of detail can be difficult for employees to find, read, and understand. Knowledge articles can be thirty pages detailing retirement benefits, featuring information from a dozen different countries. 

The key is wading through all this detail to get only the correct information in the right hands. And we’ve done this with Enterprise Cache — a system that transforms deeply buried resources into simple solutions designed to be rendered over chat.

 



![MIEBlog_EnterpriseCache | v John 9:12 PM Hey IT. Jenny Marshall just moved to another team howdo | take her off the UI roadmap dl asap. thanks. Moveworks 8:35 AM Ok, you'd like to remove Jenny Marshall from a group: UlRoadmap@globex.com The above user(s) will be removed as members and will no longer receive emails sent to this distributution list. Already uodate Name Emad Jenny Marshal jennymarshatemove ' works.ca Group name Group emaa international salescanada@movew Offerings Ul orks.ca Ok, you'd like to remove Jenny Marshall from a group: UlRoadmap@globex.com [men eeeeperer: © Room phone number: Room amenities: “a Es PISS es: sma | ‘nt ooned It los $3592, °25 accessor islet y home. 4 sss22.7" 1." AL thes CMe, om mY Wo. WHR rem employees as of 08/31/2020 wil be Provided an IT Welcome Kit to help with productivity while you are working from home. These kits will be shipped to your provided shipping address during your Oonboarding process.](https://www.moveworks.com/hs-fs/hubfs/MIEBlog_EnterpriseCache.png)

Figure 5: Moveworks personalizes the support experience by giving employees exactly the resource they need, whether that is a single sentence from a knowledge article or a conversationalized form.

As mentioned, when John asks his question there are a thousand possible solutions on the backend. Action Bid works to find out what type of solution is most meaningful for him. Maybe he needs an article on troubleshooting Outlook, contact information, access to marketing email software, a map to a certain conference room. 

Enterprise Cache works in tandem with Action Bid by making all this information useful to the end-user. It indexes all of the available resources, so every question can be answered with a single, precise snippet of information. Even when there are updates to various knowledge systems, Enterprise Cache automatically incorporates new information.

And if the answer doesn’t live in your knowledge base? Enterprise Cache also ingests knowledge from trusted, public websites to make your answer store the best it can be.

 

Semantic Match™: Personalized answers to every question

Employees expect personalized support. The same question doesn't always have the same answer, which is why support teams spend hours crafting personalized responses. Automating this process is a very difficult challenge, but it makes the difference between a typical automated system and a truly helpful solution

Semantic Match provides precise answers to employees’ questions — directly over chat. It leverages relevance and personalization models to find the most helpful information across disparate knowledge bases.



![MIE_Blog_SemanticMatch | hh Moveworks 8:32 AM VV You’ve been|removed from the UI Roadmap | ——————_ Remove from group distribution list Jenny 8:35 AM Jenny 8:35 AM | BTW, my new team|is in{Vancouver].. could | Knowledge request Personalize to location have some information on the 401K Plan? heh WV Moveworks 8:35 AM Ok, just checked our knowledge base, here is — the closest answer | could find: * Moveworks Employee Benefits Enrollment (Canada) All employees based in Canada are eligible to be enrolled in a Registered Retirement Savings Plan (RRSP).](https://www.moveworks.com/hs-fs/hubfs/MIE_Blog_SemanticMatch.png)

Figure 6: Keeping track of an employee’s location, department, and other context, Semantic Match surfaces the most relevant answer to each employee.

For example, if an employee — such as Jenny in Figure 5 above — asks for an update on retirement benefits — the bot can offer information based on her specific circumstances, like her location.

The power of Semantic Match is in how it intelligently surfaces information by considering context. Using all the capabilities of the other components of the Intelligence Engine, this system takes every disparate piece of data into account, from the proximity of certain words and phrases to the resources available to the location of the person asking. 

With a 360-degree view of your organization, our proximity, relevance, and location models retrieve the most accurate answer. So even when an employee is vague, for example not mentioning where they are or which distribution list their referencing, Moveworks is able to connect them with the right solution. So employees get a quick and straightforward answer in seconds that's personalized to their specific circumstances.

 

Greater than the sum of its parts

Each component of the Moveworks Intelligence Engine — Language Core, Dynamic Flow, Action Bid, Enterprise Cache, and Semantic Match — takes a fundamentally novel approach to the problem it solves. Each pushes the limits of what’s possible with machine learning today.

But above all, it’s the tight integrations between these components that allow Moveworks to automate support at work. Semantic Match analyzes knowledge articles using Language Core to deliver personalized answers. Action Bid weighs the utility of all the resources in Enterprise Cache to determine the best solution. We’ve built one engine — with far more horsepower than its five parts alone.

And here’s the biggest takeaway: if your solution fails to address just one of these challenges, employees won’t use it. A chatbot that understands language is still useless if it directs employees to an outdated article. A comprehensive IT portal lies dormant when people can’t find what they’re looking for. 

We built our Intelligence Engine the hard way, putting thousands of hours of R&D into everything inside. Because otherwise, when your employees need support, they’d ask you instead.

Request a demo to see the Moveworks Intelligence Engine™ in action.

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
        

