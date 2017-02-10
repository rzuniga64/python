# List comprehensions is a shortcut for a for loop.
# Python supports a concept called "list comprehensions". It can be used to
# construct lists in a very natural, easy way, like a mathematician is used to
# do. The following are common ways to describe lists (or sets, or tuples, or
# vectors) in mathematics.
# S = {x² : x in {0 ... 9}}
# V = (1, 2, 4, 8, ..., 2¹²)
# M = {x | x in S and x even}

S = [x**2 for x in range(10)]
V = [2**i for i in range(13)]
M = [x for x in S if x % 2 == 0]
print(S)
print(V)
print(M)
print()

sent = "now is the time for all good people to come to the aid of their party"
words = sent.split(' ')
# for each word create a tuple that includes the word and its length
wlen = [(word, len(word)) for word in words]
for i in wlen:
    print(i)
print()

uppercase_words = ['NOW', 'IS', 'THE', 'TIME']
print(uppercase_words)
lowercase_words = [word.lower() for word in uppercase_words]
print(lowercase_words)
