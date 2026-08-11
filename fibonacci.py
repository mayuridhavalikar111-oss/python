print("FIBONACCI PRINTER")
n=int(input("Enter number of terms: "))
a=0
b=1
counter=0
while counter<n:
    print(a)
    c=a+b
    a=b
    b=c
    counter=counter+1



'''if (n<0):
 print("Error! Enter positive number")
else:
 a=0
 b=1
 for i in range(n):
   print(a)
   temp=a+b
   a=b
   b=temp
'''