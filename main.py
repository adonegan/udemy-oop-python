from employee import Manager
from employee import Attendant
from employee import Cook
from employee import Mechanic

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

# REFACTORING
# This means breaking up code into smaller, easier to understand parts / as your code grows, you detect patterns and can break it up to make it easier to understand