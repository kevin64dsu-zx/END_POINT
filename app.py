from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Armazena as últimas leituras (sem BD ainda)
leituras = {
    "CO": None,
    "CH4": None,
    "timestamp": None
}

@app.route('/')
def home():
    return "🚀 API do Monitor de Gases está online!"

@app.route('/receber_dados', methods=['POST'])
def receber_dados():
    """
    Recebe dados JSON do Arduino.
    Exemplo: {"CO": 85.2, "CH4": 140.7}
    """
    dados = request.get_json()

    # Atualiza leituras na memória
    leituras["CO"] = dados.get("CO")
    leituras["CH4"] = dados.get("CH4")
    leituras["timestamp"] = datetime.now().strftime("%H:%M:%S")

    print(f"[{leituras['timestamp']}] Dados recebidos -> CO: {leituras['CO']} | CH4: {leituras['CH4']}")
    return jsonify({"status": "ok", "mensagem": "Dados recebidos com sucesso!"})

@app.route('/ultimas_leituras', methods=['GET'])
def ultimas_leituras():
    """Retorna as leituras mais recentes (para o Streamlit consumir)."""
    return jsonify(leituras)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
