from collections import Iterable, Iterator

class Employees(Iterable):
    _employees = {}
    _headcount = 0
    _empid = 0

    def add_employee(self, employee):
        self._headcount += 1
        self._employees[self._headcount] = employee

    def __iter__(self):
        return EmployeesIterator(self._employees, self._headcount)

class EmployeesIterator(Iterator):
    def __init__(self, employees, headcount):
        self._employees = employees
        self._headcount = headcount
        self._empid = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._empid < self._headcount:
            self._empid += 1
            return self._employees[self._empid]
        else:
            raise StopIteration
