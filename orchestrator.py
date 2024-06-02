from gpt_instances.backend_developer import BackendDeveloper
from gpt_instances.frontend_developer import FrontendDeveloper
from gpt_instances.designer import Designer
from gpt_instances.tester import Tester

class Orchestrator:
    def __init__(self):
        self.backend_developer = BackendDeveloper()
        self.frontend_developer = FrontendDeveloper()
        self.designer = Designer()
        self.tester = Tester()

    def process_request(self, prompt):
        backend_code = self.backend_developer.generate_code(prompt)
        frontend_code = self.frontend_developer.generate_code(prompt)
        design_specs = self.designer.create_design(prompt)
        test_cases = self.tester.write_tests(prompt)

        return {
            'backend_code': backend_code,
            'frontend_code': frontend_code,
            'design_specs': design_specs,
            'test_cases': test_cases
        }
