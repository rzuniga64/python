"""
 Integers can be of any length, it is only limited by the memory available.
 A floating point number is accurate up to 15 decimal places. Integer and
 floating points are separated by decimal points. 1 is integer, 1.0 is floating
 point number. Complex numbers are written in the form, x + yj, where x is the
 real part and y is the imaginary part.
"""
a = 5
print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))

a = 1+2j
print(a, "is complex number?", isinstance(1+2j, complex))
