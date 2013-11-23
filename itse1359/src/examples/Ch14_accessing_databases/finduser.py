import sqlite3

conn = sqlite3.connect('sample_database')
cursor = conn.cursor()
username = 'bunny'

query = """SELECT u.username, e.firstname, e.lastname, m.firstname, m.lastname, d.name
           FROM user u, employee e, employee m, department d
           WHERE username = ?
           AND u.employeeid = e.empid
           AND e.manager = m.empid
           AND e.dept = d.departmentid"""

cursor.execute(query, (username,))
for row in cursor.fetchall():
    (username, firstname, lastname, mgr_firstname, mgr_lastname, dept) = row
    name = firstname + ' ' + lastname
    manager = mgr_firstname + ' ' + mgr_lastname
    print(username, ':', name, 'managed by', manager, 'in', dept)

cursor.close()
conn.close()