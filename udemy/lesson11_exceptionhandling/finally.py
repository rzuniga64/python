try:
    print("Enter a file name: ")
    name = input()
    f = open(name, 'w')
    print(f)
except IOError:
    print("Error with file.")
    print("Enter a file name: ")
    name = input()
    f = open(name, 'w')
    print(f)
finally:
    f.close()
