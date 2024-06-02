import openai

class Tester:
    def __init__(self):
        openai.api_key = 'YOUR_OPENAI_API_KEY'

    def write_tests(self, prompt):
        test_prompt = f"Act as a tester. Write the test cases for the following application: {prompt}"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=test_prompt,
            max_tokens=500
        )
        return response.choices[0].text.strip()
