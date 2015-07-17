pizzasSold = int(input('Enter the number of pizzas sold: '))
length = int(input('Enter the length of a pizza: '))
width = int(input('Enter the width of a pizza: '))
diameter = float(input('Give me the diameter of a pepperoni slice: '))
thickness = float(input('Enter the thickness of a pepporoni slice: '))
stickLength = int(input('Enter the pepperoni stick length: '))
edge = float(input('Enter the edge of the pizza: '))

#How many slices go length-wise
usableLength = length - (2 * edge)
peppSliceLength = usableLength / diameter

#How many slices go width-wise
usableWidth = width - (2 * edge)
peppSliceWidth = usableWidth / diameter

#How many slices on the pizza?
slices = peppSliceLength * peppSliceWidth

#Pepperoni stick length to cover all pizzas
hypoLength = slices * thickness * pizzasSold
sticksNeeded = hypoLength / stickLength

print('You will  need', sticksNeeded, ' sticks.')
