"""
Lists can contain any type of elements, including strings, nested lists and
functions. You can even mix different types within a list. The following works
on a list of strings and produces a list of lists. Each of the sublists
contains two strings and an integer.
"""

words = 'The quick brown fox jumps over the lazy dog'.split()
print("Words =", words)
print()
# ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

stuff = [[w.upper(), w.lower(), len(w)] for w in words]
for i in stuff:
    print(i)
print()

stuff = map(lambda w: [w.upper(), w.lower(), len(w)], words)
for i in stuff:
    print(i)

"""
The above example also demonstrates that you can do exactly the same thing
with map() and a lambda function. However, there are cases when you cannot
use map() and have to use a list comprehension instead, or vice versa. When
you can use both, then it is often preferable to use a list comprehension,
because this is more efficient and easier to read, most of the time.

You cannot use list comprehensions when the construction rule is too
complicated to be expressed with "for" and "if" statements, or if the
construction rule can change dynamically at runtime. In this case, you better
use map() and / or filter() with an appropriate function. Of course, you can
combine that with list comprehensions.
"""