#Basic salary of employee
bs=float(input("Enter Basic Salary "))
da=0.5*bs
hra=0.2*bs
gs=bs+da+hra
print("Given Basic Salary is: ",bs)
print("Value of Dearness Allowance is: ",da)
print("Value of House Rent Allowance is:  ",hra)
print("Value of Gross Salary is: ",gs)


#Use the statics module to calculate mean, median,mode of a list of numbers.
import statistics
n=[10,20,30,30,40,90]
mean=statistics.mean(n)
median=statistics.median(n)
mode=statistics.mode(n)
print(mean)
print(median)
print(mode)


#Program to store students record
def add_record():
    try:
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))

        with open("students.txt", "a") as file:
            file.write(f"{roll},{name},{marks}\n")

        print("Record added successfully!\n")

    except ValueError:
        print("Invalid input! Marks should be a number.\n")

#Function to display all records
def display_records():
    try:
        with open("students.txt", "r") as file:
            data=file.readlines()

            if not data:
                print("No records found.\n")
                return
            
            print("\nStudent Records:")
            for line in data:
                roll, name, marks=line.strip().split(",")
                print(f"Roll No: {roll}, Name: {name}, Marks: {marks}")
            print()

    except FileNotFoundError:
        print("File not found!\n")

#Function to search by Roll Number
def search_record():
    try:
        search_roll = input("Enter Roll No to search: ")
        found = False

        with open("students.txt", "r") as file:
            for line in file:
                roll, name, marks=line.strip().split(",")

                if roll==search_roll:
                  print(f"\nRecord Found: Roll No: {roll}, Name:{name}, Marks:{marks}\n")   
                  found=True
                  break

        if not found:
            print("Record not found.\n")

    except FileNotFoundError:
        print("File not found!\n")

#Main menu:
while True:
    print("STUDENT RECORD SYSTEM")
    print("1. Add Record")
    print("2. Display All Records")
    print("3. Search by roll number")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        add_record()
    elif choice == "2":
        display_records()
    elif choice == "3":
        search_record()
    elif choice == "4":
        print("Exiting Program...")
        break
    else:
        print("Invalid choice!")

#Function to display all records
def display_records():
    try:
        with open("students.txt", "r") as file:
            data=file.readlines()

            if not data:
                print("No records found.\n")
                return
            
            print("\nStudent Records:")
            for line in data:
                roll, name, marks=line.strip().split(",")
                print(f"Roll No: {roll}, Name: {name}, Marks: {marks}")
            print()

    except FileNotFoundError:
        print("File not found!\n")

#Function to search by Roll Number
def search_record():
    try:
        search_roll = input("Enter Roll No to search: ")
        found = False

        with open("students.txt", "r") as file:
            for line in file:
                roll, name, marks=line.strip().split(",")

                if roll==search_roll:
                  print(f"\nRecord Found: Roll No: {roll}, Name:{name}, Marks:{marks}\n")   
                  found=True
                  break

        if not found:
            print("Record not found.\n")

    except FileNotFoundError:
        print("File not found!\n")


#Implement appropriate exception handling for invalid or missing files.
filename = "data.txt"
try:
    f=open(filename, 'r')
    content = f.read()
    print(content)
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except IOError:
    print(f"Error: Could not read file '{filename}' (invalid file).")
f.close() 

#Define a class employee
class employee:
    def __init__(self):
        self.emp_id=int(input("Enter ID"))
        self.name=input("Enter name of the employee")
        self.salary=int(input("Enter salary"))
    def display(self):
        print(self.emp_id)
        print(self.name)
        print(self.salary)
    def __del__(self):
        print("DELETED")
e=employee()
e.display()
del e


#set operations:
set1 = {1, 2, 3, 4, 5}  
set2 = {4, 5, 6, 7, 8}  
print("Set 1:", set1)  
print("Set 2:", set2)  
print("\nUnion:", set1.union(set2))  
print("Intersection:", set1.intersection(set2))  
print("Difference (Set1 - Set2):", set1.difference(set2))  
print("Symmetric Difference:", set1.symmetric_difference(set2))  
print("\nIs Set1 a subset of Set2?", set1.issubset(set2))  
print("Is Set1 a superset of Set2?", set1.issuperset(set2))  
# Removing duplicate elements from a list using set  
list_with_duplicates = [1, 2, 3, 2, 4, 5, 1, 6]  
unique_list = list(set(list_with_duplicates))  
print("\nList after removing duplicates:", unique_list)  
list1 = [10, 20, 30, 40, 50]  
list2 = [30, 40, 60, 70]  
common_elements = list(set(list1).intersection(set(list2)))  
print("Common elements between two lists:", common_elements)  


