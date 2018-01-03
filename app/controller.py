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
        return jsonify({"message": "bichinho criado com sucesso"})
    else:
        return jsonify({"message": "não foi possível criar seu bichinho com sucesso"})


if __name__ == '__main__':
    app.run(debug=True)
