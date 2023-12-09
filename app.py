from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, prepare to learn with Mr. Zane!"

if __name__ == '__main__':
    app.run(debug=True)
