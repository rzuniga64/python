"""
A higher order function is a function that uses another function as an argument.
A function is an object in python. We can assign it to a variable.
We can pass a function as an argument to another function.
Filter increases productivity and reduces errors

As the name suggests, filter creates a list of elements for which a function
returns true. Here is a short and concise example:

number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

# Output: [-5, -4, -3, -2, -1]

The filter resembles a for loop but it is a builtin function and faster.

Note: If map & filter do not appear beautiful to you then you can read about
list/dict/tuple comprehensions.
"""


def even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def main():

    # filter will take a boolean function and return elements of the sequence
    # that meet that criteria.
    numbers = list(range(1, 11))
    print(numbers)
    evens = list(filter(even, numbers))
    print(evens)

main()
