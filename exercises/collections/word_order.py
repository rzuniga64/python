"""
You are given  words. Some words may repeat. For each word, output its number
of occurrences. The output order should correspond with the input order of
appearance of the word. See the sample input/output for clarification.

Note: Each input line ends with a "\n" character.

Constraints:
1 <= n <= pow(10,5)

The sum of the lengths of all the words do not exceed pow(10,6)
All the words are composed of lowercase English letters only.

Input Format

The first line contains the integer, n.
The next n lines each contain a word.

Output Format
Output 2 lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word
according to their appearance in the input.

Sample Input
4
bcdef
abcdefg
bcde
bcdef

Sample Output
3
2 1 1
Explanation

There are  distinct words. Here, "bcdef" appears twice in the input at the first
and last positions. The other words appear once each. The order of the first
appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the output.
"""


def count_letters(words):
    if len(words) < 1:
        return 0
    else:
        return len(words[0]) + count_letters(words[1:])


def main():
    n = int(input())
    if 1 <= n <= pow(10, 5):
        num_words = dict()
        for i in range(0, n):
            word = input()
            word = word.strip('\n')
            if word in num_words and word.islower():
                num_words[word] += 1
            else:
                num_words[word] = 1
    try:
        if (count_letters(list(num_words.keys())) < pow(10, 6)):
            print(len(num_words.keys()))
            for word_count in num_words.values():
                print(str(word_count) + ' ', end='')
        else:
            raise RuntimeError()
    except RuntimeError:
        print("The sum of the lengths of all the words exceeds pow(10,6")


main()
