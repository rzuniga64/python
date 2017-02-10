grades = [grade.rstrip() for grade in open('grades.txt')]
print(grades)
print()

orig_grades = [int(grade) for grade in open('grades.txt')]
print("Original grades:", orig_grades, end='')
print()
grades = [grade + 5 for grade in orig_grades]
print("Curved grades:", grades)
print()

