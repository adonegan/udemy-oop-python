class AccountingReport:
    def __init__(self, emp_list):
        self._emp_list = emp_list

    def print_accounting_report(self):
        print("Accounting")
        print("==========")
        for e in self._emp_list:
            print(f"{e.get_full_name()}, ${e.salary}")


class StaffingReport:
    def __init__(self, emp_list):
        self._emp_list = emp_list

    def print_staffing_report(self):
        print("Staffing")
        print("========")
        for e in self._emp_list:
            print(f"{e.get_full_name()}, {e .job_title}")


# Notes: why doesn't just importing from employee.py work? Why is def __init__ and self._emp_list needed for this one?

# Look into 'dependency injection' and 'decoupling'