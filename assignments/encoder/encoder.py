Alphabet = "abcdefghijklmnopqrstuvwxyz"
NumberOfRightShifts = 1

# Purpose: To read a message from a file.
# Input:   The filename
# Output:  The message that is to be encoded

def GetOriginalMessage( filename ):
    try:
        document = open( filename, "r" )
    except:
        print( "File " + filename + " did not open." )
        document = open( "message.txt", "r" )
    message = ""
    for lineOfText in document:
        message = message + lineOfText
    return message

# Purpose: To create a list, called an encoder, that will be used to encode a message
# Input:    1. The alphabet
#           2. The number of shifts the alphabet needs to be shifted right
# Output:   An encoded list of characters generated from the alphabet

def createAlphabetEncoder():
    alphabetLength = len(Alphabet) 
    encoder = [0]*alphabetLength
            
    # initialize the encoder list with the English alphabet
    for index in range(alphabetLength):
        encoder[index] = Alphabet[index]
    
    # shift the encoder to the right for the correct number of shifts
    for shift in range(NumberOfRightShifts):
        for index in range(alphabetLength-1):
            temp = encoder[index]
            encoder[index] = encoder[index+1]
            encoder[index+1] = temp
    return encoder

# Purpose: Generate an encoded message
# Input:   The message and the encoder 
# Output:  An encoded message

def generateEncodedMessage(message, encoder):
    encodedMessage = ""

    for ch in message:
        if ch.isspace() or ch == ".":
            encodedMessage = encodedMessage + ch
        elif ch.isalpha():
            isUppercase = ch.isupper()

        # check if character is uppercase or lowercas
        # and then add it to encoded message
            letter = ch.lower()
            if letter in Alphabet:
                index = Alphabet.index(letter)          
                if isUppercase:
                    encodedLetter = encoder[index]
                    encodedMessage = encodedMessage + encodedLetter.upper()
                else:
                    encodedMessage = encodedMessage + encoder[index]

    return encodedMessage

# Purpose: Generated an encoded message
# Input:   The message
# Output:  An encoded message
def main():
    message = GetOriginalMessage( "message.txt" )

    encoder = createAlphabetEncoder()
    encodedMessage = generateEncodedMessage(message, encoder)
    print(encodedMessage)

main()
