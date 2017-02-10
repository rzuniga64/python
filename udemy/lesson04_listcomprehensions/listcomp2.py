def main():

    grades = [grade.rstrip() for grade in open('grades.txt')]
    print(grades)
main()