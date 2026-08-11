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


