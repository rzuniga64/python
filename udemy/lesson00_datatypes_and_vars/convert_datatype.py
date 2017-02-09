# We can convert between different data types by using different type conversion functions like int(), float(),
# str() etc.

print(float(5))

# Conversion from float to int will truncate the value (make it closer to zero).
print(int(10.6))
print(int(-10.6))

# Conversion to and from string must contain compatible values.
print(float('2.5'))
print(str(25))

# We can even convert one sequence to another.
a = set([1, 2, 3])
print("set = ", a)

a = tuple({5, 6, 7})
print("tuple = ", a)

list('hello')
print("string = ", a)

# To convert to dictionary, each element must be a pair
a = dict([[1,2],[3,4]])
print("dict = ", a)

a = dict([(3, 26), (4, 44)])
print("dict = ", a)
