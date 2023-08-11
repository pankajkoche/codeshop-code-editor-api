# config.py

# Flask configuration

import random
import string

# Define the characters to choose from
characters = string.ascii_letters + string.digits + string.punctuation

# Generate a secure random key with 32 characters
SECRET_KEY = ''.join(random.choice(characters) for _ in range(32))

DEBUG = True  # Set to False in production for better error handling
# Flask-Mail configuration
MAIL_SERVER = 'smtp.gmail.com'  # Replace with your email provider's SMTP server
MAIL_PORT = 587  # Replace with the appropriate port
MAIL_USE_TLS = True  # Use TLS encryption for security
MAIL_USERNAME = ''  # Replace with your email address
MAIL_PASSWORD = ''  # Replace with your email password
MAIL_DEBUG = True
# CORS configuration
CORS_ORIGINS = ['https://codeshop.co.in'] 
