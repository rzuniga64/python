"""
String is sequence of Unicode characters. We can use single quotes or double
quotes to represent strings.
Multi-line strings can be denoted using triple quotes, ''' or "".
"""
s = ' Hello, world! '

# s[4] = 'o' error
# s[6:11] = 'world' error


print("s[4] = ", s[4])
# slice
print("s[6:11] = ", s[6:11])
# number of chars I want
print("s[:4]", s[:4])
print("s[4:]", s[4:])

# Generates error
# Strings are immutable in Python
#s[5] ='d'

print("length of string is", len(s))

print("s*2", s*2)
print("s.split(',')", s.split(','))

# Strip spaces at beginning or end of string
print("s.strip()", s.strip())
print("s.rstrip()", s.rstrip())

