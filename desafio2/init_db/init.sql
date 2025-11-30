-- cria a tabela de dados de persistência
CREATE TABLE IF NOT EXISTS dados_persistentes (
    id SERIAL PRIMARY KEY,
    mensagem VARCHAR(255) NOT NULL,
    data_criacao TIMESTAMP WITHOUT TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- insere um registro inicial
INSERT INTO dados_persistentes (mensagem) VALUES ('Dados iniciais criados na primeira execucao do container.');
