def get_digits_used_in_address(st_number):
    the_counts = [0] * 10
    for n in range(len(st_number)):
        digit = st_number[n]
        digit_no = int(digit)
        the_counts[digit_no] += 1
    return the_counts


def show_results(the_counts):
    for digit in range(10):
        if the_counts[digit] > 0:
            print(digit, "occurred", the_counts[digit])


def main():
    # Ask for street number.
    start_addr = int(input("Give me a starting street number: "))
    end_addr = int(input("Give me a ending "))
    address_string = ""
    for address in range(start_addr, end_addr+1):
        address_string += str(address)

    # Count digits used in that street number.
    the_counts = get_digits_used_in_address(address_string)
    # Display digit use counts.
    show_results(the_counts)
    
main()
