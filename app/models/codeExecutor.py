import subprocess
import json
import os
import execjs
class CodeExecutor:
    def __init__(self):
        # Get the absolute path of the root directory of the Flask application
        root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.problems_file_path = os.path.join(root_dir, 'problems.json')

    def execute_code(self, language, code, input_data, problem_name):
        # Execute the provided code for a single test case with the given input_data
        # and return the result for the specific problem.
        if problem_name in self._get_problems_data():
            return self._execute_problem(language, code, input_data, problem_name)
        else:
            return {'error': 'Unsupported problem name'}

    def execute_all_tests(self, language, code, problem_name):
        # Execute the provided code for all test cases for the given problem_name
        # and return the results.
        if problem_name in self._get_problems_data():
            return self._execute_all_problem_tests(language, code, problem_name)
        else:
            return {'error': 'Unsupported problem name'}

    def _execute_problem(self, language, code, input_data, problem_name):
        # Execute the code for the specific problem with the given input_data
        # and return the result.
        if language == "python":
            try:
                process = subprocess.Popen(['python', '-c', code],
                                           stdin=subprocess.PIPE,
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE,
                                           text=True)
                stdout, stderr = process.communicate(input=input_data, timeout=5)
                output = stdout.strip()
                error = stderr.strip()

                expected_output = self._get_expected_output(problem_name, input_data)

                result = {
                    'input': input_data,
                    'output': output,
                    'expected_output': expected_output,
                    'error': error,
                }

                if output == expected_output:
                    result['is_correct'] = True
                else:
                    result['is_correct'] = False

            except subprocess.TimeoutExpired:
                result = {
                    'input': input_data,
                    'output': '',
                    'expected_output': expected_output,
                    'error': 'Timeout Error: The code took too long to execute.',
                    'is_correct': False,
                }
            except Exception as e:
                result = {
                    'input': input_data,
                    'output': '',
                    'expected_output': expected_output,
                    'error': str(e),
                    'is_correct': False,
                }

            return result
        elif language == "javascript":
            # Add JavaScript code execution logic here
            return self._execute_javascript(code, input_data)
            
        elif language == "java":
            # Add Java code execution logic here
            pass
        elif language == "cpp":
            # Add C++ code execution logic here
            pass
        else:
            return {'error': 'Unsupported language'}
    
    def _execute_javascript(self, code, input_data):
        try:
            ctx = execjs.compile(code)
            output = ctx.call('main', input_data)  # Assuming the user's function is named 'main'
            return {'output': output, 'error': '', 'is_correct': True}
        except Exception as e:
            error = str(e)
            return {'output': '', 'error': error, 'is_correct': False}
   

    def _execute_all_problem_tests(self, language, code, problem_name):
        # Execute all test cases for the specific problem with the given code
        # and return the results.
        problems_data = self._get_problems_data()
        problem_data = problems_data[problem_name]
        input_test_cases = problem_data['input_test_cases']

        results = []
        for test_case in input_test_cases:
            input_data = test_case["input"]

            result = self._execute_problem(language, code, input_data, problem_name)
            results.append(result)

        return results

    def _get_problems_data(self):
        # Fetch problems and test cases data from problems.json
        with open(self.problems_file_path) as f:
            problems_data = json.load(f)
        return problems_data

    def _get_expected_output(self, problem_name, input_data):
        # Fetch expected output for a specific input from problems.json
        problems_data = self._get_problems_data()
        problem_data = problems_data[problem_name]
        input_test_cases = problem_data['input_test_cases']

        for test_case in input_test_cases:
            if test_case["input"] == input_data:
                return test_case["expected_output"]

        return None
