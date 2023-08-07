# app/__init__.py
from flask import Flask
from flask_mail import Mail
from flask_cors import CORS

mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')

    # Initialize extensions
    mail.init_app(app)
    CORS(app)

    # Register routes
    from app.routes.InternshipRoutes import bp as main_bp
    app.register_blueprint(main_bp)

     # Register the code execution routes
    from app.routes.codeRoutes import code_bp
    app.register_blueprint(code_bp, url_prefix='/code')

    return app
