# numbers = range(1,11)
# it = iter(numbers)
# print(next(it))
import os

# popen returns a sequence of data. It allows you to run a os command like dir
# and turn that data into an iterable object.
files = os.popen('dir *.py')
fileit = iter(files)


# print(next(fileit), end='')
# print(next(fileit), end='')
# print(next(fileit), end='')
# print(next(fileit), end='')
# print(next(fileit), end='')
# print(next(fileit), end='')
# print(next(fileit), end='')
# print(next(fileit), end='')
# print(next(fileit), end='')
# print(next(fileit), end='')

for file in files:
    print(file, end='')

