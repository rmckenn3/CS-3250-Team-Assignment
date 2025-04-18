"""
Stores information about customers.
"""
#imports
from account import Account

# User class
class User:
    # Initialize variables for a user
    def __init__(self, name, birthday, ssn, address, email=None, phone=None):
        self.name = name  # User's name
        self.birthday = birthday  # User's date of birth
        self.ssn = ssn  # User's social security number
        self.address = address  # User's address
        self.phone = phone  # User's phone number
        self.email = email  # User's email address
        self.accounts = []  # List of accounts associated with the user
    #end __init__

    # Edit user information
    def edit(self, variable, value):
        # List of allowed attributes for editing
        allowed_attributes = {"name", "birthday", "address", "phone", "email"}
        # Validate the attribute
        if variable not in allowed_attributes:
            raise ValueError(f"Invalid variable name: {variable}")
        # Update the attribute dynamically
        setattr(self, variable, value)
        print(f"{variable} updated successfully.")
    #end edit

    # Add an account to the user
    def add_account(self, account, ownership_type):
        try:
            # Define valid ownership types
            valid_ownership_types = {"primary", "secondary"}
            # Validate the ownership type
            if ownership_type not in valid_ownership_types:
                raise ValueError("Ownership type must be 'primary' or 'secondary'")
            # Check if the account already exists
            if any(acc.account_number == account.account_number for acc in self.accounts):
                raise ValueError("Account already exists")
            # Validate primary holder
            if ownership_type == "primary":
                if account.get_primary_holder() != self.name:
                    raise ValueError("Primary account holder must match user name")
                if self.name in (account.secondary_holders or []):
                    raise ValueError("User cannot be a secondary holder of the account")
            # Validate secondary holder
            if ownership_type == "secondary":
                if self.name not in (account.secondary_holders or []):
                    raise ValueError("User must be a secondary holder of the account")
            # Add the account to the user's accounts
            self.accounts.append(account)
            print(f"Account {account.account_number} added successfully.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    #end add_account

    # Remove an account from the user
    def remove_account(self, account_number):
        # Search for the account and remove it
        for account in self.accounts:
            if account.account_number == account_number:
                self.accounts.remove(account)
                print(f"Account {account_number} removed successfully.")
                return
        # Raise an error if the account is not found
        raise ValueError("Account not found")
    #end remove_account

    # Display all accounts associated with the user
    def display_accounts(self):
        # Check if the user has any accounts
        if not self.accounts:
            print("No accounts found.")
            return
        # Print details of each account
        for account in self.accounts:
            print(f"Account Number: {account.account_number}, Type: {account.account_type}, Balance: {account.balance}")
    #end display_accounts

    # Report fraud for a specific account
    def report_fraud(self, account_number):
        # Validate the account number
        if not isinstance(account_number, int):
            raise ValueError("Account number must be an integer.")
        # Check if the account exists in the user's accounts
        if not any(account.account_number == account_number for account in self.accounts):
            raise ValueError("Account not found in user's accounts.")
        print(f"Fraud reported for account {account_number}. Please follow up with customer support.")
    #end report_fraud

    # Send a document or message to a recipient
    def send_document(self, recipient, content):
        # Validate the recipient and content
        if not isinstance(recipient, str) or not recipient.strip():
            raise ValueError("Recipient must be a non-empty string.")
        if not isinstance(content, str) or not content.strip():
            raise ValueError("Content must be a non-empty string.")
        print(f"Document sent to {recipient}: {content}")
    #end send_document
#end User class