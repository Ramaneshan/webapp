from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Azure DevOps! This is a sample web app.'

if __name__ == '__main__':
    app.run(debug=True, port=8000)  # Change the port number to 8000 (or any other available port)

