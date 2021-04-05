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

def print_accounting_report():
    print("Accounting")
    print("==========")
    for e in employees:
        print(f"{e.name}, ${e.salary}")

def print_staffing_report():
    print("Staffing")
    print("========")
    for e in employees:
        print(f"{e.name}, {e.job_title}")

# call function
print_accounting_report()
print()
print_staffing_report()

