import os.path
import time

# Split a path completely with a recursive function
# Notice the two uses of single-element tuples, which
# must include a comma in the parentheses.  (name, )
# is a tuple with one element; (name) is the same as name
def split_fully(path):
    parent_path, name = os.path.split(path)
    if name == "":
        return parent_path,
    else:
        return split_fully(parent_path) + (name, )

# This function loops over the list returned by os.listdir and
# calls os.path.join on each entry to construct the full path
# before printing it.


def print_dir(dir_path):
        for name in os.listdir(dir_path):
            print(os.path.join(dir_path, name))

# os.path.dir can be combined with os.listdir to process
# subdirectories recursively.  You can list the contents
# of a directory, its subdirectories, their subdirectories
# and so on.  When the function finds a subdirectory, it
# calls itself to list the contents of that subdirectory


def print_tree(dir_path):
    for name in os.listdir(dir_path):
        full_path = os.path.join(dir_path, name)
        print(full_path)
        if os.path.isdir(full_path):
            print_tree(full_path)


# modify print_dir to print the contents of a directory,
# including the size and modification time of each file.
def print_dir_info(dir_path):
    for name in os.listdir(dir_path):
        full_path = os.path.join(dir_path, name)
        file_size = os.getsize(full_path)
        mod_time = time.ctime(os.path.getmtime(full_path))
        print("%%-32s: %8d bytes, modified %s" % (name, file_size, mod_time))


def main():
    # To assemble directory names into a path, use os.path.join
    path1 = os.path.join('snakes', 'Python')
    print(path1)

    # The inverse function is os.path.split, which splits off the
    # last component of a path.  It returns a tuple of two items:
    # the path of the parent directory and the last path component.
    # the tuple can be broken into elements on LHS of the equal sign.
    parent_path, name = os.path.split("C:\Python33\Doc")
    print(parent_path)
    print(name)

    split_path = split_fully("C:\Windows\System32\drivers\zh-TW")

    # After you have the name of a file,  you can split off its
    # extension with os.path.splitext
    parts = os.path.splitext('image.jpg')
    extension = parts[1]
    extension2 = os.path.splitext("image.jpg")[1]

    # os.path.normpath normalizes or "cleans up" a path:
    norm_path = os.path.normpath(r"C\Program Files\Perl\..\Python30")

    # os.path.abspath, which converts a relative path (a path relative
    # to the current directory) to an absolute path (a path starting
    # at the root of the drive or file system.
    abs_path = os.path.abspath('file1.txt')

    # If you want to know whether a path actually does exist, use
    # os.path.exists
    path_exists = os.path.exists("C:\\Users\\Roy\\PycharmProjects\\python")

    # Get a list of entries in a directory
    dir = os.listdir("C:\\Users\\Roy\\PycharmProjects\\python")

    print_dir("C:\\Users\\Roy\\PycharmProjects\\python")

    # This produces a case-sensitive alphabetical sort
    sorted_list = sorted(os.listdir("C:\\Users\\Roy\\PycharmProjects\\python"))

    # Determine if a path refers to a file using os.path.isfile
    is_path = os.path.isfile("C:\\Users\\Roy\\PycharmProjects\\python\\oracle-driver-license.txt")

    # Determine if a path refers to a directory using os.path.isdir
    is_dir = os.path.isdir("C:\\Users\\Roy\\PycharmProjects\\python")

    # print out the contents of directory
    print_tree("C:\\Users\\Roy\\PycharmProjects\\python")

    # Output when your Python directory was last modified
    mod_time = os.path.getmtime("C:\Python33")
    print(time.ctime(mod_time))

    print_dir_info("C:\Python33")


main()