import sys
import os


def main():
    print("This was given the command line parameters: %s" % sys.argv)

    file_path = sys.argv[1]

    if os.path.isfile(file_path):
        if os.path.exists(file_path):
            f = open(file_path, "r")

            size = os.path.getsize(file_path)
            print("file size is: ", size)

            line1 = f.read(11)
            print("line 1 is ", line1)

            print("tell: ", f.tell())

            f.seek(0)
            
            line2 = f.read()
            print("line 2 is ", line2)
            
            #for line in f:
            #    print(line)
            #f.close()
        else:
            print("file: ", file_path, " does not exist")
    else:
        print("file: ", file_path, "is not a file")
main()