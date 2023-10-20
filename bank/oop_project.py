from  bank_accounts import *

Dave = BankAccount(1000, "Dave")
Sheriff = BankAccount(5000, "Sheriff")

Sheriff.getBalance()
Dave.getBalance()

Sheriff.deposit(250)