total = 0
count = 0
for grade in open('grades.txt'):
    print(grade, end='')
    total += int(grade)
    count += 1
average = total / count
print("Average: " + str(average))
