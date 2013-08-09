import sqlite3 as db

conn = db.connect('C:\\sqlite\\test.db')
cursor = conn.cursor()

#cursor.execute(".databases")
#data = cursor.fetchall()
#print len(data)
#cursor.execute("sqlite3.exe senators.db")
#cursor.execute(".databases")
#data = cursor.fetchall()
#print len(data)

cursor.execute("drop table if exists films")
cursor.execute("create table films(title text, year text, director text)")
cursor.execute('insert into films values("Annie Hall", "1977", "Woody Allen")')
cursor.execute('insert into films values("The Godfather", "1972", "Francis Ford Coppola")')
conn.row_factory = db.Row
cursor.execute("select * from films")
rows = cursor.fetchall()
for row in rows:
    print("\n",(row[0], row[1], row[2]),end='')
    
cursor.execute("delete from films where title=='Annie Hall'")
cursor.execute("select * from films")
rows = cursor.fetchall()
for row in rows:
    print("\n",(row[0], row[1], row[2]),end='')

conn.close()
#cursor = conn.cursor()
#cursor.execute("create table films(title text, year text, director text)")
