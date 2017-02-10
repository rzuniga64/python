# PURPOSE: This program determines the cost of a painting
#
# INPUT
# The size of the canvas
#
# OUTPUT
# the total cost including labor and materials

HOURLYRATE = 45         # hourly rate
COSTOFPAINTTUBE = 10    # cost of 1 tube of paint
INCHESSQUARED = 512     # canvas size used to determine cost


def canvasSizeLessThan512(sizeOfCanvas):
    hoursLaborPerSquareInch = 24/64
    numberOfTubesPerSquareInch = 1/64
    laborCost = sizeOfCanvas * hoursLaborPerSquareInch * HOURLYRATE
    materialCost = sizeOfCanvas * numberOfTubesPerSquareInch * COSTOFPAINTTUBE
    return laborCost,materialCost


def canvasSizeGreaterThanOrEqualTo512(sizeOfCanvas):
    hoursLaborPerSquareInch = 1000/512
    numberOfTubesPerSquareInch = 8/512
    laborCost = sizeOfCanvas * hoursLaborPerSquareInch * HOURLYRATE
    materialCost = sizeOfCanvas * numberOfTubesPerSquareInch * COSTOFPAINTTUBE
    return laborCost,materialCost


def main():
    sizeOfCanvas = int(input("Enter size of canvas "))
   
    if (sizeOfCanvas < INCHESSQUARED):
        laborCost, materialCost = canvasSizeLessThan512(sizeOfCanvas)
    elif sizeOfCanvas >= INCHESSQUARED:
        laborCost, materialCost = canvasSizeGreaterThanOrEqualTo512(sizeOfCanvas)
        
    totalCost = laborCost + materialCost
    print("The total cost of the painting is ", format(totalCost, ",.2f"))
        
main()
