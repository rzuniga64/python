def howManyBillsOfThatType( change, bill ):
    bills = change // bill
    print( "There were ", bills, " of $", bill , "'s.", sep = "" )
    change = change % bill
    return change
    
def main():
    cost = int( input( "Gimme the cost in $" ) )
    tendered = int( input( "Gimme the amount rec'd. in $" ) )
    change = tendered - cost
    print( "Change is $", change, ".", sep="" )
    change = howManyBillsOfThatType( change, 500 )
    change = howManyBillsOfThatType( change, 100 )
    change = howManyBillsOfThatType( change, 50 )
    change = howManyBillsOfThatType( change, 20 )
    change = howManyBillsOfThatType( change, 10 )
    change = howManyBillsOfThatType( change, 5 )
    change = howManyBillsOfThatType( change, 1 )

main()
