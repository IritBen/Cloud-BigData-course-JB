# Unit tests for bank module
import unittest
from customer_complete import Customer
from bank_complete import Bank


class TestBankingSystem(unittest.TestCase):
    def setUp(self):
        self.bank = Bank("Test Bank", "Test City", 5000)
        self.customer_1 = Customer("Alice", 30, 1000)
        self.customer_2 = Customer("Bob", 25, 500)
        self.bank.register_customer(self.customer_1)
        self.bank.register_customer(self.customer_2)
        # check customers added
        self.assertEqual(len(self.bank.customers), 2)

    def test_deposit(self):
        self.customer_1.deposit(500)
        self.assertEqual(self.customer_1.get_balance(), 1500)
        self.customer_2.deposit(300)
        self.assertEqual(self.customer_2.get_balance(), 800)

    def test_withdraw(self):
        # initiate new bank and customers for withdraw tests
        self.bank_2 = Bank("Test Bank 2", "Test City", 3000)
        self.customer_3 = Customer("Charlie", 40, 1000)
        self.bank_2.register_customer(self.customer_3)
        self.customer_4 = Customer("Diana", 35, 1500)
        self.bank_2.register_customer(self.customer_4)
        self.customer_3.withdraw(200)
        self.assertEqual(self.customer_3.get_balance(), 800)
        self.customer_2.withdraw(600)  # Should print insufficient funds
        self.assertEqual(self.customer_2.get_balance(), 500)  # Balance should remain unchanged


if __name__ == '__main__':
    unittest.main()