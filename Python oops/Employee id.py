# define a class
class Employee:
    # define an attribute
    employee_id = 0

# create two objects of the Employee class
employee1 = Employee()
employee2 = Employee()

# access attributes using employee1
employee1.employeeID = int(input("Enter employee1 id: "))
print(f"Employee ID1: {employee1.employeeID}")

# access attributes using employee2
employee2.employeeID = int(input("Enter employee1 id: "))
print(f"Employee ID2: {employee2.employeeID}")