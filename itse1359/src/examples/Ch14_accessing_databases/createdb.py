#import os
import sqlite3

conn = sqlite3.connect('sample_database')
cursor = conn.cursor()
cursor.execute("drop table if exists employee")
cursor.execute("drop table if exists department")
cursor.execute("drop table if exists user")
cursor.execute("create table employee(empid integer, firstname, varchar, lastname varchar,\
                                      dept integer, manager integer, phone varchar)")
cursor.execute("create table department(departmentid integer, name varchar, manager integer)")
cursor.execute("create table user(userid integer, username varchar, employeeid integer)")

# Populate employee table
cursor.execute("""insert into employee(empid, firstname, lastname, dept, manager, phone)
                values(1, 'Eric', 'Foster-Johnson', 1, 1, '555-5555')""")
cursor.execute("""insert into employee(empid, firstname, lastname, dept, manager, phone)
                values(2, 'Peter', 'Tosh', 2, 3, '555-5554')""")
cursor.execute("""insert into employee(empid, firstname, lastname, dept, manager, phone)
                values(3, 'Bunny', 'Waller', 2, 2, '555-5553')""")

# Populate department table
cursor.execute("""insert into department(departmentid, name, manager)
                values(1, 'development', 1)""")
cursor.execute("""insert into department(departmentid, name, manager)
                values(2, 'qa', 2)""")
cursor.execute("""insert into department(departmentid, name, manager)
                values(3, 'operations', 2)""")
# Create indices

# Populate user table
cursor.execute("""insert into user(userid, username, employeeid)
                values(1, 'ericfj', 1)""")
cursor.execute("""insert into user(userid, username, employeeid)
                values(2, 'tosh', 2)""")
cursor.execute("""insert into user(userid, username, employeeid)
                values(3, 'bunny', 3)""")

cursor.execute("create index empid on employee(empid)")
cursor.execute("create index deptfk on employee(dept)")
cursor.execute("create index mgr on employee(manager)")
cursor.execute("create index deptid on department(departmentid)")
cursor.execute("create index deptmgr on department(manager)")
cursor.execute("create index emplid on user(employeeid)")
cursor.execute("create index userid on user(userid)")
conn.commit()
cursor.close()
conn.close()