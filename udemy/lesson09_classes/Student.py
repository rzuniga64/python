class Student:

    # fields - name, id, grades(list)
    grades = []

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __str__(self):
        return "Name: " + self.name + "\n" + \
               "Id: " + self.id + "\n" + \
               "Grades: " + self.show_grades()

    def add_grade(self, grade):
        self.grades.append(grade)

    def show_grades(self):
        grds = ''
        for grade in self.grades:
            grds += str(grade) + ' '
        return grds

    def average(self):
        total = 0
        for grade in self.grades:
            total += grade
        return total / len(self.grades)

stu1 = Student('Jones', '123')
stu1.add_grade(88)
stu1.add_grade(84)
stu1.add_grade(91)
print(stu1.show_grades())
print("Average: " + str(stu1.average()))
