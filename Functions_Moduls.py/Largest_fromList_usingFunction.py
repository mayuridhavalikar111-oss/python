def find_max_min(numbers):
    largest = max(numbers)
    smallest = min(numbers)
    return largest, smallest

# Example list
nums = [10, 5, 25, 3, 18]

# Function call
max_val, min_val = find_max_min(nums)

print("List:", nums)
print("Largest element:", max_val)
print("Smallest element:", min_val)