from flask import Flask, jsonify
import os

app = Flask(__name__)

# Dados simulados de usuários
USERS = [
    {"id": 1, "name": "Alice", "status": "ativo", "joined_at": "2023-01-15"},
    {"id": 2, "name": "Bob", "status": "inativo", "joined_at": "2023-03-20"},
    {"id": 3, "name": "Charlie", "status": "ativo", "joined_at": "2024-05-10"}
]

@app.route('/users')
def get_users():
    print("Requisição recebida para /users")
    return jsonify(USERS)

if __name__ == '__main__':
    # Roda na porta 5000 por convenção de microsserviços
    app.run(host='0.0.0.0', port=5000)
