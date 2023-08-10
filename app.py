# run.py
from app import create_app

app = create_app()

@app.route('/')
def hello_world():
    return 'Hello, welcome to app!'

if __name__ == '__main__':
   
    app.run(debug=True)
    
    
