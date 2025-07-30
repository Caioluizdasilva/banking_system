import os
import getpass

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_main_menu():
    """Shows the main menu and returns the user's choice."""
    print("--- PYTHON BANKING SYSTEM ---")
    print("1. Create a new account")
    print("2. Access my account")
    print("3. Exit the system")
    return input("Choose an option: ")

def display_account_menu(account_number):
    """Shows the logged-in account menu and returns the choice."""
    clear_screen()
    print(f"--- WELCOME! ACCOUNT: {account_number} ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. View Statement")
    print("4. Logout")
    return input("Choose an option: ")

def get_new_account_data():
    """Prompts for and returns the data to create a new account."""
    clear_screen()
    print("--- CREATE NEW ACCOUNT ---")
    name = input("Enter your full name: ")
    dob = input("Enter your date of birth (DD/MM/YYYY): ")
    while True:
        password = getpass.getpass("Create a password: ")
        confirm_password = getpass.getpass("Confirm your password: ")
        if password == confirm_password:
            return name, dob, password
        else:
            print("\nPasswords do not match. Please try again.")

def get_login_credentials():
    """Prompts for and returns login credentials."""
    clear_screen()
    print("--- ACCOUNT ACCESS ---")
    try:
        account_number = int(input("Enter your account number: "))
        password = getpass.getpass("Enter your password: ")
        return account_number, password
    except ValueError:
        return None, None

def get_operation_amount(operation_type):
    """Prompts for the amount for a deposit or withdrawal."""
    clear_screen()
    print(f"--- {operation_type.upper()} ---")
    try:
        amount = float(input(f"Enter the amount to {operation_type.lower()}: $ "))
        if amount > 0:
            return amount
        return None
    except ValueError:
        return None

def display_statement(account_data, transactions, account_number):
    """Formats and displays the full account statement."""
    clear_screen()
    print("--- ACCOUNT STATEMENT ---")
    if not account_data:
        display_error_message("Failed to load account data.")
        return
        
    print(f"Client: {account_data['client_name']}")
    print(f"Account Number: {account_number}")
    print("---------------------------------")
    print(f"CURRENT BALANCE: $ {account_data['balance']:.2f}")
    print("---------------------------------")
    print("TRANSACTION HISTORY:")

    if not transactions:
        print("No transactions found.")
    else:
        for t in transactions:
            trans_type = "Deposit" if t['type'] == 'deposit' else "Withdrawal"
            sign = '+' if t['type'] == 'deposit' else '-'
            print(f"{t['datetime']} - {trans_type:<12} {sign} $ {t['amount']:.2f}")

def display_message(message):
    """Displays a generic message and waits for user confirmation."""
    print(message)
    input("\nPress Enter to continue...")

def display_success_message(message):
    """Displays a formatted success message."""
    display_message(f"\n✅ {message}")

def display_error_message(message):
    """Displays a formatted error message."""
    display_message(f"\n❌ {message}")