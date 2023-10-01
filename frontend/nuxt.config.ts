// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
	css: ['~/assets/css/main.css'],
	runtimeConfig: {
		OPENAI_API_KEY: process.env.OPENAI_API_KEY //we dont need this lol
	},
	postcss: {
		plugins: {
			tailwindcss: {},
			autoprefixer: {}
		}
	}
});
