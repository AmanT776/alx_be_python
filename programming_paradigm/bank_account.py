class BankAccount:
    def __init__(self,balance=0):
        self.balance = float(balance)
    def deposit(self,amount: float):
         self.balance = self.balance + amount
    def withdraw(self,amount: float):
        if self.balance >= amount:
            self.balance = self.balance-amount
            return True
        else:
            return False
    def display_balance(self):
        print(f"Current Balance: ${self.balance}")
    