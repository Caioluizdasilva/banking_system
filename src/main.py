from model.database import initialize_database
from controller.bank_controller import start_system

def main():
    """
    Main function to set up and start the application.
    """
    initialize_database()
    start_system()

if __name__ == "__main__":
    main()