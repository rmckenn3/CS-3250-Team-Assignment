import unittest
from unittest.mock import Mock, patch
from class_user import User

class TestUser(unittest.TestCase):
    
    def setUp(self):
        """Set up test data before each test"""
        self.user = User(
            name="John Doe",
            birthday="1990-01-01",
            ssn="123-45-6789",
            address="123 Main St",
            email="john@example.com",
            phone="555-123-4567"
        )
        
        # Create mock Account objects
        self.account1 = Mock()
        self.account1.account_number = 12345
        self.account1.account_type = "Checking"
        self.account1.balance = 1000.00
        self.account1.get_primary_holder = Mock(return_value="John Doe")
        self.account1.secondary_holders = []
        
        self.account2 = Mock()
        self.account2.account_number = 67890
        self.account2.account_type = "Savings"
        self.account2.balance = 5000.00
        self.account2.get_primary_holder = Mock(return_value="Jane Smith")
        self.account2.secondary_holders = ["John Doe"]
        
        self.account3 = Mock()
        self.account3.account_number = 54321
        self.account3.account_type = "Checking"
        self.account3.balance = 2000.00
        self.account3.get_primary_holder = Mock(return_value="John Doe")
        self.account3.secondary_holders = ["John Doe"]
        
        self.account4 = Mock()
        self.account4.account_number = 98765
        self.account4.account_type = "Savings"
        self.account4.balance = 3000.00
        self.account4.get_primary_holder = Mock(return_value="Jane Smith")
        self.account4.secondary_holders = ["Bob Johnson"]
    
    def test_init(self):
        """Test that User objects are initialized correctly"""
        self.assertEqual(self.user.name, "John Doe")
        self.assertEqual(self.user.birthday, "1990-01-01")
        self.assertEqual(self.user.ssn, "123-45-6789")
        self.assertEqual(self.user.address, "123 Main St")
        self.assertEqual(self.user.email, "john@example.com")
        self.assertEqual(self.user.phone, "555-123-4567")
        self.assertEqual(self.user.accounts, [])
    
    def test_edit_valid_field(self):
        """Test editing valid user information"""
        with patch('builtins.print') as mock_print:
            self.user.edit("name", "Jane Doe")
            self.assertEqual(self.user.name, "Jane Doe")
            mock_print.assert_called_with("name updated successfully.")
            
            self.user.edit("address", "456 Elm St")
            self.assertEqual(self.user.address, "456 Elm St")
            
            self.user.edit("phone", "555-987-6543")
            self.assertEqual(self.user.phone, "555-987-6543")
            
            self.user.edit("email", "jane@example.com")
            self.assertEqual(self.user.email, "jane@example.com")
            
            self.user.edit("birthday", "1992-02-02")
            self.assertEqual(self.user.birthday, "1992-02-02")
    
    def test_edit_invalid_field(self):
        """Test editing an invalid field"""
        with self.assertRaises(ValueError) as context:
            self.user.edit("ssn", "987-65-4321")
        self.assertEqual(str(context.exception), "Invalid variable name: ssn")
    
    def test_add_account_primary_holder(self):
        """Test adding an account as primary holder"""
        with patch('builtins.print') as mock_print:
            self.user.add_account(self.account1, "primary")
            self.assertIn(self.account1, self.user.accounts)
            mock_print.assert_called_with(f"Account {self.account1.account_number} added successfully.")
    
    def test_add_account_secondary_holder(self):
        """Test adding an account as secondary holder"""
        with patch('builtins.print') as mock_print:
            self.user.add_account(self.account2, "secondary")
            self.assertIn(self.account2, self.user.accounts)
            mock_print.assert_called_with(f"Account {self.account2.account_number} added successfully.")
    
    def test_add_account_invalid_ownership_type(self):
        """Test adding an account with invalid ownership type"""
        with patch('builtins.print') as mock_print:
            self.user.add_account(self.account1, "tertiary")
            self.assertNotIn(self.account1, self.user.accounts)
            mock_print.assert_called_with("Error: Ownership type must be 'primary' or 'secondary'")
    
    def test_add_account_duplicate(self):
        """Test adding a duplicate account"""
        # First add the account
        self.user.add_account(self.account1, "primary")
        
        # Try to add it again
        with patch('builtins.print') as mock_print:
            self.user.add_account(self.account1, "primary")
            # Check that it wasn't added twice
            self.assertEqual(self.user.accounts.count(self.account1), 1)
            mock_print.assert_called_with("Error: Account already exists")
    
    def test_add_account_primary_holder_mismatch(self):
        """Test adding an account as primary holder with name mismatch"""
        with patch('builtins.print') as mock_print:
            self.user.add_account(self.account2, "primary")
            self.assertNotIn(self.account2, self.user.accounts)
            mock_print.assert_called_with("Error: Primary account holder must match user name")
    
    def test_add_account_primary_and_secondary(self):
        """Test adding an account where user is both primary and secondary holder"""
        with patch('builtins.print') as mock_print:
            self.user.add_account(self.account3, "primary")
            self.assertNotIn(self.account3, self.user.accounts)
            mock_print.assert_called_with("Error: User cannot be a secondary holder of the account")
    
    def test_add_account_secondary_not_listed(self):
        """Test adding an account as secondary when user is not in secondary holders"""
        with patch('builtins.print') as mock_print:
            self.user.add_account(self.account4, "secondary")
            self.assertNotIn(self.account4, self.user.accounts)
            mock_print.assert_called_with("Error: User must be a secondary holder of the account")
    
    def test_remove_account_existing(self):
        """Test removing an existing account"""
        # First add an account
        self.user.add_account(self.account1, "primary")
        
        # Now remove it
        with patch('builtins.print') as mock_print:
            self.user.remove_account(self.account1.account_number)
            self.assertNotIn(self.account1, self.user.accounts)
            mock_print.assert_called_with(f"Account {self.account1.account_number} removed successfully.")
    
    def test_remove_account_nonexistent(self):
        """Test removing a non-existent account"""
        with self.assertRaises(ValueError) as context:
            self.user.remove_account(99999)
        self.assertEqual(str(context.exception), "Account not found")
    
    def test_display_accounts_with_accounts(self):
        """Test displaying accounts when accounts exist"""
        # Add some accounts
        self.user.add_account(self.account1, "primary")
        self.user.add_account(self.account2, "secondary")
        
        # Test display_accounts
        with patch('builtins.print') as mock_print:
            self.user.display_accounts()
            # Check that print was called at least twice (once for each account)
            self.assertGreaterEqual(mock_print.call_count, 2)
            # Check the format of at least one call
            mock_print.assert_any_call(f"Account Number: {self.account1.account_number}, Type: {self.account1.account_type}, Balance: {self.account1.balance}")
    
    def test_display_accounts_no_accounts(self):
        """Test displaying accounts when no accounts exist"""
        with patch('builtins.print') as mock_print:
            self.user.display_accounts()
            mock_print.assert_called_once_with("No accounts found.")
    
    def test_report_fraud_valid_account(self):
        """Test reporting fraud for a valid account"""
        # Add an account
        self.user.add_account(self.account1, "primary")
        
        # Report fraud
        with patch('builtins.print') as mock_print:
            self.user.report_fraud(self.account1.account_number)
            mock_print.assert_called_with(f"Fraud reported for account {self.account1.account_number}. Please follow up with customer support.")
    
    def test_report_fraud_non_integer(self):
        """Test reporting fraud with non-integer account number"""
        with self.assertRaises(ValueError) as context:
            self.user.report_fraud("ABC")
        self.assertEqual(str(context.exception), "Account number must be an integer.")
    
    def test_report_fraud_account_not_found(self):
        """Test reporting fraud for account not in user's accounts"""
        with self.assertRaises(ValueError) as context:
            self.user.report_fraud(99999)
        self.assertEqual(str(context.exception), "Account not found in user's accounts.")
    
    def test_send_document_valid(self):
        """Test sending a document with valid parameters"""
        with patch('builtins.print') as mock_print:
            self.user.send_document("support@bank.com", "Identification documents")
            mock_print.assert_called_with("Document sent to support@bank.com: Identification documents")
    
    def test_send_document_invalid_recipient(self):
        """Test sending a document with invalid recipient"""
        with self.assertRaises(ValueError) as context:
            self.user.send_document("", "Valid content")
        self.assertEqual(str(context.exception), "Recipient must be a non-empty string.")
    
    def test_send_document_invalid_content(self):
        """Test sending a document with invalid content"""
        with self.assertRaises(ValueError) as context:
            self.user.send_document("valid@example.com", "")
        self.assertEqual(str(context.exception), "Content must be a non-empty string.")

if __name__ == '__main__':
    unittest.main()
