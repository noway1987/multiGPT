import openai

class BackendDeveloper:
    def __init__(self):
        openai.api_key = 'YOUR_OPENAI_API_KEY'

    def generate_code(self, prompt):
        backend_prompt = f"Act as a backend developer. Create the necessary backend code for the following application: {prompt}"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=backend_prompt,
            max_tokens=500
        )
        return response.choices[0].text.strip()
