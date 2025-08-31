class Account:
    def __init__(self,balance,account_no):
        self.balance=balance
        self.account_no=account_no

    def credit(self,amout):
        self.balance+=amout
        return self.balance

    def debit(self,amount):
        self.balance-=amount
        return self.balance

ac1 = Account(1200,12345678)

print(f"balance after credit is {ac1.credit(500)}")

print(f"balance after debit is {ac1.debit(1000)}")