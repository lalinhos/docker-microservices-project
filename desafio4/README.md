# Desafio 4: Microsserviços Independentes

# Objetivo
Criar dois microsserviços independentes que se comunicam via HTTP.

# Solução, Arquitetura e Decisões Técnicas

A solução consiste em dois microsserviços implementados com Flask e orquestrados pelo Docker Compose, comunicando-se diretamente via HTTP.

# Arquitetura
1.  **Microsserviço A (`user_service`):**
    *   Implementado com **Flask** em Python.
    *   Expõe o *endpoint* `/users` que retorna uma lista de usuários em formato JSON.
    *   Roda na porta `5000`.

2.  **Microsserviço B (`consumer_service`):**
    *   Implementado com **Flask** e a biblioteca `requests` em Python.
    *   Expõe o *endpoint* `/combined_info`.
    *   Ao ser acessado, ele realiza uma requisição HTTP para o `user_service` (Microsserviço A), processa os dados recebidos e retorna uma lista de *strings* formatadas.
    *   Roda na porta `5001`.

# Decisões Técnicas
*   **Comunicação Direta HTTP:** A comunicação é feita diretamente entre os serviços usando o nome do serviço (`user_service`) como *hostname*, que é resolvido pelo DNS interno do Docker Compose.
*   **Isolamento de Containers:** Cada microsserviço possui seu próprio `Dockerfile` e seu próprio ambiente de execução, garantindo o isolamento.
*   **`depends_on`:** Usado no `docker-compose.yml` para garantir que o `user_service` inicie antes do `consumer_service`, já que o segundo depende do primeiro.
*   **Variável de Ambiente:** O `consumer_service` usa uma variável de ambiente (`USER_SERVICE_URL`) para configurar o endereço do serviço que ele consome, facilitando a configuração e a portabilidade.

# Explicação do Funcionamento

# Fluxo de Comunicação
1.  O usuário acessa o *endpoint* `/combined_info` do `consumer_service` (porta `5001`).
2.  O `consumer_service` usa a biblioteca `requests` para fazer uma requisição GET para `http://user_service:5000/users`.
3.  O Docker Compose roteia a requisição para o container `user_service`.
4.  O `user_service` retorna a lista de usuários em JSON.
5.  O `consumer_service` recebe o JSON, itera sobre a lista de usuários e constrói as frases formatadas (ex: "Usuário Alice ativo desde...").
6.  O `consumer_service` retorna o resultado final ao usuário.

# Instruções de Execução

# Pré-requisitos
*   Docker e Docker Compose instalados.

# 1. Navegar para o Diretório
```bash
cd desafio_docker_microsservicos/desafio4
```

# 2. Criar o Arquivo `docker-compose.yml`

```yaml
version: '3.8'

services:
  user_service:
    build: ./user_service
    container_name: desafio4_user_service
    ports:
      # expondo a porta 5000 para testes, mas em produção não seria exposta
      - "5000:5000"
    environment:
      SERVICE_NAME: user_service

  consumer_service:
    build: ./consumer_service
    container_name: desafio4_consumer_service
    ports:
      - "5001:5001"
    environment:
      USER_SERVICE_URL: http://user_service:5000/users
    depends_on:
      - user_service
```

# 3. Construir as Imagens e Iniciar os Containers

Execute o comando para construir as imagens e iniciar os serviços:

```bash
docker-compose up --build
```

# 4. Testar a Comunicação

Após os serviços estarem rodando, teste o *endpoint* do `consumer_service`:

```bash
curl http://localhost:5001/combined_info
```

**Resultado Esperado:** Um JSON contendo a lista de frases formatadas, provando que o `consumer_service` consumiu com sucesso o `user_service`.

# 5. Parar e Remover os Containers
Para parar e remover os containers e a rede:

```bash
docker-compose down
```

# Estrutura do Projeto
```
.
├── consumer_service
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
