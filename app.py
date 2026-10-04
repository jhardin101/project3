from flask import Flask, jsonify, request, render_template

import os

app = Flask(__name__)

MESSAGE_FILE = "messages.txt"

# CORS

@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response

@app.route("/")
def index():
    return render_template("index.html")

# Get messages

@app.route("/messages", methods=["GET"])
def get_messages():
    if not os.path.exists(MESSAGE_FILE):
        return jsonify([]), 200

    with open(MESSAGE_FILE, 'r') as file:
        messages = [line.rstrip("\n") for line in file]

    return jsonify(messages), 200

# Post Message

@app.route("/messages", methods=["POST"])
def add_message():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body must contain JSON"}), 400

    if "message" not in data:
        return jsonify({"error": "Missing 'message' property"}), 400

    message = str(data["message"]).strip()

    if message == "":
        return jsonify({"error": "Message cannot be empty"}), 400

    with open(MESSAGE_FILE, "a") as file:
        file.write(message + "\n")

    return "", 201

# OPTIONS

@app.route("/messages", methods=["OPTIONS"])
def messages_options():
    return "", 204

# 404
@app.errorhandler(404)
def not_found(error):
    return (
        """
        <h1>404 Not Found</h1>
        <p>The requested route does not exist.</p>
        """,
        404,
    )

# Start Server

if __name__ == "__main__":
    app.run(debug=True)