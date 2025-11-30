# Desafio 3: Docker Compose Orquestrando Serviços

# Objetivo
Demonstrar orquestração de múltiplos serviços com dependências usando Docker Compose.

# Conceitos Demonstrados
- **Orquestração multi-serviços** com Docker Compose
- **Dependências entre serviços** (depends_on)
- **Comunicação inter-serviços** via rede interna
- **Variáveis de ambiente** para configuração
- **Arquitetura de 3 camadas** (Web, DB, Cache)

# Solução, Arquitetura e Decisões Técnicas

A solução implementa uma arquitetura de três camadas orquestrada pelo `docker-compose.yml`, demonstrando a comunicação e as dependências entre os serviços.

# Arquitetura
1.  **Serviço Web (`web`):**
    *   Implementado com **Flask** em Python.
    *   Funciona como a camada de aplicação, tentando se comunicar com o `db` e o `cache`.
    *   Possui um *endpoint* `/status` que verifica a conectividade com os outros serviços.
    *   Possui um *endpoint* `/cache` que usa o Redis para incrementar um contador, provando a comunicação com o serviço de cache.

2.  **Serviço de Banco de Dados (`db`):**
    *   Utiliza a imagem oficial do **PostgreSQL** (`postgres:14-alpine`).
    *   Configurado com variáveis de ambiente para credenciais.

3.  **Serviço de Cache (`cache`):**
    *   Utiliza a imagem oficial do **Redis** (`redis:alpine`).

# Decisões Técnicas
*   **`docker-compose.yml`:** É a ferramenta central para definir, configurar e orquestrar os três serviços em uma única rede.
*   **`depends_on`:** Usado para garantir que o serviço `web` só tente iniciar após o `db` e o `cache` terem sido iniciados. **Importante:** `depends_on` apenas garante a ordem de inicialização, não a prontidão do serviço. Por isso, o `app.py` do serviço `web` inclui um `time.sleep(10)` para dar tempo aos serviços de `db` e `cache` de estarem totalmente prontos.
*   **Variáveis de Ambiente:** Usadas para passar configurações sensíveis (como credenciais do DB) para os containers.
*   **Rede Interna:** Todos os serviços são automaticamente colocados em uma rede *default* pelo Docker Compose, permitindo que se comuniquem usando os nomes de serviço (`db` e `cache`) como *hostnames*.

# Explicação Detalhada do Funcionamento

# Fluxo de Orquestração
1.  O comando `docker-compose up` lê o `docker-compose.yml`.
2.  O Docker Compose inicia os serviços `db` e `cache` primeiro, pois o serviço `web` depende deles (via `depends_on`).
3.  O serviço `web` é iniciado. Ele lê as variáveis de ambiente e tenta se conectar ao `db` e ao `cache` usando os nomes de serviço.
4.  O *endpoint* `/status` do serviço `web` demonstra a comunicação entre os serviços, verificando se a conexão com o Redis está ativa.
5.  O *endpoint* `/cache` demonstra uma operação de escrita/leitura no Redis, confirmando a comunicação funcional.

# Instruções de Execução

# Pré-requisitos
*   Docker e Docker Compose instalados.

# 1. Navegar para o Diretório
```bash
cd desafio_docker_microsservicos/desafio3
```

# 2. Criar o Arquivo `docker-compose.yml`

```bash
mkdir docker-compose.yml
```

# 3. Construir as Imagens e Iniciar os Containers

Execute o comando para construir a imagem do serviço `web` e iniciar todos os serviços:

```bash
docker-compose up --build
```

# 4. Testar a Comunicação

Após os serviços estarem rodando (aguarde cerca de 10-15 segundos para o `web` iniciar), teste a comunicação:

**Teste 1: Status dos Serviços**
Acesse o *endpoint* `/status` no seu navegador ou via `curl`:

```bash
curl http://localhost:8080/status
```

**Resultado Esperado:** Um JSON com `db_connection: OK` e `cache_connection: OK`.

**Teste 2: Operação de Cache**
Acesse o *endpoint* `/cache` para incrementar o contador no Redis:

```bash
curl http://localhost:8080/cache
```

Repita o comando algumas vezes. O valor de `hits` deve ser incrementado a cada chamada, provando que o serviço `web` está se comunicando com o `cache`.

# 5. Parar e Remover os Containers
Para parar e remover os containers e a rede:

```bash
docker-compose down
```

# Estrutura do Projeto
```
.
├── db
│   # imagem oficial do Postgres, não precisa de Dockerfile customizado
├── cache
│   # imagem oficial do Redis, não precisa de Dockerfile customizado
├── web
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
└── README.md
```
