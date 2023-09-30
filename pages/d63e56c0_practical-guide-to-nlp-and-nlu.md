# https://www.moveworks.com/insights/practical-guide-to-nlp-and-nlu

Forrester names Moveworks a leader in Chatbot for IT operations. Read the report today.

Moveworks named a Forrester leader in Chatbot for IT operations. 

![Image | ](https://www.moveworks.com/hubfs/img/site/qr-demo.png)

Schedule a meeting with a Moveworks representative and learn how we can help reduce employee issue resolution from days to seconds.

By checking this box, I agree to receive company news and updates. Learn more in the Privacy Policy.

Thank you.

A member of the Moveworks team will be in touch within the next 24 hours.



  Close this modal
  



Jiang Chen, VP of Machine Learning



Tomasz Jurczyk, Machine Learning Engineer


![ | ](https://www.moveworks.com/hubfs/img/blog/20191222-practical-guide-to-nlp-and-nlu/practical-guide-to-nlp-and-nlu.jpg)

![ | ](https://www.moveworks.com/hubfs/img/blog/20191222-practical-guide-to-nlp-and-nlu/practical-guide-to-nlp-and-nlu.jpg)

Many people assume computers will never understand human language. But as a company that builds artificial intelligence to do just that, it's our job to overcome this assumption. There's no doubt that AI systems are capable of solving remarkably complicated problems. Why should language — perhaps the most impactful problem of all — be any different?

So here's the challenge: making inherently ambiguous language more like the highly structured world of chess. And to develop that structure, two techniques have proven equally critical: natural language processing (NLP) and natural language understanding (NLU). NLP organizes language into the structured data that computers require to process, while NLU interprets that data to derive meaning.

To appreciate the strides computers have already made toward understanding language, let’s talk about one of the first major challenges put before them: chess. Chess is no less complex than language, and yet computers were capable of defeating even chess grandmasters decades ago. By considering a huge amount of situational data, chess-playing programs not only figure out their next move; they also anticipate the next three moves, five moves, and even ten moves down the line.

 

In this blog, we’ll cover:

To learn why computers have struggled to understand language, it’s helpful to first figure out why they're so competent at playing chess. Chess, needless to say, isn’t easy. There are more possible moves in a game than there are atoms in the universe.

But while playing chess isn’t inherently easier than processing language, chess does have extremely well-defined rules. There are certain moves each piece can make and only a certain amount of space on the board for them to move. Computers thrive at finding patterns when provided with this kind of rigid structure. Yet language is not so formulaic. It breaks rules all the time.

In the lingo of chess, NLP is processing both the rules of the game and the current state of the board. How can you move your bishop? Where is your opponent's queen? An effective NLP system takes in language and maps it — applying a rigid, uniform system to reduce its complexity to something a computer can interpret. Matching word patterns, understanding synonyms, tracking grammar — these techniques all help reduce linguistic complexity to something a computer can process.

Figure 1: At its most basic level, NLP involves treating each utterance as a unique string of words, with minimal interpretation. In this example — a chatbot only knows the preprogrammed phrase “I need Zoom,” and it is unable to respond to slightly altered phrasing.

![basic-NLP-fails | User request

Paul 3:43 °™
Ineed Zoom.

Paul 3:43 °™
Ireally need Zoom.

 

 

 

 

 

 

 

 

Action

AcmeBot APP 3:43PM
Ok, you need Zoom.

Do you want me to get Zoom for you?

Zoom is the leader in modern enterprise video communications,
with an easy, reliable cloud platform for video and audio
conferencing, chat, and webinars.

 

Yes

 

 

Cancel

 

 

 

AcmeBot APP 3:43PM
Sorry, | don't understand your request. Please try
again.](https://www.moveworks.com/hs-fs/hubfs/img/blog/20191222-practical-guide-to-nlp-and-nlu/basic-NLP-fails.png?&name=basic-NLP-fails.png)

The easiest way to structure unstructured language is to treat each unique utterance as its own data point. The equivalent in chess would be making moves completely dependent on the opponent’s last move: advancing a pawn simply because the other person moved their rook. Obviously, this is a losing strategy — both in chess and in language learning. 

While creating a chatbot like the example in Figure 1 might be a fun experiment, its inability to handle even minor typos or vocabulary choices is likely to frustrate users who urgently need access to Zoom. While human beings effortlessly handle verbose sentences, mispronunciations, swapped words, contractions, colloquialisms, and other quirks, machines are typically less adept at handling unpredictable inputs.

Figure 2: The goal of NLP is to provide structure to unstructured, ambiguous language.

![NLP-structures-ambiguous-language | oe 9. ad

User requests

Anna
Ineed Zoom

Drew
I really need Zoom!

Lewis
need Zoom

Christine
Ineed Zoom please

Georgia
Seems like Ineed Zoom

Chris

NLP: Structure
user request

Ineed Zoom =———>

 

 

 

 

Action

AcmeBot APP
Ok, you need Zoom.

Do you want me to get Zoom for you?

Zoom is the leader in modein enterprise video communications,
with an easy, reliable cloud platform for video and audio
conferencing, chat, and webinars.

 

Yes

 

 

Cancel](https://www.moveworks.com/hs-fs/hubfs/img/blog/20191222-practical-guide-to-nlp-and-nlu/NLP-structures-ambiguous-language.png?&name=NLP-structures-ambiguous-language.png)

In Figure 2, we see a more sophisticated manifestation of NLP, which gives language the structure needed to process different phrasings of what is functionally the same request. With a greater level of intelligence, NLP helps computers pick apart individual components of language and use them as variables to extract only relevant features from user utterances.

With NLP, we reduce the infinity of language to something that has a clearly defined structure and set rules. To put it simply, we make language more like chess. Crucially, however, the job isn’t done yet. 

Assembling the information extracted by NLP, NLU focuses primarily on comprehension: understanding utterances in the context of the broader conversation to choose the right response.

A number of advanced NLU techniques use the structured information provided by NLP to understand a given user's intent. These techniques include paraphrase detection, which determines whether a pair of utterances has the same meaning, and topic switching, which enables AI to follow a non-linear conversation that naturally jumps around different subjects.

Figure 3: NLU goes beyond processing language at face value: it illuminates a user’s underlying intent.

![NLU-understands-intent | User requests

NLP:
Structure user
request

NLU:
Determine user
intent

Action

Alex 11:03AM

I've been working remotely, and
manager mentioned I need

 

 

 

Gwen 11:05AM
Just hired - | already have
access to Slack, Zoom and
other basics, but is there more

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

Zoom.
information on our company
remote work policy?
1
i
i 1
i 1
1 \
1 1
i \
t \
1 1
1 \
: . t
1 | was just hired
t T
| need Zoom \
L
T
1 | need the company
! .
! remote work policy
7
| work remotely \
i \
Hf \ | have Slack
1 H
i 1
i 1
i \
1 1
i \
i 1
i \
1 1
1 \
t 1
i \
1
v
Get Zoom Get remote
access work policy

Moveworks

03 AM

V Ok, youneed Zoom.

Do you want me to get Zoom for you?

Zoom is the leader in modern enterprise video
‘communications, with an easy, reliable cloud
platform for video and audio conferencing, chat,

‘and webinars.

 

Yes

 

 

Not relevant

 

 

 

Cancel

 

 

Moveworks M
vV Ok, just checked our knowledge base, here is
the closest answer | could find:

Working from Home
When working from home:

+ Keep your regular office hours and break
schedule to ensure availability to team member:
and customers. Keep your manager appraised
of your whereabouts as you normally would.

+ Ensure that your internet service is working as
expected. Contact your cable provider if you
have any issues.

Click here to read the full article](https://www.moveworks.com/hs-fs/hubfs/img/blog/20191222-practical-guide-to-nlp-and-nlu/NLU-understands-intent.png?&name=NLU-understands-intent.png)

NLU is an integral part of NLP. If NLP is about understanding the state of the game, NLU is about strategically applying that information to win the game. Thinking dozens of moves ahead is only possible after determining the ground rules and the context. Working together, these two techniques are what makes a conversational AI system a reality. Consider the requests in Figure 3 — NLP’s previous work breaking down utterances into parts, separating the noise, and correcting the typos enable NLU to exactly determine what the users need.

While NLP and NLU are not interchangeable terms, they both work toward the end goal of understanding language. There might always be a debate on what exactly constitutes NLP versus NLU, with specialists arguing about where they overlap or diverge from one another. But, in the end, NLP and NLU are needed to break down complexity and extract valuable information.

Figure 4: Both NLP and NLU play an important role in understanding a user’s request, but the line where one approach ends and the other begins is blurry.

![NLP-with-NLU](https://www.moveworks.com/hs-fs/hubfs/img/blog/20191222-practical-guide-to-nlp-and-nlu/NLP-with-NLU.gif?&name=NLP-with-NLU.gif)

To win at chess, you need to know the rules, track the changing state of play, and develop a detailed strategy. Understanding language involves the same three elements. And like playing chess, the key is constant improvement. Chess and language present more or less infinite possibilities, and neither have been "solved" for good. Yet the more we know, the better decisions we make. 

By working diligently to understand the structure and strategy of language, we’ve gained valuable insight into the nature of our communication. Building a computer that perfectly understands us is a massive challenge, but it’s far from impossible — it’s already happening with NLP and NLU.

Contact  Moveworks to learn how AI can supercharge your workforce productivity.

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
        

