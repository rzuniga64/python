# 1. Create a python script that contains the following:
def main():
    # a. Define two variables that contain the integer values 13 and 27
    int1 = 13
    int2 = 27
    
    # b. Define a variable that is used to capture the result of
    # adding the variables defined in 1a
    sum_of_int = int1 + int2
    
    # c. Define two variables that contain the string values
    # George" and "Washington
    first_name = 'George'
    last_name = 'Washington'
    
    # d. Define a variable that is used to capture the result
    # of concatenating the two variables defined in 1c.
    full_name = first_name + " " + last_name
    
    # e. Using the two integer variables from 1a, define a
    # variable that captures 27 modulo 13.
    modulo = int2 % int1
    
    # f. Write one print statement that displays the values
    #   captured in 1b, 1d, and 1e.
    print("Sum of 13 and 17 = %d" % sum_of_int, "\nName is %s" % full_name, "\n27 modulo 13 = %d" % modulo)
    
main()