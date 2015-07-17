import sqlite3
import sys

conn = sqlite3.connect('sample_database')
cursor = conn.cursor()
employee = sys.argv[1]

"""
    when you run this script you need to pass the user name
    of the person to terminate.  you should see no output
    unless the script raises an error.

    Example: $python finduser.py bunny
             $python terminate.py bunny
             $python finduser.py bunny
"""
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
