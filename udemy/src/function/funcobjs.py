def square(number):
    return number * number


def main():
    num = 2
    sq_num = square(num)
    # a function is just an object and can 
    # be assigned to any variable
    sq_number = square
    sq_num = sq_number(2)
    print(sq_num)

    #map higher-order function
    numbers = [1, 2, 3, 4]
    numbers_sq = list(map(square, numbers))
    print(numbers_sq)
    
main()