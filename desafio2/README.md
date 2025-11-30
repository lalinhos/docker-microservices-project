# Desafio 2: Volumes e Persistência

# Objetivo
Demonstrar persistência de dados usando volumes Docker nomeados.

# Conceitos Demonstrados
- **Volumes nomeados** vs bind mounts
- **Persistência de dados** além do ciclo de vida do container
- **Inicialização de banco de dados** com scripts SQL
- **Gerenciamento de estado** em aplicações containerizadas

# Arquitetura da Solução

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│     READER      │───▶│        DB        │◄───│  postgres_data  │
│  (PostgreSQL)   │    │   (PostgreSQL)   │    │   (Volume)      │
│ Testa leitura   │    │ Armazena dados   │    │ Persiste dados  │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                              │
                              ▼
                       ┌──────────────┐
                       │  init.sql    │
                       │ (Script SQL) │
                       └──────────────┘
```

# Componentes

**1. Banco de Dados (`db`)**
- **Imagem:** postgres:14-alpine
- **Função:** Armazenar dados de forma persistente
- **Inicialização:** Executa `init.sql` na primeira execução
- **Volume:** Dados mapeados para `postgres_data:/var/lib/postgresql/data`

**2. Volume Nomeado (`postgres_data`)**
- **Tipo:** Named volume (gerenciado pelo Docker)
- **Localização:** Controlada pelo Docker Engine
- **Persistência:** Sobrevive à remoção de containers
- **Vantagens:** Backup automático, portabilidade, segurança

**3. Reader (`reader`)**
- **Função:** Validar persistência dos dados
- **Operação:** Conecta no DB e executa SELECT
- **Timing:** Executa após DB estar pronto (depends_on + sleep)

**4. Script de Inicialização (`init.sql`)**
- **Localização:** `./init_db/init.sql`
- **Execução:** Automática pelo PostgreSQL na primeira inicialização
- **Conteúdo:** CREATE TABLE + INSERT de dados de teste

# Como Funciona a Persistência

# Ciclo de Vida dos Dados

**1ª Execução (Criação)**
```
docker-compose up
├── Cria volume 'postgres_data' (se não existir)
├── Inicia container 'db'
├── PostgreSQL detecta volume vazio
├── Executa script init.sql automaticamente
├── Dados são gravados no volume
└── Reader valida dados criados
```

**Remoção (Teste de Persistência)**
```
docker-compose down  # SEM -v
├── Remove containers 'db' e 'reader'
├── Remove rede padrão
└── MANTÉM volume 'postgres_data' intacto
```

**2ª Execução (Validação)**
```
docker-compose up
├── Recria containers
├── PostgreSQL detecta volume com dados
├── NÃO executa init.sql (dados já existem)
├── Carrega dados existentes do volume
└── Reader confirma dados persistidos
```

# Diferença: Volume vs Container

| Aspecto | Container | Volume Nomeado |
|---------|-----------|----------------|
| **Ciclo de vida** | Temporário | Persistente |
| **Remoção** | `docker rm` | `docker volume rm` |
| **Localização** | Filesystem do container | Gerenciado pelo Docker |
| **Backup** | Complexo | Simples |
| **Performance** | Boa | Otimizada |

# Decisões Técnicas

# Por que PostgreSQL?
- **Robustez:** Banco com recursos avançados
- **Inicialização:** Suporte nativo a scripts SQL
- **Demonstração clara:** Perda de dados é facilmente perceptível
- **Padrão da indústria:** Amplamente usado em produção

# Por que Volume Nomeado?
- **Gerenciamento:** Docker controla localização e backup
- **Segurança:** Isolado do filesystem do host
- **Portabilidade:** Funciona igual em qualquer ambiente
- **Performance:** Otimizado para I/O de containers

# Por que Script de Inicialização?
- **Automação:** Dados criados automaticamente
- **Consistência:** Sempre os mesmos dados de teste
- **Padrão PostgreSQL:** Usa funcionalidade nativa da imagem

# Execução

# Pré-requisitos
- Docker e Docker Compose instalados

# Teste de Persistência Completo

**1. Primeira Execução (Criação)**
```bash
cd desafio2
docker-compose up --build
```

**Resultado esperado:**
```
reader | id |    nome    |         criado_em
----+------------+---------------------------
  1 | Dados Test | 2024-01-15 10:30:15.123456
```

**2. Remoção (SEM destruir volume)**
```bash
docker-compose down
```

**3. Segunda Execução (Validação)**
```bash
docker-compose up
```

**Resultado esperado:**
```
reader | id |    nome    |         criado_em
----+------------+---------------------------
  1 | Dados Test | 2024-01-15 10:30:15.123456
```

**Sucesso:** Mesmo timestamp = dados persistiram!

### Comandos Úteis

```bash
# verificar volumes existentes
docker volume ls

# inspecionar volume
docker volume inspect desafio2_postgres_data

# conectar diretamente no banco
docker exec -it desafio2_db psql -U user -d persistencia_db

# limpar tudo
docker-compose down -v
```

# Validação

**Volume criado:** `docker volume ls` mostra `desafio2_postgres_data`  
**Dados iniciais:** Reader mostra tabela com registro  
**Persistência:** Dados idênticos após recreação  
**Script executado:** Apenas na primeira inicialização

## Estrutura do Projeto
```
desafio2/
├── init_db/
│   └── init.sql         
├── docker-compose.yml  
└── README.md                   
```

### Conteúdo do init.sql
```sql
CREATE TABLE dados_persistentes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO dados_persistentes (nome) VALUES ('teste');
```

# Conceitos Aprendidos

- **Volume Management:** Diferença entre volumes e bind mounts
- **Data Persistence:** Como dados sobrevivem ao ciclo de containers
- **Database Initialization:** Uso de scripts SQL automáticos
- **Container Lifecycle:** Separação entre aplicação e dados
- **Production Patterns:** Boas práticas para dados em produção
