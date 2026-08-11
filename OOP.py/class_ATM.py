class atm:
    def __init__(self):
        self.__pin=1234
        self.__balance=5000
    
    def withdraw(self):
        pin=int(input("Enter PIN"))
        if(self.__pin==pin):
            amount=int(input("Enter amount to be withdraw:"))
            if(self.__balance>amount):
                self.__balance=self.__balance-amount
            else:
                print("Low Balance!")
        else:
            print("Invalid PIN!")

    def display(self):
        print("Now the current balance is:",self.__balance)

a=atm()
a.withdraw()
a.display()
