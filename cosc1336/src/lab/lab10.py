# Input: file name containing text to find unique words in
# Output: list of unique words

def ProcessDocument( filename ):
    try:
        document = open("\\\RGC-FP0\\StudentsHome\\3051102\workspace\\python_workspace\\hw7\\src\\senators.txt", "r" )
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
        senatorFields = line.split()
        senators.append(senatorFields)
        yearsOfService = 2013 - int(senatorFields[-2])
        if senatorFields[-3] == "(R)":
            repTotal += 1
            repTotalYearsOfservice += yearsOfService
        if senatorFields[-3] == "(D)":   
            demTotal += 1
            demTotalYearsOfService += yearsOfService
            
    print("The total number of republicans is ", repTotal)
    print("The total number of democrats is ", demTotal)    
    print("The total number of republican years of service is ", format(repTotalYearsOfservice, "d"))
    print("The total number of democrat years of service is ", format(demTotalYearsOfService, "d"))        
            
        #Watch for divide by zero         
    aveRepYearsOfService = repTotalYearsOfservice/repTotal
    aveDemYearsOfService = demTotalYearsOfService/demTotal
        
    document.close()
    
    return senators

def main():

    unique = ProcessDocument("\\\RGC-FP0\\StudentsHome\\3051102\workspace\\python_workspace\\hw7\\src\\senators.txt")
    unique.sort()
    print( unique )

main()
