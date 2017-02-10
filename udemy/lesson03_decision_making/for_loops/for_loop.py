# iterate through a range of numbers
total = 0
numbers = range(1, 11)
for number in numbers:
    total += number
print("the total is " + str(total))

# iterate through a string
sentence = "now is the time for all good people to come to the aid"
count = 0
for letter in sentence:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'u' \
            or letter == 'o':
        count += 1
print("The number of vowels is " + str(count))

# iterate through a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for number in numbers:
for i in range(0, len(numbers), 3):
    print(numbers[i])
print('\n')

# iterate through a tuple
words = ("now", "is", "time", "the")
for word in words:
    print(word)

print('\n')
maximum = 0

for i in range(1, len(words)):
    if len(words[i]) > len(words[maximum]):
        maximum = i
print("The longest word is " + words[maximum])

numbers = {'Cynthia': '2356', 'Raymond': '2345', 'David': '2373'}

for key in numbers.keys():
    print(key + "'s extension is: " + numbers[key])