import openai
from dotenv import load_dotenv
import os

class Tester:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.client = openai.OpenAI(api_key=self.api_key)
        with open('prompts/test_prompt.txt', 'r') as file:
            self.base_prompt = file.read()

    def write_tests(self, prompt):
        complete_prompt = f"{self.base_prompt}\n\n{prompt}"
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": self.base_prompt},
                {"role": "user", "content": complete_prompt}
            ]
        )
        test_cases = response.choices[0].message.content.strip()
        return test_cases
