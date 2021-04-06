import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def test_get_full_name(self):

        # create a test employee
        # not interested in testing salary or shifts
        # we write a test case that COMPARES the result of
        # the get_full_name method with the EXPECTED result.
        # to test run python3 -m unittest 

        e = Employee("Vera", "Schmidt", 0, None)
        self.assertEqual(e.get_full_name(), "Vera Schmidt")

# Imagine in employee.py there are two spaces between
# first name and last name - hard to see to the eye, 
# this is why testing with one space above is good. 
# The unittest will spot this error.

    def test_raise_salary(self):
        e = Employee("", "", 2000, None)
        e.raise_salary(100)
        self.assertEqual(e.salary, 2100)

# Note: Don't change the test, change the code
# Note: Don't change the expected result, go check the code