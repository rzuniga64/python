try:
    print("Enter the name of a file: ")
    name = input()
    f = open(name, 'r')
except IOError:
    print("Cannot open file.")
    print("Enter the name of the file to open: ")
    name = input()
    f = open(name, 'r')
