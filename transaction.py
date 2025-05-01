"""
Transaction class contains methods to handle purchases and transfers.
"""
#imports
from datetime import datetime
from document import Document

# Transaction class
class Transaction(Document):
    # Initialize variables for a transaction
    def __init__(self, source, destination, amount):
        super().__init__(type="Transaction")  # Call the parent class constructor
        self.source = source  # Source of the transaction
        self.destination = destination  # Destination of the transaction
        self.amount = amount  # Amount involved in the transaction
        self.date = datetime.strftime("%Y-%m-%d %H:%M")  # Timestamp of the transaction
    #end __init__

    # Add a transaction to a transaction list
    @staticmethod
    def add_transaction(transaction_list, transaction):
        # Validate inputs
        if not isinstance(transaction_list, list):
            raise TypeError("transaction_list must be a list.")
        if not isinstance(transaction, Transaction):
            raise TypeError("transaction must be an instance of Transaction.")
        # Append the transaction and confirm success
        transaction_list.append(transaction)
        print(f"Transaction from {transaction.source} to {transaction.destination} added successfully.")
    #end add_transaction

    # Delete a transaction from a transaction list by ID
    @staticmethod
    def delete_transaction(transaction_list, transaction_id):
        # Validate inputs
        if not isinstance(transaction_list, list):
            raise TypeError("transaction_list must be a list.")
        if not isinstance(transaction_id, int):
            raise TypeError("transaction_id must be an integer.")
        # Search for the transaction and remove it
        for transaction in transaction_list:
            if getattr(transaction, "id", None) == transaction_id:
                transaction_list.remove(transaction)
                print(f"Transaction with ID {transaction_id} deleted successfully.")
                return
        # Raise an error if the transaction is not found
        raise ValueError(f"Transaction with ID {transaction_id} not found.")
    #end delete_transaction

    # View all transactions in a transaction list
    @staticmethod
    def view_transactions(transaction_list):
        # Validate input
        if not isinstance(transaction_list, list):
            raise TypeError("transaction_list must be a list.")
        # Check if the list is empty
        if not transaction_list:
            print("No transactions found.")
            return
        # Print details of each transaction
        for transaction in transaction_list:
            print(f"Source: {transaction.source}, Destination: {transaction.destination}, Amount: {transaction.amount}, Date: {transaction.date}")
    #end view_transactions
#end Transaction class