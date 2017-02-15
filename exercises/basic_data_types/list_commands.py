"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

Initialize your list and read in the value of  N followed by  lines of commands
where each command will be of the types listed above. Iterate through each
command in order and perform the corresponding operation on your list.

Input Format
The first line contains an integer, , denoting the number of commands.
Each line  of the  subsequent lines contains one of the commands described
above.

Constraints
The elements added to the list must be integers.
Output Format

For each command of type print, print the list on a new line.

    Sample Input

    12
    insert 0 5
    insert 1 10
    insert 0 6
    print
    remove 6
    append 9
    append 1
    sort
    print
    pop
    reverse
    print

    Sample Output

    [6, 5, 10]
    [1, 5, 9, 10]
    [9, 5, 1]
"""

if __name__ == '__main__':
    N = int(input("Enter the number of commands to execute on the list: "))

    l = list()
    whitelist = ['insert', 'remove', 'append', 'sort',
                 'pop', 'reverse', 'print']
    for i in range(0, N):
        print("Command to execute on list: ")
        s = input().split()
        if s[0] in whitelist:
            # It's either a command or command and int(s)
            if len(s) == 3:
                cmd, pos, val = s
                eval('l.{}({},{})'.format(cmd, int(pos), int(val)))
            elif len(s) == 2:
                cmd, val = s
                eval('l.{}({})'.format(cmd, int(val)))
            elif len(s) == 1 and s[0] != 'print':
                cmd = s[0]
                eval('l.{}()'.format(cmd))
            elif s[0] == 'print':
                print(l)
            else:
                print("Invalid command.")
                continue






