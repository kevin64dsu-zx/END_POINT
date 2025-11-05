# Monitor de Gases – IoT (Grupo 3 — Kevin)

Resumo
Projeto MVP para monitoramento de gases (CO e CH₄). Sistema composto por:
- Backend: Flask (API hospedada no Render) — recebe leituras do Arduino.
- Interface: Streamlit (hospedada no Streamlit Cloud) — consome a API e exibe dados em tempo real.
- Simulador local: `simulador.py` para testar sem hardware.

Links
- API (Render): https://end-point-c138.onrender.com
- UI (Streamlit):https://meupaineldegasesnocivos.streamlit.app/
Como rodar local (END_POINT)
1. Abra PowerShell na pasta `END_POINT`.
2. `python -m venv venv`
3. `.\venv\Scripts\activate`
4. `pip install -r requirements.txt`
5. `python app.py`
   - API ficará disponível em `http://127.0.0.1:5000`.
   - Endpoints úteis:
     - `GET /dados` → retorna JSON `{"CO": number, "CH4": number}`
     - `GET /health` → retorna `{"status":"ok"}`

Como testar sem hardware
1. Com a API rodando local, abra outro terminal com venv ativo.
2. `python simulador.py` → envia leituras falsas para `/dados`.

Arquitetura e fluxo
Arduino → POST /dados (Flask) → Streamlit GET /dados → UI
(Deploy: Flask no Render; Streamlit no Streamlit Cloud)

Observações técnicas
- Calibração do sensor MQ-x é necessária em campo (ajuste por offset e média móvel).
- Em produção real: usar DB para histórico (InfluxDB/Timescale), TLS, autenticação e alertas externos (SMS/Push).

Feito por
Kevin & Grupo 3 Fatec — responsável pelo endpoint, deploy no Render e integração Streamlit.

O que falta / próximos passos
- Calibração com amostras reais
- Persistência de histórico (BD)
  
