# database/db.py
import sqlite3
import os

# Define o caminho do arquivo .db dentro da pasta data/
DB_NAME = os.path.join("data", "banco.db")

# Conecta ao banco (ou cria se não existir)
def connect():
    return sqlite3.connect(DB_NAME)

# Cria a tabela de contas (apenas uma vez)
def create_tables():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            account_number INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            birth_date TEXT NOT NULL,
            balance REAL NOT NULL DEFAULT 0
        )
    ''')

    conn.commit()
    conn.close()
