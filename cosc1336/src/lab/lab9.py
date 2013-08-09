# Input: Words on the current line of the document
# Output: Unique words in the document up to and including this line

def addUniqueWordOnLine( wordsOnLine, wordList ):
    for word in wordsOnLine:
        if word != "Gettysburg":
            word = word.lower()
        word = word.strip( ".," )
        if word in wordList:
            pass
        elif word == "-":
            pass
        else:
            wordList.append( word )

# Input: A line of text in the input file
# Output: Words as strings of text on that line

def gimmeWords( lineOfText ):
    wordsOnLine = lineOfText.split()
    return wordsOnLine

# Input: file name containing text to find unique words in
# Output: list of unique words

def ProcessDocument( filename ):
    try:
        document = open( filename, "r" )
    except:
        print( "File " + filename + " did not open." )
        document = open( "GettysburgAddress.txt", "r" )

    wordList = []
    for lineOfText in document:
        lineOfText = lineOfText.strip()
        wordsOnLine = gimmeWords( lineOfText )
        addUniqueWordOnLine( wordsOnLine, wordList )

    print( len( wordList ) )

    document.close()
    
    return wordList

def main():

    unique = ProcessDocument( "GettysburgAddress.txt" )
    unique.sort()
    print( unique )

main()
