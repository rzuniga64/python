import sqlite3 as db

# Purpose:  To create and then read a database of information about Texas senators
#           from a dictionary
# Input:    the dictionary
# Output:   a dictionary of senators and their corresponding state
#           and a dictionary of state and their corresponding senators.


def create_dictionaries():
    table_data = {
        'senators': (
        ("Alabama", "Richard", " ", "Shelby", "R", "1987", "2017"),
        ("Alabama", "Jeff", " ", "Sessions", "R", "1997", "2015"),
        ("Alaska", "Lisa", " ", 'Murkowski', "R", "2002", "2017"),
        ("Alaska", "Mark", " ", "Begich", "D", "2009", "2015"),
        ("Arizona", "John", " ", "McCain", "R", "1987", "2017"),
        ("Arizona", "Jeff", " ", "Flake", "R", "2013", "2019"),
        ("Arkansas", "Mark", " ", "Pryor", "D", "2003", "2015"),
        ("Arkansas", "John", " ", "Boozman", "R", "2011", "2017"),
        ("California", "Dianne", " ", "Feinstein", "D", "1992", "2019"),
        ("California", "Barbara", " ", "Boxer", "D", "1993", "2017"),
        ("Colorado", "Mark", " ", "Udall", "D", "2009", "2015"),
        ("Colorado", "Michael", "F.", "Bennet", "D", "2009", "2017"),
        ("Connecticut", "Richard", " ", "Blumenthal", "D", "2011", "2017"),
        ("Connecticut", "Chris", " ", "Murphy", "D", "2013", "2019"),
        ("Delaware", "Tom", " ", "Carper", "D", "2001", "2019"),
        ("Delaware", "Chris", " ", "Coons", "D", "2010", "2015"),
        ("Florida", "Bill", " ", "Nelson", "D", "2001", "2019"),
        ("Florida", "Marco", " ", "Rubio", "R", "2011", "2017"),
        ("Georgia", "Saxby", " ", "Chambliss", "R", "2003", "2015"),
        ("Georgia", "Johnny", " ", "Isakson", "R", "2005", "2017"),
        ("Hawaii", "Mazie", " ", "Hirono", "D", "2013", "2019"),
        ("Hawaii", "Brian", " ", "Schatz", "D", "2012", "2014"),
        ("Idaho", "Mike", " ", "Crapo", "R", "1999", "2017"),
        ("Idaho", "James", "E.", "Risch", "R", "2009", "2015"),
        ("Illinois", "Dick", " ", "Durbin", "D", "1997", "2015"),
        ("Illinois", "Mark", " ", "Kirk", "R", "2010", "2017"),
        ("Indiana", "Dan", " ", "Coats", "R", "2011", "2017"),
        ("Indiana", "Joe", " ", "Donnelly", "D", "2013", "2019"),
        ("Iowa", "Chuck", " ", "Grassley", "R", "1981", "2017"),
        ("Iowa", "Tom", " ", "Harkin", "D", "1985", "2015"),
        ("Kansas", "Pat", " ", "Roberts", "R", "1997", "2015"),
        ("Kansas", "Jerry", " ", "Moran", "R", "2011", "2017"),
        ("Kentucky", "Mitch", " ", "McConnell", "R", "1985", "2015"),
        ("Kentucky", "Rand", " ", "Paul", "R", "2011", "2017"),
        ("Louisiana", "Mary", " ", "LLandrieu", "D", "1997", "2015"),
        ("Louisiana", "David", " ", "Vitter", "R", "2005", "2017"),
        ("Maine", "Susan", " ", "Collins", "R", "1997", "2015"),
        ("Maine", "Angus", " ", "King", "I", "2013", "2019"),
        ("Maryland", "Barbara", " ", "Mikulski", "D", "1987", "2017"),
        ("Maryland", "Benjamin", "L.", "Cardin", "D", "2007", "2019"),
        ("Massachusetts", "Elizabeth", " ", "Warren", "D", "2013", "2019"),
        ("Massachusetts", "William", " ", "Cowan", "D", "2013", "2013"),
        ("Michigan", "Carl", " ", "Levin", "D", "1979", "2015"),
        ("Michigan", "Debbie", " ", "Stabenow", "D", "2001", "2019"),
        ("Minnesota", "Amy", " ", "Klobuchar", "D", "2007", "2019"),
        ("Minnesota", "Al", " ", "Franken", "D", "2009", "2015"),
        ("Mississippi", "Thad", " ", "Cochran", "R", "1979", "2015"),
        ("Mississippi", "Roger", " ", "Wicker", "R", "2007", "2019"),
        ("Missouri", "Claire", " ", "McCaskill", "D", "2007", "2019"),
        ("Missouri", "Roy", " ", "Blunt", "R", "2011", "2017"),
        ("Montana", "Max", " ", "Baucus", "D", "1979", "2015"),
        ("Montana", "Jon", " ", "Tester", "D", "2007", "2019"),
        ("Nebraska", "Mike", " ", "Ohanns", "R", "2009", "2015"),
        ("Nebraska", "Deb", " ", "Fischer", "R", "2013", "2019"),
        ("Nevada ", "Harry", " ", "Reid", "D", "1987", "2017"),
        ("Nevada", "Dean", " ", "Heller", "R", "2011", "2019"),
        ("New Hampshire", " ", "Jeanne", "Shaheen", "D", "2009", "2015"),
        ("New Hampshire", " ", "Kelly", "Ayotte", "R", "2011", "2017"),
        ("New Jersey", "Frank", "R.", "Lautenberg", "D", "2003", "2015"),
        ("New Jersey", "Robert", " ", "Menendez", "D", "2006", "2019"),
        ("New Mexico", "Tom", " ", "Udal", "D", "2009", "2015"),
        ("New Mexico", "Martin", " ", "Heinrich", "D", "2013", "2019"),
        ("New York", "Charles", "E.", "Schume", "D", "1999", "2017"),
        ("New York", "Kirsten", " ", "Gillibrand", "D", "2009", "2019"),
        ("North Carolina", "Richard", " ", "Burr", "R", "2005", "2017"),
        ("North Carolina", "Kay", " ", "Hagan", "D", "2009", "2015"),
        ("North Dakota", "John", " ", "Hoeven", "R", "2011", "2017"),
        ("North Dakota", "Heidi", " ", "Heitkamp", "D", "2013", "2019"),
        ("Ohio", "Sherrod", " ", "Brown", "D", "2007", "2019"),
        ("Ohio", "Rob", " ", "Portman", "R", "2011", "2017"),
        ("Oklahoma", "James", "M.", "Inhofe", "R", "1994", "2015"),
        ("Oklahoma", "Tom", " ", "Coburn", "R", "2005", "2017"),
        ("Oregon", "Ron", " ", "Wyden", "D", "1996", "2017"),
        ("Oregon", "Jeff", " ", "Merkley", "D", "2009", "2015"),
        ("Pennsylvania", "Robert", "P.", "Casey", "D", "2007", "2019"),
        ("Pennsylvania", "Pat", " ", "Toomey", "R", "2011", "2017"),
        ("Rhode Island", "Jack", " ", "Reed", "D", "1997", "2015"),
        ("Rhode Island", "Sheldon", " ", "Whitehouse", "D", "2007", "2019"),
        ("South Carolina", "Lindsey", " ", "Graham", "R", "2003", "2015"),
        ("South Carolina", "Tim", " ", "Scott", "R", "2013", "2015"),
        ("South Dakota", "Tim", " ", "Johnson", "D", "1997", "2015"),
        ("South Dakota", "John", " ", "Thune", "R", "2005", "2017"),
        ("Tennessee", "Lamar", " ", "Alexander", "R", "2003", "2015"),
        ("Tennessee", "Bob", " ", "Corker", "R", "2007", "2019"),
        ("Texas", "John", " ", "Cornyn", "R", "2002", "2015"),
        ("Texas", "Ted", " ", "Cruz", "R", "2013", "2019"),
        ("Utah", "Orrin", "G.", "Hatch", "R", "1977", "2019"),
        ("Utah", "Mike", " ", "Lee", "R", "2011", "2017"),
        ("Vermont", "Patrick", " ", "Leahy", "D", "1975", "2017"),
        ("Vermont", "Bernie", " ", "Sander", "I", "2007", "2019"),
        ("Virginia", "Mark", "R.", "Warner", "D", "2009", "2015"),
        ("Virginia", "Tim", " ", "Kaine", "D", "2013", "2019"),
        ("Washington", "Patty", " ", "Murray", "D", "1993", "2017"),
        ("Washington", "Maria", " ", "Cantwel", "D", "2001", "2019"),
        ("West Virginia", "Jay", " ", "Rockefeller", "D", "1985", "2015"),
        ("West Virginia", "Joseph", " ", "Manchin", "D", "2010", "2019"),
        ("Wisconsin", "Ron", " ", "Johnson", "R", "2011", "2017"),
        ("Wisconsin", "Tammy", " ", "Baldwin", "D", "2013", "2019"),
        ("Wyoming", "Mike", " ", "Enzi", "R", "1997", "2015"),
        ("Wyoming", "John", " ", "Barrasso", "R", "2007", "2019")
        )
    }
    
    conn = db.connect('senators.db')
    cursor = conn.cursor()
    cursor.execute("drop table if exists senators")
    cursor.execute("create table senators(state text, lname text, initial text, fname text, party text, termstart text, termend text)")
    for data in table_data['senators']:
        cursor.execute("insert into senators values('%s', '%s', '%s', '%s', '%s', '%s', '%s')"
                       % (data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
    
    states = dict()
    senators = dict()
    
    # The way we want to retrieve rows is so that we can specify 
    # each field using the field name. Think of the row
    # as an array and each field name is an index
    # into an element of that row.
    conn.row_factory = db.Row
    cursor.execute("select * from senators")
    rows = cursor.fetchall()
    for row in rows:
#        print("\n'%s','%s','%s','%s','%s','%s','%s'"%(row[0], row[1], row[2], row[3], row[4], row[5], row[6]),end='')
        state = row[0]
        senator = row[3]
        senators[senator] = state
        if state in states:
            states[state] = states[state] + [senator]
        else:
            states[state] = [senator]    

    conn.close()
    return senators, states


def get_user_input(senators, states):
    """ Purpose:  The getUserInput function gets a validated choice from the user
    Input:    a key to search the states and senators dictionaries
    Output:   state or senator if found and its key """
    key = input("Give the senator's last name or state: ").capitalize()
    
    senator = states.get(key, 'Not found')
    state = senators.get(key, 'Not found')
    if senator == 'Not found' and state == 'Not found':
        print("No senator or state has the name, ", key)
        print("exiting...")
    return key, senator, state


def main():
    """this program use a dictionary to keep a list of senators for each state
    and another dictionary to keep a list of the state of each senator"""

    senators, states = create_dictionaries()
    # Get the user's input
    key, senator, state = get_user_input(senators, states)
    
    while senator != 'Not found' or state != 'Not found':
        if senator != 'Not found':
            print(senator[0] + " and " + senator[1], "are senators from ", key)
        elif state != 'Not found':
            print(key, "is a senator from ", state)
        key, senator, state = get_user_input(senators, states)
    
main()