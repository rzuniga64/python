#Purpose: On a chessboard a number of grains of rice are deposited 
#         on each square each day equal to the number given on the 
#         preceding day. Give the initial square had 1 grain this program 
#         calculates the number of grains placed on each square each 
#         day (a chessboard has 64 squares), a cumulative total and 
#         depth Texas would be buried in grains of rice per day.
# Input:  1. Number of days
#         2. Radius of a rice grain
#         3. Length of a rice grain
#         4. Area of Texas in square miles
#         5. Number of square feet per square mile
#         6. Number of square inches per square feet
# Output: 1. Number of grains deposited on that day
#         2. Cumulative total number of grains up to and including that day
#         3. Depth Texas buried in grains of rice on that day in inches
import math

NumberOfDays = 64
GrainRadiusInInches = 0.05
GrainLengthInInches = 0.4
AreaOfTexasInSquareMiles = 268820
SquareFeetPerSquareMile = 27878400
SquareInchesPerSquareFoot = 144
AreaOfTexasInSquareInches = AreaOfTexasInSquareMiles * SquareFeetPerSquareMile * SquareInchesPerSquareFoot
    
def main():
    print("Day\t\t\t  Grains\t\t   Total Grains\t\tDepth Texas buried in grain(inches)")
    numberOfGrains = 0
    totalGrains = 0
    for day in range(NumberOfDays):
        numberOfGrains = pow(2,day)
        totalGrains    = totalGrains + numberOfGrains
        volumeOfGrain  = math.pi * GrainRadiusInInches**2 * GrainLengthInInches * totalGrains
        depthOfGrain   = volumeOfGrain/AreaOfTexasInSquareInches
        print(day+1, format(numberOfGrains, '30,d'), format(totalGrains, '30,d'), format(depthOfGrain, '30.20f'))
        
main()