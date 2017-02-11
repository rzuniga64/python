import os


print("Enter file name to open: ")
name = input()
while not os.path.isfile(name):
    print("File does not exist.")
    print("Enter file name to open: ")
    name = input()
file = open(name, 'r')
for line in file:
    print(line, end='')


