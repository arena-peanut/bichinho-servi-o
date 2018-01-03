from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return jsonify({'nome': 'bichinho service'})


@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'hello': 'hello world'})


if __name__ == '__main__':
    app.run(debug=True)
