"""
Assignment:
Write a program that determines the cost of 1 ounce precious metals purchases
for gold, silver and platinum coins.   It would show total number of coins
purchased, the total cost for those purchases by metal and the overall total
cost that includes the cost of all coins plus a 2% fee and an 8.00 % sales tax,
both will be constant.  So, if a buyer wanted 10 gold, 100 silver and 1 platinum
coins with gold at $1,500 per ounce, silver at $50 per ounce and platinum at
$2,000 per ounce, it would result in a total charge of $24,200.  Turn in just
an IPO chart, showing inputs, outputs and processing steps (the algorithm) to
Blackboard.

This program determines the cost of 1 ounce precious metals
purchases for gold, silver, and platinum.

INPUT
1. The number of ounces of gold
2. The number of ounces of silver
3. The number of ounces of platinum

OUTPUT
1. Total number of ounces purchased
2. The cost of purchase by metal
3. The overall cost that includes the cost of all coins
    plust a 2.00% fee and an 8.00% sales tax.
"""
ONEOUNCEGOLD = 1500
ONEOUNCESILVER = 50
ONEOUNCEPLATINUM = 2000
SERVICEFEE = 0.02
SALESTAX = 0.08


def calculate_cost(ounces, cost_per_ounce):
    return ounces * cost_per_ounce


def main():
    ounces_of_gold = int(input("Enter the number of gold ounces: "))
    ounces_of_silver = int(input("Enter the number of silver ounces: "))
    ounces_of_platinum = int(input("Enter the number of platinum ounces: "))
    total_ounces = ounces_of_gold + ounces_of_silver + ounces_of_platinum
    cost_of_gold = calculate_cost(ounces_of_gold, ONEOUNCEGOLD)
    cost_of_silver = calculate_cost(ounces_of_silver, ONEOUNCESILVER)
    cost_of_platinum = calculate_cost(ounces_of_platinum, ONEOUNCEPLATINUM)
    subtotal = cost_of_gold + cost_of_silver + cost_of_platinum
    total_cost = subtotal + subtotal * SERVICEFEE + subtotal * SALESTAX
    print("\nThe total number of ounces purchased is ", total_ounces)
    print("The total cost of gold is ", cost_of_gold)
    print("The total cost of silver is ", cost_of_silver)
    print("The total cost of platinum is", cost_of_platinum)
    print("The total cost of purchase is", total_cost, "\n")
    
main()    
