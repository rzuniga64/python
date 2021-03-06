import sqlite3
import sys

"""
    When you run this script you need to pass the name of the user
    to update, as well as the neme of the manager.  both names are
    user names from the user table.

    Example: $python updatemgr.py bunny ericfj
"""

conn = sqlite3.connect('sample_database')
cursor = conn.cursor()
newmgr = sys.argv[2]
employee = sys.argv[1]

# Query to find the employee ID.

query = """SELECT e.empid
           FROM user u, employee e
           WHERE username=?
           AND u.employeeid = e.empid"""

cursor.execute(query, (newmgr,))
for row in cursor.fetchone():
    if row is not None:
        mgrid = row

# Note how we use the same query, but with a different name.
cursor.execute(query, (employee,))
for row in cursor.fetchone():
    if row is not None:
        empid = row

# Now modify the employee.
cursor.execute("UPDATE employee SET manager=? where empid=?", (mgrid, empid))
conn.commit()
cursor.close()
conn.close()