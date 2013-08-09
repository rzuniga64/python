def convertHundreds(hundreds, numeral):
    if hundreds == 1:
        numeral += "C"
    return numeral

def convertTens(tens, numeral):
    if tens == 1:
        numeral += "X"
    elif tens == 2:
        numeral += "XX"
    elif tens == 3:
        numeral += "XXX"
    elif tens == 4:
        numeral += "XL"
    elif tens == 5:
        numeral += "L"
    elif tens == 6:
        numeral += "LX"
    elif tens == 7:
        numeral += "LXX"
    elif tens == 8:
        numeral += "LXXX"
    elif tens == 9:
        numeral += "XC"
    return numeral

def convertUnits(units, numeral):
    if units == 1:
        numeral += "I"
    elif units ==2:
        numeral += "II"
    elif units == 3:
        numeral += "III"
    elif units == 4:
        numeral += "IV"
    elif units == 5:
        numeral += "V"
    elif units == 6:
        numeral += "VI"
    elif units == 7:
        numeral += "VII"
    elif units == 8:
        numeral ++ "VIII"
    elif units == 9:
        numeral += "IX"
    return numeral
    
def main():
    numeral = ""
    number = int(input("Give an integer: "))

    #Extract the hundreds, tens, and units digit from the number.
    hundreds = number // 100
    tens = number %100 // 10
    units = number % 10
    print(hundreds, tens, units)
    numeral = convertHundreds(hundreds, numeral)
    numeral = convertTens(tens, numeral)
    numeral = convertUnits(units, numeral)
    print("the number ", number, \
          " as a Roman numeral is ", numeral, \
       ".",  sep = "")

main()
