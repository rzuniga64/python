count = 0
total = 0
inFile = open('grades.txt', 'r')
grade = inFile.readline()
while grade:
    print(grade)
    count += 1
    total += int(grade)
    grade = inFile.readline()
average = total / count
print("Average: " + str(average))
