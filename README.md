# 🏦 Python Banking System (Console App)

A command-line banking system built in Python, focused on good programming practices and code organization. The project uses a **Model-View-Controller (MVC)** architecture to separate responsibilities and a **SQLite** database for data persistence.

---

## ✨ Features

The system is structured to be robust and scalable. Current features include:

-   **Secure Account Creation**: Register new clients with a name, date of birth, and a **password** that is hidden during terminal input (using `getpass`).
-   **Data Persistence**: All account and transaction information is permanently saved in a **SQLite database** (`bank.db`).
-   **Authentication**: Secure login using the account number and the registered password.
-   **Banking Operations**:
    -   **Deposit**: Add funds to the account.
    -   **Withdraw**: Remove funds, with validation to prevent overdrawing the account balance.
-   **Detailed Statement**: View the current balance and the entire **transaction history** (deposits and withdrawals) with timestamps.
-   **Structured Codebase**: The code is organized using the MVC pattern, separating data logic (`Model`), user interface (`View`), and business rules (`Controller`).
-   **Localized Interface**: The underlying code is in English, while the user-facing interface is in Portuguese for a better user experience.

---

## 🖥️ Requirements

-   Python 3.6 or higher
-   No external libraries are needed, as `sqlite3` and `getpass` are included with Python's standard library.

---

## 🚀 How to Run

1.  Clone this repository or download the source files to your computer.
2.  Open a terminal and navigate to the project's root folder (`banking_system/`).
3.  Execute the main script with the following command:

    ```bash
    python src/main.py
    ```

4.  Follow the on-screen instructions to create an account, log in, and perform operations.