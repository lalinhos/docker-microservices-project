from flask import Flask, jsonify
import requests
import os
import time

app = Flask(__name__)

# endereço do microsserviço A (user_service)
USER_SERVICE_URL = os.environ.get('USER_SERVICE_URL', 'http://user_service:5000/users')

@app.route('/combined_info')
def combined_info():
    print("Requisição recebida para /combined_info")
    
    # 1. consome o microsserviço A
    try:
        response = requests.get(USER_SERVICE_URL, timeout=5)
        response.raise_for_status() # Levanta exceção para códigos de erro HTTP
        users = response.json()
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Erro ao conectar ao user_service: {e}"}), 500

    # 2. processa e exibe as informações combinadas
    combined_data = []
    for user in users:
        status_text = "ativo desde" if user['status'] == 'ativo' else "inativo desde"
        combined_data.append(f"Usuário {user['name']} {status_text} {user['joined_at']}")

    return jsonify({
        "message": "Informações combinadas com sucesso.",
        "data": combined_data
    })

if __name__ == '__main__':
    time.sleep(5)
    app.run(host='0.0.0.0', port=5001)
