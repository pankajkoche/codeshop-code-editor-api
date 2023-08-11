from app import create_app
from flask import Flask, request, jsonify
from flask_cors import CORS

app = create_app()

@app.route('/')
def hello_world():
    return 'Hello, welcome to app!'

if __name__ == '__main__':
    CORS(app, resources={r"/*": {"origins": "https://codeshop.co.in"}})  
    
    app.run(host='0.0.0.0', port=8080)
