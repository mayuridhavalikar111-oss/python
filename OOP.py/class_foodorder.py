from abc import ABC, abstractmethod
class FoodOrder:
    def bill(self):
        pass
class PizzaOrder(FoodOrder):
    def bill(self):
        print("Pizza Bill: 500")
class BurgerOrder(FoodOrder):
    def bill(self):
        print("Burger Bill: 200")
p = PizzaOrder()
b = BurgerOrder()
p.bill()
b.bill()