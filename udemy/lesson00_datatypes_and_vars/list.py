# List is an ordered sequence of items. It is one of the most used datatype in
# Python and is very flexible. All the items in a list do not need to be of the
# same type. Declaring a list is pretty straight forward. Items separated by
# commas are enclosed within brackets [ ].

# empty list
x = []

a = [5, 10, 15, 20, 25, 30, 35, 40]

# a[2] = 15
print("a[2] = ", a[2])

# a[0:3] = [5, 10, 15]
print("a[0:3] =", a[0:3])

# a[5:] = [30, 35, 40]
print("a[5:] =", a[5:])

list1 = ['now', 'is']
list2 = ['the', 'time']
print("list1 + list2 =", list1 + list2)

word = ['hello']
print(word * 5)

names = ['Joe', 'Mary', ['Billie Joe'], 'Fred']
print("names[2] =", names[2])

grades = ['Raymond', 92]
print(grades[0] + ' ' + str(grades[1]))
