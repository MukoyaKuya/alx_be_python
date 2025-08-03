# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def test_deposit(self):
        calc = SimpleCalculator()
        calc.deposit(100)
        self.assertEqual(calc.display_balance(), "Current Balance: $100.00")

    def test_withdraw(self):
        calc = SimpleCalculator()
        calc.deposit(200)
        calc.withdraw(50)
        self.assertEqual(calc.display_balance(), "Current Balance: $150.00")

    def test_display_balance_format(self):
        calc = SimpleCalculator()
        calc.deposit(250)
        self.assertEqual(calc.display_balance(), "Current Balance: $250.00")

if __name__ == "__main__":
    unittest.main()
