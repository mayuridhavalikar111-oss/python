class Vehicle:
    def __init__(self):
        self.days = int(input("Enter number of day's:"))

class Car(Vehicle):
    def rent(self):
        print("Car Rent:", self.days * 1000)

class Bike(Vehicle):
    def rent(self):
        print("Bike Rent:", self.days * 300)

v=Vehicle()
c=Car()
c.rent()
b=Bike()
b.rent()


class employee:
    def __init__(self, salary):
        self.salary=salary

class manager(employee):
    def bonuse(self):
        print("Bonuse for manager:", self.salary*0.2)

class developer(employee):
    def bonuse(self):
        print("Bonuse for developer is:", self.salary*0.1)

m=manager(8000)
d=developer(7000)
m.bonuse()
d.bonuse()