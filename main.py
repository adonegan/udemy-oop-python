# Code with subclasses
# Using inheritance to prevent duplicate code

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Mechanic(Employee):
    # class variable
    # use underscore
    job_title = "Mechanic"

class Cook(Employee):
    job_title = "Cook"

class Attendant(Employee):
    job_title = "Station Attendant"

class Manager(Employee):
    job_title = "Manager"

employees = [
    Manager("Vera", 2000),
    Attendant("Chuck", 1800),
    Attendant("Samantha", 1800),
    Cook("Roberto", 2100),
    Mechanic("Joe", 2000),
    Mechanic("Dave", 2200),
    Mechanic("Tina", 2300)
]

for e in employees:
    print(f"{e.name}, ${e.salary}, {e.job_title}")

# no need to write the dunder method in sub / child classes, because they inherit it from super / parent class