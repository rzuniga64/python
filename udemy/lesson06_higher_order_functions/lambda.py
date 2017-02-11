"""
Anonymous function based on a lambda form.

Lambdas are one line functions. They are also known as anonymous functions in
some other languages. You might want to use lambdas when you don’t want to use
a function twice in a program. They are just like normal functions and even
behave like them.

Blueprint

lambda argument: manipulate(argument)

Example

add = lambda x, y: x + y

print(add(3, 5))
# Output: 8

Here are a few useful use cases for lambdas and just a few way in which they are
used in the wild:

List sorting

a = [(1, 2), (4, 1), (9, 10), (13, -3)]
a.sort(key=lambda x: x[1])

print(a)
# Output: [(13, -3), (4, 1), (1, 2), (9, 10)]

Parallel sorting of lists

data = zip(list1, list2)
data.sort()
list1, list2 = map(lambda t: list(t), zip(*data))
"""


def main():

    add = lambda x, y: x + y
    print("Adding two numbers: " + str(add(3, 5)))

    square = lambda x: x*x
    print("Squaring a number: " + str(square(2)))

    numbers = [1, 2, 3, 4]
    numbers_sq = list(map(lambda x: x*x, numbers))
    print(numbers_sq)

    # List sorting
    a = [(1, 2), (4, 1), (9, 10), (13, -3)]
    a.sort(key=lambda x: x[1])

    print(a)
    print()

    # Parallel sorting of lists
    list1 = [4, 1, 19, 10]
    list2 = [45, 11, 54, 9]

    data = zip(list1, list2)

    # list(data)
    # x, y = zip(*zip(list1, list2))
    # print(x)
    # print(y)

    # list_func = lambda t: list(t)
    # print(list_func(data))

    # Map applies a function to all the items in an input_list.
    # map(function_to_apply, list_of_inputs)

    list1, list2 = map(lambda t: sorted(list(t)), zip(*data))
    print(list1)
    print(list2)

main()
