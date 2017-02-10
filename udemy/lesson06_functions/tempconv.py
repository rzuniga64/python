def convert_temp(temp, scale):
    if scale == "c":
        return (temp - 32.0) * (5.0/9.0)
    elif scale == "f":
        return temp * 9.0/5.0 + 32

temp = int(input("Enter a temperature: "))
scale = input("Enter the scale to convert to: ")
converted = convert_temp(temp, scale)
print("The converted temp is: " + str(converted))
