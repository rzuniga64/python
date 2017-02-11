"""
A higher order function is a function that uses another function as an argument.
A function is an object in python. We can assign it to a variable.
We can pass a function as an argument to another function.
Reduce increases productivity and reduces errors

Reduce is a really useful function for performing some computation on a list and
returning the result. For example, if you wanted to compute the product of a
list of integers.

So the normal way you might go about doing this task in python is using a basic
for loop:

Now let’s try it with reduce:

from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])

# Output: 24
"""


def total(x, y):
    return x + y


def main():

    # reduce
    import functools
    numbers = list(range(1, 11))
    print(numbers)
    sum = functools.reduce(total, numbers)
    print("The sum of the range is " + str(sum))

main()
