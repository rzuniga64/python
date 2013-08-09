import random

def nameGesture( n ):
    if n == 1:
        return "rock"
    elif n == 2:
        return "scissors"
    return "paper"

def single( first, second ):
    result = "PROBLEM"
    firstGesture = nameGesture( first )
    secondGesture = nameGesture( second )

    if firstGesture == secondGesture:
        result = 'Neither player won. TIE!'
    elif firstGesture == 'paper':
        if secondGesture == 'rock':
            result = '1st player won'
        elif secondGesture == 'scissors':
            result = '2nd player won'
    elif firstGesture == 'scissors':
        if secondGesture == 'rock':
            result = '2nd player won'
        elif secondGesture == 'paper':
            result = '1st player won'
    elif firstGesture == 'rock':
        if secondGesture == 'scissors':
            result = '1st player won'
        elif secondGesture == 'paper':
            result = '2nd player won'

    print( firstGesture, secondGesture, result, '.' )

def main():
    for first in range( 1, 4 ):
        for second in range( 1, 4):
            single( first, second )

main()             
