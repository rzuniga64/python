def count_letters(words):
    if len(words) < 1:
        return 0
    else:
        return len(words[0]) + count_letters(words[1:])

sentence = ['now', 'is', 'the', 'time', 'for', 'all', 'good', 'people']
print(sentence)
print(count_letters(sentence))
