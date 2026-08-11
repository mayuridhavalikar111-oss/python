print("Addition of even numbers using for loop")
sum=0
i=1
for num in range(1,101):
    if num%2==0:
        sum=sum+i
        i=i+1
print(sum)   

print("Addition of even numbers using while loop")
n=int(input("Enter a number"))
sum=0
i=1
while i<=n:
    if n%2==0:
      sum=sum+i
      i=i+1
print(sum)      