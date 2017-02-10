import os


def make_text_file():

    if not os.path.isfile('file1.txt'):
        a = open('file1.txt', 'w')
        a.write('This is how you create a new text file')
        a.close()
    else:
        a = open('file1.txt', 'a')
        a.write('\nHere is some additional text!')
        a.close()

    a = open('file1.txt', 'a')
    a.write("""
    here is
    more
    text""")
    a.close()

    # Read a line from the file using the readline method. The first time you
    # call this method on a file object, it will return the first line of text
    # in the file.
    a = open('file1.txt', 'r')
    line = a.readline()
    print(line)

    # You can read the file all at once with the read method. This method return
    # any text in the file that you haven't read yet as one long string.
    text = a.read()
    print(text)
    # When you are done reading the file, close the file by deleting the file
    # object and closing the file
    a.close()


def print_line_lengths():
    file = open('file1.txt', 'r')
    text = file.readlines()
    for line in text:
        print(len(line))
    file.close()


def main():
    make_text_file()
    print_line_lengths()

main()