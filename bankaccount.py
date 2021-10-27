from random import randint 
bank_accounts[]

class BankAccount():
    def __init__:(self, full_name, account_number, balance =0):
    self.full_name = full_name
    self.accounts_number = account_number 
    self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount Deposited: ${amount}")
        print(f"New Balance: ${self.balance}\n")
