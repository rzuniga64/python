"""
     Purpose: to create and then store  a database of information about
     students that is typed into a GUI interface from the StudentContainer
     class.
     Input: A list that is passed from StudentContainer class to input
     records into the database and a query formatted as a string to retrieve
     information from the database.
"""
import sqlite3


class StudentDB():
    def __init__(self):
        self.conn = sqlite3.connect('student.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("drop table if exists student")
        self.cursor.execute("create table student(fname varchar2(30), lname varchar2(30), street varchar(30),\
                                             city varchar2(20),state varchar2(10), zip integer(5), email varchar2(40),\
                                             phone varchar2(12),school varchar2(20),major varchar2(20))")
        self.cursor.close()
        self.conn.close()

    def run_query(self, query_string):
        self.conn = sqlite3.connect('student.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute(query_string)
        result = self.cursor.fetchall()
        self.cursor.close()
        self.conn.close()
        return result

    def insert_record(self, data):
        self.conn = sqlite3.connect('student.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("""INSERT INTO student(fname, lname, street, city, state, zip, email, phone, school, major)
                            VALUES('%s', '%s', '%s', '%s', '%s', '%d', '%s', '%s', '%s', '%s')"""
                            % (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9])
                            )
        self.conn.commit()
        self.cursor.execute("""SELECT * FROM student WHERE fname=? AND lname=? AND street=? AND city=?
                               AND state=? AND zip=? AND email=? AND phone=? AND school=? AND major=?""",
                            (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9]))
        count = len(self.cursor.fetchall())
        self.cursor.close()
        self.conn.close()
        if count >= 1:
            return True
        return False

if __name__ == '__main__':
    testdb = StudentDB()
    record = ['Raul', 'Zuniga', '1901A Woodland Avenue', 'Austin', 'Tx', int('78741'),
              'rzuniga64@gmail.com', '512-554-2185', 'Austin Community College',
              'Computer Science']
    testdb.insert_record(record)
    students = testdb.run_query('SELECT * FROM student')
    for row in students:
        print(row)