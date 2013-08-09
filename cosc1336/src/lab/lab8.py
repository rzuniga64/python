def getDigitsUsedInAddress( stNumber ):
    theCounts = [ 0 ] * 10
    for n in range( len( stNumber ) ):
        digit = stNumber[n]
        digitNo = int( digit )
        theCounts[digitNo] += 1
    return theCounts

def showResults( theCounts ):
    for digit in range( 10 ):
        if theCounts[digit] > 0:
            print( digit, "occurred", theCounts[digit] )

def main():
    # Ask for street number.
    startAddr = int(input("Give me a starting street number: " ))
    endAddr = int(input("Give me a ending "))
    addressString = ""
    for address in range(startAddr, endAddr+1):   
        addressString = addressString + str(address)

    # Count digits used in that street number.
    theCounts =  getDigitsUsedInAddress(addressString)
    # Display digit use counts.
    showResults( theCounts )
    
main()
