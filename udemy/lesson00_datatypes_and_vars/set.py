"""
Set is an unordered collection of unique items. Set is defined by values
separated by comma inside braces { }. Items in a set are not ordered.
"""

a = {5, 2, 3, 1, 4}

# printing set variable
print("a = ", a)

# data type of variable a
print(type(a))

# We can perform set operations like union, intersection on two sets. Set have
# unique values. They eliminate duplicates.

a = {1, 2, 2, 3, 3, 3}
a
{1, 2, 3}

# Since, set are unordered collection, indexing has no meaning. Hence the
# slicing operator [] does not work.
# a = {1, 2, 3}
# a[1]
