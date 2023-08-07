from flask import Blueprint, request, jsonify
from app.controllers.codeController import CodeController

code_bp = Blueprint('code', __name__)
code_controller = CodeController()

@code_bp.route('/run_single', methods=['POST'])
def handle_run_single():
    data = request.get_json()
    language = data.get('language')
    code = data.get('code')
    input_data = data.get('input')
    problem_name = data.get('problem_name')  # New field for the problem name

    result = code_controller.run_single_test(language, code, input_data, problem_name)
    return jsonify(result)

@code_bp.route('/submit', methods=['POST'])
def handle_submit():
    data = request.get_json()
    language = data.get('language')
    code = data.get('code')
    problem_name = data.get('problem_name')  # New field for the problem name

    results = code_controller.run_all_tests(language, code, problem_name)
    return jsonify(results)
