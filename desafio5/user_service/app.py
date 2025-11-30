from flask import Flask, jsonify

app = Flask(__name__)

# Dados simulados de usuários
USERS = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
]

@app.route('/users')
def get_users():
    print("Requisição recebida para /users (Service 1)")
    return jsonify(USERS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
