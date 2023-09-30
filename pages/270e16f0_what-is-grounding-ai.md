# https://www.moveworks.com/insights/what-is-grounding-ai

By checking this box, I agree to receive company news and updates. Learn more in the Privacy Policy.







  Close this modal
  



Ritwik Raj, Technical Program Manager


![ | ](https://www.moveworks.com/hubfs/grounding-ai-blog-featured-image.png)

![ | ](https://www.moveworks.com/hubfs/grounding-ai-blog-featured-image.png)

Using a solution like OpenAI’s ChatGPT can be incredibly appealing, but there’s a catch: occasionally, these AI solutions generate responses containing misleading or incorrect information. In critical tasks, can you confidently rely on these systems? 

Grounding, a key concept in the rapidly evolving field of AI, offers a potential solution. It helps develop AI systems that are better prepared to interact with the real world, with the goal of minimizing the risk of inaccurate results. 

In this article, we’ll explore the fundamentals of grounding AI, highlighting its crucial role in advancing AI decision-making. By the end, you will have a comprehensive understanding of grounding, including its incredible potential in shaping the future of AI systems that can engage with the complexities of the real world.

We’ll cover:

 

Grounding AI in machine learning refers to the process of linking abstract knowledge in AI systems to tangible, real-world examples. This enhances an AI's ability to produce better predictions and responses by using specific, contextually relevant information.

In the realm of language models, grounding AI involves giving large language models (LLMs) access to use-case specific information, which is not inherently part of their training data. By including explicitly cited data, a grounded model can generate more precise and contextually relevant output.

To go a bit deeper, generative LLMs produce text using two primary methods. In one way, the LLM relies on the knowledge and understanding gained from its training data. And in the other way, the model is provided with specific information (e.g., for summarization) and instructed to either use that information alone or combine it with its inherent knowledge to generate the text. 

Ultimately, grounding AI aims to build machine learning solutions that intelligently and effectively operate in real-world situations, offering users contextually appropriate, accurate, and meaningful results. As you can imagine, grounding becomes important because that is the way we can influence LLM outputs to be customized to the knowledge of a particular organization.

It's important to clarify that grounding does not refer to training a model with annotated data containing the information to be used for generating the response, as this would be known as supervised learning. Instead, grounding specifically relates to guiding a generative language model to generate responses that incorporate explicitly referenced information.

 

When an AI system needs to be accurate and factual in what it generates, grounding is key. This is especially true in an enterprise environment when you need to ensure a high threshold of accuracy in the answers the AI generates when those outputs are going to employees or customers.

Grounded AI systems are superior to non-grounded systems as they connect their abstract knowledge with the specifics of real-world scenarios. This enables them to generate more accurate, contextually relevant responses in comparison to non-grounded systems, which may struggle to incorporate case-specific information, leading to irrelevant or inaccurate outputs. In this way, we can harness the power of LLMs while improving the odds of getting fluent but accurate responses.

 

One intriguing aspect of large language models (LLMs) is the occurrence of the "hallucination" effect. Hallucination occurs when an AI generates outputs that sometimes appear reasonable but are not entirely accurate based on the given context. And in some rarer cases — an LLM could surface information that is just plain wrong. 

That said, hallucinations are not inherently negative, as they can demonstrate an AI model's ability to create inventive text and responses. However, if hallucinations lead to misleading outputs or if they reflect leaked world knowledge, they become problematic.

Recognizing the types and impacts of hallucinations is essential in determining their acceptability. Generally, hallucinations are less concerning in conversational responses, where there is no specific ground truth, and the goal is to generate text consistent with the overall context and tone. 

For instance, when answering a question like, "How many dinosaurs were in the Jurassic period?", the AI's response may provide the correct information, approximately 2-4 billion, alongside a long list of unneeded information, including the comparison to the number of people on Earth today. This type of hallucination is acceptable since the essential part of the answer remains accurate, and the additional information doesn't significantly affect the response's value. But the following text contains an egregious error, as there are significantly more than 2-4 billion people alive on Earth today. 



![Image | how many dinosaurs were in the jurassic period? View other drafts v ‘The exact number of dinosaurs that lived in the Jurassic period is unknown, but estimates range from 2 billion to 4 billion. This means that there were likely more dinosaurs on Earth during the Jurassic period than there are people alive today. The Jurassic period was a time of great diversity for dinosaurs, and many different types of dinosaurs lived <during this time, including sauropods, theropods, ornithopods, and stegosaurs. Here are some of the most common dinosaurs that lived in the Jurassic period: + Sauropods: These were the largest dinosaurs, and they included species such as Diplodocus, Brachiosaurus, and ‘Apatosaurus. Sauropods were herbivores, and they had long necks and tals. + Theropods: These were the meat-eating dinosaurs, and they included species such as Allosaurus, Tyrannosaurus rex, and Velociraptor. Theropods had sharp teeth and claws, and they were some of the most fearsome predators of the Jurassic period. + Ornithopods: These were the bird-hipped dinosaurs, and they included species such as Stegosaurus, Triceratops, and iguenodon. Ornithopods were herbivores, and they had beaks and teeth that were well-suited for eating plants. + Stegosaurs: These were the armored dinosaurs, and they included species such as Stegosaurus and Kentrosaurus. Stegosaurs had plates and spikes on their backs, which they used to protect themselves from predators. ‘The Jurassic period was a time of great change for dinosaurs, and many new species evolved during this time. The dinosaurs eventually went extinct at the end of the Cretaceous period, but they left a lasting legacy on the Earth.](https://www.moveworks.com/hubfs/image-png-Jul-26-2023-05-06-41-4559-PM.png)

Figure 1: If we provided the LLM with a Wikipedia article on the Jurassic period and told it to only use that article, but it still produced text that was not supported by that article, that would also be a hallucination — even if the entire generated response was accurate.

This is to say that hallucination is an intrinsic characteristic of AI systems and sometimes can be beneficial. The key is identifying when hallucinations are problematic and mitigating their drawbacks while harnessing their potential for producing more engaging and contextually relevant AI-generated responses. This is where grounding plays a vital role.

 

Particularly in enterprise settings, AI systems are increasingly relied upon to make critical decisions, offer recommendations, or provide solutions that directly impact business operations. In such scenarios, accuracy becomes a non-negotiable requirement. Grounding AI ensures that the AI model's understanding is closely linked to the real-world context, minimizing errors and maximizing the relevance of the generated outputs.

By grounding AI, systems can better decipher the surrounding context, filter through available data, and process information in a manner that reflects real-world situations. This ability significantly enhances decision-making capabilities, as the AI system can draw from specific and relevant data sources to produce outputs that are aligned with the scenario at hand.

 

AI systems often encounter difficulties when interpreting and processing complex real-world data. Identifying and addressing these challenges is crucial for developing AI models that can provide meaningful and effective responses in a wide array of applications. Some challenges faced by AI systems when understanding real-world data include: 

The consequences of the challenges listed above are that training is not always able to imbue the model with everything it needs to produce a contextually relevant response. Grounding helps the model to produce better results, without being limited by its training data. 

 

Suppose we want to use a tool to determine the office location of an employee named Mike Jordan. 

Using an ungrounded LLM, which only generates text based on the model's learning, we might encounter some issues. For instance, the ungrounded LLM could wrongly assume that our query is about basketball legend Michael Jordan and provide an irrelevant, albeit factually accurate, answer. Here, the model is making a leap in saying that Michael Jordan's office is in Charlotte based on the fact that his team was based there. That is an assumption, and it's not clear whether the model had access to any concrete evidence about the location of Jordan’s office.

On the other hand, if we utilize a grounded LLM connected to an internal employee roster, we can experience a more accurate and helpful response. Once prompted with relevant employee search results containing details about Mike Jordan, such as his title, tenure, location, email, and phone number, the grounded LLM can quickly provide us with the correct answer: "Mike Jordan is based in San Francisco, CA, and their title is IT Director."

By employing a grounded LLM in this scenario, we can ensure that the information provided is both accurate and efficient, significantly enhancing the employee data lookup process. 



![Image | Tee aad eae eee Cue ae Oe a a ne Uc chairman of the Charlotte Hornets, an NBA team. The team is based in Charlotte, North eR eee Ra en Ce Ue een oe UNO ue with the Charlotte Hornets are primarily based in Charlotte. However, please note that my Eu i See eer een ee Ue Ere CON aC CC Secs](https://www.moveworks.com/hubfs/image-png-Jul-26-2023-05-10-27-7211-PM.png)

Figure 2: Grounding prevents a language model from being misled by unrelated information.

 

AI systems must overcome a myriad of challenges to excel in interpreting and processing complex real-world data. Grounding AI models in real-world knowledge and providing them with sufficient contextual understanding are essential steps in addressing these challenges. 

By equipping AI models with the ability to seamlessly adapt to different contexts, data formats, and linguistic nuances, enterprises can harness AI's capabilities more effectively and ensure their systems are well-suited to address an extensive range of use cases across various industries.

 

Before diving deeper, it's essential to have a basic understanding of two main types of machine learning (ML) models: discriminative and generative models. 

Discriminative models are the more widespread category, which allow for tasks like predicting variable values or classifying items into categories. The primary function of these models is to map an input to an output value or category. For instance, a discriminative model can help determine whether an email is spam or non-spam, based on the input features, such as the email's content, sender information, and subject line.

On the other hand, generative models produce variations or examples of the input. To do this, these models must grasp the input's essence and create examples based on specific input requirements. For instance, these models can learn the essential elements of writing a professional email and generate completely new emails that cater to specific situations — such as crafting a friendly reminder to colleagues about an upcoming deadline or composing a thoughtful request for additional project resources.

Generative models, like GPT-4, are powerful due to their exposure to billions of text pieces during training, which has enabled them to understand what a well written poem or novel or research paper looks like, to the extent that something like ChatGPT can produce similar pieces of text, literally predicting one word at a time. On top of that, generative models can be further fine-tuned to take instructions in plain language to produce this text to match some requirements.

 

The key to grounding is finding a way to guide your LLM to produce responses that only use your data, rather than restricting its trained knowledge. By doing so, you can incorporate case-specific, relevant information that enhances your AI model's understanding and processing capabilities in real-world situations.

The goal is to control the AI model's behavior so that it utilizes explicitly provided information — without resorting to filling in blanks to create content or respond to questions. 

 

To improve the accuracy of AI models, especially in generating contextually relevant responses, we can employ several grounding techniques. Here's a closer look at three key methods: 

 

LLMs can benefit from incorporating external knowledge or databases, providing additional data and context for more effective grounding. By employing semantic search, the relevant and similar text between a user's query and available content can be quickly identified, enhancing the responses generated through retrieval augmented generation. This can be achieved by including the retrieved data in the LLM prompt or enabling API access to the data source. 

Vector databases are particularly powerful due to their use of semantic keyword-assisted search, which combines the advantages of both keyword and semantic search. Semantic search leverages the concept of embeddings – a representation of text in “semantic space”, where similar phrases are closely mapped and unrelated phrases are distant. Vector databases store these embeddings, supporting retrieval augmented generation by enabling the quick identification of relevant and similar content to answer users' queries effectively. 

As companies integrate generative AI features within their SaaS offerings, they will increasingly leverage existing APIs and platforms to ground AI models using semantic search and vector databases.

 

In this case, a user's request to the LLM is transformed into multiple internet search queries. The top results are then analyzed and fed back into the LLM through a subsequent prompt, providing context for the LLM to use. Before being presented to the user, the LLM's output can be verified and cross-referenced with the search results.

Let's take a relatable example: researching treatment options for a health condition. Suppose a user asks the LLM to suggest different therapies for addressing a particular ailment. The system creates one or more search queries, performs a web search, and retrieves a list of web pages with information on various treatments. The AI model then parses the text from these web pages and incorporates it in the next prompt using in-context learning, which helps the LLM select relevant information based on the user's original request. Finally, the model summarizes the results and facilitates a discussion with the user about the possible treatment options. 

In this case, the actual web search results on treatment options act as grounding, using the search context to provide factual responses based on reliable and more up-to-date sources discovered in the search. Additionally, integrating citations and references from the web search results allows users to delve into the external data used for grounding, instilling confidence as they explore different healthcare options. 

 

Engineers can incorporate system messages to provide context that helps ground and align the model with user needs. Regularly updating the LLM's internal system messages can keep the model informed about current trends and terminology, making its responses more relevant and accurate to users. 

For instance, you could use a system message like, "You are an expert nutritionist providing advice to health-conscious individuals, and all responses must be accurate and based on scientific research." This ensures more precise nutritional guidance in the model's responses. 

Regularly updating an LLM's internal system messages can keep the model informed about current trends and terminology, making its responses more relevant and accurate to users. In-context learning enables users to efficiently develop models for new scenarios like recognizing and responding to new slang terms or emerging health trends that gain popularity. 

By providing a prompt composed of various input-output pairs, we can keep the AI model informed without adjusting and maintaining new parameters for each task. Ensuring that context is delivered through system messages and updating them regularly allows the AI model to generate responses that stay current and relevant to the user's requirements, ultimately enhancing the overall user experience.

 

Supplementing AI models with user-provided data sources, such as documents, significantly boosts their ability to understand context. 

For instance, when summarizing a lengthy report, a more accurate and succinct summary can be achieved if the AI utilizes the document itself as context. Previously, models were limited by the maximum input tokens. However, the emergence of models like GPT-4 allows for substantially longer input contexts. 

One effective method for grounding models is to enable users to provide documentation links for obtaining context. OpenAI's GPT-4 launch demo illustrates this approach, where a developer received Python code from the model, based on specific requirements. After encountering an error message, the user supplied a link to the relevant technical documentation, allowing the model to deduce the appropriate bug fixes. As the context length increases and models access user/company-specific information, their output becomes more potent. 

 

Integrating multimodal features, such as visual input, can enrich an LLM's contextual understanding when addressing inquiries. For instance, a user asking about an artwork's style can provide its image along with the question, allowing the AI to analyze the picture and deliver a well-informed answer based on its assessment. 

Although it might not be a traditional form of grounding, modern multimodal models accepting text and images as prompts offer innovative ways to align with a user's scope and context. Imagine a scenario where a user requests dinner recipe suggestions and provides a photo of the available pantry or fridge items. 

The AI model can utilize image context to recommend recipes based on the ingredients at hand. In more advanced applications, users could request step-by-step repair instructions for an appliance or device while submitting images at each stage for the AI model to maintain context and provide accurate guidance. 

 

Allowing an LLM to access external tools, such as calculators, can improve its accuracy when handling mathematical or computational questions. 

An AI-driven digital assistant calculating long-term investment growth can utilize an external financial calculator to provide precise and contextually relevant results. Future models may have access to multiple external tools that can be used for verification, referencing, and grounding responses. 

Currently, when an LLM is asked for driving directions, it provides turn-by-turn instructions based on its training dataset, which only includes up-to-date information up to a certain point. If the model could access and be trained to use external tools like real-time traffic data or personal user information through third-party APIs, its responses could factor in road closures, traffic conditions, and personalized requirements, such as electric charging stations.

 

Businesses are constantly searching for technologies that set them apart from their competitors and offer them a decisive edge. Grounding AI has emerged as a differentiator that can enhance the AI model's effectiveness and value in real-world applications.

By incorporating grounding techniques, AI-driven solutions can achieve more accurate, contextually relevant, and reliable results, paving the way for enterprises to gain a competitive advantage in today's rapidly evolving market. 

Here are just a few of the ways grounding can benefit businesses:

 

Grounded AI has led to numerous practical advancements in various industries. By leveraging contextual information and real-world data, these AI systems offer significant improvements over traditional models. Below, we explore several case studies where grounding has been successfully applied. 

Example 1: Employee support with grounded conversational AI 

Tools like Moveworks leverage company information, such as employee names, contact lists, meeting room titles, and software details, to make the AI's responses more accurate. This approach leads to better support and helps enhance overall user satisfaction.

Example 2: Medical diagnosis and treatment planning

AI-assisted medical diagnosis tools benefit from additional patient-provided information. For example, while describing their symptoms to a doctor, patients can also share relevant medical history or lab results. This extra data helps doctors gain a deeper understanding of the patient's condition, leading to more accurate diagnoses and better patient care.

Example 3: Financial trading 

AI-powered financial trading tools can benefit from additional information from traders. For example, if a trader is making a decision about whether to buy or sell a stock, they can provide the AI tool with the company's financial statements or the latest news about the company. This additional information helps the AI tool to make a more informed decision.

Example 4: Education

AI-powered educational tools can benefit from additional information from students. For example, if a student is working on a math problem, they can provide the AI tool with the steps they have already taken to solve the problem. This additional information helps the AI tool provide more helpful feedback.

 

Grounding AI in real-world experiences elevates AI systems' capacity to become more efficient, context-aware, and adaptable to users' diverse needs. The importance of grounding AI cannot be overstated, as it bridges the gap between data-driven intelligence and human intuition, paving the way for more seamless and productive human-AI collaborations. 

To harness the potential of grounded AI, further research and development are essential. Researchers, industries, and AI enthusiasts should continue to explore opportunities for integrating contextual data and real-world experiences in AI systems, unlocking their full capability and versatility. 

Large language models are not one-size-fits-all. Learn more about benchmarking LLM performance for the enterprise. 

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
        

