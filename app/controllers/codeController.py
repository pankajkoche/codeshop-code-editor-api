from app.models.codeExecutor import CodeExecutor

class CodeController:
    def __init__(self):
        self.code_executor = CodeExecutor()

    def run_single_test(self, language, code, input_data, problem_name):
        return self.code_executor.execute_code(language, code, input_data, problem_name)

    def run_all_tests(self, language, code, problem_name):
        return self.code_executor.execute_all_tests(language, code, problem_name)
