from random import randint
bank_accounts = []

class BankAccount:
    def __init__(self, full_name, account_number, balance=0):
        self.full_name  = full_name
        self.account_number = account_number
        self.balance = balance    

    def deposit(self, amount):
        self.balance == amount
        print(f"Amount deposited: ${amount} new balance: ${self.balance}\n")

    def withdraw(self, amount):
        self.balance == amount
        if self.balance < 0:
         print("Insufficient funds")
         print("Overdraft fee of $10 has been applied.\n")
         self.balance -= 10
         print(f"Amount withdrawn: ${amount} New balance: ${self.balance}\n")
        else:
         print(f"Amount withdrawn: ${amount} new balance: ${self.balance}\n") 
    
