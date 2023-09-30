export default defineEventHandler(async (event) => {
	const config = useRuntimeConfig();
	let messages = [];
	const previosMessages = await readBody(event);
	messages = messages.concat(previosMessages);
	/*
	console.log(messages)
	let prompt =
		messages.map((message) => `${message.role}: ${message.message}`).join('\n') + `\nAI:`;
	// prompt = "hello, wha tis you rname?"
	console.log(prompt)
	*/


// Convert the JSON strings in the messages array into objects
	console.log(messages)
// Parse the JSON string into an array of message objects
	const messageObjects = JSON.parse(messages[0]);

	// Create a formatted prompt string
	let prompt = "";

	for (let i = 0; i < messageObjects.length; i++) {
	const message = messageObjects[i];
	
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
		message: result
	};


	// Check if the request was successful (status code 200)
    if (req.status === 200) {
        // Parse the JSON response
        const responseJson = await req.json();
        const result = responseJson['results'][0]['history']['visible'][0];
        console.log(result); // You can replace this with your desired handling

        // Handle the response data here

    } else {
        // Handle errors here (e.g., non-200 status codes)
        console.error(`Request failed with status ${req.status}`);
    }
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