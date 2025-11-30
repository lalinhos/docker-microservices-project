# Desafio 5: Microsserviços com API Gateway

# Objetivo
Criar uma arquitetura com API Gateway centralizando o acesso a dois microsserviços.

# Solução, Arquitetura e Decisões Técnicas

A solução implementa um **API Gateway** simples usando Flask, que atua como ponto único de entrada para dois microsserviços de *backend* (User e Order Service), orquestrados pelo Docker Compose.

# Arquitetura
1.  **Microsserviço 1 (`user_service`):**
    *   Implementado com Flask.
    *   Expõe o *endpoint* `/users` (dados de usuários).
    *   Roda na porta `5000`.

2.  **Microsserviço 2 (`order_service`):**
    *   Implementado com Flask.
    *   Expõe o *endpoint* `/orders` (dados de pedidos).
    *   Roda na porta `5001`.

3.  **API Gateway (`api_gateway`):**
    *   Implementado com Flask e a biblioteca `requests`.
    *   Expõe os *endpoints* `/users` e `/orders` na porta `8080`.
    *   Quando um *endpoint* é acessado, o Gateway roteia a requisição internamente para o microsserviço correspondente e retorna a resposta ao cliente.

# Decisões Técnicas
*   **API Gateway Simples (Flask):** Para este desafio, um Gateway implementado em Flask é suficiente para demonstrar o conceito de roteamento e orquestração. Em um cenário real, poderíamos usar soluções mais robustas como Nginx, Kong ou um *framework* dedicado.
*   **Comunicação Interna:** Os microsserviços não têm suas portas expostas diretamente para o *host* (exceto o Gateway), garantindo que todo o tráfego externo passe pelo Gateway.
*   **Docker Compose:** Usado para definir a rede interna e garantir que todos os serviços possam se comunicar usando seus nomes de serviço.

# Explicação Detalhada do Funcionamento

# Fluxo de Requisição
1.  O cliente externo faz uma requisição para `http://localhost:8080/users`.
2.  O Docker roteia a requisição para o container `api_gateway`.
3.  O Gateway recebe a requisição no *endpoint* `/users`.
4.  O Gateway faz uma requisição interna (via `requests`) para `http://user_service:5000/users`.
5.  O `user_service` processa e retorna os dados de usuários.
6.  O Gateway recebe os dados e os repassa como resposta final ao cliente externo.
O mesmo fluxo ocorre para o *endpoint* `/orders`, roteando para o `order_service`.

# Instruções de Execução Passo a Passo

# Pré-requisitos
*   Docker e Docker Compose instalados.

# 1. Navegar para o Diretório
```bash
cd desafio_docker_microsservicos/desafio5
```

# 2. Criar o Arquivo `docker-compose.yml`
```bash
mkdir docker-compose.yml
```

# 3. Construir as Imagens e Iniciar os Containers

Execute o comando para construir as imagens e iniciar os serviços:

```bash
docker-compose up --build
```

# 4. Testar a Comunicação

Após os serviços estarem rodando, teste os *endpoints* do **API Gateway**:

**Teste 1: Acessar Usuários**
```bash
curl http://localhost:8080/users
```

**Teste 2: Acessar Pedidos**
```bash
curl http://localhost:8080/orders
```

**Teste 3: Status do Gateway**
```bash
curl http://localhost:8080/status
```

**Resultado Esperado:** Os comandos devem retornar os dados simulados de usuários e pedidos, provando que o Gateway está roteando corretamente as requisições.

# 5. Parar e Remover os Containers
Para parar e remover os containers e a rede:

```bash
docker-compose down
```

# Estrutura do Projeto
```
.
├── api_gateway
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
├── order_service
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
├── user_service
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
├── docker-compose.yml
└── README.md
```
