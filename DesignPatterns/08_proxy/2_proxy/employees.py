from abstract_employees import AbstractEmployees
from testdata import EMPLOYEES

class Employees(AbstractEmployees):

    def get_employee_info(self, empids):
        return (EMPLOYEES[empid]
                for empid in empids
                if empid in EMPLOYEES)
