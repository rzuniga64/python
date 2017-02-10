# 5! = 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4!


def fact(num):
    if num <= 1:
        return 1
    else:
        return num * fact(num-1)
number = 10
print(str(number) + "! = " + str(fact(10)))
