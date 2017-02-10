# break = break out of a loop and continue execution with next statement after
# loop

number = 0
total = 0
average = 0.0
count = 0
while True:
    print("Enter a number: ")
    number = float(input())
    if number == -1:
        break
    total += number
    count += 1
average = total / count
print("Average: " + str(average))
