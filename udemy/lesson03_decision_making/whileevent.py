# event-controlled loops
average = 0.0
total = 0
count = 0
print("Enter a grade (-1 to quit): ")
grade = int(input())
while grade != -1:
    total += grade
    count += 1
    print("Enter a grade (-1 to quit): ")
    grade = int(input())
average = total / count
print("Average grade: " + str(average))
