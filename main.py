from employee import Manager
from employee import Attendant
from employee import Cook
from employee import Mechanic
from reporting import AccountingReport
from reporting import StaffingReport

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

reports = [
    AccountingReport(employees),
    StaffingReport(employees)
]

for r in reports:
    r.print_report()
    print()

# Using polymorphism to print all reports
# A good way to prevent if/else blocks that lead to fragile code
# Note: different subclasses cause different behaviour