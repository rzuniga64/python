import os
import shutil
    # Purpose: This script prints the list of files and/or folders that exist in a folder.


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
    
    """ Create a folder named 'FilesToList' """
    folder = 'C:\\tmp\\FilesToList'

    if not (os.path.isdir(folder)):
        os.mkdir(folder)

    # Create 3 empty files named 'file1.txt', 'file2.txt', 'file3.txt'
    # in the 'FilesToList' folder you just created.
    out_file1 = open(folder + '\\file1.txt', 'w')
    out_file2 = open(folder + '\\file2.txt', 'w')
    out_file3 = open(folder + '\\file3.txt', 'w')
    out_file1.close()
    out_file2.close()
    out_file3.close()

    # Call the 'getFileList' function in main passing in the path of the folder you
    # created in Part 1.
    
    # Call the 'printFileList' function in main passing in the path of the folder
    # as the first argument and the file list returned from 'getFileList' as the second argument.
    print_file_list(folder, get_file_list(folder))
    
    #Remove the non-empty directory that was created
    shutil.rmtree(folder)
    
main()