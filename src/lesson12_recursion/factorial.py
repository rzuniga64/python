def factorial(number):
    product = 1
    for i in range(1, number+1):
        product *= i
    return product


def main():
    print("Enter a number: ")
    num = int(input())
    print(str(num) + "! equals " + str(factorial(num)))
    
main()