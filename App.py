"""
Acts as a user interface and runs main.
"""
#class file imports
from account import Account
from document import Document
from user import User
from transaction import Transaction

def main():
    users = []
    accounts = []
    transactions = []

    while True:
        print("\nWelcome to the Bank App")
        print("1. Create User")
        print("2. Create Account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. View Accounts")
        print("6. View Transactions")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            birthday = input("Enter birthday (YYYY-MM-DD): ")
            ssn = input("Enter SSN: ")
            address = input("Enter address: ")
            email = input("Enter email (optional): ")
            phone = input("Enter phone (optional): ")
            user = User(name, birthday, ssn, address, email, phone)
            users.append(user)
            print(f"User {name} created successfully.")

        elif choice == "2":
            if not users:
                print("No users available. Please create a user first.")
                continue
            primary_holder = input("Enter primary holder's name: ")
            account_type = input("Enter account type (e.g., Savings, Checking): ")
            balance = float(input("Enter initial balance: "))
            user = next((u for u in users if u.name == primary_holder), None)
            if not user:
                print("User not found.")
                continue
            account = Account(primary_holder, account_type, balance)
            user.add_account(account, "primary")
            accounts.append(account)
            print(f"Account {account.account_number} created successfully.")

        elif choice == "3":
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter deposit amount: "))
            account = next((a for a in accounts if a.account_number == account_number), None)
            if not account:
                print("Account not found.")
                continue
            user_name = account.get_primary_holder()
            account.deposit(user_name, amount)

        elif choice == "4":
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter withdrawal amount: "))
            account = next((a for a in accounts if a.account_number == account_number), None)
            if not account:
                print("Account not found.")
                continue
            user_name = account.get_primary_holder()
            try:
                account.withdraw(user_name, amount)
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "5":
            if not accounts:
                print("No accounts found.")
                continue
            for account in accounts:
                print(f"Account Number: {account.account_number}, Type: {account.account_type}, Balance: {account.balance}")

        elif choice == "6":
            if not transactions:
                print("No transactions found.")
                continue
            Transaction.view_transactions(transactions)

        elif choice == "7":
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
#end main

#entry point
if __name__ == "__main__":
    main()