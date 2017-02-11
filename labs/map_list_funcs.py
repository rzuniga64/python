def add(y):
    return y[0] + y[1]


def substract(y):
    return y[0] - y[1]


def multiply(y):
    return y[0] * y[1]


if __name__ == '__main__':
    print("Enter a number: ")
    a = int(input())
    print("Enter another number: ")
    b = int(input())

    if 1 <= a <= pow(10, 10) and 1 <= b <= pow(10, 10):
        lst = [(a, b)]
        funcs = [add, substract, multiply]

        for nums in lst:
            value = list(map(lambda x: x(nums), funcs))

        for num in value:
            print(num)
