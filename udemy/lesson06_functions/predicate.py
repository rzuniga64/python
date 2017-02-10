# predicate function or boolean function


def is_vowel(letter):
    if letter == "a" or letter == "e" or \
       letter == "i" or letter == "o" or \
       letter == "u":
        return True
    else:
        return False


def num_vowels(string):
    string = string.lower()
    count = 0
    for i in range(len(string)):
        if is_vowel(string[i]):
           count += 1
    return count

print("Enter a string: ")
strng = input()
print("There are " + str(num_vowels(strng)) + " vowels in the string.")
