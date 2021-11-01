from random import randint 
bank_accounts = []

class BankAccount():
    def __init__(self, full_name, account_number, balance=0):
        self.full_name = full_name
        self.account_number = account_number 
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount Deposited: ${amount}")
        print(f"New Balance: ${self.balance}\n")

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
         print("Insufficient funds")
         print("Overdraft fee of $10 has been applied.\n")
         self.balance -= 10
         print(f"Amount withdrawn: ${amount} New balance: ${self.balance}\n")
        else:
         print(f"Amount withdrawn: ${amount} new balance: ${self.balance}\n") 

    def get_balance(self):
        print(f"Account balance: ${self.balance}\n")
        return self.balance

    def add_interest(self):
        self.balance += self.balance * 0.00083

    def print_hidden_acc(self):
        new_account = "*" * (len(self.account_number) - 4)
        account_number = list(self.account_number) [-4:]

        for num in account_number:
            new_account += num
        return new_account

    def print_statement(self):
        print(self.full_name)
        print(f"Account No. :{self.print_hidden_acc()}")
        self.get_balance()   

mitchellAccount = BankAccount("Mitchell Trubisky", "03141592")
mitchellAccount.deposit(400000)
mitchellAccount.print_statement()
mitchellAccount.add_interest() 
mitchellAccount.print_statement()
mitchellAccount.withdraw(150)
mitchellAccount.print_statement()