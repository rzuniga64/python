"""
You are given a string . Your task is to swap cases. In other words, convert all
lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2

Input Format
A single line containing a string S.

Constraints
0 < len(s) <= 1000

Output Format
Print the modified string S.

Sample Input
HackerRank.com presents "Pythonist 2".

Sample Output
hACKERrANK.COM PRESENTS "pYTHONIST 2".
"""

import re


def swap_case(string):
    return string.swapcase()

if __name__ == '__main__':
    s = input()
    if 0 < len(s) <= 1000:
        result = swap_case(s)
        print(result)

