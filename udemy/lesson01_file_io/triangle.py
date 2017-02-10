# Triangle
# By starting at the top of the triangle and moving to adjacent numbers on the
# row below, the maximum total from top to bottom is 27.
#
#        5
#      9  6
#    4   6  8
#  0   7  1   5
#
# I.e. 5 + 9 + 6 + 7 = 27.
#
# Write a program in a language of your choice to find the maximum total 
# from top to bottom in triangle.txt, a text file containing a triangle with
# 100 rows. Send your solution and resume to [123456 AT yodle dot com],
# replacing 123456 with the maximum sum for the triangle.


def process_document(filename):
    try:
        document = open(filename, "r")
    except:
        print("File " + filename + " did not open.")
        document = open("C:\\Users\\Owner\\PycharmProjects\\python\\udemy\\lesson01_file_io\\docs\\triangle.txt", "r")

    numbers = list()
    for line in document:
        line = line.strip()
        numbers.append(int(number) for number in line.split())

    return numbers


def main():
    numbers = process_document("triangle.txt")
    total = 0
    maxlist = list()
    for row in numbers:
        maxlist.append(max(row))

    for number in maxlist:
        total += number
    print(maxlist)
    print(total)
        
main()