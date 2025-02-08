from flask import Flask

app = Flask(__name__)

@app.route('/posts', methods=['GET'])
def posts():
    return 'posts'

app.run(debug=True)