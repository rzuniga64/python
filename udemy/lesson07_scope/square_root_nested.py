import math


def square(number):
    return number * number


def sqrt(number):
    return sqrt_helper(1.0, number)


def sqrt_helper(guess, number):
    if close_enough(guess, number):
        return guess
    else:
        return sqrt_helper(improve(guess, number), number)


def close_enough(guess, number):
    return math.fabs((square(guess)) - number) < 0.001


def improve(guess, x):
    return average(guess, (x / guess))


def average(x, y):
    return (x + y) / 2

print(sqrt(144))
