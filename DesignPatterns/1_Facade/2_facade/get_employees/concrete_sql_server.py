import pyodbc
from .abstract_facade import AbstractFacade
from . import CONNSTR, QUERY

class GetEmployeesFacade(AbstractFacade):
    def get_employees(self):
        connection = pyodbc.connect(CONNSTR)
        cursor = connection.cursor()
        cursor.execute(QUERY)
        for row in cursor:
            print(row.FirstName, row.LastName)
        connection.commit()
        connection.close()
