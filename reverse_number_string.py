print("reverse of number")
n=int(input("Enter number to be reversed: "))
rev=0
while n>0:
    dig=n%10
    rev=rev*10+dig
    n=n//10
    print("result",rev)
  

print("reverse of string")
name= str((input("Enter the name: ")))
n = len(name) - 1
while n>= 0:
    print(name[n], end = '')
    n = n - 1

