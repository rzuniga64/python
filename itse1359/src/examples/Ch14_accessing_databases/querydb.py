import sqlite3

conn = sqlite3.connect('sample_database')
cursor = conn.cursor()
cursor.execute("""select e.firstname, e.lastname, d.name
                  from employee e, department d
                  where e.dept = d.departmentid
                  order by e.lastname desc""")

for row in cursor.fetchall():
    print(row)

cursor.execute("""select * from user""")

print(' ')
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()



