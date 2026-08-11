
import math

# 1. Base Class: Shape
class Shape:
    def area(self):
        """Method to be overridden by derived classes."""
        pass

# 2. Derived Class: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Specific implementation for Circle: πr²"""
        return math.pi * (self.radius ** 2)

# 3. Derived Class: Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Specific implementation for Rectangle: width * height"""
        return self.width * self.height


my_circle = Circle(5)
my_rectangle = Rectangle(4, 6)

shapes = [my_circle, my_rectangle]

for shape in shapes:
    print(f"{type(shape).__name__} Area: {shape.area():.2f}")

class Area:
    def __init__(self):
        self.area=Area
    def square(self):
        self.side=int(input("Enter length of side"))
        self.area=self.side*self.side
        print(self.area)
    def rectangle(self):
        self.len=int(input("Enter length"))
        self.bre=int(input("Enter breadth"))
        self.area=self.len*self.bre
        print(self.area)
a=Area()
a.square()
a.rectangle()

class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
    def display(self):
        print(self.name , self.author)

b1 = Book("A", "X")
b2= Book("B", "Y")
b3 = Book("C", "Z")
b1.display()
b2.display()
b3.display()

class shape:
    def area(self):
        return 0
class square(shape):
    def __init__(self):
        self.s=int(input())
    def area(self):
        self.area=self.s*self.s
        print(self.area)
class rectangle(shape):
    def __init__(self):
        self.l=int(input())
        self.b=int(input())
    def area(self):
        self.area=self.l*self.b
        print(self.area)
s=shape()
sq=square()
sq.area()
r=rectangle()
r.area()
