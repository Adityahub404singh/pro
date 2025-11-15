from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/")
def home():
    return "🤖 AI is Running!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    message = data.get("message", "")
    response = f"AI: I received your message - {message}"
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
