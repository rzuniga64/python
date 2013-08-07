# This program determines the cost of 1 ounce precious metals
# purchases for gold, silver, and platinum.
#
# INPUT
# 1. The number of ounces of gold
# 2. The number of ounces of silver
# 3. The number of ounces of platinum
#
# OUTPUT
# 1. Total number of ounces purchased
# 2. The cost of purchase by metal
# 3. The overall cost that includes the cost of all coins
#    plust a 2.00% fee and an 8.00% sales tax.

ONEOUNCEGOLD = 1500
ONEOUNCESILVER = 50
ONEOUNCEPLATINUM = 2000
SERVICEFEE = 0.02
SALESTAX = 0.10

def calculateCost(ounces, costPerOunce):
    return (ounces * costPerOunce)

def main():
    ouncesOfGold = int(input("Enter the number of gold ounces: "))
    ouncesOfSilver = int(input("Enter the number of silver ounces: "))
    ouncesOfPlatinum = int(input("Enter the number of platinum ounces: "))
    totalOunces = ouncesOfGold + ouncesOfSilver + ouncesOfPlatinum
    costOfGold = calculateCost(ouncesOfGold, ONEOUNCEGOLD)
    costOfSilver = calculateCost(ouncesOfSilver, ONEOUNCESILVER)
    costOfPlatinum = calculateCost(ouncesOfPlatinum, ONEOUNCEPLATINUM)
    subtotal = costOfGold + costOfSilver + costOfPlatinum
    totalCost = subtotal + subtotal * SERVICEFEE + subtotal * SALESTAX
    print("\nThe total number of ounces purchased is ", totalOunces)
    print("The total cost of gold is ", costOfGold)
    print("The total cost of silver is ", costOfSilver)
    print("The total cost of platinum is", costOfPlatinum)
    print("The total cost of purchase is", totalCost, "\n")
    
main()    
