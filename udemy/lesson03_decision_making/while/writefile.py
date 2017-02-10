outFile = open('grades.txt', 'w')
print("Enter a grade (q to quit): ")
grade = input()
while grade != 'q':
    outFile.write(grade + '\n')
    print("Enter a grade (q to quit): ")
    grade = input()
   
outFile.close()
