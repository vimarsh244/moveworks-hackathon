export default defineEventHandler(async (event) => {
	const config = useRuntimeConfig();
	let messages = [];
	const previosMessages = await readBody(event);
	messages = messages.concat(previosMessages);
	// Convert the JSON strings in the messages array into objects
	// console.log(messages)
	// Parse the JSON string into an array of message objects
	const messageObjects = JSON.parse(messages[0]);


	// Create a formatted prompt string
	let prompt = "";
	let url_data;
	let sources_data = "";
	// Define the URL you want to make a GET request to


	// Use the fetch function to make the GET request

	for (let i = 0; i < messageObjects.length; i++) {
		const message = messageObjects[i];

		// console.log(message)

		if (i === 0) {

			const url = 'https://prime-bits-pharmacology-carrier.trycloudflare.com/get_answer/' + `${message.message}`;


			const req2 = await fetch(url);

			const res = await req2.text();
			console.log(res)
			const result = JSON.parse(res);
			// console.log(result + "context output"); // You can replace this with your desired handling
			const urls = Object.keys(result);
			console.log(urls);

			url_data = urls

			const data = Object.values(result)
			prompt+= `System: ` + data;





		}
		sources_data = "\nSources:\n"+url_data;

		if (message.role === "User") {
			prompt += `User: ${message.message}\n`;
		} else if (message.role === "AI") {
			prompt += `AI: ${message.message || '...'}\n`;
		}
	}
	console.log(prompt);

	// let prompt = "What is your name?";
	// let prompt = message.message
	// let prompt = `${message.role}: ${message.message}`+`\nAI:`

	const req = await fetch('https://michael-dave-mas-privileges.trycloudflare.com/api/v1/chat', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
			// Authorization: `Bearer ${config.OPENAI_API_KEY}`
		},
		body: JSON.stringify({
			// model: 'text-davinci-003',
			// "model" : "mistral",
			// "prompt": prompt,


			user_input: prompt,
			temperature: 0.0,
			max_new_tokens: 512,
			// top_p: 1.0,
			// frequency_penalty: 0,
			// presence_penalty: 0.6,
			// stop: [' User:', ' AI:']
		})
	});

	const res = await req.json();
	const result = res['results'][0]['history']['visible'][0][1];
	console.log(result); // You can replace this with your desired handling

	// const result = res.choices[0];
	return {
		message: result+sources_data
	};

	
});

/*
	const res = await req.json();
	// print()
	// console.log(res.stringify())
	// const result = res.choices[0];
	result = res.response
	console.log(result.stringify())

	return {
		message: result.text
	};
});
*/