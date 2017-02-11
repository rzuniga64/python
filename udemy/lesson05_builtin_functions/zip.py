"""
Make an iterator that aggregates elements from each of the iterables.

Returns an iterator of tuples, where the i-th tuple contains the i-th element
from each of the argument sequences or iterables. The iterator stops when the
shortest input iterable is exhausted. With a single iterable argument, it
returns an iterator of 1-tuples. With no arguments, it returns an empty
iterator.
"""

x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
print(list(zipped))
# [(1, 4), (2, 5), (3, 6)]

x2, y2 = zip(*zip(x, y))
print("x2 = " + str(x2))
print("y2 = " + str(y2))
print(x == list(x2) and y == list(y2))
