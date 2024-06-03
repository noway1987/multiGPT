from gpt_instances.backend_developer import BackendDeveloper
from gpt_instances.frontend_developer import FrontendDeveloper
from gpt_instances.designer import Designer
from gpt_instances.tester import Tester
import openai
from dotenv import load_dotenv
import os
from flask_socketio import SocketIO

class Orchestrator:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.backend_developer = BackendDeveloper()
        self.frontend_developer = FrontendDeveloper()
        self.designer = Designer()
        self.tester = Tester()

    def optimize_prompt(self, prompt):
        optimization_prompt = f"Optimize the following prompt for backend, frontend, design, and testing tasks: {prompt}"
        client = openai.OpenAI(api_key=self.api_key)
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an expert project manager."},
                {"role": "user", "content": optimization_prompt}
            ]
        )
        optimized_prompt = response.choices[0].message.content.strip()
        return optimized_prompt

    def process_request(self, prompt):
        optimized_prompt = self.optimize_prompt(prompt)

        backend_prompt = f"Backend Task: Set up the database architecture, create necessary models, configure database connections, and provide robust APIs for data access and manipulation. Include user authentication and data validation.\n\n{optimized_prompt}"
        frontend_prompt = f"Frontend Task: Develop the user interface, implement responsive design principles, integrate with backend APIs for data fetching, and ensure a seamless user experience. Utilize modern UI libraries and best practices.\n\n{optimized_prompt}"
        design_prompt = f"Design Task: Develop a comprehensive color palette and design system. Ensure the design is visually appealing and provides a great user experience. Provide design assets and guidelines.\n\n{optimized_prompt}"
        test_prompt = f"Testing Task: Write and implement comprehensive test cases, including unit tests, integration tests, and end-to-end tests. Utilize tools like Jest and Cypress.\n\n{optimized_prompt}"

        backend_code = self.backend_developer.generate_code(backend_prompt)
        frontend_code = self.frontend_developer.generate_code(frontend_prompt)
        design_specs = self.designer.create_design(design_prompt)
        test_cases = self.tester.write_tests(test_prompt)

        self.send_status_update('backend_developer', backend_prompt, backend_code)
        self.send_status_update('frontend_developer', frontend_prompt, frontend_code)
        self.send_status_update('designer', design_prompt, design_specs)
        self.send_status_update('tester', test_prompt, test_cases)

        return {
            "backend_developer_code": backend_code,
            "frontend_developer_code": frontend_code,
            "designer_code": design_specs,
            "tester_code": test_cases
        }

    def send_status_update(self, agent, prompt, response):
        socketio.emit('agent_status', {
            'name': agent,
            'status': 'completed',
            'prompt': prompt,
            'response': response
        }, to='/')

socketio = SocketIO()
