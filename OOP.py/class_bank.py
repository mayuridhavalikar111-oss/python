"""class bank:
   def __init__(self):
    self.__account_name=input("Enter name of account holder:")
    self.__account_no=int(input("Enter Account number:"))
    self.__balance=int(input("Enter balance:"))
    print("Current balance is:", self. balance)

   def deposit(self):
    amount=int(input("Enter Amount tobe added to the account:"))
    self.balance=self.balance+ amount
    print("Balance after adding amount", amount, " is:", self. balance)

   def withdrawl(self):
    withdrawl_amount=int(input("Enter amount to be withdraw:"))
    self.balance=self.balance-withdrawl_amount
    print("Balance after withdrawl", withdrawl_amount, " is:", self. balance)

   def display(self):
    print(self.balance)

b=bank()
b.deposit()
b.withdrawl()
b.display()"""

class BankAccount:
    def __init__(self):
        self.__balance = int(input("Enter the balance:"))

    def deposit(self):
        amount=int(input("Enter amount to be deposit:"))
        self.__balance=self.__balance+amount

    def withdraw(self):
        amount_w=int(input("Enter the amount to be withdraw:"))
        if amount_w > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance= self.__balance-amount_w

    def checkBalance(self):
        print("Balance:", self.__balance)

a=BankAccount()
a.deposit()
a.withdraw()
a.checkBalance()