# https://www.moveworks.com/insights/collective-learning-for-it-issues

By checking this box, I agree to receive company news and updates. Learn more in the Privacy Policy.

Thank you.

A member of the Moveworks team will be in touch within the next 24 hours.



  Close this modal
  



Chang Liu, Tech Lead


![collective learning | ](https://www.moveworks.com/hubfs/22_MW_Blog_CollectiveLearning_Feature_v03.jpg)

![collective learning | ](https://www.moveworks.com/hubfs/22_MW_Blog_CollectiveLearning_Feature_v03.jpg)

Large service desks are flooded with hundreds of IT support issues a day. And because no two issues have exactly the same wording, service desks must manually resolve each one — from resetting passwords to provisioning software to answering questions about policy.

New employees, for instance, inevitably encounter a number of IT issues during onboarding, such as: “Hi! I joined the marketing team two days ago and I just realized I don’t have a Zoom Pro license. I’m sure you get a ton of these requests, but I’d really appreciate help as soon as possible. Thanks!” At most companies, this kind of issue requires the attention of service desk agents, who read through a long and complex description to find what is often a simple fix.

In fact, under the surface, one-of-a-kind support requests describe surprisingly similar problems. The rise of SaaS applications in particular — Zoom, Salesforce, Office 365 — is driving homogeneity across companies and industries, which means that just a handful of automated workflows can resolve thousands of issues on the back end. Ultimately, the challenge for us at Moveworks is to understand the unique ways that employees talk about these same issues.

Figure 1: While every company is unquestionably unique, many use the same IT to conduct business.

![blog-illos-1D | loT Company , es peenn SA ad ae 4% re Manufacturer ae “— ° Tae : “Zoom “Nt / Outlook ‘ meee Salesforce \ woos. MS Office \ a _ Adobe Acrobat \ a“ s ‘ ‘ Dropbox / Zendesk ie DocuSign “° Law Firm Slack “ Health Care Provider :](https://www.moveworks.com/hs-fs/hubfs/blog-illos-1D.png)

One of the critical techniques we use to understand these support tickets is Collective Learning. At Moveworks, we benefit from analyzing over 75 million IT issues, and by analyzing what they have in common, our machine learning models can understand the language employees use to explain their IT problems. In this blog, we'll cover:

The idea behind Collective Learning is simple: strength in numbers. What we realized was that — as a third party — Moveworks could aggregate data from dozens of different companies to gain universal insights about seemingly unique IT issues.

Behind the scenes, Collective Learning requires pooling anonymized data from as many sources as possible. Anonymization has two major benefits: first, protecting internal data; and second, allowing our models to identify linguistic patterns under the surface.

After we anonymize data, the next step is normalization, which throws these patterns into sharp relief. Simply put, normalization means transforming language into a generic form in order to highlight common characteristics. Consider Figure 2. “Mark” and “sales email list” are specific nouns, but, these entities can be considered in broader, more universal categories, like $PERSON or $GROUP. By generalizing these entities, a model receives a large input of training data relevant to the IT world and applicable across many companies and industries.

Figure 2: By normalizing data, specific entities become generic entities, which can be used to train machine learning systems. 

![normalizing data-2 | Kelly 3:09 PM Can you add Mark to the sales email list? can | $PERSON $GROUP](https://www.moveworks.com/hs-fs/hubfs/normalizing%20data-2.png)

So what does Collective Learning look like in a live environment?

Let’s explore Figure 3: three different questions from three different organizations in three different industries. Attempting to train a machine learning system on these specific issues at each company will result in poor performance because there are simply not enough examples.

However, Collective Learning gives us an opportunity to use machine learning to solve all of these issues. Through normalization, we can apply the same name — video conferencing application — to entities like Zoom, Webex, and Google Hangouts:

Figure 3: Collective Learning takes advantage of common IT entities, like video conferencing application, to automatically resolve issues.

![Collective Learning | Alex at ABC Bank = 5:09» Our quarterly earnings call is in 10mins, but my WebEx audio connection is funky Aaron at Health Services Need everyone on board with the new treatment schedule. How to setup an all- hands on Google Hangouts? Amanda at E-commerce 3.» | need to show a spreadsheet on Zoom. How do | share my screen? $VCA $VCA $VCA](https://www.moveworks.com/hs-fs/hubfs/Collective%20Learning.png)

And Collective Learning can go even further, normalizing entire sentences to learn the underlying logic of language. Here in Figure 4, at first glance, these look like completely different IT issues that would require the service desk to address manually. But, considering “Zoom” and “Confluence” and “Trello” all as $SOFTWARE makes it easier for the model to pinpoint patterns in how people ask for support.

Figure 4: Collective Learning applies this logic of normalizing entities to entire sentences, illuminating patterns across companies and industries.   

![Collective Learning in action | Varun =. 3:09 PM | need a license for Zoom. | Jose 3741p Can | get Confluence access? | Sarah 3.27pm Please give John a Trello account | eeeeehowao a] Rew ewew een al sea enaeaanan! preter eee eee $SOFTWARE peeeesieeueen,s](https://www.moveworks.com/hs-fs/hubfs/Collective%20Learning%20in%20action.png)

Despite starting with only a couple of examples, generalizing language patterns allows us to generate many alternate combinations. That way, our machine learning models already recognize the structure of future issues — even if they look different from the original examples.

Figure 5: Learning language patterns lets us generate similar utterances from a few examples.

![language patterns-2 | SPERSON need a license for SOFTWARE SPERSON need a SOFTWARE license SPERSON need SSOFTWARE access SPERSON need access to $SOFTWARE SPERSON need a $SOFTWARE account SPERSON need an account for $SOFTWARE Can $PERSON get license for $SOFTWARE Can $PERSON get a SSOFTWARE license Can $PERSON get $SOFTWARE access Can $PERSON get access to $SOFTWARE Can $PERSON get a SSOFTWARE account Can $PERSON get an account for $SOFTWARE Please give $PERSON a liconse for $SOFTWARE Please give SPERSON a $SOFTWARE license](https://www.moveworks.com/hs-fs/hubfs/language%20patterns-2.png)

In the past, machine learning has been the exclusive domain of large enterprises, which have access to larger data sets. The power of Collective Learning lies in allowing smaller companies to reap the benefits of machine learning — by transforming a couple of examples into millions of data points.

In fact, when Moveworks onboards a new organization to our platform, Collective Learning allows us to recognize an ever-increasing percentage of relevant entities, on day one. Now, this network effect means our bot can make sense of 99.9% of IT entities, without additional training.

Figure 6: As our customer base grows and we continue to collect IT ticket data, Moveworks’ ability to recognize entities increases exponentially. 

![impact of collective learning | Percent entities recognized at latest customer 100% 90% 80% 70% 60% 50% 40% The Impact of Collective Learning Percentage of entities Moveworks recognizes when onboarding latest customer 10 20 30 40 50 60 Number of other companies already using Moveworks 70](https://www.moveworks.com/hs-fs/hubfs/impact%20of%20collective%20learning.png)

Thanks to Collective Learning, Moveworks immediately understands our customers’ IT environments, regardless of their size or industry. Every company has its own support challenges, of course, but understanding the language of IT issues shouldn’t be one of them. The trick is capturing the right information, giving machine learning models the data needed to make accurate predictions about what employees need. For Moveworks, that trick is Collective Learning.

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
        

