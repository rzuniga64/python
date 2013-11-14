import os
import shutil


"""
    Purpose: Keep over versions of a file around.  Often older
    versions of a file are named with a numerical suffix - for 
    instance, web.log.1, web.log.2 ad so on - in a larger number
    indicates an older version.  To make room for a new version of
    the file, the old versions are rotated.  The current version of
    web.log becomes version web.log.1, web.log.1 becomes web.log.2,
    and so on. A short function, make_version_path constructs the
    right path for both current and old versions.  The other subtle
    point is to rename the oldest version first. We will use a
    recursive function, rotate, to rotate the next-older version of 
    log file before it gets overwritten.
    
    The rotate function uses a technique common in recursive functions:
    a second argument for handling recursive cases - in this case, the
    version number of the file being rotated.  The argument has a 
    default value, zero, which indicates the current version of the file.
    When you call the function (as opposed to when the function is calling
    itself) you don't specify a value for this argument.  For example, you
    can just call rotate('web.log').
"""
def make_version_path(path, version):
    if version == 0:
        # No suffix for version 0, the current version
        return path
    else:
        # Append a suffix to indicate the older version
        return path + '.' + str(version)
    
def rotate(path, version=0):
        #Construct the name of the version we're rotating
    old_path = make_version_path(path, version)
    if not os.path.exists(old_path):
        # It doesn't exist, so complain
        raise IOError("'%s' doesn't exist" % path)
    # Construct the new version name for this file.
    new_path = make_version_path(path, version + 1)
    # Is there already a version with this name?
    if os.path.exists(new_path):
        #Yes.  Rotate it out of the way first!
        rotate(path, version + 1)
    # Now we can rename the version safely.
    shutil.move(old_path, new_path)
    
    # But suppose you want to rotate a system log file that may or may not
    # exist.  One way to handle this is to create an empty log file whenever 
    # it's missing.  Remember that when you open a file that doesn't exist for 
    # writing Python creates the file automatically. 
    
    def rotate_log_file(path):
        if not os.path.exists(path):
            # The file is missing, so create it.
            new_file = open(path, 'w')
            # Close the new file immediately, which leaves it empty.
            del new_file
        # Now rotate it
        rotate(path)
        
def main():
    # Rename a file using shutil.move
    #shutil.move('file2.txt', 'file3.txt')
    
    # Move a file to another directory
    shutil.move('file1.txt', '..\\file1.txt')
    
    # copy a file
    shutil.copy('..\\file1.txt', 'file1.txt' )
    
    #delete a file 
    os.remove('junk.txt')
    
    
main()