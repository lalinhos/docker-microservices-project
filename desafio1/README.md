# Desafio 1: Containers em Rede

# Objetivo
Criar dois containers que se comunicam por uma rede Docker customizada.

# Solução, Arquitetura e Decisões Técnicas

A solução implementada utiliza dois containers: um **Servidor Web** e um **Cliente de Requisições**, conectados por uma rede Docker customizada.

# Arquitetura
A arquitetura é simples e segue o padrão **Cliente-Servidor** em uma rede isolada:

1.  **Rede Docker Customizada (`desafio1_net`):** Garante que os containers possam se comunicar usando seus nomes de serviço como *hostname* (resolução de DNS interna do Docker).

2.  **Servidor Web (`server`):**
    *   Implementado com **Flask** em Python, pois é leve e atende ao requisito de rodar na porta `8080`.
    *   O `Dockerfile` é baseado em `python:3.9-slim`.
    *   A aplicação (`app.py`) retorna uma mensagem simples e registra no log do container a hora e o *hostname* do servidor a cada requisição.

3.  **Cliente de Requisições (`client`):**
    *   Implementado com um *script* `request_loop.sh` que usa o comando `curl`.
    *   O `Dockerfile` é baseado em `alpine/curl`, uma imagem mínima que já inclui o `curl`.
    *   O *script* executa requisições HTTP para o servidor a cada 5 segundos em um *loop* infinito. O endereço do servidor é referenciado pelo nome do serviço (`server`).

# Decisões Técnicas
*   **Servidor Web (Flask):** Escolhido pela familiaridade, simplicidade e rapidez de implementação para um servidor web que apenas precisa responder a requisições HTTP.
*   **Cliente (Alpine/curl):** Escolhido por ser uma imagem leve, ideal para tarefas simples de linha de comando como fazer requisições com `curl`.
*   **Rede Customizada:** A rede é criada explicitamente para isolar a comunicação e permitir a resolução de nomes de serviço, cumprindo o requisito principal do desafio.

# Explicação Detalhada do Funcionamento

# Fluxo de Comunicação
1.  O usuário executa o *script* de *build* e *run* (`./run.sh`).
2.  O Docker cria a rede customizada `desafio1_net`.
3.  O container `server` é iniciado e fica escutando na porta `8080`.
4.  O container `client` é iniciado e começa a executar o `request_loop.sh`.
5.  O `curl` dentro do container `client` resolve o nome `server` para o IP interno do container do servidor, graças à rede customizada.
6.  O `client` envia a requisição HTTP para `http://server:8080`.
7.  O `server` recebe a requisição, imprime uma linha no seu log e retorna a mensagem de sucesso.
8.  O `client` imprime a resposta e espera 5 segundos antes de repetir o processo.

# Logs da Troca de Mensagens
A comunicação é demonstrada observando os logs de ambos os containers:

*   **Log do Cliente:** Mostrará o *timestamp* local do cliente e a resposta recebida do servidor.
*   **Log do Servidor:** Mostrará a mensagem de "Request received from client..." a cada requisição, confirmando que a comunicação foi bem-sucedida.

# Instruções de Execução

# Pré-requisitos
*   Docker e Docker Compose instalados.

# 1. Navegar para o Diretório
```bash
cd desafio_docker_microsservicos/desafio1
```

# 2. Construir as Imagens e Iniciar os Containers
Crie o arquivo `docker-compose.yml` na pasta `desafio1`:

Execute o comando para construir as imagens e iniciar os serviços:

```bash
docker-compose up --build
```

# 3. Demonstrar a Comunicação e Logs

Com o `docker-compose up` rodando, você verá os logs de ambos os containers.

**Log do Cliente (`desafio1_client`):**
Mostrará a saída do `curl` a cada 5 segundos, confirmando que a requisição está sendo feita e a resposta está sendo recebida.

**Log do Servidor (`desafio1_server`):**
Mostrará a mensagem de log do Flask a cada requisição, confirmando que o servidor está recebendo as chamadas.

# 4. Parar e Remover os Containers
Para parar e remover os containers e a rede:

```bash
docker-compose down
```

# Estrutura do Projeto
```
.
├── client
│   ├── Dockerfile
│   └── request_loop.sh
├── server
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
└── README.md
```
