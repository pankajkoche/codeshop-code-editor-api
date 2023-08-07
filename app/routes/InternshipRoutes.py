# app/routes/main_routes.py
from flask import Blueprint, jsonify, request
from app.controllers.InternshipController import send_form_data

bp = Blueprint('main', __name__)

@bp.route('/submit_form', methods=['POST'])
def submit_form():
    data = request.form.to_dict()
    resume = request.files.get('resume')

    response = send_form_data(data, resume)
    return jsonify(response)
