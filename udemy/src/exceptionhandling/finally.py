try:
    print("Enter a file name: ")
    name = input()
    file = open(name, 'w')
except:
    print("Error with file.")
    print("Enter a file name: ")
    name = input()
    file = open(name, 'w')
finally:
    file.close()