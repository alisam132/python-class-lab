import random


class BankAccount:

    def __init__(self, owner, balance = 0.00, account_no = 0, deposit=0.00, withdraw=0.00):
        self.owner = owner
        self.balance = balance
        self.account_no = random.randint(111111111, 999999999)
        self.deposit = deposit
        self.withdraw = withdraw

    def __str__(self):
        return f"{self.account_no} - balance : {self.balance}"


    def withdrawfunction(self, withdraw)
        return new_balance = self.balance - withdraw 


    def depositfunction(self, deposit)
        return new_balance = self.balance + deposit 


new_account = BankAccount('Ali', 1000)

print(new_account)