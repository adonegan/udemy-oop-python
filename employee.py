class Employee:
    # abstract base class - no need to import 
    def __init__(self, first_name, last_name, salary):
        self._first_name = first_name
        self._last_name = last_name
        self.salary = salary

    def get_full_name(self):
        return f"{self._first_name} {self._last_name}"

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