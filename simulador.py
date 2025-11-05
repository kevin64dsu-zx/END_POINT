import requests
import random
import time

URL = "http://127.0.0.1:5000/receber_dados"

for i in range(5):  # envia 5 leituras simuladas
    dados = {
        "CO": round(random.uniform(0, 100), 2),
        "CH4": round(random.uniform(0, 200), 2)
    }
    resposta = requests.post(URL, json=dados)
    print(f"Enviado: {dados} | Resposta: {resposta.json()}")
    time.sleep(2)
