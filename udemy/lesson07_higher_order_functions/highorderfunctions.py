# A higher order function is a function that uses another function as an
# argument.
# A function is an object in python. We can assign it to a variable.
# We can pass a function as an argument to another function.

# Let's look at three higher order functions:
# map, filter and reduce
# increases productivity and reduces errors


def square(number):
    return number * number


def even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def total(x, y):
    return x + y


def main():
    # map
    numbers = [1, 2, 3]
    print(numbers)
    numberssq = list(map(square, numbers))
    print(numberssq)

    # filter
    numbers = list(range(1, 11))
    print(numbers)
    evens = list(filter(even, numbers))
    print(evens)

    # reduce
    import functools
    numbers = list(range(1, 11))
    print(numbers)
    sum = functools.reduce(total, numbers)
    print("The sum is of the range is " + str(sum))

main()
