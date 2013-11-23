import sqlite3
import sys

conn = sqlite3.connect('sample_database')
cursor = conn.cursor()
employee = sys.argv[1]

# Query to find the employee ID.
query = """SELECT e.empid
           FROM user u, employee e
           WHERE username = ?
           AND u.employeeid = e.empid"""

cursor.execute(query, (employee,))
for row in cursor.fetchone():
    if row is not None:
        empid = row

# Now modify the employee
cursor.execute("DELETE from employee WHERE empid = ?", (empid,))
conn.commit()
cursor.close()
conn.close()



