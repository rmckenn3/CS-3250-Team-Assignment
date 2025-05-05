import unittest
from datetime import datetime
from class_transaction import Transaction

class TestTransaction(unittest.TestCase):
    
    def setUp(self):
        """Set up test data before each test"""
        self.transactions = []
        self.transaction1 = Transaction("Account1", "Account2", 100.00)
        self.transaction2 = Transaction("Account3", "Account4", 200.00)
        
    def test_init(self):
        """Test that Transaction objects are initialized correctly"""
        transaction = Transaction("Source", "Destination", 500.00)
        self.assertEqual(transaction.source, "Source")
        self.assertEqual(transaction.destination, "Destination")
        self.assertEqual(transaction.amount, 500.00)
        self.assertIsNotNone(transaction.date)
        
    def test_add_transaction_success(self):
        """Test adding a valid transaction to the list"""
        try:
            Transaction.add_transaction(self.transactions, self.transaction1)
            self.assertEqual(len(self.transactions), 1)
            self.assertEqual(self.transactions[0], self.transaction1)
        except Exception as e:
            self.fail(f"add_transaction raised {type(e).__name__} unexpectedly!")
            
    def test_add_transaction_invalid_list(self):
        """Test adding a transaction with an invalid list (negative test)"""
        with self.assertRaises(TypeError):
            Transaction.add_transaction("not a list", self.transaction1)
            
    def test_add_transaction_invalid_transaction(self):
        """Test adding an invalid transaction object (negative test)"""
        with self.assertRaises(TypeError):
            Transaction.add_transaction(self.transactions, "not a transaction")
            
    def test_delete_transaction_success(self):
        """Test deleting an existing transaction"""
        # First add a transaction with an ID attribute
        self.transaction1.id = 1
        self.transactions.append(self.transaction1)
        
        try:
            Transaction.delete_transaction(self.transactions, 1)
            self.assertEqual(len(self.transactions), 0)
        except Exception as e:
            self.fail(f"delete_transaction raised {type(e).__name__} unexpectedly!")
            
    def test_delete_transaction_not_found(self):
        """Test deleting a non-existent transaction (negative test)"""
        with self.assertRaises(ValueError):
            Transaction.delete_transaction(self.transactions, 999)
            
    def test_delete_transaction_invalid_list(self):
        """Test deleting with an invalid list (negative test)"""
        with self.assertRaises(TypeError):
            Transaction.delete_transaction("not a list", 1)
            
    def test_delete_transaction_invalid_id(self):
        """Test deleting with an invalid ID type (negative test)"""
        with self.assertRaises(TypeError):
            Transaction.delete_transaction(self.transactions, "not an integer")
            
    def test_view_transactions_with_data(self):
        """Test viewing transactions with data in the list"""
        self.transactions.append(self.transaction1)
        self.transactions.append(self.transaction2)
        # Since view_transactions just prints to console, we're mainly testing that it doesn't raise exceptions
        try:
            Transaction.view_transactions(self.transactions)
            # Success means no exception was raised
            self.assertEqual(len(self.transactions), 2)
        except Exception as e:
            self.fail(f"view_transactions raised {type(e).__name__} unexpectedly!")
            
    def test_view_transactions_empty(self):
        """Test viewing transactions with an empty list"""
        try:
            Transaction.view_transactions(self.transactions)
            self.assertEqual(len(self.transactions), 0)
        except Exception as e:
            self.fail(f"view_transactions raised {type(e).__name__} unexpectedly!")
            
    def test_view_transactions_invalid_list(self):
        """Test viewing with an invalid list (negative test)"""
        with self.assertRaises(TypeError):
            Transaction.view_transactions("not a list")

if __name__ == '__main__':
    unittest.main()
