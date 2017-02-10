# count-controlled loops
sum = 0
number = 1
while number <= 10:
    sum += number
    number += 1
print("The sum is " + str(sum) + "\n")

balance = 437000
rate = 1.20
year = 1
while year <= 10:
    balance *= rate
    print("Year: " + str(year) + ": " + str(balance))
    year += 1

