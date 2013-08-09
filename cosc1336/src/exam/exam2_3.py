def processDocument(filename):
        try:
            document = open(filename)
        except: 
            print("File " + filename + " did not open.")
            document = open("\\\RGC-FP0\\StudentsHome\\3051102\\workspace\\python_workspace\\exam2_3\\src\\113thCongress.txt")
            
        states = dict()
        for line in document:
            line = line.strip()
            congressField = line.split('\t')
            congressman = congressField[2]
            stateabbr = congressField[4]
            state = stateabbr[0:2]
            if state != 'PR' and state != 'GU' and state != 'VI' and state != 'AS' and state != 'DC':
                if state in states: 
                    states[state] = states[state] + [congressman]
                else:
                    states[state] = [congressman]

        document.close()
        
        return states
    
    
def main():
    outfile = open('congressman.txt', 'w')
    states = processDocument("113thCongress.txt")
    total = 0
    for key in states.keys():
        numOfCongressmen = len(states[key])
        outfile.write(key+ ' '  + str(numOfCongressmen) + '\n' )
        total += numOfCongressmen

    outfile.write('\nThe total number of Congressmen is: ' + str(total))
    
main()
