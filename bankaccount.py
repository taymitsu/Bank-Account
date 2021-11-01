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

    def withdrawl(self, amount):
        self.balance -= amount 
        if self.balance < 0:
            print("INSUFFICIENT FUNDS")
            print("Overdraft fee of $10 has been applied to your account. \n")
            self.balance -= 10
            print(f"Amount withdrawn: ${self.balance}\n")
        else: 
            print(f"Amount withdrawn: ${amount}")
            print(f"New balance: ${self.balance}")

    def get_balance(self):
        print(f"Account balance: ${self.balance}\n")
        return self.balance

    def add_interst(self):
        self.balance += self.balance * 0.00083

    