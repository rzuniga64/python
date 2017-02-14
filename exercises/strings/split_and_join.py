"""
a = "this is a string"
a = a.split(" ") # a is converted to a list of strings.
print a

Result
['this', 'is', 'a', 'string']

Joining a string is simple:
a = "-".join(a)
print a

Result
this-is-a-string

Task
You are given a string. Split the string on a " " (space) delimiter and join
using a - hyphen.

Input Format
The first line contains a string consisting of space separated words.

Output Format
Print the formatted string as explained above.

Sample Input
this is a string

Sample Output
this-is-a-string
"""


def split_and_join(line):
    a = line.split(" ")
    a = "-".join(a)
    return a

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
