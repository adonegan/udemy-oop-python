class Report:
    def __init__(self, emp_list):
        self._emp_list = emp_list

class AccountingReport(Report):
    def print_accounting_report(self):
        print("Accounting")
        print("==========")
        for e in self._emp_list:
            print(f"{e.get_full_name()}, ${e.salary}")

class StaffingReport(Report):
    def print_staffing_report(self):
        print("Staffing")
        print("========")
        for e in self._emp_list:
            print(f"{e.get_full_name()}, {e .job_title}")

# Create super/parent class to remove duplicate code. This class is abstract and is not supposed to be instantiated. 
