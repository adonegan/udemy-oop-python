from employee import Manager
from employee import Attendant
from employee import Cook
from employee import Mechanic

employees = [
    Manager("Vera", "Schmidt", 2000),
    Attendant("Chuck", "Norris", 1800),
    Attendant("Samantha", "Carrington", 1800),
    Cook("Roberto", "Jacketti", 2100),
    Mechanic("Joe", "Rama", 2000),
    Mechanic("Dave", "Dreilig", 2200),
    Mechanic("Tina", "River", 2300),
    Mechanic("Chuck", "Rainey", 1800)
]

def print_accounting_report():
    print("Accounting")
    print("==========")
    for e in employees:
        print(f"{e.get_full_name()}, ${e.salary}")

def print_staffing_report():
    print("Staffing")
    print("========")
    for e in employees:
        print(f"{e.get_full_name()}, {e.job_title}")

# call function
print_accounting_report()
print() # empty line
print_staffing_report() 

