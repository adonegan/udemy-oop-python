# Fragile code
#because if you change a name, you must remember to change the salary

names = ["Vera", "Chuck", "Samantha", "Roberto", "Joe", "Dave", "Tina"]
salaries = [2000, 1800, 1800, 2100, 2000, 2200, 2300]

# count = len(names)
# for c in range(count):
#     print(f"{names[c]}, {salaries[c]}")
# This class below describes an object that has a name and salary
# Once you define a class, you create as many objects as you want

class Employee:
    # class initializer
    def __init__(self, name, salary, job_title):
        self.name = name
        self.salary = salary
        self.job_title = job_title

# e = Employee("Vera", 2000)
# print(f"{e.name}, ${e.salary}")
# Make a list of all your employees

employees = [
    Employee("Vera", 2000, "Manager"),
    Employee("Chuck", 1800, "Station Attendant"),
    Employee("Samantha", 1800, "Station Attendant"),
    Employee("Roberto", 2100, "Cook"),
    Employee("Joe", 2000, "Mechanic"),
    Employee("Dave", 2200, "Mechanic"),
    Employee("Tina", 2300, "Mechanic")
]

for e in employees:
    print(f"{e.name}, ${e.salary}, {e.job_title}")

# Why is this approach better? Instead of two lists, there is one list and it must contain name and salary - it is not possible to have a name without a salary, a salary without a name.

# Note: if you need to modify code in multiple places to make a single change, this is inefficient / bad code.
