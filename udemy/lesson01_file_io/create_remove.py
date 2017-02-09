import os
import shutil

def main():
    # Create a child and parent directly using os.makedirs 
    os.makedirs(r"C:\Users\3964505\Music\pop")
    
    # Remove a directory with os.rmdir.  This only works 
    # for empty directories; if the directory is not empty, 
    # you'll have to remove its contents first.
    os.rmdir(r"C:\Users\3964505\Music\pop")
    
    # There is way to remove a directory even if it contains
    # other files and sub directories. The function shutil.rmtree
    # does this.  Be careful, however,, if you pass the wrong 
    # path to this function, you could delete a whole bunch of 
    # files before you know what's going on!
    
    shutil.rmtree(r"C:\Users\3964505\Music\pop")
main()