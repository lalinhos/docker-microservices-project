from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

# endereços dos microsserviços
USER_SERVICE_URL = os.environ.get('USER_SERVICE_URL', 'http://user_service:5000')
ORDER_SERVICE_URL = os.environ.get('ORDER_SERVICE_URL', 'http://order_service:5001')

def fetch_data(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Erro ao conectar a {url}: {e}"}

@app.route('/users')
def get_users():
    print("Gateway: Roteando para user_service")
    data = fetch_data(f"{USER_SERVICE_URL}/users")
    return jsonify(data)

@app.route('/orders')
def get_orders():
    print("Gateway: Roteando para order_service")
    data = fetch_data(f"{ORDER_SERVICE_URL}/orders")
    return jsonify(data)

@app.route('/status')
def status():
    user_status = "OK" if "error" not in fetch_data(f"{USER_SERVICE_URL}/users") else "FAIL"
    order_status = "OK" if "error" not in fetch_data(f"{ORDER_SERVICE_URL}/orders") else "FAIL"
    
    return jsonify({
        "gateway_status": "OK",
        "user_service_status": user_status,
        "order_service_status": order_status
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
