import glob
import os

"""
    Globbing is hacker's jargon for expanding wildcards in file
    patterns.  Python provides a function blob, in the lesson09_module
    also named glob, which implements globbing of directory
    contents.  The glob.glob function takes a glob pattern and
    returns a list of matching file names or paths, similar to
    listdir. Glob.glob returns paths containing drive letters and
    directory names if the pattern includes them, unlike os.listdir
    which only returns the names in the specified directory.
"""
def main():
    print(glob.glob(r"C:\Program Files\M*"))
    
    # Globbing is a handy way of selecting a group of similar files
    # for a file operation.  For instance, deleting all backup files
    # with the extenion .bak in a directory.
    
    # Globbing is more powerful than os.listdir because you can
    # specify wildcards in directory and subdirectory names. 
    glob.glob("*\\*.txt")
    for path in glob.glob(r"C:\source\*.bak"):
        os.remove(path)
    
main()