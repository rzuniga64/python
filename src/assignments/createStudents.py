import student


def main():

    students = []
    s = student.Student("Russ", "Collins", "undefined", 63)
    students.append(s)
    s = student.Student("Michael", "Deitch", "neuroscience", 20)
    students.append(s)
    s = student.Student("David", "Olguin", "undefined", 20)
    students.append(s)
    s = student.Student("Sean", "Brown", "neuroscience", 20)
    students.append(s)
    s = student.Student("Raul", "Zuniga", "neuroscience", 20)
    students.append(s)
    students[-1].display()

    for s in students:
        print(s)

main()
