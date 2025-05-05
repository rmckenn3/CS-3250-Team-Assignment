"""
Manages account information.
"""
#imports
from class_transaction import Transaction
from class_user import User

# Account class
class Account:
    # Static variable to track account numbers
    index = 0

    # Initialize variables for an account
    def __init__(self, primary_holder, account_type, balance=0, secondary_holders=None, card=None):
        Account.index += 1  # Increment the account number
        self.account_number = Account.index  # Assign a unique account number
        self.primary_holder = primary_holder  # Primary holder of the account
        self.account_type = account_type  # Type of the account (e.g., "Savings", "Checking")
        self.balance = balance  # Current balance of the account
        self.secondary_holders = secondary_holders  # List of secondary holders
        self.card = card  # Associated card information
        self.transaction_history = []  # List of transactions for the account
    #end __init__

    # Deposit funds into the account
    def deposit(self, user_name, amount):
        # Validate the deposit amount
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        # Update the balance and record the transaction
        self.balance += amount
        self.transaction_history.append(Transaction(user_name, self.account_number, amount))
        print(f"Deposit of {amount} successful! New balance: {self.balance}.")
    #end deposit

    # Withdraw funds from the account
    def withdraw(self, user_name, amount):
        # Validate the withdrawal amount
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        # Update the balance and record the transaction
        self.balance -= amount
        self.transaction_history.append(Transaction(self.account_number, user_name, amount))
        print(f"Withdrawal of {amount} successful! New balance: {self.balance}.")
    #end withdraw

    # Get the primary account holder
    def get_primary_holder(self):
        return self.primary_holder
    #end get_primary_holder

    # Add a holder to the account
    def add_holder(self, holder, ownership_type):
        try:
            # Validate the ownership type
            if ownership_type not in ["primary", "secondary"]:
                raise ValueError("Ownership type must be 'primary' or 'secondary'")
            # Add a primary holder
            if ownership_type == "primary":
                if self.primary_holder:
                    raise ValueError("Primary holder already exists.")
                self.primary_holder = holder
                print(f"Primary holder {holder} added successfully.")
            # Add a secondary holder
            elif ownership_type == "secondary":
                if not self.secondary_holders:
                    self.secondary_holders = []
                if holder in self.secondary_holders:
                    raise ValueError(f"Holder {holder} already exists as a secondary holder.")
                self.secondary_holders.append(holder)
                print(f"Secondary holder {holder} added successfully.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    #end add_holder

    # Remove a holder from the account
    def remove_holder(self, holder):
        try:
            # Prevent removal of the primary holder
            if holder == self.primary_holder:
                raise ValueError("Cannot remove the primary holder.")
            # Remove a secondary holder
            if self.secondary_holders and holder in self.secondary_holders:
                self.secondary_holders.remove(holder)
                print(f"Holder {holder} removed successfully.")
            else:
                raise ValueError(f"Holder {holder} does not exist.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    #end remove_holder

    # Check the account balance
    def check_balance(self):
        return self.balance
    #end check_balance

    # Check the transaction history
    def check_transaction_history(self):
        # Check if there are any transactions
        if not self.transaction_history:
            print("No transactions found.")
            return []
        # Print details of each transaction
        for transaction in self.transaction_history:
            print(f"Source: {transaction.source}, Destination: {transaction.destination}, Amount: {transaction.amount}, Date: {transaction.date}")
        return self.transaction_history
    #end check_transaction_history

    # Close the account
    def close_account(self):
        # Prevent closing the account if there is a positive balance
        if self.balance > 0:
            raise ValueError("Account cannot be closed with a positive balance.")
        # Reset all account attributes
        self.primary_holder = None
        self.account_type = None
        self.account_number = None
        self.balance = None
        self.secondary_holders = None
        self.card = None
        self.transaction_history = None
        print("Account closed successfully.")
    #end close_account
#end Account class