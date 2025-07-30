import sqlite3
import os

# Caminho para o arquivo do banco de dados
db_path = os.path.join('data', 'banco.db')

# Conectar ao banco de dados
conexao = sqlite3.connect(db_path)
cursor = conexao.cursor()

# Criar tabela de usuários
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL
)
""")

# Criar tabela de contas bancárias
cursor.execute("""
CREATE TABLE IF NOT EXISTS contas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER,
    saldo REAL DEFAULT 0.0,
    FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
)
""")

# Criar tabela de transações
cursor.execute("""
CREATE TABLE IF NOT EXISTS transacoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    conta_id INTEGER,
    tipo TEXT NOT NULL,
    valor REAL NOT NULL,
    data TEXT NOT NULL,
    FOREIGN KEY (conta_id) REFERENCES contas (id)
)
""")

# Salvar as alterações e fechar a conexão
conexao.commit()
conexao.close()

print("Tabelas criadas com sucesso!")
