# Purpose:  Given a file of senators this program will print the
#           senators given the state and the state if give the senator's
#           last name.
# Input:    An input file called "senators.txt"
# Output:   The names of senators if given the state and the state if given
#           the senator's last name
##############################################################################

# Purpose:  To read a file of information about Texas senators
#           into a list of lists.
# Input:    the filename
# Output:   a dictionary of senators and their corresponding state
#           and a dictionary of state and their corresponding senators.

def ProcessDocument( filename ):
    try:
        document = open(filename )
    except:
        print( "File " + filename + " did not open." )
        document = open("senators.txt", "r")

    senators = dict()
    states = dict()
    
    for line in document:
        line = line.strip()
        senatorFields = line.split("\t")
        theSenator = senatorFields[1].split()
        if "." in theSenator[1]:
            senatorFields = [senatorFields[0], theSenator[0] +" " + theSenator[1], theSenator[2], theSenator[3]]+ senatorFields[2:]    
        else:
            senatorFields = [senatorFields[0], theSenator[0], theSenator[1], theSenator[2]]+ senatorFields[2:]
            
        state = senatorFields[0]
        senator = senatorFields[2]
        senators[senator] = state
        if state in states:
            states[state] += [senator]
        else:
            states[state] = [senator]
            
    document.close()
    
    return senators, states

# Purpose:  The getUserInput function gets a validated choice from the user
# Input:    a key to search the states and senators dictionaries
# Output:   state or senator if found and its key

def getUserInput(senators, states):
    key = input("Give the senator's last name or state: ")
    
    senator = states.get(key, 'Not found')
    state = senators.get(key, 'Not found')
    if senator == 'Not found' and state == 'Not found':
        print("No senator or state has the name, ", key)
        print("exiting...")
    return key, senator, state

# this program use a dictionary to keep a list of senators for each state
# and another dictionary to keep a list of the state of each senator
def main():

    senators, states = ProcessDocument("senators.txt")
    # Get the user's input
    key, senator, state = getUserInput(senators, states)
        
    while senator != 'Not found' or state != 'Not found':
        if senator != 'Not found':
            print(senator[0] + " and " + senator[1], "are senators from ",key )
        elif state != 'Not found':
            print(key, "is a senator from ", state)
        key, senator, state = getUserInput(senators, states)
            
main()