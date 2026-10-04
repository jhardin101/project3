from flask import Flask, jsonify, request

app = Flask(__name__)

messages = ["Hello", "World"]

@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response

@app.route("/messages", methods=["GET", "POST", "OPTIONS"])
def messages_route():
    if request.method == "OPTIONS":
        return "", 200

    if request.method == "GET":
        return jsonify(messages)

    if request.method == "POST":
        payload = request.get_json(silent=True) or {}
        message = payload.get("message" or "").strip()

        if not message:
            return jsonify({"error": "Message is required"}), 400

        messages.append(message)
        return jsonify({"message": message}), 201

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)