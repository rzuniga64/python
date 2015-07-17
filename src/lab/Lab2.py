cost = int(input("Enter the cost in $: "))
tendered = int(input("Enter the amount received in $: "))
change = tendered - cost
print("Total change will be $", change, ".", sep="")

#Print out the number of five hundred dollar bills
fivehundreds = change//500
print("$500 bills: ", fivehundreds, sep="")

#Print out the number of hundred dollar bills
change = change % 500
hundreds = change//100
print("$100 bills: ", hundreds, sep="")

#Print out the number of fifty dollar bills
change = change % 100
fifties = change//50
print("$50 bills: ", fifties, sep="")

#Print out the number of twenty dollar bills
change = change % 50
twenties = change//20
print("$20 bills: ", twenties, sep="")

#Print out the number of ten dollar bills
change = change % 20
tens= change//10
print("$10 bills: ", tens, sep="")

#Print out the number of five dollar bills
change = change % 10
fives = change//5
print("$5 bills: ", fives, sep="")

#Print out the  number of one dollar bills
ones = change % 5
print("$1 bills: ", ones, sep="")
