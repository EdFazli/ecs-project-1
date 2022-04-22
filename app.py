from flask import flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Welcome to ECS Test Page!"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)