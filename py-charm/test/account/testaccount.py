from unittest import TestCase
from atmapp.account import Account
class TestAccount(TestCase):
    def test_getBalance(self):
        self.assertEqual(Account(1,"correct_pin").getBalance("correct_pin"), 0)
    def test_to_get_balance_with_incorrect_pin(self):
        account = Account(1,"correct_pin")
        self.assertRaises(ValueError, account.getBalance,"wrong_pin")
    def test_deposit(self):
        account = Account(1, "correct_pin")
        account.deposit(1,1000)
        self.assertEqual(account.getBalance("correct_pin"), 1000)
    def test_that_negative_amount_cant_be_deposited(self):
        account = Account(1, "correct_pin")
        account.deposit(1,1000)
        self.assertRaises(ValueError, account.deposit, 1, -1000)
        self.assertEqual(account.getBalance("correct_pin"), 1000)

    def test_withdraw(self):
        account = Account(1, "correct_pin")
        account.deposit(1,2000)
        account.withdraw("correct_pin",1000)
        self.assertEqual(account.getBalance("correct_pin"), 1000)
    def test_withdraw_negative(self):
        account = Account(1, "correct_pin")
        account.deposit(1,2000)
        self.assertRaises(ValueError, account.withdraw, "correct_pin",-1000)
        self.assertEqual(account.getBalance("correct_pin"), 2000)

    def test_to_withdraw_money_not_in_balance(self):
        account = Account(1, "correct_pin")
        account.deposit(1,2000)
        self.assertRaises(ValueError, account.withdraw, "correct_pin",10000)
        self.assertEqual(account.getBalance("correct_pin"), 2000)
    def test_to_update_pin(self):
        account = Account(1, "old_pin")
        account.deposit(1,2000)
        account.update_pin("old_pin","new_pin")
        self.assertEqual(account.getBalance("new_pin"), 2000)