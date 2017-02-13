# number of words
sentence = "now is the time for all good people to come"
sentence += " to the aid of their party"
words = sentence.split(' ')
words = sorted(words)
print("Sentence in sorted order:\n")
print(words)
numWords = {}
for i in range(0, len(words)):
    if words[i] in numWords:
        numWords[words[i]] += 1
    else:
        numWords[words[i]] = 1
print("Word list and count: \n")
for key in numWords.keys():
    print(key, numWords[key])


def take(num, lyst):
    rlist = []
    for i in range(0, num):
        rlist.append(lyst[i])
    return rlist

# takedrop
def drop(num, lyst):
    rlist = []
    for i in range(num, len(lyst)):
        rlist.append(lyst[i])
    return rlist

names = ['Raymond', 'Cynthia', 'David', 'Jennifer', 'Clayton']
somenames = take(-3, names)
print(somenames)
names = drop(-3, names)
print(names)
