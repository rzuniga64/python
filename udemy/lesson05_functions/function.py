"""
A function is a piece of source code, separate from the larger program, that
performs a specific task.

Reasons to use functions:
1. Reduce complex tasks into simpler tasks.
2. Eliminate duplicate code.
3. Code reuse.
4. Distribute tasks to multiple programmers.
5. Hide implementation details - abstraction.
6. Improves debugging by improving traceability.
"""


def square(num):
    return num * num


def num_vowels(string):
    string = string.lower()
    count = 0
    for i in range(len(string)):
        if string[i] == "a" or string[i] == "e" or string[i] == "i" or \
           string[i] == "o" or string[i] == "u":
            count += 1
    return count


def one_per_line(s):
    for i in s:
        print(i)

number = 12
print(str(number) + " squared = " + str(square(number)))
print()

print("Enter a string: ")
strng = input()
print("There are " + str(num_vowels(strng)) + " vowels in the string.")

word = input("Enter a word: ")
one_per_line(word)
