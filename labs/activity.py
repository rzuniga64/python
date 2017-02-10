message = "The recommended activity is "
print("Enter the temperature: ")
temp = int(input())
if temp > 85:
    message += "swimming."
elif temp >= 70:
    message += "tennis."
elif temp >= 32:
    message += "golf."
elif temp >= 0:
    message += "dancing."
else:
    message += "sitting by the fire."
print(message)