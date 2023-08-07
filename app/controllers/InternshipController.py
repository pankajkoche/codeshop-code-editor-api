# app/controllers/main_controller.py
from flask import current_app, jsonify
from flask_mail import Message
import os

def send_form_data(data,resume):
    try:
        name = data.get('name', '')
        email = data.get('email', '')
        resume_content = data.get('resume', '')
        mobile_no = data.get('mobileNo', '')

        # You can perform additional validation or processing of the data here
        subject='Internship'+' '+email
        # Send email using Flask-Mail
        message = Message(subject, sender=current_app.config['MAIL_USERNAME'], recipients=['pankajkoche04@gmail.com'])  # Replace with your email address
        message.body = f"Name: {name}\nEmail: {email}\nMobile No: {mobile_no}"
        if resume and resume.filename.endswith('.pdf'):
            resume_content = resume.read()
            message.attach('resume.pdf', 'application/pdf', resume_content)

        mail = current_app.extensions['mail']
        mail.send(message)

        return {'message': 'Your application has been submitted successfully! Thank you for your interest. We will get back to you soon.'}

    except Exception as e:
        return {'error': str(e)}
