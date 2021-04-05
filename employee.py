class Employee:
    # abstract base class - no need to import 
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