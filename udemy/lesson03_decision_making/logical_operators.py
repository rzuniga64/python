'''
    and

    true    true    true
    true    false   false
    false   true    false
    false   false   false

    or

    true    true    true
    true    false   true
    false   true    true
    false   false   false

    not

    true    false
    false   true
'''

hoursWorked = 39
salary = 39000
print(hoursWorked > 40 and salary <= 5000)

password = "GUEST"
print(password == "guest" or password == "GUEST")
print(not(100 < 1))

