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

# create instance and call
accounting_report = AccountingReport(employees)
accounting_report.print_accounting_report()

print() # empty line

staffing_report = StaffingReport(employees)
staffing_report.print_staffing_report()