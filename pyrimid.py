"""n=4
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()    
    
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end="")
    print()    
 """   
# Heart pattern using stars
# Simple console heart pattern
n = 6
# Upper part of the heart
for i in range(n//2, n, 2):
    # Print spaces
    print(" " * (n - i - 1), end="")
    # Print stars
    print("*" * (i + 1), end="")
    # Print center spaces
    print(" " * (n - i), end="")
    # Print stars
    print("*" * (i + 1))

# Lower part (inverted triangle)
for i in range(n, 0, -1):
    print(" " * (n - i), end="")
    print("*" * (i * 2 - 1))
