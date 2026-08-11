import random

# a. Generate a random integer between two numbers
rand_int = random.randint(1, 10)
print("Random Integer between 1 and 10:", rand_int)

# b. Generate a random floating-point number
rand_float = random.random()
print("Random Floating-point number (0 to 1):", rand_float)

# c. Select a random element from a list
my_list = ['apple', 'banana', 'cherry', 'mango']
rand_element = random.choice(my_list)
print("Random element from list:", rand_element)