#Employee Attendance System 
class Employee:
    def __init__(self, name):
        self.name = name
        self.attendance = 0

    def markAttendance(self):
        self.attendance += 1

    def display(self):
        print(self.name, "Attendance:", self.attendance)

e1 = Employee("Ravi")
e1.markAttendance()
e1.markAttendance()
e1.display()