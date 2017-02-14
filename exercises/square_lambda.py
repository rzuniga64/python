"""
Task
Read an integer . For all non-negative integers , print . See the sample for details.

Input Format
The first and only line contains the integer, N.

Constraints
0 <= N <= 20
Output Format
Print  lines, one corresponding to each i

Sample Input
5

Sample Output
0 1 4 9 16
"""


def main():
    print("Enter a number from 1 to 20: ")
    n = int(input())

    if 1 <= abs(n) <= 20:
        for i in range(0, n):
            value = lambda i: i*i
            print(value(i))

main()