#Program to find the sum of all even numbers between 1 to 100.
print("Addition of even numbers using for loop")
sum=0
i=1
for num in range(1,101):
    if num%2==0:
        sum=sum+i
        i=i+1
print(sum)   


#Write a program to reverse a given number
print("reverse of number")
n=int(input("Enter number to be reversed: "))
rev=0
while n>0:
    dig=n%10
    rev=rev*10+dig
    n=n//10
    print("result",rev)


#Matrix operations:
# Defining two matrices  
A = [ [1, 2], [3, 4]]  
B = [ [5, 6],   [7, 8]]  
print("Matrix A:", A)  
print("Matrix B:", B)  
add = [  [A[i][j] + B[i][j] for j in range(len(A[0]))]  
for i in range(len(A))]  
print("\nAddition of A and B:", add)  
sub = [  
[A[i][j] - B[i][j] for j in range(len(A[0]))]  
for i in range(len(A))  
]  
print("Subtraction of A and B:", sub)  
transpose = [  
[A[j][i] for j in range(len(A))]  
for i in range(len(A[0]))  
]  
print("Transpose of Matrix A:", transpose)  
mul = [ 
A[i][0] * B[0][j] + A[i][1] * B[1][j]  
for j in range(len(B[0]))  
for i in range(len(A))  
]  
print("Multiplication of A and B:", mul)  
if A == transpose:  
    print("\nMatrix A is Symmetric")  
else:  
    print("\nMatrix A is Not Symmetric") 


#Multiplication table from 1 to 10:
for i in range(1, 11):
    print("Multiplication Table of", i)
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
    print()

#String palindrome
string=input("Enter a string: ")
rev=""
for ch in string:
    rev=ch+rev
if string==rev:
    print("palindrome")
else:
    print("not palindrome")     
#Type 2:      
text=input("Enter string")
if text==text[ : :-1]:
    print("P")
else:
    print("Not P")
    

#List operations:
numbers = [12, 25, 7, 18, 25, 7, 40]  
print("Original List:", numbers)  
numbers.append(30)  
print("After Adding 30:", numbers)  
numbers.remove(25)  
print("After Removing 25:", numbers)  
numbers[2] = 15  
print("After Modifying index 2:", numbers)  
numbers.sort()  
print("Sorted List:", numbers)  
print("Maximum Element:", max(numbers))  
print("Minimum Element:", min(numbers))  
print("Sum of Elements:", sum(numbers))  
unique_list = list(set(numbers))  
print("List after Removing Duplicates:", unique_list)  
sub_list = numbers[1:5]  
print("Sub-list using Slicing:", sub_list)  



#Program to check if a given matrix is symmetric
'''import numpy as np

def is_symmetric(matrix):
    # np.array_equal checks if all elements in matrix match its transpose (matrix.T)
    return np.array_equal(matrix, matrix.T)
# Example Usage:
mat = np.array([
    [1, 2, 3],
    [2, 1, 4],
    [3, 4, 1]
])

print(is_symmetric(mat)) '''
#Type 2
def is_symmetric(matrix):
    rows = len(matrix)
    # A symmetric matrix must be square
    if rows == 0 or rows != len(matrix[0]):
        return False
        
    # Check elements: only need to check one half (above or below diagonal)
    for i in range(rows):
        for j in range(i + 1, rows):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

# Example Usage
symmetric_matrix = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

non_symmetric_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(f"Matrix 1 is symmetric: {is_symmetric(symmetric_matrix)}")
print(f"Matrix 2 is symmetric: {is_symmetric(non_symmetric_matrix)}")



