import openai

class Designer:
    def __init__(self):
        openai.api_key = 'YOUR_OPENAI_API_KEY'

    def create_design(self, prompt):
        design_prompt = f"Act as a designer. Create the design specifications for the following application: {prompt}"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=design_prompt,
            max_tokens=500
        )
        return response.choices[0].text.strip()
