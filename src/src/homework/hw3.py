# This program determines the cost of a painting
#
# INPUT
# The size of the canvas
#
# OUTPUT
# the total cost including labor and materials

HOURLYRATE = 45         # hourly rate
COSTOFPAINTTUBE = 10    # cost of 1 tube of paint
INCHESSQUARED = 512     # canvas size used to determine cost

def main():
    sizeOfCanvas = int(input("Enter size of canvas "))
   
    if (sizeOfCanvas < INCHESSQUARED):
        hoursLaborPerSquareInch = 24/64
        numberOfTubesPerSquareInch = 1/64
    elif sizeOfCanvas >= INCHESSQUARED:
        hoursLaborPerSquareInch = 1000/512
        numberOfTubesPerSquareInch = 8/512

    costOfLabor = sizeOfCanvas * hoursLaborPerSquareInch * HOURLYRATE
    costOfMaterial = sizeOfCanvas * numberOfTubesPerSquareInch * COSTOFPAINTTUBE
    totalCost = costOfLabor + costOfMaterial

    print("The total cost of the painting is ", format(totalCost, ",.2f"))
        
main()
