 #needed for popen which allows you to run an os
 # command like a dir and return that data into an
 # object which is iterable.

import os


def main():
    numbers = range(1, 11)
    it = iter(numbers)
    print(next(it))
    
    files = os.popen('dir *.py')
    file_it = iter(files)
    for file in files:
        print(file)
        
    print(next(file_it), end='')
    print(next(file_it), end='')


main()