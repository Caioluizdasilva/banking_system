from database.db import connect

def create_account():
    print("\n=== Create New Account ===")
    name = input("Enter your full name: ")
    birth_date = input("Enter your date of birth (dd/mm/yyyy): ")

    conn = connect()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO accounts (name, birth_date)
        VALUES (?, ?)
    ''', (name, birth_date))

    conn.commit()
    account_number = cursor.lastrowid  # Pega o número da conta gerado
    conn.close()

    print(f"\n✅ Account created successfully! Your account number is: {account_number}")