from flask import Flask, jsonify, request
from bichinhos_repository import insert

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return jsonify({'nome': 'bichinho service'})


@app.route('/bichinhos', methods=['POST'])
def create_bichinhos():
    file = request.get_json()
    if insert(file):
        return jsonify({"message": "bichinho successfully created"})
    else:
        return jsonify({"message": "it was not possible to create the bichinho"})


if __name__ == '__main__':
    app.run(debug=True)
