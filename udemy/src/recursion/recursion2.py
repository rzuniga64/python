#explode('hello')->'h e l l o'
#removeDups('aabbcc')->'abc'


def explode(word):
    if len(word) <= 1:
        return word
    else:
        return word[0] + ' ' + explode(word[1:])


def remove_dups(word):
    if len(word) <= 1:
        return word
    elif word[0] == word[1]:
        return remove_dups(word[1:])
    else:
        return word[0] + remove_dups(word[1:])


def main():
    print(explode('hello'))
    word = 'aabbbccccdd'
    print(word)
    print(remove_dups(word))

main()