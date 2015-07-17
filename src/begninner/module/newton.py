import math


def average(x, y):
    return (x + y) / 2


def square(number):
    return number * number


def sqrt(number):
    def close_enough(guess):
        return math.fabs((square(guess)) - number < 0.001)

    def improve(guess):
        return average(guess, (number / guess))

    def sqrt_helper(guess):
        if close_enough(guess):
            return guess
        else:
            return sqrt_helper(improve(guess))
    return sqrtHelper(1.0)