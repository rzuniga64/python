from newton import average, square, sqrt

num1 = 199
num2 = 78
#print("The average is " + str(average(num1, num2)))
#print(sqrt(9))
avg = average(num1, num2)
print("The average is " + str(avg))
print("The square of the average " + str(square(avg)))

print("Enter a number: ")
number = int(input())
print("the square root of " + str(number) + ' is ' + str(sqrt(number)))
