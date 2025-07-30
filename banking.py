import random

# Dictionary to store accounts
accounts = {}

def create_account():
    print("\n--- Create Account ---")
    name = input("Enter your full name: ")
    birth_date = input("Enter your date of birth (dd/mm/yyyy): ")
    account_number = random.randint(100000, 999999)

    while account_number in accounts:
        account_number = random.randint(100000, 999999)

    accounts[account_number] = {
        "name": name,
        "birth_date": birth_date,
        "balance": 0.0
    }

    print("\nAccount successfully created!")
    print(f"Welcome, {name}!")
    print(f"Your account number is: {account_number}")
    return account_number

def access_account():
    print("\n--- Access Account ---")
    try:
        account_number = int(input("Enter your account number: "))
    except ValueError:
        print("Invalid account number.")
        return None

    if account_number in accounts:
        print(f"Welcome back, {accounts[account_number]['name']}!")
        return account_number
    else:
        print("Account not found.")
        return None

def banking_menu(account_number):
    while True:
        print("\n--- Banking Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: $"))
            accounts[account_number]["balance"] += amount
            print(f"Successfully deposited ${amount:.2f}")

        elif choice == '2':
            amount = float(input("Enter amount to withdraw: $"))
            if amount <= accounts[account_number]["balance"]:
                accounts[account_number]["balance"] -= amount
                print(f"Successfully withdrew ${amount:.2f}")
            else:
                print("Insufficient funds.")

        elif choice == '3':
            balance = accounts[account_number]["balance"]
            print(f"Your current balance is: ${balance:.2f}")

        elif choice == '4':
            print("Logging out. See you next time!")
            break

        else:
            print("Invalid option. Please try again.")

def main():
    while True:
        print("\n=== PYTHON BANKING SYSTEM ===")
        print("1. Create new account")
        print("2. Access existing account")
        print("3. Exit")

        option = input("Choose an option: ")

        if option == '1':
            account_number = create_account()
            banking_menu(account_number)

        elif option == '2':
            account_number = access_account()
            if account_number:
                banking_menu(account_number)

        elif option == '3':
            print("Exiting the banking system. Thank you for using it!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
