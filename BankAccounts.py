class BalanceException(Exception):
    pass
class Bank_Account:
    def __init__(self,initialAmount,accName):
        self.balance = initialAmount
        self.name = accName
        print(f"Account '{self.name}' created"
              f"\nBalance = {self.balance}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = {self.balance}")

    def deposit(self,amount):
        self.balance = self.balance+amount
        print(f"\nDeposit complete")
        self.getBalance()

    def viableTransaction(self,amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry,account '{self.name}' only has a balance of {self.balance}"
            )

    def withdraw(self,amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance-amount
            print("\n withdraw complete")
            self.getBalance()
        except BalanceException as error:
            print(f'\nwithdraw interrupted :{error}')
    def transfer(self,amount,account):
        try:
            print('\n*******\n\nBegining Transfer...')
            self.viableTransaction(amount)
            account.deposit(amount)
            print('\\nTransfer complete! \n\n*****' )
        except BalanceException as error:
            print(f'\nTransfer interupted. {error}')


class IntersetRewardsAcc(Bank_Account):
    def deposit(self,amount):
        self.balance = self.balance + (amount*1.05)
        print("\nDepsoit complete")
        self.getBalance()
class SavingdAcct(IntersetRewardsAcc):
    def __init__(self,initialAmount,accName):
        super().__init__(initialAmount,accName)
        self.fee = 5

    def withdraw(self,amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nwithdraw completed")
            self.getBalance()
        except BalanceException as error:
            print(f'\nwithdraw interuppted:{error}')





