# An iterator is an object that represents a stream of data. Unlike a sequence,
# an iterator can (usually) only provide the next item. The for-in statement
# uses iterators to control the loop, and iterators can also be used in many
# other contexts. To add iteration support to your own classes, implement the
# __iter__ method.

# numbers = [1,2,3]
# it = iter(numbers)
# print(next(it))
# print(next(it))
# print(next(it))

# a file object is an iterator.
fileIt = open('grades.txt', 'r')
print(next(fileIt), end='')
