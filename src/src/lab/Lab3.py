def CToF(temp):
    output_temp = temp * 9 / 5 + 32
    return output_temp, 'F'


def FToC(temp):
    output_temp = (temp -32) * 5/9
    return output_temp, 'C'


def main():
    input_temp = float(input('Give temp: '))
    input_scale = input('Give scale: ')
    input_scale = input_scale.upper()
    print(input_temp, input_scale)
    if input_scale == "F":
        output_temp, output_scale = FToC(input_temp)
    else:
        output_temp, output_scale = CToF(input_temp)
    print(output_temp, output_scale)

main()
