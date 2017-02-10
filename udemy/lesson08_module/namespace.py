"""
    Importing this way we can have other names in our program we can use that
    have the same name as a function from newton. We have to qualify the
    name with the module name if we use a function from the module.
"""
import newton


def square(number):
    print("not from the newton module")
    return number * number

num = 12
print("Square from newton.py: ")
print(newton.square(num))
print("Square from main program: ")
print(square(num))
