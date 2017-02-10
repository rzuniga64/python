import re
import os


def get_file_list(folder):

    """
    Function: getFileList(folder)
    Input:    One argument called 'folder'.
    Output:   The function returns a list of files that exist in that folder.
    """
    return os.listdir(folder)


def print_file_list(folder, file_list):

    """
    Function: printFileList(folder, fileList)
    Input:  Two arguments - one called 'folder', one called 'fileList'.
    Output: Prints the name of the folder and the list of files in the folder
    """

    print("Files for folder %s:" % folder)

    for file in file_list:
        print("%s" % file)


def main():
    infilename = "C:\\Users\\Owner\\PycharmProjects\\python\\udemy\\" \
                 "lesson01_file_io\\program_6_4.cpp"
    outfilename = "_program_6_4.cpp";

    try:
        infile = open(infilename, "r")
    except:
        print("File " + infilename + " did not open")
        infile = open(infilename, "r")

    try:
        outfile = open(outfilename, "w")
    except:
        print("File " + outfilename + " did not open")
        outfile = open(outfilename, "w")

    for line_of_text in infile:
        match = re.match(r"^[0-9]*", line_of_text)
        line_of_text = line_of_text[:match.start()] + line_of_text[match.end():]
        outfile.write(line_of_text)

    infile.close()
    outfile.close()


    if os.path.isfile(infilename):
        os.remove(infilename)
        os.replace(outfilename, infilename)
        print_file_list(".", get_file_list("."))
main()
