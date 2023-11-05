from bank_accounts import  *

Dave = Bank_Account(2000,"Dave")
Sara = Bank_Account(1000,"sara")

Dave.getBalance()

Dave.deposit(400)

Dave.withdraw(5000)

Dave.transfer(200,Sara)

balze = SavingdAcct(1000,"Blaze")
balze.getBalance()

balze.deposit(100)
balze.transfer(1000,Sara)