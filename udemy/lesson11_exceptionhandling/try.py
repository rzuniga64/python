try:
    print("Enter a numerator: ")
    numerator = int(input())
    print("Enter a denominator: ")
    denominator = int(input())
    quotient = numerator / denominator
    print(quotient)
except ZeroDivisionError:
    print("Cannot divide by zero.")
    print("Enter a new denominator: ")
    denominator = int(input())
    quotient = numerator / denominator
    print(quotient)
