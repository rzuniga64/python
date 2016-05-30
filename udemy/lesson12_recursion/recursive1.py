#5! = 5 * 4 * 3 * 2 * 1


def fact(number):
    if number <= 1:
        return 1
    else:
        return number * fact(number-1)


def main():
    print(fact(10))

main()