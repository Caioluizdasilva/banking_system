from model import database
from view import terminal_view

def handle_account_creation():
    """Orchestrates the creation of a new account."""
    name, dob, password = terminal_view.get_new_account_data()
    new_account_number = database.create_account_db(name, dob, password)
    
    if new_account_number:
        msg = f"Account successfully created! Your account number is: {new_account_number}"
        terminal_view.display_success_message(msg)
    else:
        terminal_view.display_error_message("An error occurred while creating the account.")

def handle_login():
    """Orchestrates the login process and returns the account number on success."""
    account_number, password = terminal_view.get_login_credentials()
    if not account_number:
        terminal_view.display_error_message("Invalid account number. Use numbers only.")
        return None
    
    account = database.verify_login_db(account_number, password)
    if account:
        terminal_view.display_success_message("Login successful!")
        return account_number
    else:
        terminal_view.display_error_message("Invalid account number or password.")
        return None

def handle_deposit(account_number):
    """Orchestrates a deposit operation."""
    amount = terminal_view.get_operation_amount('deposit')
    if amount is None:
        terminal_view.display_error_message("Invalid amount. Deposit must be a positive number.")
        return

    database.update_balance_db(account_number, amount)
    database.log_transaction_db(account_number, 'deposit', amount)
    terminal_view.display_success_message(f"Deposit of $ {amount:.2f} completed successfully.")

def handle_withdrawal(account_number):
    """Orchestrates a withdrawal operation."""
    amount = terminal_view.get_operation_amount('withdraw')
    if amount is None:
        terminal_view.display_error_message("Invalid amount. Withdrawal must be a positive number.")
        return
        
    current_balance = database.get_balance_db(account_number)
    if amount > current_balance:
        terminal_view.display_error_message(f"Insufficient funds. Current balance: $ {current_balance:.2f}")
    else:
        database.update_balance_db(account_number, -amount) 
        database.log_transaction_db(account_number, 'withdrawal', amount)
        terminal_view.display_success_message(f"Withdrawal of $ {amount:.2f} completed successfully.")

def handle_statement(account_number):
    """Orchestrates the statement display."""
    account_data, transactions = database.get_statement_db(account_number)
    terminal_view.display_statement(account_data, transactions, account_number)
    terminal_view.display_message("")

def manage_logged_in_account(account_number):
    """Controls the menu for a logged-in account."""
    while True:
        choice = terminal_view.display_account_menu(account_number)
        if choice == '1':
            handle_deposit(account_number)
        elif choice == '2':
            handle_withdrawal(account_number)
        elif choice == '3':
            handle_statement(account_number)
        elif choice == '4':
            terminal_view.display_message("Logging out...")
            break
        else:
            terminal_view.display_error_message("Invalid option.")

def start_system():
    """Controls the main menu and the application's flow."""
    while True:
        terminal_view.clear_screen()
        choice = terminal_view.display_main_menu()
        if choice == '1':
            handle_account_creation()
        elif choice == '2':
            account_number = handle_login()
            if account_number:
                manage_logged_in_account(account_number)
        elif choice == '3':
            print("Thank you for using our system. Goodbye!")
            break
        else:
            terminal_view.display_error_message("Invalid option.")