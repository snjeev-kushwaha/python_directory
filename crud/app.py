from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = "data.json"


# ---------- Helper Functions ----------
def read_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as file:
        return json.load(file)


def write_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)


# ---------- CREATE ----------
@app.route("/users", methods=["POST"])
def create_user():
    data = read_data()
    user = request.json

    user_id = str(user["id"])
    if user_id in data:
        return jsonify({"message": "User already exists"}), 400

    data[user_id] = {
        "name": user["name"],
        "age": user["age"]
    }

    write_data(data)
    return jsonify({"message": "User created successfully"}), 201


# ---------- LIST ----------
@app.route("/users", methods=["GET"])
def read_users():
    data = read_data()
    if data:
        return jsonify(data), 200
    else:
        return jsonify({}), 200

# ---------- READ ----------
@app.route("/user/<user_id>", methods=["GET"])
def read_user(user_id):
    data = read_data()

    if user_id not in data:
        return jsonify({"message": "User not found"}), 404

    return jsonify(data[user_id]), 200


# ---------- UPDATE ----------
@app.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    data = read_data()

    if user_id not in data:
        return jsonify({"message": "User not found"}), 404

    user = request.json
    data[user_id]["name"] = user.get("name", data[user_id]["name"])
    data[user_id]["age"] = user.get("age", data[user_id]["age"])

    write_data(data)
    return jsonify({"message": "User updated successfully"}), 200


# ---------- DELETE ----------
@app.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    data = read_data()

    if user_id not in data:
        return jsonify({"message": "User not found"}), 404

    del data[user_id]
    write_data(data)

    return jsonify({"message": "User deleted successfully"}), 200


# ---------- RUN SERVER ----------
if __name__ == "__main__":
    app.run(port=5000, debug=True)
