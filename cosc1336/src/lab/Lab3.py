def CToF(temp):
    outputTemp = temp * 9 / 5 + 32
    return outputTemp, 'F'

def FToC(temp):
    outputTemp = (temp -32) * 5/9
    return outputTemp, 'C'

def main():
    inputTemp = float( input( 'Give temp: ' ) )
    inputScale = input( 'Give scale: ')
    inputScale = inputScale.upper()
    print( inputTemp, inputScale)
    if inputScale == "F":
        outputTemp, outputScale = FToC(inputTemp)
    else:
        outputTemp, outputScale = CToF(inputTemp)
    print( outputTemp, outputScale )

main()
