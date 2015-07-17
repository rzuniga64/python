def how_many_bills_of_that_type(change, bill):
    bills = change // bill
    print("There were ", bills, " of $", bill, "'s.", sep="")
    change = change % bill
    return change


def main():
    cost = int(input("Gimme the cost in $"))
    tendered = int(input("Gimme the amount rec'd. in $"))
    change = tendered - cost
    print("Change is $", change, ".", sep="")
    change = how_many_bills_of_that_type(change, 500)
    change = how_many_bills_of_that_type(change, 100)
    change = how_many_bills_of_that_type(change, 50)
    change = how_many_bills_of_that_type(change, 20)
    change = how_many_bills_of_that_type(change, 10)
    change = how_many_bills_of_that_type(change, 5)
    change = how_many_bills_of_that_type(change, 1)

main()
