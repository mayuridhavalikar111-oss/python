class employee:
      def __init__(self):
        self.emp_id=int(input("Enter ID:"))
        self.name=input("Enter Nane:")
        self.salary=int(input("Enter Salary of enployee:"))
      def display(self):
        print(self.emp_id)
        print(self.name)
        print(self.salary)
      def __del__(self):
        print("DELETED")
e = employee()
e.display()
del e