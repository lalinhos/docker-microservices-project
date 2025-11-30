from flask import Flask, jsonify

app = Flask(__name__)

# dados simulados de pedidos
ORDERS = [
    {"id": 101, "user_id": 1, "product": "Laptop", "status": "Shipped"},
    {"id": 102, "user_id": 2, "product": "Mouse", "status": "Processing"},
    {"id": 103, "user_id": 1, "product": "Keyboard", "status": "Delivered"},
]

@app.route('/orders')
def get_orders():
    print("Requisição recebida para /orders (Service 2)")
    return jsonify(ORDERS)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
