"""
    scope
    global / local
    Squared is a local variable so is only accessible within the function.
"""


def square(number):
    squared = number * number
    return squared

print(square(2))
# print("Squared (defined in square function): " + str(squared))