#Conversion of Temperature from Celsius to Fahrenheit Using List Comprehension 
celsius = [0, 10, 20, 30, 40]  
print("Temperatures in Celsius:", celsius)  
fahrenheit = [(temp * 9/5) + 32 for temp in celsius]  
print("Temperatures in Fahrenheit:", fahrenheit) 


#Implementation of Dictionary Operations and Word Frequency Count Using Python 
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


#Write a fubction to calculate the factorial of a number using recursion
def fact(n):
    if(n==1 or n==0):
        return 1
    return fact(n-1)*n

print(fact(5))
print(fact(6))

 #Class shape
import math
class Shape:
    def area(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
my_circle = Circle(5)
my_rectangle = Rectangle(4, 6)

shapes = [my_circle, my_rectangle]

for shape in shapes:
    print(f"{type(shape).__name__} Area: {shape.area():.2f}")




#Write a python program to creat a file named example.txt
f=open("example.txt","w")
f.write("I am a CSE student studying in DPGU a first year student.")
f.close()
f=open("example.txt","r")
print(f.read())
f.close()
f=open("example.txt","a")
f.append("Also studying Python")
f.close()
f=open("example.txt","r")
print(f.read())



#program to filter even numbers from a list using filter and a lambda function.
l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
e=list(filter((lambda n:n%2==0),l))
print(e)


#Use reduce to compute the sum of elements in a list
from functools import reduce
l1=[5,8,9,5]
result=reduce(lambda x,y:x+y,l1)
print(result)


#Creat  a class person with atributes like name and age
class Person: 
    def __init__(self, name, age): 
        self.name = name   
        self.age = age     
 
    def display_person(self):
        print(f"Name: {self.name}, Age: {self.age}") 
 
class Employee(Person): 
    def __init__(self, name, age, emp_id, department): 
         
        super().__init__(name, age) 
        self.emp_id = emp_id           
        self.department = department   
 
    def display_employee(self): 
        """Method to display employee details, including inherited ones.""" 
        print(f"ID: {self.emp_id}, Dept: {self.department}") 
 
class Manager(Employee): 
    def __init__(self, name, age, emp_id, department, team_size): 
        super().__init__(name, age, emp_id, department) 
        self.team_size = team_size   
 
    def display_manager(self): 
        """Method to display manager details, including all inherited attributes.""" 
        print("--- Manager Details ---") 
        self.display_person()     
        self.display_employee()    
        print(f"Team Size: {self.team_size}") 
 
if __name__ == "__main__": 
    mgr = Manager("Alice", 40, "M001", "IT", 15) 
    mgr.display_manager()  
    print(f"\nAccessing individual attributes: {mgr.name} manages {mgr.team_size}people.")


#Python Built-in math module
import math
n=2
s=math.sqrt(n)
print(s)
w=30
r=math.radians(w)
s=math.sin(r)
c=math.cos(r)
t=math.tan(r)
print(s)
print(c)
print(t)

#class bankaccount
class BankAccount:
    def __init__(self):
        self.__balance = int(input("Enter the balance:"))

    def deposit(self):
        amount=int(input("Enter amount to be deposit:"))
        self.__balance=self.__balance+amount

    def withdraw(self):
        amount_w=int(input("Enter the amount to be withdraw:"))
        if amount_w > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance= self.__balance-amount_w

    def checkBalance(self):
        print("Balance:", self.__balance)

a=BankAccount()
a.deposit()
a.withdraw()
a.checkBalance()


#Use the random module to generate:
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



#Write a python program to create a CSV file data.csv with fields: ID,Name and Age
#CSV file stands for -comma saperated values
import csv
f=open("D:\Python\File_handling.py\data.csv","w",newline="")  #the newline="" will remove the extra line from CSV module.
writer=csv.writer(f)                            #To Insert 5 records into the file.
writer.writerow(["ID","Name","Age"])
writer.writerow([1,"ABC",30])
writer.writerow([2,"XYZ",28])
writer.writerow([3,"PQR",25])
writer.writerow([4,"IGF",23])
writer.writerow([5,"MNO",22])
f.close()

f=open("D:\Python\File_handling.py\data.csv","r")     
 #To Read and display the contents of the CSV file.
reader=csv.reader(f)
for row in reader:
    print(row)
f.close()

search_id=input("Enter ID to be searched:")               
 #To Search and display a specific record by ID.
f=open("D:\Python\File_handling.py\data.csv","r")
reader=csv.reader(f)
next(reader)
found=False
for i in reader:
    if i[0]==search_id:
        print("Found",i)
        found=True
        break
if not found:
    print("Not found")

Name=input("Enter Name to be searched:")               


#Use datetime module
from datetime import datetime
current_datetime = datetime.now()
print("Current Date and Time:", current_datetime)
date1 = datetime(2025, 1, 1)
date2 = datetime(2026, 6, 20)
difference = date2 - date1
print("Difference between dates:", difference)



#Program to split the sentance in the file called story.txt.
f=open("D:\Python\File_handling.py\story.txt","w")   
f.write("Welcome to CTP lab or python lab")              #To write the data in the file story.txt file
f.close()

f=open("D:\Python\File_handling.py\story.txt","r")
data=f.read()
print(data)             
f.close() 

words=data.split()            
print(words)     

dict={}                        
for i in words:
    if i in dict:
        dict[i]=dict[i]+1
    else:
        dict[i]=1
print(dict)
sorted_words=sorted(dict.items(),key=lambda x:x[1],reverse=True)
print(sorted_words)

#Implementation of Tuple Operations Using Indexing and Built-in Methods 
my_tuple = (10, 20, "Python", 20, 3.5)  
print("Original Tuple:", my_tuple)  
print("Element at index 2:", my_tuple[2])  
print("Index of element 20:", my_tuple.index(20))  
print("Count of element 20:", my_tuple.count(20))  
temp_list = list(my_tuple)  
temp_list.append("Programming")  
temp_list[0] = 15  
modified_tuple = tuple(temp_list)  
print("Modified Tuple:", modified_tuple)

#To copy the data from source.txt file to destination.txt file
try:                                
    f=open("D:\Python\File_handling.py\source.txt","r")           #Create a file named source.txt and add some data to it and then make a copy in the destination.txt file
    data=f.read()
    f.close()
    d=open("D:\Python\File_handling.py\destination.txt","w")
    d.write(data)
    d.close()
    print("Contain copied sucessfully")
except:
    print("file not exist")
      
#Use the OS module to:
import os

# a. Get the current working directory
cwd = os.getcwd()
print("Current Working Directory:", cwd)

# b. List all files in a directory
print("\nFiles in the directory:")
files = os.listdir(cwd)
for file in files:
    print(file)

# c. Create a new directory
new_dir = "my_new_folder"
if not os.path.exists(new_dir):
    os.mkdir(new_dir)
    print("\nDirectory created:", new_dir)
else:
    print("\nDirectory already exists:", new_dir)

#Define a class student with different attributes
class student:
    def __init__(self):
        self.name=input("Enter name:")
        self.rollno=int(input("Enter roll no.:"))
        self.marks=input("Enter marks:")
    def display(self):
        print(self.name)
        print(self.rollno)
        print(self.marks)
n=int(input("Enter number of students:"))
for i in range(n):
    s=student()
s.display


#Creat a custom module named math_utils with functions for ....
# math_utils.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

#Create a function that takes a list as input and returns the largest and smallest elements.
def find_max_min(numbers):
    largest = max(numbers)
    smallest = min(numbers)
    return largest, smallest
nums = [10, 5, 25, 3, 18]
max_val, min_val = find_max_min(nums)

print("List:", nums)
print("Largest element:", max_val)
print("Smallest element:", min_val)


#Write a function to check wether a number is prime using function.
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
print(is_prime(2))
print(is_prime(6))


#Use lambda function to calculate the square of the number
num=int(input("Enter a number"))
sq=lambda num:num**2
print(sq(num))

#Marke obtained by a student in five different subject is the input, Python program to calculate avg marks of the student.
print("Average Marks of Student-")
s1=int(input("Enter marks of CTP: "))
s2=int(input("Enter marks of PC: "))
s3=int(input("Enter marks of DM: "))
s4=int(input("Enter marks of DLDM: "))
s5=int(input("Enter marks of PBL: "))
total=s1+s2+s3+s4+s5
avg=total/5
print("Aggregate Marks of the student are: ",total)
print("Percentage= ",avg)