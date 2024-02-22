from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get-data")
def get_data():
    data = {
        "value": "Hello World!"
    }
    return jsonify(data), 200

@app.route("/set-data", methods=["POST"])
def set_data():
    data = request.get_json()
    return jsonify(data), 201


if __name__ == "__main__":
    app.run(debug=True)
