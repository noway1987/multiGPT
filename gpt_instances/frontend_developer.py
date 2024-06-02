import openai

class FrontendDeveloper:
    def __init__(self):
        openai.api_key = 'YOUR_OPENAI_API_KEY'

    def generate_code(self, prompt):
        frontend_prompt = f"Act as a frontend developer. Create the necessary frontend code for the following application: {prompt}"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=frontend_prompt,
            max_tokens=500
        )
        return response.choices[0].text.strip()
