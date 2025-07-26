from flask import Flask, request, jsonify
from chatbot import responder_usuario
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "LeanBot API está corriendo. Usa POST en /chat"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    pregunta = data.get("mensaje", "")
    respuesta = responder_usuario(pregunta)
    return jsonify({"respuesta": respuesta})

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5050)
