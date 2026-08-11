class Person:
    def __init__(self, name, age):
        self.name = name  
        self.age = age    

    def display_person(self):
        """Method to display personal details."""
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
    print(f"\nAccessing individual attributes: {mgr.name} manages {mgr.team_size} people.")
