import openai
from dotenv import load_dotenv
import os

class Designer:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.client = openai.OpenAI(api_key=self.api_key)
        with open('prompts/design_prompt.txt', 'r') as file:
            self.base_prompt = file.read()

    def create_design(self, prompt):
        complete_prompt = f"{self.base_prompt}\n\n{prompt}"
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": self.base_prompt},
                {"role": "user", "content": complete_prompt}
            ]
        )
        design_specs = response.choices[0].message.content.strip()
        return design_specs
