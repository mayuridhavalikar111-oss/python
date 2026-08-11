class UPI:
    def pay(self):
        print("Payment done using UPI")

class CreditCard:
    def pay(self):
        print("Payment done using Credit Card")

class DebitCard:
    def pay(self):
        print("Payment done using Debit Card")

for method in (UPI(), CreditCard(), DebitCard()):
    method.pay()
