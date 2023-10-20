class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initialAmount, accName):
        self.name = accName
        self.balance = initialAmount
        print(f"\nAccount  '{self.name}' created.\nBalance = ${self.balance:.2f}")
    def getBalance(self):
        print(f"\nAccount  '{self.name}' Balance = ${self.balance:.2f}")
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\n Deposit completed")
        self.getBalance()
    def viableTransaction(self, amount):
        if self.balance > amount:
            return
        else:
            raise BalanceException(f"\nSorry, {self.name} only has a balance of ${self.balance:.2f}")
        
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\n Withdraw complete")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")
        
        