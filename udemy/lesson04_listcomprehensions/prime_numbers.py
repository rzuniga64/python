# The build a list of non-prime numbers, using a single list comprehension, then
#  use another list comprehension to get the "inverse" of the list, which are
# prime numbers.

noprimes = [j for i in range(2, 8) for j in range(i*2, 50, i)]
primes = [x for x in range(2, 50) if x not in noprimes]
print(primes)
print()
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
