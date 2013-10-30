import os.path


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

    print()

main()