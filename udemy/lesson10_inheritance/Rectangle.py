class Shape:

    def __init__(self, xcor, ycor):
        self.x = xcor
        self.y = ycor

    def __str__(self):
        return 'x: ' + str(self.x) + ' y: ' + str(self.y)

    def move(self, x1, y1):
        self.x = self.x + x1
        self.y = self.y + y1


class Rectangle(Shape):

    def __init__(self, xcor, ycor, width, height):
        Shape.__init__(self, xcor, ycor)
        self.width = width
        self.height = height

    def __str__(self):
        ret_str = Shape.__str__(self)
        ret_str += ' width: ' + str(self.width) + \
            ' height: ' + str(self.height)
        return ret_str

rec = Rectangle(5, 10, 8, 9)
print(rec)
rec.move(10, 12)
print(rec)
