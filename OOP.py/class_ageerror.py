class AgeError(Exception):
    pass

try:
    age = int(input("Enter your age: "))
    
    if age < 18:
        raise AgeError("Not eligible for driving licence")
    else:
        print("Eligible for driving licence")

except AgeError as e:
    print(e)
except ValueError:
    print("Invalid input! Please enter a numeric value for age.")