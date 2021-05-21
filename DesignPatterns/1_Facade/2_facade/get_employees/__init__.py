PROVIDER = 'concrete_sql_server'

CONNSTR = \
'DRIVER={SQL Server};SERVER=.\SQLEXPRESS;DATABASE=AdventureWorks2019;UID=user;PWD=password'

QUERY = '''
    SELECT DISTINCT TOP 5 FirstName, LastName 
    FROM Person.Person
    ORDER BY LastName, FirstName;
'''