export default defineEventHandler(async (event) => {
	const config = useRuntimeConfig();
	let messages = [];
	const previosMessages = await readBody(event);
	messages = messages.concat(previosMessages);
	let prompt =
		messages.map((message) => `${message.role}: ${message.message}`).join('\n') + `\nAI:`;
	const req = await fetch('https://college-carlo-editorial-sub.trycloudflare.com/api/v1/chat', {
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
			temperature: 0.1,
			max_new_tokens: 512,
			// top_p: 1.0,
			// frequency_penalty: 0,
			// presence_penalty: 0.6,
			// stop: [' User:', ' AI:']
		})
	});

	const res = await req.json();
	console.log(res)
	// const result = res.choices[0];
	result = res.response
	return {
		message: result.text
	};
});
