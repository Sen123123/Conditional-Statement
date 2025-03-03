class square:
    def __init__ (self,sides):
        self.sides= sides
    
    def area(self):
        print("The area of the square is",self.sides**2,"(Length^2)")

class rectangle:
    def __init__ (self,length,width):
        self.length = length
        self.width = width

    def area(self):
        print("The area of the rectangle is",self.length*self.width,"(Length X Width)")

class circle:
    def __init__ (self,radius):
        self.radius= radius

    def area(self):
        print("The area of the circle is ",(22/7)*self.radius*self.radius)


class trapezium:
    def __init__ (self,A,B):
        self.A = A
        self.B = B

    def area(self):
        print("The area of the trapezium is",1/2*(self.A+self.B),"{1/2 X (Length of the top section + Length of the bottom section)}")

class equilateral_triangle:
    def __init__ (self,height,length):
        self.height = height
        self.length = length

    def area(self):
        print("The area of an equilateral triangle is",self.height*(1/2*self.length),"(1/2 X Length X Height)")


osquare = square(5)
ocircle = circle(5)
orectangle = rectangle(5,6)
otrapezium = trapezium(5,7)
oequilateral_triangle = equilateral_triangle(5,4)


for shape in (osquare,ocircle,orectangle,otrapezium,oequilateral_triangle):
    shape.area()