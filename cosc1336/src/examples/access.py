import pyodbc

def main():
    data = pyodbc.dataSources()
#    connect = pyodbc.connect('DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\\sakila.accdb')
    connect = pyodbc.connect('DSN=MS Access Database;Dbq=C:\\sakila.accdb')    
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM actor")
    rows = cursor.fetchall()
    actors = dict()
    for row in rows:
        lname = row[2].capitalize()
        fname = row[1].capitalize()
        if lname in actors:
            actors[lname] = actors[lname] + [fname]
        else:
            actors[lname] = [fname]
    
    connect.close()

main()