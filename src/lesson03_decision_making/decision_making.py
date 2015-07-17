def main(): 
    # 1. Define an integer variable named "val" and assign it a value of 20. 
    val = 20

    # 2. Write a series of 3 separate 'if' statements that will check whether
    # the integer variable you defined in 1 is equal to 10, 20 or 30 and, if equal,
    # print a message indicating such (for example: print("variable is equal to 10")).
    if val == 10:
        print('variable is equal to 10\n')
    elif val == 20:
        print('variable is equal to 20\n')
    elif val == 30:
        print('variable is equal to 30\n')

    # 3. Write an 'if-else' statement that will check whether the integer variable
    # defined in 1 is between 25 and 40 inclusive. Print the message "value is between
    # 25 and 40" for the true branch and print the message "value is NOT between 25 and 40"
    # for the false branch.

    if val >= 25 and val <= 40:
        print('Value is between 25 and 40\n')
    else:
        print('Value is NOT between 25 and 40\n') 

    # 4. Define a string value named "name" and assign it a value of "Bob".
    # 5. Define an integer value named "index" and assign it a value of 0.
    name = 'Bob'
    index = 0

    # 6. Write a "while" statement whose condition checks whether "index" is less than 3
    # and, if so, prints out the value of the character in the variable "name" at the position
    # identified by the index variable. Make sure to add code in the loop body to increment the
    # loop control variable ('index'), so the loop will terminate after 3 iterations.
    while index < 3:
        print(index * ' ' + name)
        index += 1

main()