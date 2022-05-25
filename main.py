from flask import Flask, jsonify #jsonify formats the output properly. ie, it returns a valid json
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

@app.route("/resource/<string:n>/comments")
def comments(n):
    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{n}/comments')
    return jsonify(response.json())

@app.route("/resource/comments?postId=<string:n>")
def comments_2(n):
    url_params = {'postId': n}
    response = requests.get(f'https://jsonplaceholder.typicode.com/comments',params=url_params)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True)