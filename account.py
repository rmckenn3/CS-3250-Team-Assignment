"""
Manages account information.
"""
#imports
from transaction import Transaction

#Account class
class Account:
    #initialize variables
    def __init__(self, primary_holder, account_type, account_number, balance=0, secondary_holders=None, card=None):
        self.primary_holder = primary_holder
        self.account_type = account_type
        self.account_number = account_number
        self.balance = balance
        self.secondary_holders = secondary_holders
        self.card = card
        self.transaction_history = []
    #end __init__
    
    #methods
    #create a deposit transaction
    def deposit(self, user_name, amount):
        try:
            if amount <= 0:
                raise ValueError("Deposit amount must be positive")
            self.balance += amount
            self.transaction_history.append(
                Transaction(user_name, self.account_number, amount))
            print(f"Deposit successful! New balance: {self.balance}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    #end deposit
    #create a withdrawal transaction
    def withdraw(self, user_name, amount):
        try:
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive")
            if amount > self.balance:
                raise ValueError("Insufficient funds")
            self.balance -= amount
            self.transaction_history.append(
                Transaction(self.account_number, user_name, amount))
            print(f"Withdrawal successful! New balance: {self.balance}")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
#end Account class