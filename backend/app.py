from flask import Flask, jsonify
from db import getAllPosts

app = Flask(__name__)

@app.route('/posts', methods=['GET'])
def posts():
    return jsonify(getAllPosts())

app.run(debug=True)