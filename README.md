# Desafios de Docker e Microsserviços

# Descrição do Projeto

Este repositório contém a solução para 5 desafios práticos focados em **Docker** e **Microsserviços**. O objetivo é demonstrar o domínio na conteinerização de aplicações, orquestração de serviços com Docker Compose, persistência de dados e implementação de arquiteturas de microsserviços, incluindo a utilização de um API Gateway.

Cada desafio está contido em sua própria pasta (`desafio1` a `desafio5`) e inclui todos os arquivos necessários (Dockerfiles, códigos-fonte, scripts e `docker-compose.yml`), além de um `README.md` detalhado com a descrição da solução, arquitetura, decisões técnicas e instruções de execução.

## Estrutura do Repositório

O repositório segue a estrutura solicitada, com uma pasta para cada desafio:

```
.
├── desafio1/
│   ├── client/
│   ├── server/
│   ├── docker-compose.yml
│   └── README.md
├── desafio2/
│   ├── init_db/
│   ├── docker-compose.yml
│   └── README.md
├── desafio3/
│   ├── web/
│   ├── docker-compose.yml
│   └── README.md
├── desafio4/
│   ├── consumer_service/
│   ├── user_service/
│   ├── docker-compose.yml
│   └── README.md
├── desafio5/
│   ├── api_gateway/
│   ├── order_service/
│   ├── user_service/
│   ├── docker-compose.yml
│   └── README.md
└── README.md  <-- Este arquivo
```

# Visão Geral dos Desafios

| Desafio | Tópico Principal | Descrição Breve |
| :--- | :--- | :--- |
| **Desafio 1** | Containers em Rede | Comunicação entre dois containers (servidor web e cliente) em uma rede Docker customizada. |
| **Desafio 2** | Volumes e Persistência | Demonstração da persistência de dados de um banco de dados PostgreSQL usando volumes nomeados do Docker. |
| **Desafio 3** | Docker Compose Orquestração | Orquestração de uma aplicação de três camadas (Web, DB, Cache/Redis) usando `docker-compose.yml`, incluindo `depends_on`. |
| **Desafio 4** | Microsserviços Independentes | Comunicação direta via HTTP entre dois microsserviços (User Service e Consumer Service), cada um em seu container isolado. |
| **Desafio 5** | Microsserviços com API Gateway | Implementação de um API Gateway para centralizar o acesso e rotear requisições para dois microsserviços de *backend* (User e Order Service). |

# Execução

Para executar qualquer um dos desafios, siga os passos abaixo:

# Pré-requisitos
*   Docker e Docker Compose instalados na sua máquina.

# 1. Navegar para o Diretório do Desafio
Substitua `[NUMERO_DO_DESAFIO]` pelo número desejado (1 a 5).

```bash
cd desafio_docker_microsservicos/desafio[NUMERO_DO_DESAFIO]
```

# 2. Construir e Iniciar os Serviços
Dentro da pasta do desafio, execute o comando para construir as imagens (se necessário) e iniciar os containers:

```bash
docker-compose up --build
```

# 3. Testar e Verificar
Consulte o `README.md` específico de cada desafio para as instruções detalhadas de teste (endpoints, logs, etc.).

# 4. Parar e Limpar
Para parar e remover os containers e a rede (e volumes, se aplicável, no Desafio 2):

```bash
docker-compose down
# para o Desafio 2, use: docker-compose down -v
```

# Considerações Finais

O código-fonte e a documentação foram desenvolvidos com foco em clareza, organização e às boas práticas de conteinerização e arquitetura de microsserviços. O `README.md` de cada desafio detalha a arquitetura, as decisões técnicas e o fluxo de comunicação.
