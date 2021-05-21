import pyodbc

CONNSTR = \
'DRIVER={SQL Server};SERVER=.\SQLEXPRESS;DATABASE=AdventureWorks2019;UID=user;PWD=password'

def get_employees():
    connection = pyodbc.connect(CONNSTR)
    query = '''
        SELECT DISTINCT TOP 5 FirstName, LastName 
        FROM Person.Person
        ORDER BY LastName, FirstName;
    '''
    cursor = connection.cursor()
    cursor.execute(query)
    for row in cursor:
        print(row.FirstName, row.LastName)
    connection.commit()
    connection.close()

get_employees()
