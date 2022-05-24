from flask import Flask, jsonify, request #jsonify formats the output properly. ie, it returns a valid json
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    return jsonify(response.json())

@app.route("/resource/<string:n>")
def particular_rep(n):
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{n}')
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True)