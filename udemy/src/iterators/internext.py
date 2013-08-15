# creating an explicit iterator
def main():
    numbers = [1,2,3]
    
    # create an explicit iterator
    it = iter(numbers)
    print(next(it))
    print(next(it))
    print(next(it))
    
    #file object is automatically set up as an iterator
    # so don't need to call an iter function
    fileIt = open("grades.txt", "r")
    print(next(fileIt), end='')
    
main()