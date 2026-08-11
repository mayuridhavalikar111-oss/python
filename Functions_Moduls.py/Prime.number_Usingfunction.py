def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
print(is_prime(2))
print(is_prime(6))

'''# Taking input from user
number = int(input("Enter a number: "))

# Checking prime
if is_prime(number):
    print(number, "is a Prime number")
else:
    print(number, "is not a Prime number")'''

