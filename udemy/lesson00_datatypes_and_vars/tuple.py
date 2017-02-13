"""
Tuple is an ordered sequence of items same as list. The only difference is
that tuples are immutable. Tuples once created cannot be modified.
If you change a tuple you are making another copy. Tuples are used to
write-protect data and are usually faster than list as it cannot change
dynamically. It is defined within parentheses () where items are separated by
commas. One thing we can do with a tuple that we can't do with a list is make
it a key in a dictionary.
"""

t = (5, 'program', 1+3j)

# t[1] = 'program'
print("t[1] = ", t[1])

# t[0:3] = (5, 'program', (1+3j))
print("t[0:3] = ", t[0:3])

# Generates error
# Tuples are immutable
# t[0] = 10

print("length of tuple is", len(t))

# add tuples together
num1 = (1, 2)
num2 = (3, 4)
num3 = num1 + num2
print("num1 + num2", num3)

# we can replicate a tuple
sentence = ('now', 'is', 'the', 'time')
print(sentence * 3)


