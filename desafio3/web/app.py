from flask import Flask, jsonify
import redis
import os
import time

app = Flask(__name__)

# configurações do Redis
# o nome do host 'cache' é resolvido pelo Docker Compose
CACHE_HOST = os.environ.get('CACHE_HOST', 'cache')
CACHE_PORT = int(os.environ.get('CACHE_PORT', 6379))
try:
    cache = redis.Redis(host=CACHE_HOST, port=CACHE_PORT)
    cache.ping()
    print("Conexão com Redis estabelecida com sucesso.")
except Exception as e:
    print(f"Não foi possível conectar ao Redis: {e}")
    cache = None

# simulação de conexão com o banco
DB_HOST = os.environ.get('DB_HOST', 'db')
DB_PORT = os.environ.get('DB_PORT', '5432')
print(f"Tentando conectar ao DB em: {DB_HOST}:{DB_PORT}")

@app.route('/')
def index():
    return "Serviço Web rodando. Tente /status ou /cache."

@app.route('/status')
def status():
    # verifica a comunicação com o banco
    db_status = "OK" if DB_HOST and DB_PORT else "FAIL"
    
    # verifica a comunicação com o redis
    cache_status = "FAIL"
    cache_value = "N/A"
    if cache:
        try:
            cache.set('key', 'value')
            cache_value = cache.get('key').decode('utf-8')
            cache_status = "OK"
        except Exception as e:
            cache_status = f"FAIL ({e})"

    return jsonify({
        "service": "web",
        "db_connection": db_status,
        "cache_connection": cache_status,
        "cache_test_value": cache_value,
        "message": "Orquestração de serviços funcionando."
    })

@app.route('/cache')
def cache_test():
    if not cache:
        return jsonify({"error": "Cache indisponível"}), 500

    # tenta obter o contador do cache
    try:
        count = cache.incr('hits')
        return jsonify({
            "message": "Contador de acessos atualizado no Redis.",
            "hits": count
        })
    except Exception as e:
        return jsonify({"error": f"Erro ao acessar o Redis: {e}"}), 500

if __name__ == '__main__':
    time.sleep(10) 
    app.run(host='0.0.0.0', port=8080)
