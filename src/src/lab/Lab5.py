import random


def name_gesture(n):
    if n == 1:
        return "rock"
    elif n == 2:
        return "scissors"
    return "paper"


def single(first, second):
    result = "PROBLEM"
    first_gesture = name_gesture(first)
    second_gesture = name_gesture(second)

    if first_gesture == second_gesture:
        result = 'Neither player won. TIE!'
    elif first_gesture == 'paper':
        if second_gesture == 'rock':
            result = '1st player won'
        elif second_gesture == 'scissors':
            result = '2nd player won'
    elif first_gesture == 'scissors':
        if second_gesture == 'rock':
            result = '2nd player won'
        elif second_gesture == 'paper':
            result = '1st player won'
    elif first_gesture == 'rock':
        if second_gesture == 'scissors':
            result = '1st player won'
        elif second_gesture == 'paper':
            result = '2nd player won'

    print(first_gesture, second_gesture, result, '.')


def main():
    for first in range(1, 4):
        for second in range(1, 4):
            single(first, second)

main()             
