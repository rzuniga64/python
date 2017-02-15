"""
Integers in Python can be as big as the bytes in your machine's memory. There is no limit in size as there is: (c++ int) or  (C++ long long int).

As we know, the result of  grows really fast with increasing .

Let's do some calculations on very large integers.

Task
Read four numbers, , , , and , and print the result of .

Input Format
Integers , , , and  are given on four separate lines, respectively.

Constraints
1 <= a <= 1000
1 <= b <= 1000
1 <= c <= 1000
1 <= d <= 1000

Output Format
Print the result of pow(a,b) + pow(c,d) on one line.

Sample Input
9
29
7
27

Sample Output
4710194409608608369201743232

Note: This result is bigger than pow(2 63)-1. Hence, it won't fit in the long
long int of  C++ or a 64-bit integer.
"""


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    if 1 <= a <= 1000 and 1 <= b <= 1000 and 1 <= c <= 1000 and 1 <= d <= 1000:
        print(pow(a,b) + pow(c,d))

main()
