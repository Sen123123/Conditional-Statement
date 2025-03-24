class Square:
    def __init__ (self,sides):
        self.sides= sides

    def area(self):
        print("The area of the square is ",self.sides**2)

class Circles:
    def __init__ (self,radius):
        self.radius= radius

    def area(self):
        print("The area of the circle is ",(22/7)*self.radius*self.radius)

oSquare = Square(5)
oCircles = Circles(5)

for shape in (oSquare, oCircles):
    shape.area()

