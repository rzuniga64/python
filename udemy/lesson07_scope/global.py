"""
    scope
    global / local
    Once a variable is declared in the main program then its visibility is
    throughout the program. We can access the variable in a function.
"""


def get_number():
    print(number)

number = 1
print(number)
get_number()
