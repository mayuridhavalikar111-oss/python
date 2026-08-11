                                                                            #FUNCTION
#Printing sum of two numbers using function:
def sum(a,b):
    sum=a+b
    print(sum)

sum(2,3)
sum(10,11)
sum(3,4)

#Printing product of two numbers using function:
def cal_product(n1,n2):
   mul=n1*n2
   print(mul)

cal_product(2,4)
cal_product(9,10)

#Average of 3 numbers using function:
def avg(a,b,c):
    avg=(a+b+c)/3
    print(avg)

avg(4,6,8)
avg(1,10,35)
avg(3,4,5)
avg(89,90,98)

#Write a function to print the length of a list.
list1=[1,2,3,4,5,6,7,8]
list2=[11,12,13,14,151]

def print_len(list):
    print(len(list))

print_len(list1)
print_len(list2)

#Write a function to print the elements of a list in a single line.
def print_list(list):
    for i in list:
        print(i,end="")

print_list(list1)
print_list(list2)

#Write a function to find factorial of n.
'''#Regular method:
n=5
for i in range(1,n+1):
    fact=1
    fact=fact* i
print(fact)'''

#Using function:
def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact* i
    print(fact)

fact(8)
fact(5)

#Write a function to convert USD to INR
def converter(usd_val):
    inr_val=usd_val*83
    print(usd_val,"USD=",inr_val,"INR")

converter(1)
converter(100)

#Write a function to check wether a number is even or odd:
def even_odd(n):
    if n%2==0:
        print("EVEN")
    else:
        print("ODD")

even_odd(3)
even_odd(8)


                                                                      #RECURSION
#Recursion function
def show(n):
    if(n==0):     #Basecase: is a condition on which our program knows where to return
        return
    print(n)
    show(n-1)
    print("END")

show(5)

#Factorial using recursion:
def fact(n):
    if(n==1 or n==0):
        return 1
    return fact(n-1)*n

print(fact(5))
print(fact(6))

#Write a recursion function to calculate the sum of first n natural numbers.
def cal_sum(n):
    if(n==0):
        return 0
    print(n)
    return cal_sum(n-1) +n

sum=cal_sum(5)
print(sum)

#Write a recursive function to print all elements in a list.
def print_list(list,index=0):
    if(index==len(list)):
        return
    print(list[index])
    print_list(list,index+1)

l=["a","b","c"]
print_list(l)