def is_leap(year):
    leap = False

    if year % 4 == 0 and 1900 <= year <= 10 ** 5:
        if year % 400 == 0 and year % 100 == 0:
            leap = True
        elif year % 400 != 0 and year % 100 == 0:
            leap = False
        else:
            leap = True

    return leap


def main():

    print("Please enter a year between 1900 and 10**5: ")
    year = int(input())
    print(is_leap(year))

main()