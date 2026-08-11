#Squaring a number using lambda function:
num=int(input("Enter a number"))
sq=lambda num:num**2
print(sq(num))

#program to filter even numbers from a list using filter and a lambda function.
l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
e=list(filter((lambda n:n%2==0),l))
print(e)

#built in function
import math
n=4
s=math.sqrt(n)
print(s)
w=30
r=math.radians(w)
s=math.sin(r)
c=math.cos(r)
t=math.tan(r)
print(s)
print(c)
print(t)

