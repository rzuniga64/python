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
# Output:   a list of lists of senators and the average years of service
#           for the Republican and Democratic parties.
def ProcessDocument( filename ):
    try:
        document = open("senators.txt", "r" )
    except:
        print( "File " + filename + " did not open." )
        document = open("senators.txt", "r")

    senators = []
    demTotal = 0
    repTotal = 0
    demTotalYearsOfService = 0
    repTotalYearsOfservice = 0
    
    for line in document:
        line = line.strip()
        senatorFields = line.split("\t")
        theSenator = senatorFields[1].split()
        if "." in theSenator[1]:
            senatorFields = [senatorFields[0], theSenator[0] +" " + theSenator[1], theSenator[2], theSenator[3]]+ senatorFields[2:]    
        else:
            senatorFields = [senatorFields[0], theSenator[0], theSenator[1], theSenator[2]]+ senatorFields[2:]
            
        senatorFields = [senatorFields[0], theSenator[0], theSenator[1], theSenator[2]]+ senatorFields[2:]
        senators.append(senatorFields)
        yearsOfService = 2013 - int(senatorFields[-2])
        if senatorFields[-3] == "(R)":
            repTotal += 1
            repTotalYearsOfservice += yearsOfService
        if senatorFields[-3] == "(D)":   
            demTotal += 1
            demTotalYearsOfService += yearsOfService      
      
    try:
        aveRepYearsOfService = repTotalYearsOfservice/repTotal
        aveDemYearsOfService = demTotalYearsOfService/demTotal
    except ZeroDivisionError:
        print("Division by zero error")
            
    document.close()
    
    return senators, aveRepYearsOfService, aveDemYearsOfService

def main():

    senators, aveRepYearsOfService, aveDemYearsOfService = ProcessDocument("senators.txt")
    print("The average years of service among Republicans is ", format(aveRepYearsOfService, ".2f"), sep="")
    print("The average years of service among Democrats is ", format(aveDemYearsOfService, ".2f"), "\n", sep="")
    for senator in senators:
        yearsOfService = 2013 - int(senator[-2])
        party = senator[-3]
        if (party == "(R)" and yearsOfService > aveRepYearsOfService) or \
           (party == "(D)" and yearsOfService > aveDemYearsOfService):
            print("Senator ", senator[1] + " " +senator[2] + senator[3], " has ", yearsOfService, " years of service.", sep="" )
            
main()
