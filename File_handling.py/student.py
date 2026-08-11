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