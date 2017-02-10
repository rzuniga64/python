# continue - control is transferred to the top of the loop
numerator = 0
denominator = 0
while denominator != -1:
    print("Enter a numerator: ")
    numerator = float(input())
    print("Enter a denominator: ")
    denominator = float(input())
    if denominator == 0:
        continue
    elif denominator == -1:
        exit()
    print(numerator / denominator)
