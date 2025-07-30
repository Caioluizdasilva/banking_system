from database.db import create_tables
from services.banking import create_account

def main():
    create_tables()

    while True:
        print("\n=== PYTHON BANKING SYSTEM ===")
        print("1. Create Account")
        print("2. Exit")

        option = input("Choose an option: ")

        if option == '1':
            create_account()
        elif option == '2':
            print("Exiting... Bye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
