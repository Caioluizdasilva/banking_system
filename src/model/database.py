import sqlite3
from datetime import datetime

DATABASE_FILE = 'bank.db'

def initialize_database():
    """Creates the database and its tables if they don't exist."""
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            account_number INTEGER PRIMARY KEY AUTOINCREMENT,
            client_name TEXT NOT NULL,
            date_of_birth TEXT NOT NULL,
            password TEXT NOT NULL,
            balance REAL NOT NULL DEFAULT 0
        );
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_number INTEGER,
            type TEXT NOT NULL, -- 'deposit' or 'withdrawal'
            amount REAL NOT NULL,
            datetime TEXT NOT NULL,
            FOREIGN KEY (account_number) REFERENCES accounts(account_number)
        );
    ''')
    connection.commit()
    connection.close()

def create_account_db(name, dob, password):
    """Inserts a new account into the database and returns the account number."""
    try:
        connection = sqlite3.connect(DATABASE_FILE)
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO accounts (client_name, date_of_birth, password) VALUES (?, ?, ?)",
            (name, dob, password)
        )
        new_account_number = cursor.lastrowid
        connection.commit()
        connection.close()
        return new_account_number
    except sqlite3.Error:
        return None

def verify_login_db(account_number, password):
    """Checks if credentials exist in the database. Returns account data or None."""
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM accounts WHERE account_number = ? AND password = ?", (account_number, password))
    account = cursor.fetchone()
    connection.close()
    return account

def get_balance_db(account_number):
    """Fetches and returns the balance for a given account."""
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    cursor.execute("SELECT balance FROM accounts WHERE account_number = ?", (account_number,))
    balance = cursor.fetchone()[0]
    connection.close()
    return balance

def update_balance_db(account_number, operation_amount):
    """Adds or subtracts an amount from the account's balance."""
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    cursor.execute("UPDATE accounts SET balance = balance + ? WHERE account_number = ?", (operation_amount, account_number))
    connection.commit()
    connection.close()

def log_transaction_db(account_number, type, amount):
    """Logs a transaction in the database."""
    connection = sqlite3.connect(DATABASE_FILE)
    cursor = connection.cursor()
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute(
        "INSERT INTO transactions (account_number, type, amount, datetime) VALUES (?, ?, ?, ?)",
        (account_number, type, amount, current_datetime)
    )
    connection.commit()
    connection.close()

def get_statement_db(account_number):
    """Fetches account data and transaction history."""
    connection = sqlite3.connect(DATABASE_FILE)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute("SELECT client_name, balance FROM accounts WHERE account_number = ?", (account_number,))
    account_data = cursor.fetchone()

    cursor.execute("SELECT datetime, type, amount FROM transactions WHERE account_number = ? ORDER BY datetime DESC", (account_number,))
    transactions = cursor.fetchall()
    
    connection.close()
    return account_data, transactions