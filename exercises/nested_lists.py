"""
Given the names and grades for each student in a Physics class of  students,
store them in a nested list and print the name(s) of any student(s) having the
second lowest grade.

Note: If there are multiple students with the same grade, order their names
alphabetically and print each name on a new line.

Input Format

The first line contains an integer, , the number of students.
The  subsequent lines describe each student over  lines; the first line contains
a student's name, and the second line contains their grade.

Constraints

- 2 <= N <= 5
- There will always be one or more students having the second lowest grade.

Output Format
Print the name(s) of any student(s) having the second lowest grade in Physics;
if there are multiple students, order their names alphabetically and print each
one on a new line.

Sample Input
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output
Berry
Harry
Explanation

There are 5 students in this class whose names and grades are assembled to build
the following list:

students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41],
            ['Harsh', 39]]

The lowest grade of 37.2 belongs to Tina. The second lowest grade of 37.21
belongs to both Harry and Berry, so we order their names alphabetically and
print each name on a new line.
"""

from operator import itemgetter

if __name__ == '__main__':
    students = list()
    scores = set()
    targets = list()

    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append((name, score))
        scores.add(score)
    students.sort(key=lambda x: x[1])
    scores = sorted(list(scores))
    second_lowest_score = scores[1]

    for student in students:
        if student[1] == second_lowest_score:
            targets.append(student[0])

    targets.sort()
    for target in targets:
        print(target)
