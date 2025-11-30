# o nome do host 'server' vai ser resolvido pelo Docker na rede customizada
SERVER_HOST="server"
SERVER_PORT="8080"

echo "Iniciando loop de requisições para http://${SERVER_HOST}:${SERVER_PORT}"

while true; do
    TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
    echo "[$TIMESTAMP] Enviando requisição para o servidor..."
    curl -s http://${SERVER_HOST}:${SERVER_PORT}
    echo ""
    sleep 5
done
