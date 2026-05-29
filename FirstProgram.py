class Account:

    def __init__(self, balance, accNo):
        self.balance = balance
        self.accNo = accNo

    def credit(self, amount):
        self.balance += amount

    def debit(self, amount):
        self.balance -= amount

    def showBalance(self):
        print(self.balance)

acc = Account(1000, 12)
acc.showBalance()

acc.credit(100)

acc.showBalance()

acc.debit(100)

acc.showBalance()