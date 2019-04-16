import pyodbc
import datetime
import pandas as pd
from matplotlib import pyplot as plt
connection = pyodbc.connect(driver='{SQL Server}',
    server='LAGNIGDEV001',
    database='StudentDB',
    user='sa',
    password='P@ssw0rd')
createdon = datetime.datetime.now()
cursor = connection.cursor()
try:
    query = "SELECT Fullname,DOB,Sex, CreatedOn FROM Student where DOB is not null"
    #rows = cursor.execute("SELECT Fullname,DOB,Sex, CreatedOn FROM Student")
except:
    print("Error reading records from database")

#for row in rows:
    #print(row.Fullname)

df = pd.read_sql(query, connection)
plt.plot(df.Fullname, df.DOB)
plt.show()
print(df.head())



#connection.commit()
