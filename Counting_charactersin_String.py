char= "programming"

char_counts = {}

if char in char_counts:
        char_counts[char] += 1
else:
        char_counts[char] = 1
count_duplicates = 0
for char in char_counts:
    if char_counts[char] > 1:
        count_duplicates += 1
print(char)
