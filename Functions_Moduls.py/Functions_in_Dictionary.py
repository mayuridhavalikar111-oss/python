'''set={1,4,"J","Hi",3}
r=set.remove("Hi")
print(set)
s=set.discard("J")
print("J")'''


'''students = { "Rahul": 85,"Amit": 90,  "Neha": 78, "Sita": 88}
print("Student Marks:")
for name, marks in students.items():
    print(name, ":", marks)'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)

l=[1,2,3,4,5,6,7,8,9,10,11,12,13]
even_number=[num for num in l if num%2==0]
print(even_number)

student = { "Name": "Mayuri", "Roll No": 28, "Course": "CSE", "Age": 18} 
print("Original Dictionary:") 
print(student) 

# Adding a new key-value pair 
student["Marks"] = 85 
print("\nAfter Adding Marks:") 
print(student) 

# Updating an existing value 
student["Age"] = 20 
print("\nAfter Updating Age:") 
print(student) 
del student["Course"] 
print("\nAfter Deleting Course:") 
print(student) 
print("\nIterating through Dictionary:") 
for key, value in student.items(): 
 print(key, ":", value) 
sentence = "python is easy and python is powerful" 
words = sentence.split() 
word_count = {} 
for word in words: 
 word_count[word] = word_count.get(word, 0) + 1 
 print("\nWord Frequency Count:") 
print(word_count) 
