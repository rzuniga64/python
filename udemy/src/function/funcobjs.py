def square(number):
   return number * number

def main():
    num = 2
    sqnum = square(num)
    # a function is just an object and can 
    # be assigned to any variable
    sqnumber = square
    sqnum = sqnumber(2)
    print(sqnum)

    #map higher-order function
    numbers = [1,2,3,4]
    numberssq = list(map(square, numbers))
    print(numberssq)
    
main()