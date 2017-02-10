# anonymous function based on a lambda form

# def square(number):
#   return number * number

# sq = square


def main():
    square = lambda x: x*x
    print(square(2))

    numbers = [1, 2, 3, 4]
    numbers_sq = list(map(lambda x: x*x, numbers))
    print(numbers_sq)
    
main()
