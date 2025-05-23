from flask import Flask, request, jsonify

app = Flask(__name__)

mensagens = [
    "Confie no processo. Às vezes, o caminho difícil é o certo.",
    "Você é mais forte do que pensa.",
    "O universo conspira a favor de quem se move.",
    "Respire fundo. Está tudo se encaixando.",
]

@app.route("/mensagens", methods=["GET"])
def get_mensagens():
    if request.args.get("aleatoria") == "true":
        import random
        return jsonify({"mensagem": random.choice(mensagens)})
    return jsonify({"mensagens": mensagens})

@app.route("/mensagens", methods=["POST"])
def post_mensagem():
    data = request.get_json()
    mensagem = data.get("mensagem", "").strip()

    if not mensagem:
        return jsonify({"erro": "Mensagem não pode estar vazia."}), 400

    mensagens.append(mensagem)
    return jsonify({"status": "sucesso", "mensagem": "Mensagem adicionada com sucesso."}), 201
