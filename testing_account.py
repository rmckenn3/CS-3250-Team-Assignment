import unittest
from class_account import Account
from class_user import User

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.user = User("Alice")
        self.account = Account(self.user, "Checking", balance=1000)

    def test_deposit_valid(self):
        self.account.deposit("Alice", 500)
        self.assertEqual(self.account.balance, 1500)

    def test_deposit_invalid(self):
        with self.assertRaises(ValueError):
            self.account.deposit("Alice", -100)

    def test_withdraw_valid(self):
        self.account.withdraw("Alice", 200)
        self.assertEqual(self.account.balance, 800)

    def test_withdraw_invalid_negative(self):
        with self.assertRaises(ValueError):
            self.account.withdraw("Alice", -50)

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw("Alice", 2000)

    def test_add_secondary_holder(self):
        self.account.add_holder("Bob", "secondary")
        self.assertIn("Bob", self.account.secondary_holders)

    def test_add_primary_when_exists(self):
        with self.assertRaises(ValueError):
            self.account.add_holder("Charlie", "primary")

    def test_remove_secondary_holder(self):
        self.account.add_holder("Bob", "secondary")
        self.account.remove_holder("Bob")
        self.assertNotIn("Bob", self.account.secondary_holders)

    def test_remove_primary_holder_should_fail(self):
        with self.assertRaises(ValueError):
            self.account.remove_holder(self.user)

    def test_close_account_with_balance(self):
        with self.assertRaises(ValueError):
            self.account.close_account()

    def test_close_account_successfully(self):
        self.account.balance = 0
        self.account.close_account()
        self.assertIsNone(self.account.primary_holder)
