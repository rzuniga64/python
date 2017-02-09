# Dictionary is an unordered collection of key-value pairs.
# It is generally used when we have a huge amount of data. Dictionaries are optimized for retrieving data.
# We must know the key to retrieve the value.
# In Python, dictionaries are defined within braces {} with each item being a pair in the form key:value.
# Key and value can be of any type.

empty = {}  # empty dictionary

d = {1: 'value', 'key': 2}
type(d)

# We use key to retrieve the respective value. But not the other way around.
d = {1: 'value', 'key': 2}
print(type(d))

print("d[1] = ", d[1])

print("d['key'] = ", d['key'])

# Generates error
# print("d[2] = ", d[2])

grades = {'Raymond': 92, 'Cynthia': 83, 'Terrill': 64, 'Jennifer': 75, 'Clayton': 88, 'David': 91, 'Bryan': 100}
print(grades)
print("keys = ", grades.keys())
print("values = ", grades.values())
