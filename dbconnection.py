import pyodbc
import datetime
connection = pyodbc.connect(driver='{SQL Server}',
    server='LAGNIGDEV001',
    database='StudentDB',
    user='sa',
    password='P@ssw0rd')
createdon = datetime.datetime.now()
cursor = connection.cursor()

#cursor.execute("INSERT INTO Student(Fullname,DOB,Sex, CreatedOn) VALUES('Hey There', '2016-10-10','Female', '"+ createdon  +"')")
cursor.execute("INSERT INTO Student(Fullname,DOB,Sex, CreatedOn) VALUES(?,?,?,?)",('Hey There', '2016-10-10','Female',  createdon))
connection.commit()
