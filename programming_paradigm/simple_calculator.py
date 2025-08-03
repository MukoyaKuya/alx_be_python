# simple_calculator.py

class SimpleCalculator:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Deposit amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("Invalid withdraw amount")

    def display_balance(self):
        return f"Current Balance: ${self.balance:.2f}"
