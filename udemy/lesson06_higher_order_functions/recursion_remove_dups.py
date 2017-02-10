def explode(w):
    if len(w) <= 1:
        return w
    else:
        return w[0] + ' ' + explode(w[1:])


def remove_dupes(w):
    if len(w) <= 1:
        return w
    elif w[0] == w[1]:
        return remove_dupes(w[1:])
    else:
        return w[0] + remove_dupes(w[1:])

print(explode('hello'))
print()
word = 'aabbbccccdd'
print(word)
print(remove_dupes(word))
